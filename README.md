<h1 align="center">
📖KnowledgeGPT
</h1>

<div id="top" align="center">

![GitHub](https://img.shields.io/github/license/mmz-001/knowledge_gpt)
![GitHub Repo stars](https://img.shields.io/github/stars/mmz-001/knowledge_gpt?style=social)
![GitHub forks](https://img.shields.io/github/forks/mmz-001/knowledge_gpt?style=social)
[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/mm_sasmitha)](https://twitter.com/mm_sasmitha)

</div>

คำตอบที่แม่นยำและการอ้างอิงเอกสารของคุณทันที PDF BY Mint Jiraphinya Wechabut

อัปโหลดเอกสารของคุณและรับคำตอบ สำหรับคำถามของคุณ พร้อมการอ้างอิงจากข้อความ
[Demo](https://twitter.com/mm_sasmitha/status/1620999984085884930)

## Installation การติดตั้ง

ทำตามคำแนะนำด้านล่างเพื่อเรียกใช้เซิร์ฟเวอร์ Streamlit ภายในเครื่อง

### Pre-requisites ข้อกำหนดเบื้องต้น

ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้ง Python ≥3.10 แล้ว

### Steps ขั้นตอนดังนี้

1. Clone the repository - โคลนพื้นที่เก็บข้อมูล

```bash
git clone https://github.com/mmz-001/knowledge_gpt
cd knowledge_gpt
```

2. Install dependencies with [Poetry](https://python-poetry.org/) and activate virtual environment

```bash
poetry install
poetry shell
```

3. (Optional) Avoid adding the OpenAI API every time you run the server by adding it to environment variables.
   - Make a copy of `.env.example` named `.env`
   - Add your API key to the `.env` file

> **Note:** Make sure you have a paid OpenAI API key for faster completions and to avoid hitting rate limits.

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

## Contributing

All contributions are welcome!

## Contributors

Big thanks to the following people for their contributions!

<a href="https://github.com/mmz-001/knowledge_gpt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=mmz-001/knowledge_gpt" />
</a>

## License

Distributed under the MIT License. See [LICENSE](https://github.com/mmz-001/knowledge_gpt/blob/main/LICENSE) for more information.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=mmz-001/knowledge_gpt&type=Date)](https://star-history.com/#mmz-001/knowledge_gpt&Date)
