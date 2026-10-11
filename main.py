import os
from fastapi import FastAPI, HTTPException
from .models import ChatRequest, MemoryCreate, TaskCreate, ToolRequest
from .store import InMemoryStore, PersistentStore
from .router import classify
from .context import build_context
from .executor import OpenHandsAdapter

app = FastAPI(title='jarvis-core', version='0.1.0')
store = PersistentStore(os.environ['STATE_FILE']) if os.environ.get('STATE_FILE') else InMemoryStore()
executor = OpenHandsAdapter()

@app.get('/health')
def health(): return {'status':'ok','service':'jarvis-core'}

@app.post('/v1/memories')
def create_memory(item: MemoryCreate): return store.add_memory(item)

@app.get('/v1/memories/search')
def search_memory(q: str, kind: str | None = None): return store.search_memories(q, kind)

@app.post('/v1/tasks')
def create_task(item: TaskCreate): return store.create_task(item)

@app.get('/v1/tasks/{task_id}')
def get_task(task_id: str):
    try: return store.tasks[__import__('uuid').UUID(task_id)]
    except (KeyError, ValueError): raise HTTPException(404, 'task not found')

@app.get('/v1/events')
def events():
    return store.events

@app.post('/v1/chat')
def chat(item: ChatRequest):
    route = classify(item.message)
    memories = store.search_memories(item.message)
    context = build_context('You are Jarvis Core.', item.message, memories=memories)
    return {'route': route.__dict__, 'context': context, 'memory_hits': len(memories)}

@app.post('/v1/tools/validate')
def validate_tool(item: ToolRequest):
    try: return {'tool':item.tool, 'policy':executor.allowed_tool(item.tool, item.arguments)}
    except (ValueError, PermissionError) as exc: raise HTTPException(403, str(exc))
