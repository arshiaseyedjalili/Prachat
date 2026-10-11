# Token Optimization

context به‌صورت پویا از policy، درخواست جاری، task state، project summary، memoryهای مرتبط، فایل‌ها و آخرین tool result ساخته می‌شود؛ کل conversation ارسال نمی‌شود. `estimate_tokens` و `compress` سقف را اعمال می‌کنند.

- small: classification، summary و metadata
- medium: planning و code review
- large: architecture و debugging پیچیده

بودجه با `CONTEXT_TOKEN_BUDGET` قابل تنظیم است.
