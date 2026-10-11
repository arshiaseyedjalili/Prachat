import json
from pathlib import Path
from uuid import UUID, uuid4
from .security import validate_tool

class WorkspaceManager:
    def __init__(self, root='/workspaces'):
        self.root = Path(root)
    def create(self, workspace_id: str | None = None) -> Path:
        wid = workspace_id or str(uuid4()); base = self.root / wid
        for name in ('repository','inputs','outputs','logs'): (base / name).mkdir(parents=True, exist_ok=True)
        (base / 'metadata.json').write_text(json.dumps({'workspace_id':wid,'status':'ready'}, indent=2))
        return base

class OpenHandsAdapter:
    def __init__(self, workspace_root='/workspaces'):
        self.workspace_root = workspace_root
    def validate_task(self, task: dict) -> None:
        if not task.get('title'): raise ValueError('task title is required')
        if task.get('run_as_root'): raise PermissionError('root execution is prohibited')
        if task.get('docker_socket'): raise PermissionError('docker socket access is prohibited')
    def allowed_tool(self, tool: str, arguments: dict):
        return validate_tool(tool, arguments, self.workspace_root)
