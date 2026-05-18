import streamlit as st
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
from pypdf import PdfReader
import docx2txt

# ==========================================
# 1. تحميل المفتاح السري بأمان (Responsible AI)
# ==========================================
load_dotenv()

# ==========================================
# 2. دوال قراءة وتمرير النصوص من الملفات المرفوعة
# ==========================================
def extract_text_from_pdf(file):
    """قراءة وتمرير النصوص من ملفات PDF بأمان"""
    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return ""

def extract_text_from_docx(file):
    """قراءة وتمرير النصوص من ملفات Word بأمان"""
    try:
        text = docx2txt.process(file)
        return text
    except Exception as e:
        st.error(f"Error reading DOCX file: {e}")
        return ""

# بيانات تجريبية (Demo) لتسهيل العرض المباشر أمام الدكتور
DEMO_CV = """John Doe
Software Engineer

TECHNICAL SKILLS:
- Programming: Python, JavaScript, C++
- Frameworks: Django, React
- Tools: Git, VS Code
- Database: MySQL

EXPERIENCE:
Junior Developer at TechCorp (2024 - Present)
- Developed web applications using Python and Django.
- Collaborated with teams to deliver clean and optimized code.
- Worked on fixing bugs and improving database queries."""

DEMO_JD = """We are looking for a Senior Software Engineer to join our growing team.

Requirements:
- Strong experience with Python and FastAPI.
- Deep understanding of REST APIs and Cloud environments (AWS/Docker).
- Experience with modern development tools like Git and CI/CD pipelines.
- Excellent teamwork and communication skills.
- Ability to optimize code and write clean, maintainable software."""

# ==========================================
# 3. واجهة المستخدم الرسومية وحقن أكواد الـ CSS
# ==========================================
st.set_page_config(page_title="Smart CV Optimizer", layout="wide")

# تصميم مخصص لتسهيل قراءة النتائج (البطاقات، كرات التقييم والـ Pills الملونة)
st.markdown("""
<style>
    /* تصميم بطاقة عرض نقاط الـ ATS */
    .metric-card {
        background-color: #1E293B;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #334155;
        text-align: center;
        margin-bottom: 20px;
    }
    .score-circle {
        font-size: 52px;
        font-weight: 800;
        margin: 10px 0;
    }
    .pill-matched {
        background-color: #064E3B;
        color: #34D399;
        padding: 6px 14px;
        border-radius: 20px;
        display: inline-block;
        margin: 5px;
        font-size: 14px;
        font-weight: 600;
    }
    .pill-missing {
        background-color: #7F1D1D;
        color: #FCA5A5;
        padding: 6px 14px;
        border-radius: 20px;
        display: inline-block;
        margin: 5px;
        font-size: 14px;
        font-weight: 600;
    }
    .stButton>button {
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. محدد اللغتين وعناوين التطبيق
# ==========================================
with st.sidebar:
    st.header("⚙️ Settings / الإعدادات")
    lang = st.selectbox("Application Language / لغة التطبيق", ["English", "العربية"])
    st.markdown("---")
    st.header("📂 Upload CV / رفع السيرة")
    uploaded_file = st.file_uploader("Upload PDF or DOCX / ارفع ملف سيرة ذاتية", type=["pdf", "docx"])

# تخصيص النصوص بناء على لغة الاختيار
if lang == "العربية":
    title = "📄 مُحسّن ومُقيّم السير الذاتية الذكي (CV & ATS Optimizer Pro)"
    subtitle = "نظام متقدم مدعوم بالذكاء الاصطناعي لتحليل التطابق مع الوصف الوظيفي واقتراح التحسينات الاحترافية لتجاوز أنظمة الفرز الآلي."
    btn_demo = "📥 تحميل نموذج تجريبي سريع (Try Demo)"
    btn_analyze = "🔍 بدء التحليل الفوري للسيرة الذاتية"
    lbl_cv = "السيرة الذاتية (CV)"
    lbl_jd = "الوصف الوظيفي المستهدف (Job Description)"
    lbl_result = "نتائج التحليل والتقييم الاحترافي"
else:
    title = "📄 Smart CV Optimizer & ATS Scorer Pro"
    subtitle = "An advanced AI-powered system designed to optimize resumes, analyze job description alignment, and beat Applicant Tracking Systems (ATS)."
    btn_demo = "📥 Load Demo Example"
    btn_analyze = "🔍 Start AI CV Analysis"
    lbl_cv = "Your Resume / CV"
    lbl_jd = "Target Job Description"
    lbl_result = "Analysis & Optimization Results"

st.title(title)
st.write(subtitle)

# ==========================================
# 5. معالجة المدخلات وحقن بيانات الديمو التفاعلي
# ==========================================
col1, col2 = st.columns(2)

cv_input_value = ""
if uploaded_file is not None:
    if uploaded_file.name.endswith(".pdf"):
        cv_input_value = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        cv_input_value = extract_text_from_docx(uploaded_file)
    st.sidebar.success("✅ File parsed successfully! / تم قراءة الملف بنجاح!")

# تفعيل زر الديمو وتخزين القيم في الجلسة المفتوحة (Session State)
if st.button(btn_demo, use_container_width=True):
    st.session_state["cv_text_val"] = DEMO_CV
    st.session_state["jd_text_val"] = DEMO_JD

cv_text = st.session_state.get("cv_text_val", cv_input_value)
jd_text = st.session_state.get("jd_text_val", "")

with col1:
    st.subheader(f"1. {lbl_cv}")
    cv_text_area = st.text_area("Paste CV text / ألصق نص السيرة:", value=cv_text, height=320, key="cv_area")
    st.session_state["cv_text_val"] = cv_text_area

with col2:
    st.subheader(f"2. {lbl_jd}")
    jd_text_area = st.text_area("Paste Job Description / ألصق الوصف الوظيفي:", value=jd_text, height=320, key="jd_area")
    st.session_state["jd_text_val"] = jd_text_area

st.markdown("---")
submit_btn = st.button(btn_analyze, type="primary", use_container_width=True)

# ==========================================
# 6. الربط الذكي مع الموديل ومعالجة البيانات
# ==========================================
if submit_btn:
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        st.error("🔒 API Key is missing. Please check your .env file.")
    elif not cv_text_area.strip() or not jd_text_area.strip():
        st.warning("⚠️ Please provide both CV and Job Description to proceed.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # برومبت صارم يجبر الموديل على إرسال مخرجات بصيغة JSON نظيفة لتحويلها لعناصر بصرية في الواجهة
            prompt = f"""
            You are an elite ATS system and an expert Executive Career Coach.
            Compare the user's CV against the target Job Description (JD).
            
            You must respond ONLY with a valid JSON object. Do not include any markdown formatting like ```json ... ``` in your raw output. 
            The JSON structure must match this scheme exactly:
            {{
                "score": 75,
                "grade": "Excellent Match / Good Match / Needs Improvement",
                "grade_color": "#10B981 for green, #F59E0B for orange, #EF4444 for red",
                "matched_keywords": ["keyword1", "keyword2"],
                "missing_keywords": ["keyword3", "keyword4"],
                "actionable_tips": ["tip1", "tip2"],
                "optimized_summary": "An optimized 2-3 sentence resume summary tailor-made for this JD.",
                "cover_letter": "A highly customized professional cover letter based on this CV and JD.",
                "interview_prep": [
                    {{"question": "Question 1?", "answer": "Suggested bulletproof answer based on CV background."}}
                ]
            }}
            
            ---
            CV Text:
            {cv_text_area}
            
            ---
            Job Description:
            {jd_text_area}
            """
            
            with st.spinner("🤖 AI is deeply analyzing skills match, weights, and scoring metrics..."):
                response = model.generate_content(prompt)
                
                # تنظيف النص المسترجع للتأكد من خلوه من علامات الماركداون الزائدة
                raw_text = response.text.strip()
                if raw_text.startswith("```json"):
                    raw_text = raw_text.replace("```json", "", 1)
                if raw_text.endswith("```"):
                    raw_text = raw_text[:-3]
                raw_text = raw_text.strip()
                
                # تفكيك الـ JSON
                data = json.loads(raw_text)
                
                # إظهار النتائج
                st.success(f"✅ {lbl_result}")
                
                # عرض كرات التقييم والـ Pills الملونة
                score = data.get("score", 0)
                grade = data.get("grade", "Needs Analysis")
                color = data.get("grade_color", "#334155")
                
                col_metric, col_desc = st.columns([1, 2])
                
                with col_metric:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div style="color: #94A3B8; font-size: 16px; font-weight: 600;">ATS MATCH SCORE</div>
                        <div class="score-circle" style="color: {color};">{score}%</div>
                        <div style="background-color: {color}22; color: {color}; padding: 6px 12px; border-radius: 8px; display: inline-block; font-weight: 700; font-size: 14px;">
                            {grade}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_desc:
                    st.write("### 🔑 Keyword & Skill Highlight")
                    st.write("**Matched Skills / الكلمات المتطابقة:**")
                    matched_html = "".join([f'<span class="pill-matched">{kw}</span>' for kw in data.get("matched_keywords", [])])
                    st.markdown(matched_html or "No exact matches found.", unsafe_allow_html=True)
                    
                    st.write("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
                    st.write("**Missing Keywords / الكلمات الناقصة:**")
                    missing_html = "".join([f'<span class="pill-missing">{kw}</span>' for kw in data.get("missing_keywords", [])])
                    st.markdown(missing_html or "No missing key skills found!", unsafe_allow_html=True)

                # تبويبات التنقل التفاعلية للنتائج المتقدمة
                tab_feedback, tab_summary, tab_letter, tab_interview = st.tabs([
                    "📋 Improvement Feedback", 
                    "✨ Tailored CV Summary", 
                    "✉️ Cover Letter Generator", 
                    "🎤 Custom Interview Prep"
                ])
                
                with tab_feedback:
                    st.write("### 💡 Recommended Improvements")
                    for tip in data.get("actionable_tips", []):
                        st.markdown(f"- {tip}")
                
                with tab_summary:
                    st.write("### ✨ Professional Summary")
                    st.info(data.get("optimized_summary", ""))
                    st.caption("💡 Tip: Replace your current CV summary with this optimized version to boost ATS scores instantly.")
                
                with tab_letter:
                    st.write("### ✉️ AI-Generated Cover Letter")
                    st.text_area("Tailored Cover Letter:", value=data.get("cover_letter", ""), height=300)
                    st.caption("💡 Copy and edit this letter to match the company name before applying.")
                
                with tab_interview:
                    st.write("### 🎤 Customized Interview Prep questions")
                    st.write("Based on the gaps in your CV relative to the target job description, practice these specific questions:")
                    for idx, qa in enumerate(data.get("interview_prep", [])):
                        with st.expander(f"Question {idx+1}: {qa.get('question')}"):
                            st.write(f"**Suggested Strategy / Answer:**\n{qa.get('answer')}")
                            
        except json.JSONDecodeError:
            st.error("❌ Failed to parse the AI response. Please try clicking the analyze button again.")
        except Exception as e:
            st.error(f"❌ Connection error: {str(e)}")

# ==========================================
# 7. التذييل وكتابة الأسماء (تأكد من تعديل الأسماء هنا)
# ==========================================
st.markdown("---")
st.caption("Developed by: **Meshal&Mishari** | Selected Topics - Almaarefa University")