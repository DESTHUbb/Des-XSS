# 𝔻𝕖𝕤-𝕏𝕊𝕊
![Des-xss](https://github.com/DESTHUbb/Des-XSS/assets/90658763/49830780-f4c7-47db-afb9-179f8181b83a)

![found](https://img.shields.io/badge/found-200%2B%20xss-red)
[![issues](https://img.shields.io/github/issues/DESTHUbb/Des-XSS)](https://github.com/DESTHUbb/Des-XSS/issues)
[![release](https://img.shields.io/badge/release-v2.0--beta-blue)](https://github.com/ESTHUbb/Des-XSS/releases)
[![license](https://img.shields.io/github/license/DESTHUbb/Des-XSS)](https://github.com/DESTHUbb/Des-XSS/blob/master/LICENSE)


## Des-XSS is a quick tool that scans millions of URLs for cross-site scripting vulnerabilities. It has found XSS vulnerabilities in bug bounty programs.

# Features
+ Fast and suitable for testing millions of urls
+ Support Dom-based xss(use Chrome or Phantomjs) and reflected xss
+ Only use 8 Payloads based on injection postion now(not fuzz,more accurate,faster)
+ Async request(use gevent) and Multi-processed
+ Support single url,file and traffic from Burpsuite
+ Traffic filter based on interface
+ Support speicial headers(referer,cookie,customized token,e.g.)
+ Support rescan quickly by id
# Directory
```python
├── engine.py
├── logo
├── cookie.py
├── url.txt
├── cookie
│   └── test.com_cookie
├── traffic
│   ├── 49226b2cbc77b71b.traffic    #traffic file(pickled)
│   └── 49226b2cbc77b71b.reflect    #reflected file(pickled)
├── config.py
├── start.py
├── url.txt.filtered    #filtered urls
├── util.py
├── README.md
├── banner.py
├── requirements.txt
├── result
│   └── 49226b2cbc77b71b-2019_10_29_11_24_44.json   #result
├── model.py
└── test.py
```
# Screenshot 
![s1](https://github.com/lwzSoviet/download/blob/master/images/s1.png)  
# Environment
Linux  
Python2.7  
Browser:Phantomjs or Chrome
# Install
### Ubuntu
+ 1.`apt-get install flex bison phantomjs`
+ 2.`pip install -r requirements.txt`
### Centos
+ 1.`yum install flex bison phantomjs`
+ 2.`pip install -r requirements.txt`
### MacOS
+ 1.`brew install grep findutils flex phantomjs`
+ 2.`pip install -r requirements.txt`  
-----
*If you want to scan use "--browser=chrome",you must install chrome mannually. You can use "--check" to test the installation.*  
`python start.py --check`
# Usage
```python

python start.py --url url --save
python start.py --url url --cookie cookie --browser chrome --save  
python start.py --url url --cookie cookie --browser chrome-headless --save  
python start.py --file ./url.txt --save  
python start.py --burp ./test.xml --save  
python start.py --file file --filter

```
# --Help  
**--url**&emsp;scan from url.  
**--id**&emsp;rescan from *.traffic file by task id.  
**--file**&emsp;scan urls from text file(like ./url.txt).  
**--burp**&emsp;scan *.xml(base64 encoded,like ./test.xml) from burpsuite proxy.  
**--process**&emsp;number of process.  
**--coroutine**&emsp;number of coroutine.    
**--cookie**&emsp;use cookie.  
**--filter**&emsp;filter urls.  
**--browser**&emsp;use browser(chrome,chrome-headless or phantomjs) to scan,it's good at DOM-based xss but slow.  
**--save**&emsp;save results to ./result/id.json.  
**--clear**&emsp;delete traffic files after scanning.
### How to scan data from Burpsuite
In Proxy,"Save items" ==> "test.xml"  
![image](https://github.com/DESTHUbb/Des-XSS/assets/90658763/abccd4c6-a454-41c4-8b93-b1dd857df4f5)
Then you can scan test.xml:  
`python start.py --burp=./test.xml`
### How to rescan
After scanning firstly,there will be taskid.traffic and taskid.reflect in ./traffic/:  
+ taskid.traffic: Web traffic of request(pickled).
+ taskid.reflect: Reflected result (pickled)that included reflected params,reflected position,type and others.  
Des-XSS will use these middle files to rescan:  
`python start.py --id taskid --save`
# How does Des-XSS work?
### Payloads
Des-XSS use only 8 payloads for scanning.These payloads are based on param's reflected position.Fewer payloads make it faster than fuzzing.
### Async&multi-process
Des-XSS is highly concurrent for using coroutine.
### Support dom-based xss
More and more page is using dom to render html.Des-XSS can parse it with using Phantomjs(default) or chrome.   
### Analysis files
Some xss is difficult to scan.Des-XSS will save some files in traffic/ for analysing,include:
+ *.traffic(traffic file during scanning)
+ *.reflect(param's reflected result)
+ *.redirect(30x response)
+ *.error(some error happened such as timeout,connection reset,etc.)
+ *.multipart(when request is multupart-formed,not easy to scan)
# Example
