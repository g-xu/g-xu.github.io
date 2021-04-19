## [linux常用压缩解压缩命令](#) ##

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
-
-



## [Bash数组用法](https://www.skidu.me/bash_array.html)
### 数组赋值：
```
array=(var1 var2 var3 ... varN)
```
```
array=([0]=var1 [1]=var2 [2]=var3 ... [n]=varN)
``` 
```
array[0]=var1
arrya[1]=var2
...
array[n]=varN
```

### 计算数组元素个数：
```
${#array[@]}  或者  ${#array[*]}
```

BASH的特殊参数 @ 和 * 都表示“扩展位置参数，从1开始”，但形式稍有差异，但在数组里使用好像是可以通用的。

### 打印整个数组：
```
echo ${array[*]}  或者 echo ${array[@]}
```
### 打印某一数组元素：
```
echo ${array[3]}
```
### 清除指定的单个数组元素：
```
unset array[2]
```
### 清除整个数组：
```
unset array
```
### 引用数组：
```
echo ${array[n]}
```

### 遍历数组：
```
filename=(`ls`)
for var in ${filename[@]};do
    echo $var
done
```
### 数组实用示例：
#### 从 标准输入 读入n次字符串，每次输入的字符串保存在数组array里
``` 
i=0
n=5
while [ "$i" -lt $n ] ; do
    echo "Please input strings ... `expr $i + 1`"
    read array[$i]
    b=${array[$i]}
    echo "$b"
    i=`expr $i + 1`
done
``` 
#### 将字符串里的字母逐个放入数组，并输出到标准输出
``` 
chars='abcdefghijklmnopqrstuvwxyz'
for (( i=0; i<26; i++ )) ; do
    array[$i]=${chars:$i:1}
    echo ${array[$i]}
done
# ${chars:$i:1}，表示从chars字符串的 $i 位置开始，获取 1 个字符。如果将 1 改为 3 ，就获取 3 个字符
```


## [bash字符串用法](https://www.skidu.me/bash_string.html)
### 计算svn tag里面的field数目
```
echo 20150513-z5-natalie-cstm_idl-A |sed 's/\-/ /g'|wc -w
5
```
### 取长度
```
str="abcd"
expr length $str   # 4
echo ${#str}       # 4
expr "$str" : ".*" # 4
```
### 查找子串的位置
```
str="abc"
expr index $str "a"  # 1
expr index $str "b"  # 2
expr index $str "x"  # 0
expr index $str ""   # 0
```

### 选取子串

```
str="abcdef"
expr substr "$str" 1 3  # 从第一个位置开始取3个字符， abc
expr substr "$str" 2 5  # 从第二个位置开始取5个字符， bcdef
expr substr "$str" 4 5  # 从第四个位置开始取5个字符， def

echo ${str:2}           # 从第二个位置开始提取字符串， bcdef
echo ${str:2:3}         # 从第二个位置开始提取3个字符, bcd
echo ${str:(-6):5}      # 从倒数第二个位置向左提取字符串, abcde
echo ${str:(-4):3}      # 从倒数第二个位置向左提取6个字符, cde
```

### 截取子串

```
str="abbc,def,ghi,abcjkl"
echo ${str#a*c}     # 输出,def,ghi,abcjkl  一个井号(#) 表示从左边截取掉最短的匹配 (这里把abbc字串去掉）
echo ${str##a*c}    # 输出jkl，             两个井号(##) 表示从左边截取掉最长的匹配 (这里把abbc,def,ghi,abc字串去掉)

echo ${str#"a*c"}   # 输出abbc,def,ghi,abcjkl 因为str中没有"a*c"子串
echo ${str##"a*c"}  # 输出abbc,def,ghi,abcjkl 同理
echo ${str#*a*c*}   # 空
echo ${str##*a*c*}  # 空
echo ${str#d*f)     # 输出abbc,def,ghi,abcjkl,
echo ${str#*d*f}    # 输出,ghi,abcjkl  
 
echo ${str%a*l}     # abbc,def,ghi  一个百分号(%)表示从右边截取最短的匹配
echo ${str%%b*l}    # a             两个百分号表示(%%)表示从右边截取最长的匹配
echo ${str%a*c}     # abbc,def,ghi,abcjkl
```
### 字符串替换
```
str="apple, tree, apple tree"
echo ${str/apple/APPLE}   # 替换第一次出现的apple
echo ${str//apple/APPLE}  # 替换所有apple
 
echo ${str/#apple/APPLE}  # 如果字符串str以apple开头，则用APPLE替换它
echo ${str/%apple/APPLE}  # 如果字符串str以apple结尾，则用APPLE替换它
比较
[[ "a.txt" == a* ]]        # 逻辑真 (pattern matching)
[[ "a.txt" =~ .*\.txt ]]   # 逻辑真 (regex matching)
[[ "abc" == "abc" ]]       # 逻辑真 (string comparision)
[[ "11" < "2" ]]           # 逻辑真 (string comparision), 按ascii值比较
```
### 翻转
```
#使用rev
echo "STRING" | rev
```

### 自定义函数

```
A="abcd def ghd;"
B=$(echo $A | rev)
echo "first way result= [$B]"
 
len=$(echo -n $A | wc -c )
rev=""
while [ $len -gt 0 ]
do
    B="$(echo -n $A | cut -b$len)"
    rev="$rev$B"
    len=$(($len-1))
done
echo "second way result=[$rev]"
echo
```

 