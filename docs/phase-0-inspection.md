# Phase 0 — System Inspection

## یافته‌ها

| مورد | نتیجه |
|---|---|
| OS | Ubuntu 24.04.5 LTS |
| CPU | 6 vCPU Intel Xeon |
| RAM | 7.8 GiB، بدون swap |
| Disk | 49G کل، حدود 40G آزاد |
| GPU | NVIDIA موجود نیست؛ `nvidia-smi` قابل اجرا نیست |
| Docker | نصب نیست و سرویس inactive است |
| ابزار پایه | Python 3.12.3، Git 2.43، Node 22.13 |

## تصمیم اجرایی

این sandbox برای نصب daemonهای Docker، GPU toolkit و اجرای دائمی سرویس‌ها مناسب نیست. پیکربندی تولیدی کامل در `infra/` ارائه شده، اما تست CI با هسته FastAPI و store درون‌حافظه‌ای انجام می‌شود. روی Ubuntu واقعی کافی است Docker Engine، Compose و در صورت وجود GPU، NVIDIA Container Toolkit نصب شود.

## اثر روی معیارها

- persistence واقعی PostgreSQL/Redis/Ollama/Open WebUI: با Compose قابل استقرار است، اما در این sandbox smoke-test نمی‌شود.
- منطق orchestration، حافظه، context، امنیت workspace و ساختار task: در همین محیط تست شده است.
