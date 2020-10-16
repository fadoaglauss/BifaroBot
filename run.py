import datetime
from crawler.scheduler import Scheduler
from crawler.page_fetcher import PageFetcher
from crawler.domain import Domain
from crawler.scheduler import Scheduler
from urllib.parse import urlparse
from multiprocessing import Process

pages_fetchers = []
pages_fetchers_limit = 60
inicio = datetime.datetime.now()

arr_str_urls_seeds = ["http://cnn.com/",
                      "https://pt.wikipedia.org/wiki/House,_M.D./", "https://globoesporte.globo.com/"]
arr_urls_seeds = [(urlparse(str_url), 0) for str_url in arr_str_urls_seeds]
scheduler = Scheduler(str_usr_agent="bifaroBot", int_page_limit=1000,
                      int_depth_limit=6, arr_urls_seeds=arr_urls_seeds)

for a in range(0, pages_fetchers_limit):
    pages_fetchers.append(PageFetcher(scheduler))

proc = []
for pages_fetcher in pages_fetchers:
    p = Process(target=pages_fetcher.run())
    p.start()
    proc.append(p)
for p in proc:
    p.join()

fim = datetime.datetime.now()
print(f"Tempo gasto: {(fim-inicio).total_seconds()}")

with open("docs/times.txt", "a", encoding="utf-8") as file:
    file.write(
        f"Quantidade escalonadores: {pages_fetchers_limit};Tempo gasto: {(fim-inicio).total_seconds()}\n")
