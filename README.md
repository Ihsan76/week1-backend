
# آفاق | Afaq — الخادم (Backend API)

الواجهة الخلفية لمنصة **آفاق التعليمية** مبنية باستخدام Django، وتوفر REST API للتوثيق وإدارة المستخدمين وباقي وحدات المنصة التعليمية.

## Live (Render)
- Base URL: https://week1-backend.onrender.com/  [page:94]

> ملاحظة: قد يعرض السيرفر 404 على المسار `/` وهذا طبيعي إن لم يوجد route رئيسي، واستخدامك سيكون عبر `/api/...`. [page:94]

## التقنيات
- Python + Django. [page:94]

## التشغيل محليًا
### 1) إنشاء بيئة افتراضية
bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
2) تثبيت المتطلبات
bash
pip install -r requirements.txt
3) الترحيلات والتشغيل
bash
python manage.py migrate
python manage.py runserver
http://127.0.0.1:8000

إعدادات الإنتاج (مهم)
قبل إطلاق المنصة للمستخدمين الفعليين:

اجعل DEBUG=False.

اضبط ALLOWED_HOSTS.

اضبط CORS للسماح للواجهة الأمامية (Vercel) بالوصول للـ API.

خارطة الطريق
Courses → Modules → Lessons

Enrollment + Progress

Attachments: المرحلة 1 روابط URL، المرحلة 2 رفع ملفات (Storage)

i18n: حزم ترجمة تُدار من لوحة الإدارة

المساهمة
PRs مرحب بها، ويفضل فتح Issue لأي تغيير كبير قبل البدء.