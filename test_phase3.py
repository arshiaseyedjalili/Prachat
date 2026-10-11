import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
from app.tool_schemas import TOOL_SCHEMAS
from app.executor import OpenHandsAdapter

def test_all_tools_have_json_schema_and_policy():
    adapter = OpenHandsAdapter('/tmp')
    for name, schema in TOOL_SCHEMAS.items():
        assert schema['type'] == 'object'
        assert adapter.allowed_tool(name, {})['timeout'] > 0

def test_openhands_rejects_privileged_task():
    try:
        OpenHandsAdapter().validate_task({'title':'bad','run_as_root':True})
        assert False
    except PermissionError:
        pass
