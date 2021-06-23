## 如何生成文本静态github page
1. 确保已经安装git，可以git clone已经存在的repo,或者新建一个repo
2. 安装npm（mac), windows下上网搜索类似步骤：

	```
	brew install node
	sudo npm install npm -g  #升级npm
	```
		
3. 后面主要参考[docsify官网](https://docsify.js.org/#/quickstart)
	```
	npm i docsify-cli -g  #首先安装docsify命令行
	docsify init ./docs
	```
4. 开始运行 docsify serve docs		