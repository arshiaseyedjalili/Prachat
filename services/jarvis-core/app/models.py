from typing import Any, Literal
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

MemoryKind = Literal['project', 'task', 'knowledge', 'experience']

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=20000)
    project_id: UUID | None = None
    task_id: UUID | None = None

class MemoryCreate(BaseModel):
    kind: MemoryKind
    content: str = Field(min_length=1, max_length=50000)
    metadata: dict[str, Any] = Field(default_factory=dict)

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=500)
    project_id: UUID | None = None
    state: dict[str, Any] = Field(default_factory=dict)

class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    project_id: UUID | None = None
    status: Literal['pending','running','blocked','completed','failed'] = 'pending'
    state: dict[str, Any] = Field(default_factory=dict)

class ToolRequest(BaseModel):
    tool: str
    arguments: dict[str, Any] = Field(default_factory=dict)
