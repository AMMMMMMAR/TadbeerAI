import google.generativeai as genai
import creds

# تعريف API Key
genai.configure(api_key=creds.API_KEY)

# إنشاء النموذج
model = genai.GenerativeModel('gemini-2.0-flash')

# بناء الـ Prompt ديناميكيًّا
def prompt(ingredients, meal_type):
    return f"""
أنت مساعد ذكي لإنشاء وصفات طعام. قم بإنشاء وصفة باستخدام المكونات التالية: {ingredients}. تأكد من أن الوصفة:  
1. تركز على تقليل الهدر باستخدام المكونات المتوفرة.  
2. تكون مناسبة لـ {meal_type}.  
أضف قائمة بالمكونات بالجرامات أو الكؤوس، خطوات التحضير، ونصائح لتقديم الوجبة.

**ملاحظة:**  
- إذا كتب المستخدم أشياء ليست مكونات طعام (مثل أسماء أشخاص، أماكن، أو مواضيع غير متعلقة بالطهي)، لا تستطيع إنشاء وصفة طعام.  
- في هذه الحالة، أرسل له رسالة تفيد بعدم الفهم ووضح له ماذا يجب أن يكتب.  
- مثال: "عذرًا، يبدو أنك لم تدخل مكونات طعام. الرجاء إدخال مكونات صالحة للطهي، مثل: 'طماطم، بصل، دجاج، أرز'."
"""

# استقبال مدخلات المستخدم
def get_user_input():
    print("مرحبًا! سنساعدك في إنشاء وصفة طعام مخصصة.")
    ingredients = input("ما هي المكونات المتوفرة لديك؟ (افصل بينها بفاصلة): ")
    meal_type = input("ما نوع الوجبة التي تريدها؟ (فطور، غداء، عشاء): ")
    return ingredients, meal_type

# عرض الوصفة وطلب إعادة إنشائها إذا لزم الأمر
def display_recipe_and_ask_for_another(ingredients, meal_type):
    while True:
        # توليد الـ Prompt
        prompt_text = prompt(ingredients, meal_type)

        # إرسال الطلب واستقبال النتيجة
        response = model.generate_content(prompt_text)
        print(response.text)

        # سؤال المستخدم إذا كان يريد وصفة أخرى
        user_choice = input("\nهل تريد وصفة أخرى بنفس المكونات؟ (نعم/لا): ").strip().lower()
        if user_choice not in ["نعم", "yes", "y", "لا", "no", "n"]:
            print("عذرًا، لم أفهم اختيارك. الرجاء الإجابة بـ 'نعم' أو 'لا'.")
            continue
        if user_choice in ["لا", "no", "n"]:
            print("شكرًا لاستخدامك خدمة إنشاء الوصفات. نتمنى لك وجبة لذيذة!")
            break

# الحصول على مدخلات المستخدم
ingredients, meal_type = get_user_input()

# عرض الوصفة والسماح بإنشاء وصفات أخرى
display_recipe_and_ask_for_another(ingredients, meal_type)