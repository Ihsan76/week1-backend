## 2) CONTRIBUTING.md (Backend) — `week1-backend/CONTRIBUTING.md`

```md
# المساهمة في آفاق (Backend)

شكرًا لمساهمتك في Backend منصة آفاق التعليمية.

## متطلبات
- Python 3.10+ (يفضل)
- pip + venv

## تشغيل محلي
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# Windows: .venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
أسلوب العمل
افتح Issue قبل أي تغيير كبير.

اعمل فرعًا: feat/... أو fix/....

أي تغيير في Models أو API لازم يرافقه Migration (إذا لزم).

ملاحظات إنتاج
لا ترفع SECRET_KEY أو بيانات حساسة.

يجب أن يكون DEBUG=False في الإنتاج.