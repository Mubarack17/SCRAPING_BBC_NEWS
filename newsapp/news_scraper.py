import feedparser

def get_bbc_news():
    rss_url = "http://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(rss_url)
    news_list = []

    for entry in feed.entries[:10]:
        title = entry.title
        link = entry.link

        # Try to get image
        image_url = "https://via.placeholder.com/300x200"  # default placeholder

        # Check if media_thumbnail exists
        if 'media_thumbnail' in entry:
            image_url = entry.media_thumbnail[0]['url']
        # Sometimes media_content is used
        elif 'media_content' in entry:
            image_url = entry.media_content[0]['url']

        news_list.append((title, link, image_url))

    return news_list

