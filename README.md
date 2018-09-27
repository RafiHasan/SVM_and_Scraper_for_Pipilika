# SVM_and_Scraper_for_Pipilika

##**TASK 1.1(spider latestnews.py):** <br />
(cmd scrapy run spider latestnews.py) <br />
1. Need to install scrapy(pip install scrapy) <br />
2. Also may need to install pywin32(pip install pywin32) <br />
3. Scraped data is stored in news.txt file <br />
4. data is formated as (title,date,Caterogy,details) <br />
5. 3200 scroll page is scraped <br />

##**TASK 1.2(project lastnews):** <br />
(cmd scrapy crawl lnews) <br />
1. Docker toolbox needs to be installed(https://docs.docker.com/toolbox/toolbox_install_windows) <br />
2. splash needs to be installed(pip install scrapy_splash) <br />
3. splash server needs to be running (https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash) <br />
4. In setting.py SPLASH_URL=docker url <br />
5. Scraped data is stored in latestnews.txt file <br />
6. data is formated as (Like,title,date,Caterogy,details)(like is -1 if could not find the link) <br />


##**TASK 2(MultiSVM.py):** <br />

1. sklearn need to be installed (pip install sklearn) <br />
2. svm.SVC is used which is a wrapper of libsvm <br />
3. param(C=1.4,Karnel='rbf',Gamma=.0008,Decision='ovo') <br />
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
