import feedparser
from feedgen.feed import FeedGenerator
import time

# Fetch latest feed
url = 'https://developer.apple.com/news/releases/rss/releases.rss'
latest_feed = feedparser.parse(url)

# Create new feed
fg = FeedGenerator()
fg.title('iOS Beta Updates')
fg.link(href='https://github.com/ryanpato/ios-beta-releases-rss/raw/main/ios-beta-feed.xml')
fg.description('This feed contains only iOS beta updates.')

# Add new items to feed
for entry in latest_feed.entries:
    if 'iOS' in entry.title and ('beta' in entry.title or 'RC' in entry.title):
        fe = fg.add_entry()
        fe.title(entry.title)
        fe.link(href=entry.link)
        fe.published(time.strftime('%Y-%m-%dT%H:%M:%SZ', entry.published_parsed))

# Format new feed
rss_feed = fg.rss_str(pretty=True)

# Save new feed to file
with open('ios-beta-feed.xml', 'wb') as f:
    f.write(rss_feed)
