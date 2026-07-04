import requests
import re

url = "https://www.maspero.eg/stream/11"

try:
    response = requests.get(url)
    # البحث عن الرابط الذي يحتوي على كلمة live وينتهي بـ m3u8
    match = re.search(r'https://.*?live.*?\.m3u8', response.text)
    
    if match:
        radio_link = match.group(0)
        print("تم العثور على الرابط بنجاح:")
        print(radio_link)
    else:
        print("لم يتم العثور على رابط البث، قد يكون هناك تحديث في الموقع.")
        
except Exception as e:
    print(f"حدث خطأ: {e}")
