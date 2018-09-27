# SVM_and_Scraper_for_Pipilika (Python 3.5)

##**TASK 1.1(spider latestnews.py):** <br />
(cmd scrapy genspider latestnews (for creating the spider) , scrapy run spider latestnews.py (for start crawling)) <br />
1. Need to install scrapy(pip install scrapy) <br />
2. Also may need to install pywin32(pip install pywin32) <br />
3. Scraped data is stored in news.txt file <br />
4. data is formated as (title,date,Caterogy,details) <br />
5. 121829 news article is scraped (https://drive.google.com/drive/folders/1i9-rdcnhDTKcT_QaVCUPVKruz9g4KadO?usp=sharing) <br />

##**TASK 1.2(project lastnews):** <br />
(cmd scrapy startproject lastnews (for creating project), scrapy crawl lnews(for start crawling)) <br />
<br />
Previous part of the task one can only crawl into pages and collect raw html data. But the detail news page also contains total number of people liked the news which is controlled by js and dynamically created. For that scrapy cant directly excess it. For that this part is used splash(a js rendarer) for parsing the js genarated data into regular html so that scrapy can scrap them.Sometimes splash cant render the full page so some of the likecount data is missing.
<br />
<br />
1. Docker toolbox needs to be installed(https://docs.docker.com/toolbox/toolbox_install_windows) <br />
2. splash needs to be installed(pip install scrapy_splash) <br />
3. splash server needs to be running (https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash) also in run command must include --disable-private-mode <br />
4. In settings.py include <br /> SPLASH_URL=docker url <br /> DOWNLOADER_MIDDLEWARES= {
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
        } <br />SPIDER_MIDDLEWARES= {
            'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
        } <br /> DUPEFILTER_CLASS= 'scrapy_splash.SplashAwareDupeFilter' <br /> HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage' <br /> ROBOTSTXT_OBEY = False <br />
5. Scraped data is stored in newslike.txt file <br />
6. data is formated as (Likecount,title,date,Caterogy,details)(like is -1 if could not find the link) <br />
7. 10137 news is scraped (https://drive.google.com/drive/folders/1i9-rdcnhDTKcT_QaVCUPVKruz9g4KadO?usp=sharing) <br />


##**TASK 2(MultiSVM.py):** <br />

1. sklearn need to be installed (pip install sklearn) <br />
2. svm.SVC is used which is a wrapper of libsvm <br />
3. data is loaded with load_svmlight_file and features and levels are converted to numpy array <br />
3. param(C=1.4,Karnel='rbf',Gamma=.0008,Decision='ovo') is used as it gave the best result for given dataset <br />
4. result of svm is <br />
	accuracy=0.9153318077803204 <br />
	confution matrix= <br />
[[427   8   4   5   0   1   1] <br />
 [  4 492   2  11   6   2   5] <br />
 [  3   4 767  12   8  23  11] <br />
 [  1   7   6 420  14   1   1] <br />
 [  1  18  28   9 502   2  20] <br />
 [  1   0  33   4   1 506  11] <br />
 [  0   5   7  13  23  10 486]] <br />
