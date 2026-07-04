import requests

# هذا هو رابط الصفحة التي تحتوي على البث
url = "https://www.maspero.eg/stream/11"

# هنا سنقوم بجلب محتوى الصفحة والبحث عن رابط البث
try:
    response = requests.get(url)
    # ملاحظة: هذا كود تجريبي، سنقوم بتطويره لاستخراج الرابط بدقة لاحقاً
    print("تم الاتصال بنجاح!")
    # سنضيف لاحقاً منطق استخراج رابط m3u8 وحفظه في ملف
except Exception as e:
    print(f"حدث خطأ: {e}")
