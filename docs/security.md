# Security

- container هسته با UID غیر root اجرا می‌شود.
- OpenHands نباید Docker socket، secrets یا کل filesystem میزبان را ببیند.
- filesystem read فقط زیر workspace resolve می‌شود و traversal را رد می‌کند.
- هر ابزار policy شامل scope، timeout و output limit دارد.
- در production secrets فقط از secret manager یا `.env` خارج از Git تزریق شوند؛ `.env` در ignore است.
- اجرای command باید در container اختصاصی workspace و با network policy محدود انجام شود.
