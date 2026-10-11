# Architecture

```mermaid
flowchart TD
 U[User] --> W[Open WebUI]
 W --> C[jarvis-core FastAPI]
 C --> M[(PostgreSQL + pgvector)]
 C --> R[(Redis)]
 C --> L[LiteLLM]
 L --> O[Ollama]
 C --> A[OpenHands Adapter]
 A --> S[Isolated Workspace]
```

## رویکرد

Compose همه سرویس‌ها را روی شبکه داخلی `jarvis` و با volumeهای نام‌دار اجرا می‌کند. هسته، interfaceهای کوچک دارد تا برای CI به‌صورت مستقل تست شود و در production به PostgreSQL/Redis/OpenHands متصل گردد.
