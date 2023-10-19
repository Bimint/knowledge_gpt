import streamlit as st

from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## วิธีใช้งาน\n"
            "1. ป้อนคีย์ api ส่วนตัวของคุณ [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. อัพโหลด a pdf, docx, or txt file📄\n"
            "3. ถามคำถามเกี่ยวกับเอกสาร💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖KnowledgeGPT ช่วยให้คุณสามารถถามคำถามเกี่ยวกับ "
            "เอกสารและรับคำตอบที่แม่นยำพร้อมการอ้างอิงทันที. "
        )
        st.markdown(
            "จากใจ:โครงการทดลองเพื่อใช้ประโยชน์ร่วมกัน"
            "หากต้องการศึกษารายละเอียดเพิ่มเติม [GitHub](https://github.com/Bimint/knowledge_gpt) "  # noqa: E501
            "หรือสนันสนุน ทุนการศึกษา น้องจะยินดีมากๆค่ะ💡"
            "มิ้น-มิว:จิรภิญญา-ปรีดิ์ปราโมทย์💡"
        )
        st.markdown("Made by [มิ้น จิรภิญญา](https://medium.com/@mint-jiraphinya)")
        st.markdown("---")

        faq()
