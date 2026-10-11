# Task System

مدل پایدار `Project -> Task -> Subtask -> Files/Tests/Status` با UUID طراحی شده است. هر تغییر رویداد audit تولید می‌کند: `TaskStarted`، `TaskUpdated`، `FileChanged`، `CommandExecuted`، `TestFinished`، `DecisionMade` و `MemoryCreated`.

درخواست‌های coding/debugging/execution از مسیر executor عبور می‌کنند؛ کارهای قطع‌شده با `state` و event log قابل ادامه هستند.
