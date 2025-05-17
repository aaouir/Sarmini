from flask import Flask, render_template_string
import feedparser
import datetime

app = Flask(__name__)

RSS_FEEDS = {
    'Syria': 'https://www.sana.sy/en/?feed=rss2',
    'Iraq': 'https://www.iraqinews.com/feed/',
    'Lebanon': 'https://www.dailystar.com.lb/RSS.aspx?id=1',
    'Egypt': 'https://english.ahram.org.eg/UI/Front/inner.aspx?NewsPortalID=3',
    'Algeria': 'https://www.aps.dz/en/component/k2/k2.itemlist?format=feed',
    'Sudan': 'http://sudantribune.com/spip.php?page=backend',
    'Somalia': 'https://www.hiiraan.com/rss.xml',
    'Qatar': 'https://www.gulf-times.com/rss',
    'Mauritania': 'http://cridem.org/RSS.xml',
    'Jordan': 'https://jordantimes.com/rss.xml',
    'Palestine': 'http://english.wafa.ps/rss.aspx',
    'Israel': 'https://www.jpost.com/Rss/RssFeedsHeadlines.aspx',
    'Morocco': 'https://www.moroccoworldnews.com/feed',
    'Tunisia': 'https://www.tap.info.tn/en/rss',
    'Libya': 'https://www.libyaobserver.ly/rss.xml',
    'Yemen': 'https://www.almashhad-alyemeni.com/rss.xml',
}

latest_news = {}

def fetch_news():
    global latest_news
    latest_news = {}
    for country, url in RSS_FEEDS.items():
        try:
            feed = feedparser.parse(url)
            if feed.entries:
                latest_news[country] = feed.entries[:5]
            else:
                latest_news[country] = []
        except Exception as e:
            latest_news[country] = [{'title': f"Error fetching news: {e}", 'link': "#"}]
    print(f"News updated at {datetime.datetime.now()}")

fetch_news()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Regional News Aggregator</title>
    <link href='https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css' rel='stylesheet'>
</head>
<body class='bg-gray-100 font-sans'>
    <div class='max-w-5xl mx-auto py-8'>
        <h1 class='text-3xl font-bold mb-4 text-center'>Regional News Aggregator</h1>
        {% for country, articles in news.items() %}
        <div class='bg-white p-4 rounded shadow mb-6'>
            <h2 class='text-xl font-semibold mb-2'>{{ country }}</h2>
            <ul class='list-disc pl-6'>
                {% for article in articles %}
                <li class='mb-1'>
                    <a href='{{ article.link }}' target='_blank' class='text-blue-600 hover:underline'>{{ article.title }}</a>
                </li>
                {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    fetch_news()
    return render_template_string(HTML_TEMPLATE, news=latest_news)
