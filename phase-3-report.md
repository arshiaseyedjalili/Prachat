# Phase 3 — Autonomous Development Agent

## تغییرات

`OpenHandsAdapter` یک قرارداد امن برای دریافت task ساختاریافته فراهم می‌کند. `WorkspaceManager` برای هر workspace پوشه‌های `repository/`، `inputs/`، `outputs/`، `logs/` و `metadata.json` می‌سازد. ابزارهای filesystem read، git status/diff، test/build runner و docker status policyهای scope، timeout، output limit و audit-compatible دارند.

## کنترل‌های امنیتی

root execution و Docker socket رد می‌شوند و filesystem traversal خارج از workspace مجاز نیست. اجرای واقعی OpenHands باید به container جدا، user غیر root، secretهای تزریق‌نشده و network محدود متصل شود.

## تست پذیرش

ساخت layout workspace و رد path escape/privileged flags تست شده است. اتصال شبکه‌ای OpenHands در sandbox فعال نیست و adapter به‌صورت deterministic و قابل اتصال به آن سرویس ارائه شده است.
