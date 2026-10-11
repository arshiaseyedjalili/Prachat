import re
from typing import Any

def estimate_tokens(text: str) -> int:
    return max(1, len(re.findall(r'\w+|[^\w\s]', text, re.UNICODE)))

def compress(text: str, max_tokens: int) -> str:
    if estimate_tokens(text) <= max_tokens: return text
    words = text.split()
    keep = max(1, max_tokens - 8)
    return ' '.join(words[:keep]) + ' … [compressed]'

def build_context(system_policy: str, request: str, task_state: dict[str, Any] | None = None,
                  project_summary: str = '', memories: list[dict[str, Any]] | None = None,
                  files: list[str] | None = None, tool_results: list[str] | None = None,
                  budget: int = 4096) -> str:
    sections = [system_policy, request, str(task_state or {}), project_summary,
                '\n'.join(m['content'] for m in (memories or [])), '\n'.join(files or []),
                '\n'.join(tool_results or [])]
    return compress('\n\n'.join(s for s in sections if s), budget)
