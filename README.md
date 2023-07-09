# 𝔻𝕖𝕤-𝕏𝕊𝕊
![Des-xss](https://github.com/DESTHUbb/Des-XSS/assets/90658763/5a62d599-2905-47aa-aa81-cae3ce7894cc)

![found](https://img.shields.io/badge/found-200%2B%20xss-red) [![issues](https://img.shields.io/github/issues/DESTHUbb/Des-XSS)](https://github.com/DESTHUbb/Des-XSS/issues) ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=flat-square) [![Python](https://img.shields.io/badge/Python-%E2%89%A5%203.6-yellow.svg)](https://www.python.org/) <img src="https://img.shields.io/badge/Developed%20on-Ubuntu-blueviolet">
 [![release](https://img.shields.io/badge/release-v2.0--beta-blue)](https://github.com/ESTHUbb/Des-XSS/releases) [![license](https://img.shields.io/github/license/DESTHUbb/Des-XSS)](https://github.com/DESTHUbb/Des-XSS/blob/master/LICENSE)

## Des-XSS is a quick tool that scans millions of URLs for cross-site scripting vulnerabilities. It has found XSS vulnerabilities in bug bounty programs.

## I'm still working on improving the program¡¡

# Features
+ Fast and suitable for testing millions of urls
+ Support Dom-based xss(use Chrome or Phantomjs) and reflected xss
+ Only use 8 Payloads based on injection postion now(not fuzz,more accurate,faster)
+ Async request(use gevent) and Multi-processed
+ Support single url,file and traffic from Burpsuite
+ Traffic filter based on interface
+ Support speicial headers(referer,cookie,customized token,e.g.)
+ Support rescan quickly by id
# Upcoming py3 features:
### What are the improvements?
+ Improved Unicode handling: Python 3 has better support for Unicode, making it easier to handle non-ASCII characters and strings.
+ Performance improvement: Python 3 has better performance than Python 2.7, which can make your program faster and more efficient.
+ Improved security: Python 3 has better security features, such as better exception handling and better support for SSL/TLS.
+ Improved syntax and features: Python 3 has introduced many new features and syntax improvements that can make your code more concise and readable.
+ Better support for asyncio: Python 3 has better support for asynchronous programming, which can make your program more efficient and scalable.
+ Improved libraries and modules: Python 3 has many new and improved libraries and modules that can make it easier to develop your program.
+ Support for modern tools and technologies: Python 3 is more compatible with modern tools and technologies, such as Docker and Kubernetes, which can make it easier to deploy and manage your program.

# Directory
```python
├── engine.py
├── logo
├── cookie.py
├── url.txt
├── cookie
│   └── test.com_cookie
├── traffic
│   ├── ****************.traffic    #traffic file(pickled)
│   └── ****************.reflect    #reflected file(pickled)
├── config.py
├── start.py
├── url.txt.filtered    #filtered urls
├── util.py
├── README.md
├── banner.py
├── requirements.txt
├── result
│   └── ****************.json   #result
├── model.py
└── test.py
```
# Screenshot 
### -url
![image](https://github.com/DESTHUbb/Des-XSS/assets/90658763/6da0f4d8-599c-47e1-a29f-6acc6092ceab)

# Environment
Linux

Python2.7 a & 3.0

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
`python3 start.py --check`
# Usage
```python

python3 start.py --url url --save
python3 start.py --url url --cookie cookie --browser chrome --save  
python3 start.py --url url --cookie cookie --browser chrome-headless --save  
python3 start.py --file ./url.txt --save  
python3 start.py --burp ./test.xml --save  
python3 start.py --file file --filter

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
![image](https://github.com/DESTHUbb/Des-XSS/assets/90658763/0be7e353-c35a-4fa9-b094-e79223f8f8cb)


### How to scan data from Burpsuite
In Proxy,"Save items" ==> "test.xml"  
![image](https://github.com/DESTHUbb/Des-XSS/assets/90658763/689ea612-2083-4e4f-a1a8-ca68cf8005a2)
Then you can scan test.xml:  
`python3 start.py --burp=./test.xml`
### How to rescan
After scanning firstly,there will be taskid.traffic and taskid.reflect in ./traffic/:  
+ taskid.traffic: Web traffic of request(pickled).
+ taskid.reflect: Reflected result (pickled)that included reflected params,reflected position,type and others.  
Des-XSS will use these middle files to rescan:  
`python3 start.py --id taskid --save`
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
# Samples:

# Used libraries:


