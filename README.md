# 🌍 Regional News Aggregator

This is a simple Flask-based web app that aggregates news from 16 MENA countries using RSS feeds and displays the top 5 latest articles from each.

---

## 📦 Features

- Aggregates RSS feeds from:
  **Syria, Iraq, Lebanon, Egypt, Algeria, Sudan, Somalia, Qatar, Mauritania, Jordan, Palestine, Israel, Morocco, Tunisia, Libya, Yemen**
- Built with `Flask` + `feedparser`
- Fully deployable on [Render](https://render.com)

---

## 🚀 How to Deploy on Render

### 1. Create a New Web Service
- Visit [https://dashboard.render.com](https://dashboard.render.com)
- Click **New Web Service**
- Choose **"Deploy from a Git repository"**
- Use this project zipped or upload the files to GitHub first

### 2. Configure Deployment

#### Build & Start Settings:

- **Runtime**: Python 3
- **Start Command**:
  ```
  gunicorn app:app
  ```

- **Build Command**: *(leave empty or default)*

#### Add a file named `render.yaml` to your repo:
```yaml
services:
  - type: web
    name: news-aggregator
    env: python
    buildCommand: ""
    startCommand: "gunicorn app:app"
    plan: free
```

---

## 🖥 Local Development (Optional)

If you want to run the app locally:
```bash
pip install flask feedparser
python app.py
```
Then go to `http://localhost:5000`

---

## 🧠 Credits

Developed as a lightweight aggregator using public news sources and open technologies.

