## linux常用压缩解压缩命令 ##

### .tar ###
- 解包：`tar zxvf FileName.tar`
- 打包：`tar czvf FileName.tar DirName`

### .gz ###
- 解压1：`gunzip FileName.gz`
- 解压2：`gzip -d FileName.gz`
- 压缩：`gzip FileName`

### .tar.gz 和 .tgz ###
- 解压：`tar zxvf FileName.tar.gz`
- 压缩：`tar zcvf FileName.tar.gz DirName`

### .bz2 ###
- 解压1：`bzip2 -d FileName.bz2`
- 解压2：`bunzip2 FileName.bz2`
- 压缩： `bzip2 -z FileName`

### .tar.bz2 ###
- 解压：`tar jxvf FileName.tar.bz2`
- 压缩：`tar jcvf FileName.tar.bz2 DirName`

### .bz ###
- 解压1：`bzip2 -d FileName.bz`
- 解压2：`bunzip2 FileName.bz`

### .tar.bz ###
- 解压：`tar jxvf FileName.tar.bz`

### .Z ###
- 解压：`uncompress FileName.Z`
- 压缩：`compress FileName`
- 
### .tar.Z ###
- 解压：`tar Zxvf FileName.tar.Z`
- 压缩：`tar Zcvf FileName.tar.Z DirName`

### .zip ###
- 解压：`unzip FileName.zip`
- 压缩：`zip FileName.zip DirName`

### .rar ###
- 解压：`rar a FileName.rar`
- 压缩：`r ar e FileName.rar`

### .lha ###
- 解压：`lha -e FileName.lha`
- 压缩：`lha -a FileName.lha FileName`

### .rpm ###
- 解包：`rpm2cpio FileName.rpm | cpio -div`

### .deb ###
- 解包：`ar p FileName.deb data.tar.gz | tar zxf -`


## SED ##
