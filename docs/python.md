## python字符串操作
 
1、去空格及特殊符号
```
s.strip().lstrip().rstrip(',')
```
2、复制字符串
```
#strcpy(sStr1,sStr2)
sStr1 = 'strcpy'
sStr2 = sStr1
sStr1 = 'strcpy2'
print sStr2
```
3、连接字符串
```
#strcat(sStr1,sStr2)
sStr1 = 'strcat'
sStr2 = 'append'
sStr1 += sStr2
print sStr1
```
4、查找字符
```
#strchr(sStr1,sStr2)
# < 0 为未找到
sStr1 = 'strchr'
sStr2 = 's'
nPos = sStr1.index(sStr2)
print nPos
```
5、比较字符串
```
#strcmp(sStr1,sStr2)
sStr1 = 'strchr'
sStr2 = 'strch'
print cmp(sStr1,sStr2)
```
6、扫描字符串是否包含指定的字符
```
#strspn(sStr1,sStr2)
sStr1 = '12345678'
sStr2 = '456'
#sStr1 and chars both in sStr1 and sStr2
print len(sStr1 and sStr2)
```
7、字符串长度
```
#strlen(sStr1)
sStr1 = 'strlen'
print len(sStr1)
```
8、将字符串中的大小写转换
```
S.lower() #小写 
S.upper() #大写 
S.swapcase() #大小写互换 
S.capitalize() #首字母大写 
String.capwords(S) #这是模块中的方法。它把S用split()函数分开，然后用capitalize()把首字母变成大写，最后用join()合并到一起 
#实例：
#strlwr(sStr1)
sStr1 = 'JCstrlwr'
sStr1 = sStr1.upper()
#sStr1 = sStr1.lower()
print sStr1
```
9、追加指定长度的字符串
```
#strncat(sStr1,sStr2,n)
sStr1 = '12345'
sStr2 = 'abcdef'
n = 3
sStr1 += sStr2[0:n]
print sStr1
```
10、字符串指定长度比较
```
#strncmp(sStr1,sStr2,n)
sStr1 = '12345'
sStr2 = '123bc'
n = 3
print cmp(sStr1[0:n],sStr2[0:n])
```
11、复制指定长度的字符
```
#strncpy(sStr1,sStr2,n)
sStr1 = ''
sStr2 = '12345'
n = 3
sStr1 = sStr2[0:n]
print sStr1
```
12、将字符串前n个字符替换为指定的字符
```
#strnset(sStr1,ch,n)
sStr1 = '12345'
ch = 'r'
n = 3
sStr1 = n * ch + sStr1[3:]
print sStr1
```
13、扫描字符串
```
#strpbrk(sStr1,sStr2)
sStr1 = 'cekjgdklab'
sStr2 = 'gka'
nPos = -1
for c in sStr1:
    if c in sStr2:
        nPos = sStr1.index(c)
        break
print nPos
```
14、翻转字符串
```
#strrev(sStr1)
sStr1 = 'abcdefg'
sStr1 = sStr1[::-1]
print sStr1
```
15、查找字符串
```
#strstr(sStr1,sStr2)
sStr1 = 'abcdefg'
sStr2 = 'cde'
print sStr1.find(sStr2)
```
16、分割字符串
```
#strtok(sStr1,sStr2)
sStr1 = 'ab,cde,fgh,ijk'
sStr2 = ','
sStr1 = sStr1[sStr1.find(sStr2) + 1:]
print sStr1
#或者
s = 'ab,cde,fgh,ijk'
print(s.split(','))
```
17、连接字符串
```
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)
```
18、PHP 中 addslashes 的实现
```
def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)

s = "John 'Johny' Doe (a.k.a. \"Super Joe\")\\\0"
print s
print addslashes(s)
```
19、只显示字母与数字
```
def OnlyCharNum(s,oth=''):
    s2 = s.lower();
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c,'');
    return s;

print(OnlyStr("a000 aa-b"))
```
20、截取字符串
```
str = '0123456789′
print str[0:3] #截取第一位到第三位的字符
print str[:] #截取字符串的全部字符
print str[6:] #截取第七个字符到结尾
print str[:-3] #截取从头开始到倒数第三个字符之前
print str[2] #截取第三个字符
print str[-1] #截取倒数第一个字符
print str[::-1] #创造一个与原字符串顺序相反的字符串
print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
print str[-3:] #截取倒数第三位到结尾
print str[:-5:-3] #逆序截取，具体啥意思没搞明白？
```
21、字符串在输出时的对齐 
```
S.ljust(width,[fillchar]) 
#输出width个字符，S左对齐，不足部分用fillchar填充，默认的为空格。 
S.rjust(width,[fillchar]) #右对齐 
S.center(width, [fillchar]) #中间对齐 
S.zfill(width) #把S变成width长，并在右对齐，不足部分用0补足
```
22、字符串中的搜索和替换 
```
S.find(substr, [start, [end]]) 
#返回S中出现substr的第一个字母的标号，如果S中没有substr则返回-1。start和end作用就相当于在S[start:end]中搜索 
S.index(substr, [start, [end]]) 
#与find()相同，只是在S中没有substr时，会返回一个运行时错误 
S.rfind(substr, [start, [end]]) 
#返回S中最后出现的substr的第一个字母的标号，如果S中没有substr则返回-1，也就是说从右边算起的第一次出现的substr的首字母标号 
S.rindex(substr, [start, [end]]) 
S.count(substr, [start, [end]]) #计算substr在S中出现的次数 
S.replace(oldstr, newstr, [count]) 
#把S中的oldstar替换为newstr，count为替换次数。这是替换的通用形式，还有一些函数进行特殊字符的替换 
S.strip([chars]) 
#把S中前后chars中有的字符全部去掉，可以理解为把S前后chars替换为None 
S.lstrip([chars]) 
S.rstrip([chars]) 
S.expandtabs([tabsize]) 
#把S中的tab字符替换没空格，每个tab替换为tabsize个空格，默认是8个
```
23、字符串的分割和组合 
```
S.split([sep, [maxsplit]]) 
#以sep为分隔符，把S分成一个list。maxsplit表示分割的次数。默认的分割符为空白字符 
S.rsplit([sep, [maxsplit]]) 
S.splitlines([keepends]) 
#把S按照行分割符分为一个list，keepends是一个bool值，如果为真每行后而会保留行分割符。 
S.join(seq) #把seq代表的序列──字符串序列，用S连接起来
```
24、字符串的mapping，这一功能包含两个函数 
```
String.maketrans(from, to) 
#返回一个256个字符组成的翻译表，其中from中的字符被一一对应地转换成to，所以from和to必须是等长的。 
S.translate(table[,deletechars]) 
# 使用上面的函数产后的翻译表，把S进行翻译，并把deletechars中有的字符删掉。需要注意的是，如果S为unicode字符串，那么就不支持 deletechars参数，可以使用把某个字符翻译为None的方式实现相同的功能。此外还可以使用codecs模块的功能来创建更加功能强大的翻译表。
```
25、字符串还有一对编码和解码的函数 
```
S.encode([encoding,[errors]]) 
# 其中encoding可以有多种值，比如gb2312 gbk gb18030 bz2 zlib big5 bzse64等都支持。errors默认值为"strict"，意思是UnicodeError。可能的值还有'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 和所有的通过codecs.register_error注册的值。这一部分内容涉及codecs模块，不是特明白 
S.decode([encoding,[errors]])
```
26、字符串的测试、判断函数，这一类函数在string模块中没有，这些函数返回的都是bool值 
```
S.startswith(prefix[,start[,end]]) 
#是否以prefix开头 
S.endswith(suffix[,start[,end]]) 
#以suffix结尾 
S.isalnum() 
#是否全是字母和数字，并至少有一个字符 
S.isalpha() #是否全是字母，并至少有一个字符 
S.isdigit() #是否全是数字，并至少有一个字符 
S.isspace() #是否全是空白字符，并至少有一个字符 
S.islower() #S中的字母是否全是小写 
S.isupper() #S中的字母是否便是大写 
S.istitle() #S是否是首字母大写的
```
27、字符串类型转换函数，这几个函数只在string模块中有
```
string.atoi(s[,base]) 
#base默认为10，如果为0,那么s就可以是012或0x23这种形式的字符串，如果是16那么s就只能是0x23或0X12这种形式的字符串 
string.atol(s[,base]) #转成long 
string.atof(s[,base]) #转成float
这里再强调一次，字符串对象是不可改变的，也就是说在python创建一个字符串后，你不能把这个字符中的某一部分改变。任何上面的函数改变了字符串后，都会返回一个新的字符串，原字串并没有变。其实这也是有变通的办法的，可以用S=list(S)这个函数把S变为由单个字符为成员的list，这样的话就可以使用S[3]='a'的方式改变值，然后再使用S=" ".join(S)还原成字符串
```


## [python 字符串编码]()
字符串编码常用类型：utf-8,gb2312,cp936,gbk等。

python中，我们使用decode()和encode()来进行解码和编码

在python中，使用unicode类型作为编码的基础类型。即

     decode              encode

str ---------> unicode --------->str
```
u = u'中文' #显示指定unicode类型对象
ustr = u.encode('gb2312')#以gb2312编码对unicode对像进行编码
str1 = u.encode('gbk') #以gbk编码对unicode对像进行编码
str2 = u.encode('utf-8')#以utf-8编码对unicode对像进行编码
u1 = str.decode('gb2312')#以gb2312编码对字符串str进行解码，以获取
unicodeu2 = str.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型
```
如上面代码，str\str1\str2均为字符串类型（str）,给字符串操作带来较大的复杂性。

好消息来了，对，那就是python3，在新版本的python3中，取消了unicode类型，代替它的是使用unicode字符的字符串类型(str),字符串类型（str）成为基础类型如下所示，而编码后的变为了字节类型(bytes)但是两个函数的使用方法不变：

     decode              encode

bytes ------> str(unicode)------>bytes

```
u = '中文' #指定字符串类型对象
ustr = u.encode('gb2312')#以gb2312编码对u进行编码，获得bytes类型对象
stru1 = str.decode('gb2312')#以gb2312编码对字符串str进行解码，获得字符串类型对象
u1u2 = str.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的字符串内容
```
避免不了的是，文件读取问题：

假如我们读取一个文件，文件保存时，使用的编码格式，决定了我们从文件读取的内容的编码格式，例如，我们从记事本新建一个文本文件test.txt, 编辑内容，保存的时候注意，编码格式是可以选择的，例如我们可以选择gb2312,那么使用python读取文件内容，方式如下：
```
f = open('test.txt','r')
s = f.read() #读取文件内容,如果是不识别的encoding格式（识别的encoding类型跟使用的系统有关），这里将读取失败
假设文件保存时以gb2312编码保存
u = s.decode('gb2312')#以文件保存格式对内容进行解码，获得unicode字符串
```
下面我们就可以对内容进行各种编码的转换了
```
str = u.encode('utf-8')#转换为utf-8编码的字符串
strstr1 = u.encode('gbk')#转换为gbk编码的字符串str1str1 = u.encode('utf-16')#转换为utf-16编码的字符串str1
```

python给我们提供了一个包codecs进行文件的读取，这个包中的open()函数可以指定编码的类型：

```
import
codecs
f = codecs.open('text.text','r+',encoding='utf-8'
)#必须事先知道文件的编码格式，这里文件编码是使用的utf-8
content = f.read()#如果open时使用的encoding和文件本身的encoding不一致的话，那么这里将将会产生错误f.write('你想要写入的信息'
)
f.close()
```

来源： <http://www.cnblogs.com/evening/archive/2012/04/19/2457440.html>
 
 
## [python 字典排序]()
### 最简单的方法，这个是按照key值排序： 
```
def sortedDictValues1(adict): 
    items = adict.items() 
    items.sort() 
    return [value for key, value in items] 
```
### 又一个按照key值排序，貌似比上一个速度要快点 
```
def sortedDictValues2(adict): 
    keys = adict.keys() 
    keys.sort() 
    return [dict[key] for key in keys] 
```
### 还是按key值排序，据说更快。。。而且当key为tuple的时候照样适用 
```
def sortedDictValues3(adict): 
    keys = adict.keys() 
    keys.sort() 
    return map(adict.get, keys) 
```
### 一行语句搞定： 
```
[(k,di[k]) for k in sorted(di.keys())] 
```

### 来一个根据value排序的，先把item的key和value交换位置放入一个list中，再根据list每个元素的第一个值，即原来的value值，排序： 
```
def sort_by_value(d): 
    items=d.items() 
    backitems=[[v[1],v[0]] for v in items] 
    backitems.sort() 
    return [ backitems[i][1] for i in range(0,len(backitems))] 
```

### 还是一行搞定： 
```
[ v for v in sorted(di.values())] 
```
### 用lambda表达式来排序，更灵活： 
```
sorted(d.items(), lambda x, y: cmp(x[1], y[1])), 或反序： 
sorted(d.items(), lambda x, y: cmp(x[1], y[1]), reverse=True) 
```
### 用sorted函数的key= 参数排序： 
```
# 按照key进行排序 
print sorted(dict1.items(), key=lambda d: d[0]) 
# 按照value进行排序 
print sorted(dict1.items(), key=lambda d: d[1]) 
```

### 下面给出python内置sorted函数的帮助文档： 
```
sorted(...) 
sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list 
```

看了上面这么多种对dictionary排序的方法，其实它们的核心思想都一样，即把dictionary中的元素分离出来放到一个list中，对list排序，从而间接实现对dictionary的排序。这个“元素”可以是key，value或者item。 


## [python 小技巧合集]()

### 1.1 拆箱

```
>>> a, b, c = 1, 2, 3
>>> a, b, c
(1, 2, 3)
>>> a, b, c = [1, 2, 3]
>>> a, b, c
(1, 2, 3)
>>> a, b, c = (2 * i + 1 for i in range(3))
>>> a, b, c
(1, 3, 5)
>>> a, (b, c), d = [1, (2, 3), 4]
>>> a
1
>>> b
2
>>> c
3
>>> d
4
```

### 1.2 拆箱变量交换

```
>>> a, b = 1, 2
>>> a, b = b, a
>>> a, b
(2, 1)
```

### 1.3 扩展拆箱（只兼容```3）

```
>>> a, *b, c = [1, 2, 3, 4, 5]
>>> a
1
>>> b
[2, 3, 4]
>>> c
5
```

### 1.4 负数索引

```
>>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[-1]
10
>>> a[-3]
8
```

### 1.5 切割列表

```
>>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[2:8]
[2, 3, 4, 5, 6, 7]
```

### 1.6 负数索引切割列表

```
>>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[-4:-2]
[7, 8]
```

### 1.7指定步长切割列表

```
>>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[::2]
[0, 2, 4, 6, 8, 10]
>>> a[::3]
[0, 3, 6, 9]
>>> a[2:8:2]
[2, 4, 6]
```

### 1.8 负数步长切割列表

```
>>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> a[::-2]
[10, 8, 6, 4, 2, 0]
```
### 1.9 列表切割赋值

```
>>> a = [1, 2, 3, 4, 5]
>>> a[2:3] = [0, 0]
>>> a
[1, 2, 0, 0, 4, 5]
>>> a[1:1] = [8, 9]
>>> a
[1, 8, 9, 2, 0, 0, 4, 5]
>>> a[1:-1] = []
>>> a
[1, 5]
```

### 1.10 命名列表切割方式

```
>>> a = [0, 1, 2, 3, 4, 5]
>>> LASTTHREE = slice(-3, None)
>>> LASTTHREE
slice(-3, None, None)
>>> a[LASTTHREE]
[3, 4, 5]
```

### 1.11 列表以及迭代器的压缩和解压缩

```
>>> a = [1, 2, 3]
>>> b = ['a', 'b', 'c']
>>> z = zip(a, b)
>>> z
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> zip(*z)
[(1, 2, 3), ('a', 'b', 'c')]
```

### 1.12 列表相邻元素压缩器

```
>>> a = [1, 2, 3, 4, 5, 6]
>>> zip(*([iter(a)] * 2))
[(1, 2), (3, 4), (5, 6)]

>>> group_adjacent = lambda a, k: zip(*([iter(a)] * k))
>>> group_adjacent(a, 3)
[(1, 2, 3), (4, 5, 6)]
>>> group_adjacent(a, 2)
[(1, 2), (3, 4), (5, 6)]
>>> group_adjacent(a, 1)
[(1,), (2,), (3,), (4,), (5,), (6,)]
```

### 1.13 在列表中用压缩器和迭代器滑动取值窗口

```
>>> def n_grams(a, n):
...     z = [iter(a[i:]) for i in range(n)]
...     return zip(*z)
...
>>> a = [1, 2, 3, 4, 5, 6]
>>> n_grams(a, 3)
[(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
>>> n_grams(a, 2)
[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
>>> n_grams(a, 4)
[(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]
```

### 1.14 用压缩器反转字典

```
>>> m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> m.items()
[('a', 1), ('c', 3), ('b', 2), ('d', 4)]
>>> zip(m.values(), m.keys())
[(1, 'a'), (3, 'c'), (2, 'b'), (4, 'd')]
>>> mi = dict(zip(m.values(), m.keys()))
>>> mi
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
```

### 1.15 列表展开

```
>>> a = [[1, 2], [3, 4], [5, 6]]
>>> list(itertools.chain.from_iterable(a))
[1, 2, 3, 4, 5, 6]

>>> sum(a, [])
[1, 2, 3, 4, 5, 6]

>>> [x for l in a for x in l]
[1, 2, 3, 4, 5, 6]

>>> a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
>>> [x for l1 in a for l2 in l1 for x in l2]
[1, 2, 3, 4, 5, 6, 7, 8]

>>> a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
>>> flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
>>> flatten(a)
[1, 2, 3, 4, 5, 6, 7, 8]
```

### 1.16 生成器表达式

```
>>> g = (x ** 2 for x in xrange(10))
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
>>> sum(x ** 3 for x in xrange(10))
2025
>>> sum(x ** 3 for x in xrange(10) if x % 3 == 1)
408
```

### 1.17 字典推导

```
>>> m = {x: x ** 2 for x in range(5)}
>>> m
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

>>> m = {x: 'A' + str(x) for x in range(10)}
>>> m
{0: 'A0', 1: 'A1', 2: 'A2', 3: 'A3', 4: 'A4', 5: 'A5', 6: 'A6', 7: 'A7', 8: 'A8', 9: 'A9'}
```

### 1.18 用字典推导反转字典

```
>>> m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> m
{'d': 4, 'a': 1, 'b': 2, 'c': 3}
>>> {v: k for k, v in m.items()}
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
```

### 1.19 命名元组

```
>>> Point = collections.namedtuple('Point', ['x', 'y'])
>>> p = Point(x=1.0, y=2.0)
>>> p
Point(x=1.0, y=2.0)
>>> p.x
1.0
>>> p.y
2.0
```

### 1.20 继承命名元组

```
>>> class Point(collections.namedtuple('PointBase', ['x', 'y'])):
...     __slots__ = ()
...     def __add__(self, other):
...             return Point(x=self.x + other.x, y=self.y + other.y)
...
>>> p = Point(x=1.0, y=2.0)
>>> q = Point(x=2.0, y=3.0)
>>> p + q
Point(x=3.0, y=5.0)
```

### 1.21 操作集合

```
>>> A = {1, 2, 3, 3}
>>> A
set([1, 2, 3])
>>> B = {3, 4, 5, 6, 7}
>>> B
set([3, 4, 5, 6, 7])
>>> A | B
set([1, 2, 3, 4, 5, 6, 7])
>>> A & B
set([3])
>>> A - B
set([1, 2])
>>> B - A
set([4, 5, 6, 7])
>>> A ^ B
set([1, 2, 4, 5, 6, 7])
>>> (A ^ B) == ((A - B) | (B - A))
True
```

### 1.22 操作多重集合

```
>>> A = collections.Counter([1, 2, 2])
>>> B = collections.Counter([2, 2, 3])
>>> A
Counter({2: 2, 1: 1})
>>> B
Counter({2: 2, 3: 1})
>>> A | B
Counter({2: 2, 1: 1, 3: 1})
>>> A & B
Counter({2: 2})
>>> A + B
Counter({2: 4, 1: 1, 3: 1})
>>> A - B
Counter({1: 1})
>>> B - A
Counter({3: 1})
```

### 1.23 统计在可迭代器中最常出现的元素

```
>>> A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
>>> A
Counter({3: 4, 1: 2, 2: 2, 4: 1, 5: 1, 6: 1, 7: 1})
>>> A.most_common(1)
[(3, 4)]
>>> A.most_common(3)
[(3, 4), (1, 2), (2, 2)]
```

### 1.24 两端都可操作的队列

```
>>> Q = collections.deque()
>>> Q.append(1)
>>> Q.appendleft(2)
>>> Q.extend([3, 4])
>>> Q.extendleft([5, 6])
>>> Q
deque([6, 5, 2, 1, 3, 4])
>>> Q.pop()
4
>>> Q.popleft()
6
>>> Q
deque([5, 2, 1, 3])
>>> Q.rotate(3)
>>> Q
deque([2, 1, 3, 5])
>>> Q.rotate(-3)
>>> Q
deque([5, 2, 1, 3])
```

### 1.25 有最大长度的双端队列

```
>>> last_three = collections.deque(maxlen=3)
>>> for i in xrange(10):
...     last_three.append(i)
...     print ', '.join(str(x) for x in last_three)
...
0
0, 1
0, 1, 2
1, 2, 3
2, 3, 4
3, 4, 5
4, 5, 6
5, 6, 7
6, 7, 8
7, 8, 9
```

### 1.26 可排序词典

```
>>> m = dict((str(x), x) for x in range(10))
>>> print ', '.join(m.keys())
1, 0, 3, 2, 5, 4, 7, 6, 9, 8
>>> m = collections.OrderedDict((str(x), x) for x in range(10))
>>> print ', '.join(m.keys())
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
>>> m = collections.OrderedDict((str(x), x) for x in range(10, 0, -1))
>>> print ', '.join(m.keys())
10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### 1.27 默认词典

```
>>> m = dict()
>>> m['a']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'a'
>>>
>>> m = collections.defaultdict(int)
>>> m['a']
0
>>> m['b']
0
>>> m = collections.defaultdict(str)
>>> m['a']
''
>>> m['b'] += 'a'
>>> m['b']
'a'
>>> m = collections.defaultdict(lambda: '[default value]')
>>> m['a']
'[default value]'
>>> m['b']
'[default value]'
```

### 1.28 默认字典的简单树状表达

```
>>> import json
>>> tree = lambda: collections.defaultdict(tree)
>>> root = tree()
>>> root['menu']['id'] = 'file'
>>> root['menu']['value'] = 'File'
>>> root['menu']['menuitems']['new']['value'] = 'New'
>>> root['menu']['menuitems']['new']['onclick'] = 'new();'
>>> root['menu']['menuitems']['open']['value'] = 'Open'
>>> root['menu']['menuitems']['open']['onclick'] = 'open();'
>>> root['menu']['menuitems']['close']['value'] = 'Close'
>>> root['menu']['menuitems']['close']['onclick'] = 'close();'
>>> print json.dumps(root, sort_keys=True, indent=4, separators=(',', ': '))
{
    "menu": {
        "id": "file",
        "menuitems": {
            "close": {
                "onclick": "close();",
                "value": "Close"
            },
            "new": {
                "onclick": "new();",
                "value": "New"
            },
            "open": {
                "onclick": "open();",
                "value": "Open"
            }
        },
        "value": "File"
    }
}
```

### 1.29 对象到唯一计数的映射

```
>>> import itertools, collections
>>> value_to_numeric_map = collections.defaultdict(itertools.count().next)
>>> value_to_numeric_map['a']
0
>>> value_to_numeric_map['b']
1
>>> value_to_numeric_map['c']
2
>>> value_to_numeric_map['a']
0
>>> value_to_numeric_map['b']
1
```

### 1.30 最大和最小的几个列表元素

```
>>> a = [random.randint(0, 100) for __ in xrange(100)]
>>> heapq.nsmallest(5, a)
[3, 3, 5, 6, 8]
>>> heapq.nlargest(5, a)
[100, 100, 99, 98, 98]
```

### 1.31 两个列表的笛卡尔积

```
>>> for p in itertools.product([1, 2, 3], [4, 5]):
(1, 4)
(1, 5)
(2, 4)
(2, 5)
(3, 4)
(3, 5)
>>> for p in itertools.product([0, 1], repeat=4):
...     print ''.join(str(x) for x in p)
...
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
```

### 1.32 列表组合和列表元素替代组合

```
>>> for c in itertools.combinations([1, 2, 3, 4, 5], 3):
...     print ''.join(str(x) for x in c)
...
123
124
125
134
135
145
234
235
245
345
>>> for c in itertools.combinations_with_replacement([1, 2, 3], 2):
...     print ''.join(str(x) for x in c)
...
11
12
13
22
23
33
```

### 1.33 列表元素排列组合

```
>>> for p in itertools.permutations([1, 2, 3, 4]):
...     print ''.join(str(x) for x in p)
...
1234
1243
1324
1342
1423
1432
2134
2143
2314
2341
2413
2431
3124
3142
3214
3241
3412
3421
4123
4132
4213
4231
4312
4321
```

### 1.34 可链接迭代器

```
>>> a = [1, 2, 3, 4]
>>> for p in itertools.chain(itertools.combinations(a, 2), itertools.combinations(a, 3)):
...     print p
...
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
(1, 2, 3)
(1, 2, 4)
(1, 3, 4)
(2, 3, 4)
>>> for subset in itertools.chain.from_iterable(itertools.combinations(a, n) for n in range(len(a) + 1))
...     print subset
...
()
(1,)
(2,)
(3,)
(4,)
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
(1, 2, 3)
(1, 2, 4)
(1, 3, 4)
(2, 3, 4)
(1, 2, 3, 4)
```

### 1.35 根据文件指定列类聚

```
>>> import itertools
>>> with open('contactlenses.csv', 'r') as infile:
...     data = [line.strip().split(',') for line in infile]
...
>>> data = data[1:]
>>> def print_data(rows):
...     print '\n'.join('\t'.join('{: <16}'.format(s) for s in row) for row in rows)
...

>>> print_data(data)
young               myope                   no                      reduced                 none
young               myope                   no                      normal                  soft
young               myope                   yes                     reduced                 none
young               myope                   yes                     normal                  hard
young               hypermetrope            no                      reduced                 none
young               hypermetrope            no                      normal                  soft
young               hypermetrope            yes                     reduced                 none
young               hypermetrope            yes                     normal                  hard
pre-presbyopic      myope                   no                      reduced                 none
pre-presbyopic      myope                   no                      normal                  soft
pre-presbyopic      myope                   yes                     reduced                 none
pre-presbyopic      myope                   yes                     normal                  hard
pre-presbyopic      hypermetrope            no                      reduced                 none
pre-presbyopic      hypermetrope            no                      normal                  soft
pre-presbyopic      hypermetrope            yes                     reduced                 none
pre-presbyopic      hypermetrope            yes                     normal                  none
presbyopic          myope                   no                      reduced                 none
presbyopic          myope                   no                      normal                  none
presbyopic          myope                   yes                     reduced                 none
presbyopic          myope                   yes                     normal                  hard
presbyopic          hypermetrope            no                      reduced                 none
presbyopic          hypermetrope            no                      normal                  soft
presbyopic          hypermetrope            yes                     reduced                 none
presbyopic          hypermetrope            yes                     normal                  none

>>> data.sort(key=lambda r: r[-1])
>>> for value, group in itertools.groupby(data, lambda r: r[-1]):
...     print '-----------'
...     print 'Group: ' + value
...     print_data(group)
...
-----------
Group: hard
young               myope                   yes                     normal                  hard
young               hypermetrope            yes                     normal                  hard
pre-presbyopic      myope                   yes                     normal                  hard
presbyopic          myope                   yes                     normal                  hard
-----------
Group: none
young               myope                   no                      reduced                 none
young               myope                   yes                     reduced                 none
young               hypermetrope            no                      reduced                 none
young               hypermetrope            yes                     reduced                 none
pre-presbyopic      myope                   no                      reduced                 none
pre-presbyopic      myope                   yes                     reduced                 none
pre-presbyopic      hypermetrope            no                      reduced                 none
pre-presbyopic      hypermetrope            yes                     reduced                 none
pre-presbyopic      hypermetrope            yes                     normal                  none
presbyopic          myope                   no                      reduced                 none
presbyopic          myope                   no                      normal                  none
presbyopic          myope                   yes                     reduced                 none
presbyopic          hypermetrope            no                      reduced                 none
presbyopic          hypermetrope            yes                     reduced                 none
presbyopic          hypermetrope            yes                     normal                  none
-----------
Group: soft
young               myope                   no                      normal                  soft
young               hypermetrope            no                      normal                  soft
pre-presbyopic      myope                   no                      normal                  soft
pre-presbyopic      hypermetrope            no                      normal                  soft
presbyopic          hypermetrope            no                      normal                  soft
```

## python代码实现
- [crc](https://github.com/g-xu/g-xu.github.io/blob/master/python/crc.py)
- [des/md5](https://github.com/g-xu/g-xu.github.io/blob/master/python/des_md5.py)
- [string](https://github.com/g-xu/g-xu.github.io/blob/master/python/string.py)
- [文件遍历](https://github.com/g-xu/g-xu.github.io/blob/master/python/traverse.py)