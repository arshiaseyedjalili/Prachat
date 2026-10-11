from fastapi.testclient import TestClient
from app.main import app, store
from app.context import estimate_tokens, build_context
from app.router import classify
from app.executor import WorkspaceManager

client = TestClient(app)

def setup_function():
    store.memories.clear(); store.tasks.clear(); store.events.clear()

def test_health_and_memory_retrieval():
    assert client.get('/health').json()['status'] == 'ok'
    client.post('/v1/memories', json={'kind':'project','content':'React PostgreSQL architecture'})
    hits = client.get('/v1/memories/search?q=PostgreSQL').json()
    assert len(hits) == 1

def test_intent_routing_and_context_budget():
    assert classify('please debug this traceback').intent == 'debugging'
    ctx = build_context('policy', 'request', memories=[{'content':'memory'}], budget=3)
    assert estimate_tokens(ctx) <= 12

def test_task_persists_in_store():
    response = client.post('/v1/tasks', json={'title':'Implement auth'})
    task_id = response.json()['id']
    assert client.get(f'/v1/tasks/{task_id}').status_code == 200
    assert store.events[0]['event_type'] == 'TaskStarted'

def test_tool_security_blocks_escape_and_privileged_flags():
    assert client.post('/v1/tools/validate', json={'tool':'git_status'}).status_code == 200
    assert client.post('/v1/tools/validate', json={'tool':'filesystem_read','arguments':{'path':'../../etc/passwd'}}).status_code == 403

def test_workspace_layout(tmp_path):
    base = WorkspaceManager(tmp_path).create('w1')
    assert all((base / p).is_dir() for p in ('repository','inputs','outputs','logs'))
    assert (base / 'metadata.json').exists()
