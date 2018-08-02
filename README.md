# **文档水印检测**
## 目的 ##
提取文档中的水印与数据库中的水印进行比对，防止抄袭
 ## 环境
 wps或者word，修改对应的config文件 word安装对应word wps安装对应wps 
 安装 python
 运行 `pip install -r requirement.txt`  
 安装 ghostscript https://www.ghostscript.com/download/gsdnld.html  
 安装 imagemagick https://legacy.imagemagick.org/script/binary-releases.php
 ## 构建数据库水印
 将空白水印文档放在word目录下，运行test目录下data_base_test.py
## 文档水印检测
新建temp目录，将上传文档放在temp目录下
运行test目录下，single_test.py，修改其temp目录中的文件名
 
 
  
