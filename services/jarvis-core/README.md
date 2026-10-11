# jarvis-core

هسته FastAPI پروژه prachat است. این سرویس تشخیص نوع درخواست، حافظه چهارگانه، بودجه‌بندی context، task graph، رویدادها و adapter اجرای امن را فراهم می‌کند.

## رویکرد

لایه‌های domain بدون وابستگی به PostgreSQL پیاده شده‌اند تا در CI و توسعه محلی با SQLite/حافظه تست شوند؛ persistence و OpenHands از طریق interface قابل تعویض هستند.

## اجرا

```bash
pip install -e '.[test]'
uvicorn app.main:app --reload
pytest -q
```

## تست‌ها

تست‌ها API، طبقه‌بندی، فشرده‌سازی context، کنترل دسترسی ابزار و اعتبارسنجی task را پوشش می‌دهند.
