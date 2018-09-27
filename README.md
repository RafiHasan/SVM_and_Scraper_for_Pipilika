# SVM_and_Scraper_for_Pipilika

TASK 1.1(spider latestnews.py):
(cmd scrapy run spider latestnews.py)
1.Need to install scrapy(pip install scrapy)
2.Also may need to install pywin32(pip install pywin32)
3.Scraped data is stored in news.txt file
4.data is formated as (title,date,Caterogy,details)
5.3200 scroll page is scraped

TASK 1.2(project lastnews):
(cmd scrapy crawl lnews)
1.Docker toolbox needs to be installed(https://docs.docker.com/toolbox/toolbox_install_windows)
2.splash needs to be installed(pip install scrapy_splash)
3.splash server needs to be running (https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash)
4.In setting.py SPLASH_URL=docker url
5.Scraped data is stored in latestnews.txt file
6.data is formated as (Like,title,date,Caterogy,details)(like is -1 if could not find the link)


TASK 2(MultiSVM.py):

1.sklearn need to be installed
2.svm.SVC is used which is a wrapper of libsvm
3.result of svm is
	accuracy=0.9153318077803204
	confution matrix=
[[427   8   4   5   0   1   1]
 [  4 492   2  11   6   2   5]
 [  3   4 767  12   8  23  11]
 [  1   7   6 420  14   1   1]
 [  1  18  28   9 502   2  20]
 [  1   0  33   4   1 506  11]
 [  0   5   7  13  23  10 486]]