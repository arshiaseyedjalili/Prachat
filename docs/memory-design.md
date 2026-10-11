# Memory Design

چهار نوع حافظه داریم: `project` برای تصمیم‌های پروژه، `task` برای وضعیت اجرای کار، `knowledge` برای اسناد و `experience` برای راه‌حل‌ها و شکست‌های قبلی. هر رکورد metadata و timestamp دارد؛ PostgreSQL با pgvector محل production است و store درون‌حافظه‌ای فقط برای تست/توسعه است.

بازیابی فعلی lexical و deterministic است. در production embedding 384 بعدی در migration تعریف شده و می‌تواند با embedding service جایگزین شود.
