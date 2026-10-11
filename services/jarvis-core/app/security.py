from pathlib import Path
from typing import Any

TOOL_POLICIES = {
    'filesystem_read': {'scope':'workspace:read', 'timeout':5, 'output_limit':20000},
    'git_status': {'scope':'workspace:read', 'timeout':10, 'output_limit':10000},
    'git_diff': {'scope':'workspace:read', 'timeout':10, 'output_limit':50000},
    'test_runner': {'scope':'workspace:execute', 'timeout':300, 'output_limit':50000},
    'build_runner': {'scope':'workspace:execute', 'timeout':600, 'output_limit':50000},
    'docker_status': {'scope':'runtime:read', 'timeout':10, 'output_limit':10000},
}

def validate_tool(name: str, args: dict[str, Any], workspace_root: str) -> dict[str, Any]:
    if name not in TOOL_POLICIES: raise ValueError(f'unknown tool: {name}')
    if name == 'filesystem_read':
        path = (Path(workspace_root) / args.get('path', '')).resolve()
        root = Path(workspace_root).resolve()
        if root not in path.parents and path != root: raise PermissionError('path escapes workspace')
    return TOOL_POLICIES[name]
