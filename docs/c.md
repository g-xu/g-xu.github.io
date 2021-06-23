## 常用算法
- [md5](https://github.com/g-xu/g-xu.github.io/tree/master/c)
- [des](https://github.com/g-xu/g-xu.github.io/tree/master/c)
- [RSA](https://github.com/g-xu/g-xu.github.io/tree/master/c/rsa)

## 获得调用者的函数名
调试的时候，有时候需要知道调用者的函数名，从而来判断到底哪里调用出问题，下面是从[stackoverflow](https://stackoverflow.com/questions/16100090/how-can-we-know-the-calnctions-name)找到的一个办法:
```
void a()
{
    /* Your code */
}

void a_special( char const * caller_name )
{
    printf( "a was called from %s", caller_name );
    a();
}

#define a() a_special(__func__)

void b()
{
    a();
}
```
