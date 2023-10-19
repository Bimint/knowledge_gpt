<h1 align="center">
📖สร้างฐานการเรียนรู้ เอกสาร ด้วย gpt
</h1>

<div id="top" align="center">




</div>

คำตอบที่แม่นยำและการอ้างอิงเอกสารของคุณทันที PDF BY มิ้น จิรภิญญา เวชบุตร 

[ตัวอย่าง](https://jiraphinya.streamlit.app)

## Installation การติดตั้ง

ทำตามคำแนะนำด้านล่างเพื่อเรียกใช้เซิร์ฟเวอร์ Streamlit ภายในเครื่อง

### Pre-requisites ข้อกำหนดเบื้องต้น

ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้ง Python ≥3.10 แล้ว

### Steps ขั้นตอนดังนี้

1. Clone the repository - โคลนพื้นที่เก็บข้อมูล

```bash
git clone https://github.com/Bimint/knowledge_gpt.git
```

2. Install dependencies with [Poetry](https://python-poetry.org/) and activate virtual environment

```bash
poetry install
poetry shell
```

3. (Optional) หลีกเลี่ยงการเพิ่ม OpenAI API ทุกครั้งที่คุณเรียกใช้เซิร์ฟเวอร์โดยการเพิ่มลงในตัวแปรสภาพแวดล้อม (ไม่บังคับเเล้วเเต่ความสะดวกผู้ใช้งาน).
   - Make a copy of `.env.example` named `.env`
   - Add your API key to the `.env` file

> **Note:** ตรวจสอบให้แน่ใจว่าคุณมีคีย์ OpenAI API แบบชำระเงินเพื่อให้ทำงานเสร็จเร็วขึ้น และเพื่อหลีกเลี่ยงไม่ให้ถึงขีดจำกัดของอัตรา(ไม่บังคับจะใช้ฟรีก็ได้ค่ะ)

4. Run the Streamlit server

```bash
cd knowledge_gpt
streamlit run main.py
```

## Build with Docker - สร้างด้วย Docker

รันคำสั่งต่อไปนี้เพื่อสร้างและรันอิมเมจ Docker
```bash
cd knowledge_gpt
docker build -t knowledge_gpt .
docker run -p 8501:8501 knowledge_gpt
```

Open http://localhost:8501 in your browser to access the app.

## Customization

คุณสามารถเพิ่มขนาดไฟล์อัพโหลดสูงสุดได้โดยการเปลี่ยนแปลง `maxUploadSize` ใน `.streamlit/config.toml`.
ปัจจุบัน ขนาดอัพโหลดสูงสุดคือ 25 MB สำหรับเวอร์ชันที่โฮสต์

## Tech Stack

- User Interface - [Streamlit](https://streamlit.io/)
- LLM Tooling - [Langchain](https://github.com/hwchase17/langchain)

## Roadmap

- Add support for more formats (e.g. webpages, PPTX, etc.)
- Highlight relevant phrases in citations
- Support scanned documents with OCR
- More customization options (e.g. chain type, chunk size, etc.)
- Visual PDF viewer
- Support for Local LLMs



