# Test Strategy

تست‌ها با pytest و TestClient اجرا می‌شوند و به Docker، GPU یا سرویس بیرونی نیاز ندارند. قراردادهای health، memory retrieval، intent routing، task event، context budget، workspace layout و security traversal پوشش داده شده‌اند.

```bash
pytest -q
```
