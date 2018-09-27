# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 07:11:52 2018

@author: Rafi
"""

import scrapy
from scrapy_splash import SplashRequest
import codecs

class QuotesJSSpider(scrapy.Spider):
    name = 'lnews'
    # all these settings can be put in your project's settings.py file
    
    #the spider will not leave this domain
    #allowed_domains = ['dailyjanakantha.com','facebook.com']
    #defines where our spider will start crawling from
    start_urls = ['http://www.dailyjanakantha.com/online']
    #file where the output data is stored
    file=codecs.open('newslike.txt', 'a','utf-8')
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
            #first it is rendered through splash
            request=SplashRequest(url=urls,callback=self.parse_details)
           # scrapy.Request(url=urls, callback=self.parse_details)
            #passing current dictionary in metadata to the next function
            request.meta['item'] = item
            #returning the data retrived by parse_details
            yield request
        #number of page we will extract
        if   self.page<350:
            self.page=self.page+1
            #form data to create a formrequest for scroll button
            frmdata={"Ymd":str(self.page),"dispId":"Ymd"+str(self.page),"actionLink":self.form_urls,"bik":"1"}
            yield scrapy.FormRequest(url=self.form_urls, callback=self.parse ,method='post',formdata=frmdata)     
            
            
    #prsing the detailpage
    def parse_details(self, response):
        #retriving the metadata
        #and ading new data to it
        
        item = response.meta['item']
        #adding detail news to item
        item['details'] = response.css('div.artContent > p::text').extract()
        
        
        #finding if an url exist for facebooklike 
        #splash cant always render this data so some iframe url is missing
        urls = response.css('iframe::attr(src)').extract()
        for i in urls:
            if i.find("like.php")>-1:
                url=i
                break
            else:
                url="nourl"
                

        #writing it into a file
        
        if url=="nourl":
            item['like']="-1"
            self.file.write(item['like']+","+item['title']+","+item['publish date']+","+item['category']+","+' '.join(item['details']))
            yield item
        else:
            #if an url is found like count is scraped
            request=SplashRequest(url=url, callback=self.parse_iframe)
            request.meta['item'] = item
            yield request
        
        
        
        
        
        
    
    def parse_iframe(self, response):
        item =response.meta['item']
        #like count is stored in span id-u_0_1
        item['like']=response.css('span#u_0_1::text').extract_first()
        self.file.write(item['like']+","+item['title']+","+item['publish date']+","+item['category']+","+' '.join(item['details']))
        
        yield item