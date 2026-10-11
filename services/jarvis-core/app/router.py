from dataclasses import dataclass

@dataclass(frozen=True)
class Route:
    intent: str
    model: str
    execution_required: bool

def classify(message: str) -> Route:
    text = message.lower()
    if any(x in text for x in ('run ', 'execute ', 'command', 'terminal')):
        return Route('execution', 'local-medium', True)
    if any(x in text for x in ('debug', 'error', 'traceback', 'fix bug')):
        return Route('debugging', 'local-large', True)
    if any(x in text for x in ('create app', 'implement', 'code', 'repository', 'file')):
        return Route('coding', 'local-medium', True)
    if any(x in text for x in ('document', 'pdf', 'file says', 'according to')):
        return Route('document_question', 'local-small', False)
    return Route('normal_chat', 'local-small', False)
