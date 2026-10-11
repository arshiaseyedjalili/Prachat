from dataclasses import dataclass, field
import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4
from .models import MemoryCreate, Task, TaskCreate

@dataclass
class InMemoryStore:
    memories: list[dict[str, Any]] = field(default_factory=list)
    tasks: dict[UUID, Task] = field(default_factory=dict)
    events: list[dict[str, Any]] = field(default_factory=list)

    def add_memory(self, item: MemoryCreate) -> dict[str, Any]:
        row = {'id': str(uuid4()), 'kind': item.kind, 'content': item.content,
               'metadata': item.metadata, 'created_at': datetime.now(timezone.utc).isoformat()}
        self.memories.append(row); self.events.append({'event_type':'MemoryCreated','payload':row})
        return row

    def search_memories(self, query: str, kind: str | None = None, limit: int = 5):
        words = set(query.lower().split())
        rows = [m for m in self.memories if not kind or m['kind'] == kind]
        scored = [(len(words & set(m['content'].lower().split())), m) for m in rows]
        return [m for score, m in sorted(scored, key=lambda x: x[0], reverse=True) if score > 0][:limit]

    def create_task(self, item: TaskCreate) -> Task:
        task = Task(title=item.title, project_id=item.project_id, state=item.state)
        self.tasks[task.id] = task
        self.events.append({'event_type':'TaskStarted','task_id':str(task.id),'payload':task.model_dump(mode='json')})
        return task

    def update_task(self, task_id: UUID, **changes: Any) -> Task:
        task = self.tasks[task_id].model_copy(update=changes)
        self.tasks[task_id] = task
        self.events.append({'event_type':'TaskUpdated','task_id':str(task_id),'payload':changes})
        return task

class PersistentStore(InMemoryStore):
    """Small local-dev persistence adapter; production uses PostgreSQL migrations."""
    def __init__(self, path: str):
        super().__init__()
        self.path = Path(path)
        self._load()

    def _load(self):
        if not self.path.exists(): return
        data = json.loads(self.path.read_text())
        self.memories = data.get('memories', [])
        self.events = data.get('events', [])
        self.tasks = {UUID(k): Task.model_validate(v) for k, v in data.get('tasks', {}).items()}

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps({'memories': self.memories, 'events': self.events,
            'tasks': {str(k): v.model_dump(mode='json') for k, v in self.tasks.items()}}, indent=2))

    def add_memory(self, item):
        row = super().add_memory(item); self._save(); return row

    def create_task(self, item):
        task = super().create_task(item); self._save(); return task

    def update_task(self, task_id, **changes):
        task = super().update_task(task_id, **changes); self._save(); return task
