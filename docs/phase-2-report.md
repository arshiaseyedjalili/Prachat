# Phase 2 — JARVIS Core Intelligence Layer

## تغییرات

هسته FastAPI intent classification، انتخاب مدل، چهار نوع حافظه، بازیابی، context budget، compression، task graph و event history را اضافه می‌کند. `PersistentStore` برای restart recovery محلی دارد و Compose آن را در `/data/state.json` نگه می‌دارد؛ production migration به PostgreSQL/pgvector آماده است.

## تست پذیرش

تست‌های health، memory retrieval، routing، task recovery، event history و context budget در `services/jarvis-core/tests/test_core.py` اجرا شدند. برای persistence واقعی PostgreSQL باید روی Ubuntu هدف `docker compose up` اجرا شود.
