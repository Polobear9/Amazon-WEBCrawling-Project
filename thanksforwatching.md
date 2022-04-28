# WEB crawling

it is my frist WEB crawling code of python.<br>
amazon crawling file. <br>
<br>
i want do crawling use a keyword. use a URL method but i can't now. [i need to study]<br>
ex. keyword is 'bag' maybe it is work?<br>
<br>
keyword = '...#$#$'<br>
<br>
and i want search more detail look like 'https//...amazon search URL' + 'keyword' + 'cartegory is URL'<br>
<br>
class AmazontrSpider(scrapy.Spider):<br>
    name = 'amazonTR'<br>
    allowed_domains = ['www.amazon.co.jp']<br>
    start_urls = ['https://www.amazon.co.jp/s?k='] + (keyword) ?<br>
    <br>
keyword= 'iphone13pro512gb'<br>
<br>
smp = '&rh=n%3A2497181051&dc&qid=1650883483&rnid=2321267051&ref=sr_nr_n_2'<br>
start_urls = ['https://www.amazon.co.jp/s?k=' + str(keyword) + str(smp)]<br>
it is work. but i want set a cartegory a number['1','2','3'....els]<br>
1 = smartphone<br>
2 = tablet<br>
3 = camera ... els<br>
<br>
but i can't i need study.<br>
<br>
i want crawling the item html not only list. but now i cant not [i need to study]<br>
*item['Amazon_Title'] = Amazon_Title <-get a url. and crawling that item is html..<br>
maybe i think it is similar to next page method. [it is just my mind]<br>
<br>
still i colud not understand how next_page method is work.<br>
<br>
i need to study of method 'return' i colud not understand what return do act in python.<br>
<br>
i want crawling<br>
