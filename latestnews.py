# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:34:21 2018

@author: Rafi



"""

import scrapy
import codecs

class SingleQuoteSpider(scrapy.Spider):
    #name of the spyder which will be called from scrapy
    name = 'latestnews'
    #the spider will not leave this domain
    allowed_domains = ['dailyjanakantha.com']
    #defines where our spider will start crawling from
    start_urls = ['http://www.dailyjanakantha.com/online']
    #file where the output data is stored
    file=codecs.open('news.txt', 'a','utf-8')
    #view more news buttons request link
    form_urls='http://www.dailyjanakantha.com/pages/newsListOnline_ext.php?p=online'
    #scroll page count used for tracking current scroll page
    page=0
    
    
    #when spider is called this method executes and all the other code are excessed in here
    def parse(self, response):
        #response hold our data of a single request
        #our desired data are in div with css class listDivImg
        #response.css returns a list we will iterate through it
        for quote in response.css('div.listDivImg'):
            
            #here we extract the detail pages url
            urls = quote.css('h1.recentNewsHead > a::attr(href)').extract_first()
            
            
            #creating a dictionary
            item = {
                'title': quote.css('h1.recentNewsHead > a::text').extract_first(),
                'publish date': quote.css('span.published::text').extract_first(),
                'category': quote.css('div.listDivImg > a::text').extract_first(),
                
            }
            
            #following the ling retrived previously to find more data
            request=scrapy.Request(url=urls, callback=self.parse_details)
            #passing current dictionary in metadata to the next function
            request.meta['item'] = item
            #returning the data retrived by parse_details
            yield request
        #number of page we will extract
        if   self.page<3200:
            self.page=self.page+1
            frmdata={"Ymd":str(self.page),"dispId":"Ymd"+str(self.page),"actionLink":self.form_urls,"bik":"1"}
            yield scrapy.FormRequest(url=self.form_urls, callback=self.parse ,method='post',formdata=frmdata)     
            
            
    #prsing the detailpage
    def parse_details(self, response):
        #retriving the metadata
        #and ading new data to it
        item = response.meta['item']
        item['details'] = response.css('div.artContent > p::text').extract()
       # item['like']=response.css('div._5n6j _5n6l > span::text').extract_first()
       # item['share']= response.css('div.fbLike > span.st_facebook_hcount >span.stBubble_hcount::text').extract_first()

        #writing it into a file
        self.file.write(item['title']+","+item['publish date']+","+item['category']+","+' '.join(item['details']))
        
        yield item