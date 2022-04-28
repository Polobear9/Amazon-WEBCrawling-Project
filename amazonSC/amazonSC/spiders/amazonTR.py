from cgitb import text
from fake_useragent import UserAgent
from amazonSC.items import AmazonscItem
import scrapy
import datetime
import re


class AmazontrSpider(scrapy.Spider):
    name = 'amazonTR'
    allowed_domains = ['www.amazon.co.jp']
    start_urls = ['https://www.amazon.co.jp/s?k=%E9%9E%84+%E7%89%9B%E9%9D%A9&i=shoes&rh=n%3A2016926051%2Cn%3A2221077051%2Cn%3A2221075051%2Cn%3A5355945051%2Cn%3A2221189051&dc&crid=3A8WZ8BV4QTT9&qid=1651157186&rnid=2016926051&sprefix=%E9%9E%84+gyuukawa%2Caps%2C177&ref=sr_nr_n_1']
    #基本検索　URL　：　https://www.amazon.co.jp/s?k=
    #タブレット　：　&rh=n%3A2152014051&dc&qid=1650883326&rnid=2321267051&ref=sr_nr_n_1
    #スマートフォン　：　&rh=n%3A2497181051&dc&qid=1650883483&rnid=2321267051&ref=sr_nr_n_2
    #ノートパソコン　：　&rh=n%3A2151981051&dc&qid=1650883508&rnid=2321267051&ref=sr_nr_n_3
    #家電＆カメラ　：　&i=electronics&dc&qid=1650883534&rnid=2321267051&ref=sr_nr_i_10

    print("keyword" , start_urls)

    def parse(self, response):
        for amazonD in response.xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div'):
            Amazon_Title = amazonD.css('h2 > a > span::text').get()
            Amazon_Price = amazonD.css('span.a-price-whole::text').get()
            Amazon_Brand = amazonD.css('div > h5 > span::text').get()
            Amazon_Star = amazonD.css('div > span:nth-child(1) > span > a > i > span::text').get()
            Amazon_review = amazonD.css('div:nth-child(n) > div > span:nth-child(2) > a > span::text').get()
            Amazon_asin = amazonD.xpath('./@data-asin').extract()
            
            print(Amazon_Title,Amazon_Price,Amazon_Brand,Amazon_Star,Amazon_review,Amazon_asin)
            
            item = AmazonscItem()
            item['Amazon_Brand'] = Amazon_Brand
            item['Amazon_Title'] = Amazon_Title
            item['Amazon_Price'] = Amazon_Price
            item['Amazon_Star'] = Amazon_Star
            item['Amazon_review'] = Amazon_review
            item['Amazon_asin'] = Amazon_asin
            yield item 
        next_page = response.css('div > div >span > a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator::attr(href)').get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
            
def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]' , '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','', cleaned_text)
    return cleaned_text
        