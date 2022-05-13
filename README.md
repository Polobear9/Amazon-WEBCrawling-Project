# WEBCrawling-Project

this project is my first python web crawling project.

crawling is use a library 'scrapy'

this project is for crawl the web site 'amazon'
you can import the keyword and cartegory.


WEB crawling

it is my frist WEB crawling code of python.
amazon crawling file.

i want do crawling use a keyword. use a URL method but i can't now. [i need to study]
ex. keyword is 'bag' maybe it is work?

keyword = '...#$#$'

and i want search more detail look like 'https//...amazon search URL' + 'keyword' + 'cartegory is URL'

class AmazontrSpider(scrapy.Spider):
name = 'amazonTR'
allowed_domains = ['www.amazon.co.jp']
start_urls = ['https://www.amazon.co.jp/s?k='] + (keyword) ?

keyword= 'iphone13pro512gb'

smp = '&rh=n%3A2497181051&dc&qid=1650883483&rnid=2321267051&ref=sr_nr_n_2'
start_urls = ['https://www.amazon.co.jp/s?k=' + str(keyword) + str(smp)] it is work.
but i want set a cartegory a number['1','2','3'....els]
1 = smartphone
2 = tablet
3 = camera ... els

but i can't i need study.

i want crawling the item html not only list. but now i cant not [i need to study]
*item['Amazon_Title'] = Amazon_Title <-get a url. and crawling that item is html..
maybe i think it is similar to next page method. [it is just my mind]

still i colud not understand how next_page method is work.

i need to study of method 'return' i colud not understand what return do act in python.

i want crawling
