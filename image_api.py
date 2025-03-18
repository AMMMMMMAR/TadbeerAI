import sys
import io
from google.cloud import vision
import google.generativeai as genai
import creds
import os



# تغيير ترميز الإخراج إلى UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# تعيين مسار ملف JSON لـ Google Vision API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds.api_key

# تهيئة Gemini API
GEMINI_API_KEY = "AIzaSyDgNboDtt2ncO1nHCk4e5BLNeOSEBb_2Lw"  # استبدل بمفتاح API الخاص بك
genai.configure(api_key=GEMINI_API_KEY)

# تحليل الصورة باستخدام Google Vision API
def analyze_image(image_path):
    # إنشاء عميل Vision
    vision_client = vision.ImageAnnotatorClient()

    # قراءة الصورة
    with open(image_path, "rb") as image_file:
        content = image_file.read()

    # إنشاء كائن Image
    image = vision.Image(content=content)

    # تحليل الصورة
    response = vision_client.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]
    return labels

# توليد الوصفة باستخدام Gemini API
def generate_recipe(ingredients, meal_type):
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"""
    أنت مساعد ذكي لإنشاء وصفات طعام. قم بإنشاء وصفة باستخدام المكونات التالية: {ingredients}. تأكد من أن الوصفة:  
    1. تركز على تقليل الهدر باستخدام المكونات المتوفرة.  
    2. تكون مناسبة لـ {meal_type}.  
    أضف قائمة بالمكونات بالجرامات أو الكؤوس، خطوات التحضير، ونصائح لتقديم الوجبة.
    """
    response = model.generate_content(prompt)
    return response.text

# تعيين مسار الصورة مباشرة داخل الكود
image_path = "cabse.jpeg"  # استبدل بمسار الصورة الفعلي

# تحليل الصورة
print("جارٍ تحليل الصورة...")
ingredients = analyze_image(image_path)
print(f"تم التعرف على المكونات: {', '.join(ingredients)}")

# توليد الوصفة
print("جارٍ إنشاء الوصفة...")
meal_type = "فطور"  # يمكن تغييرها حسب الحاجة
recipe = generate_recipe(', '.join(ingredients), meal_type)
print("\nالوصفة المقترحة:\n")
print(recipe)