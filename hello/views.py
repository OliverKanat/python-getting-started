from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def home(request):
    parsed_entries = []
    feed_url = ''
    selected = "desc"
    if request.POST:
        print(request.POST)
        feed_url = request.POST["rss_feed"]
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            parsed_entries.append({"title": entry.title, "date": datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z"), "img": entry.links[0].href, "link": entry.link,
                                   "sum": entry.summary})
        reverse = True
        if request.POST["sort"] == "asc":
            reverse = False
            selected = "asc"
        parsed_entries = sorted(parsed_entries, key=lambda i: i['date'], reverse=reverse)

    return render(request, "home.html", {"entries": parsed_entries,
                                         "feed_url": feed_url,
                                         "selected": selected})