import google.generativeai as genai

# تعريف API Key
API_KEY = "AIzaSyDgNboDtt2ncO1nHCk4e5BLNeOSEBb_2Lw"
genai.configure(api_key=API_KEY)

# إنشاء النموذج
model = genai.GenerativeModel('gemini-2.0-flash')

# بناء الـ Prompt ديناميكيًّا
def prompt(ingredients, meal_type):
    return f"""
    أنت مساعد ذكي لإنشاء وصفات طعام. قم بإنشاء وصفة باستخدام المكونات التالية: {ingredients}. تأكد من أن الوصفة:  
    1. تركز على تقليل الهدر باستخدام المكونات المتوفرة.  
    2. تكون مناسبة لـ {meal_type}.  
    أضف قائمة بالمكونات بالجرامات أو الكؤوس، خطوات التحضير، ونصائح لتقديم الوجبة.
    """

# استقبال مدخلات المستخدم
def get_user_input():
    print("مرحبًا! سنساعدك في إنشاء وصفة طعام مخصصة.")
    ingredients = input("ما هي المكونات المتوفرة لديك؟ (افصل بينها بفاصلة): ")
    meal_type = input("ما نوع الوجبة التي تريدها؟ (فطور، غداء، عشاء): ")
    return ingredients, meal_type

# الحصول على مدخلات المستخدم
ingredients, meal_type = get_user_input()

# توليد الـ Prompt
prompt = prompt(ingredients, meal_type)  

# إرسال الطلب واستقبال النتيجة
response = model.generate_content(prompt)
print(response.text)