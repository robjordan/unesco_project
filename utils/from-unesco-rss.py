import feedparser
u = feedparser.parse('http://whc.unesco.org/en/list/rss/')
u['feed']['title']
