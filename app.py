import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. تحميل المفتاح السري بأمان
load_dotenv()

# 2. تصميم واجهة المستخدم (بشكل رسمي واحترافي)
st.set_page_config(page_title="مُحسّن السير الذاتية", layout="wide")

st.title("نظام تحليل وتحسين السير الذاتية (CV & ATS Optimizer)")
st.markdown("""
مرحباً بك في أداة التحليل.
يرجى إدخال نص سيرتك الذاتية الحالية والوصف الوظيفي المستهدف، وسيقوم النظام بتحليل التطابق واقتراح التحسينات اللازمة.
""")

# حقول إدخال البيانات
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. السيرة الذاتية (CV)")
    cv_text = st.text_area("ألصق نص السيرة الذاتية هنا:", height=300)

with col2:
    st.subheader("2. الوصف الوظيفي (Job Description)")
    jd_text = st.text_area("ألصق نص الوصف الوظيفي هنا:", height=300)

st.markdown("---")
submit_btn = st.button("بدء تحليل السيرة الذاتية", use_container_width=True)

# 3. الربط مع الذكاء الاصطناعي (Gemini)
if submit_btn:
    api_key = os.getenv("GEMINI_API_KEY")
    
    # معالجة الأخطاء (Error Handling)
    if not api_key:
        st.error("تنبيه أمني: مفتاح الـ API غير موجود. الرجاء إضافته في ملف .env")
    elif not cv_text.strip() or not jd_text.strip():
        st.warning("الرجاء إدخال السيرة الذاتية والوصف الوظيفي قبل المتابعة.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # تصميم الأمر (Prompt Design) - معدل ليكون رسمي ومجدول بشكل صحيح
            prompt = f"""
            أنت خبير في الموارد البشرية وأنظمة التوظيف الآلي (ATS).
            قم بتحليل السيرة الذاتية التالية ومقارنتها بالوصف الوظيفي.
            
            يجب أن تكون إجابتك باللغة الإنجليزية، وبصيغة Markdown احترافية وخالية من الرموز التعبيرية (Emojis).
            هام جداً: يجب أن تضع مسافة (سطر جديد) قبل وبعد الجدول، وتتأكد من كتابة كل صف في الجدول في سطر مستقل لضمان عرضه بشكل صحيح.
            
            ### ATS Match Score
            [ضع نسبة التطابق المئوية]
            
            ### Missing Keywords & Skills
            
            | Skill/Keyword | Importance in JD | How to add it to CV |
            |---------------|------------------|---------------------|
            [ضع المهارات هنا، صف واحد لكل مهارة]
            
            ### Actionable Improvement Tips
            - [نصيحة 1]
            - [نصيحة 2]
            
            ### AI-Optimized Professional Summary
            [اكتب ملخص مهني قصير مخصص لهذه الوظيفة يمكن للمستخدم نسخه]
            
            ---
            CV Text:
            {cv_text}
            
            Job Description:
            {jd_text}
            """
            
            with st.spinner("جاري معالجة البيانات وتحليل السيرة الذاتية..."):
                response = model.generate_content(prompt)
                
                # 4. عرض النتائج
                st.success("اكتمل التحليل بنجاح.")
                st.markdown("---")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال بالخادم: {str(e)}")

st.markdown("---")
# التعديل هنا: الأسماء والجامعة باللغة الإنجليزية
st.caption("Developed by: **[ MESHAL ALDHAFEERI ] & [Mishari Almaliki ]** | Almaarefa University")