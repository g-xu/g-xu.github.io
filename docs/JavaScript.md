# JavaScript

## 简介

- 与html/css集成,最广泛的浏览器语言

- 语法索引:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference

- F12 or Cmd+opt+J打开调试

## 基础知识

- 插入脚本：< script src="path/to/script.js">< /script> 或 完整路径

- type/language不需要

- 最好不省略分号

### 数据类型

- let variable=‘something' 

	const NAME=’HelloWorld‘
- number：整数或者浮点数
- bigint： 任意长度整数，末尾加n表示
- string：字符串
- boolean：true/false
- null：未知值
- undefined:未定义
- symbol：唯一的标识符
- object：复杂数据结构
- typeof x/typeof(x) ：查看数据类型

### 交互

- alert：显示信息
- prompt：显示信息并要求用户输入文本
- confirm：显示信息等待用户确定或取消

### 类型转换

- 字符串转换 String(value)
- 数字转换 Number(value)

	- undefined -> NaN
	- null -> 0
	- true / false -> 1/0
	- string -> 忽略两端空白，空字串 ->0, 出错 -> NaN

- 布尔型转换 Boolean(value)

	- 0, null, undefined, NaN, "" -> false
	- other -> true

### 运算符

- `+-*/% **`
- 一元运算符 + 相当于Number(...)
- 二元运算符 + 连接字符串，其他算数运算符只对数字起作用，并且将运算元转出数字
- 位运算符： `& | ^ ~<< >> >>>`

### 比较

- `> < >= <= == ===`
- 比较运算返回布尔值
- 字符串比较，会按照字典顺序逐个字符比较大小
- 不同类型比较时，先被转化为数字再比较
- 非严格相等==下，null和undefined相等，且各自不等于其他任何情况
- 使用 > < 比较时，特别注意变量可能为 null/undefined 情况！！

### 更多运算符

- ？||  && !
- || 或运算返回第一个真值，如果不存在真值返回该链的最后一个值
&& 与运算返回第一个假值，没有假值返回最后一个值
- ??:从列表中选择第一个已定义的值(不是null和undefined)
- 循环：for while switch
- break/continue支持循环前标签

### 函数

函数声明  
```
function showMessage(from, text = "no text given") {    
  alert( from + ": " + text );   
}
```

函数表达式
```
let sum = function(a, b) {
  return a + b;
};
sum(2,3);
```

- 参数会被复制到函数的局部变量
- 函数可以访问外部变量，内部重名变量会覆盖外部变量
- 函数如果没有返回值，返回undefined
- 函数也是值，如果函数在主代码流中被声明为单独的语句，称为函数声明，如果函数作为表达式的一部分，称为函数表达式
- 箭头函数： (...args) => expression
(...args) => {body}

## Object

```
let user = { // 一个对象
  name: "John", // 键 "name"，值 "John"
  age: 30 // 键 "age"，值 30
};
```

- 通过new调用建立新对象
```
function Calculator() {
  this.read = function() {
    this.a = +prompt('a?', 0);
    this.b = +prompt('b?', 0);
  };
  this.sum = function() {
    return this.a + this.b;
  };
  this.mul = function() {
    return this.a * this.b;
  };
}
```
```
let calculator = new Calculator();
calculator.read();
alert( "Sum=" + calculator.sum() );
alert( "Mul=" + calculator.mul() );
```

- 对象是具有特殊行的关联数组

- 存储键值对：属性键必须是字符串或者symbol, 值可以是任何类型

- 访问:  `obj.property`
`obj["property"] ([]中允许使用变量）`

- 检查存在： `"key" in obj`
遍历：  `for(let key in obj)`

- 对象通过引用被赋值和copy，通过Object.assign 来浅拷贝,对象内含有对象时候通过递归实现深层copy

- 存储在对象属性中的函数称为方法，方法允许对象 obj.dosomething() 操作， 方法将对象引用为 this， 箭头函数没有自己的this

- 构造函数就是常规函数，首字母大写，使用new调用

- obj?.prop 对象存在返回obj.prop，否则返回undefined, obj?.[prop]   obj.method?.()同上

- Symbol是唯一标识符的基本类型，总是不同的值，即使名字相同， 主要用来隐藏对象属性,
对象字面量 {...} 中使用 Symbol，则需要使用方括号把它括起来

## 数据类型

### 数字类型

- 将"e"和0的数量附加到数字后，“e”后面的负数将使数字除以1后面0的个数，1.23e6=1.23*1000000， 1.2e-6=1.2/1000000
- parseInt(str,base)将字符串解析为数字
num.toString(base) 数字转为字符串
- 使用Math.floor,Math.ceil,Math.trunc,Math.round,num.toFixed(precision)进行舍入
- 小数有精度损失，尽量避免小数的相等性检查

### String

https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String


- 三种引号，反引号允许多行并且可以使用${...}嵌入表达式
- javascript字符串是utf-16编码
- 大小写：toLowerCase/toUpperCase
- 查找子串：indexOf/includes/startsWith/endsWith
- 获取字符[], 字符子串用slice或substring
- 根据语言比较：localCompare
- str.trim() 删除前后空格

### Array

- 声明：let arr = [item1, item2,...]
- length属性是数组的长度，由数组最后一个数字索引加1，手动调节length会截断数组
- 遍历：for(let i=0; i<arr.length; i++) 最快  
for(let item of arr) 只能访问items

### 数组方法

- push/pop 末端添加删除  
unshift/shift首端添加删除  
splice:从指定位置开始删除添加新的item  
slice:切片返回新数组  
concat：连接并添加不同元素  
- 搜索：indexOf/lastIndexOf / includes   
过滤返回 find /filter   
返回索引 findIndex  
- 遍历： forEach  
- 转换：map(func)返回新数组  
sort/reverse: 原地转换 
split/join: 字符串转为数组并返回  
/reduce/reduceRight(func,initial)通过对每个原始调用func并在调用之间传递结果  

### Iterable object

- 可以应用 for..of 的对象被称为 可迭代的
- 可迭代对象必须实现Symbol.iterator方法，迭代器必须有next()方法
- Symbol.iterator 方法会被 for..of 自动调用，但我们也可以直接调用它
- Array.from 将可迭代对象或类数组对象 obj 转化为真正的数组 Array

### Map & Set

- Map是一个带键的数据项的集合，跟Object区别在于Map允许任何类型的key, 有size属性
- Map方法：new Map()  
map.set()/get()/has()/delete()/clear()/size  
- Map迭代: map.keys()/map.values()/map.entries()  
- 从对象创建Map： 
let map = new Map(Object.entries(obj))  
从map创建对象：
let obj = Object.fromEntries(map.entries());  
- Set 是一个特殊的类型集合 —— “值的集合”（没有键），它的每一个值只能出现一次  
- Set方法： new Set() 
set.add()/delete()/has()/clear()/size 
- Set的迭代方法与Map相同：set.keys()/values/entris()  

### WeakMap &WeakSet

- WeakMap 是类似于 Map 的集合，它仅允许对象作为键，当对象无法访问，便会将它们与其关联值一同删除。
- WeakSet 是类似于 Set 的集合，它仅存储对象，当对象无法访问，便会将其删除
- 它们都不支持引用所有键或其计数的方法和属性。仅允许单个操作

### Object.keys，values，entries

- Object.keys(obj) —— 返回一个包含该对象所有的键的数组
- Object.values(obj) —— 返回一个包含该对象所有的值的数组
- Object.entries(obj) —— 返回一个包含该对象所有 [key, value] 键值对的数组
- 使用 Object.entries(obj) 从 obj 获取由键/值对组成的数组。
对该数组使用数组方法，例如 map。
对结果数组使用 Object.fromEntries(array) 方法，将结果转回成对象

### 解析赋值

- 解构赋值可以立即将一个对象或数组映射到多个变量上
- 解构数组语法：let [item1 = default, item2, ...rest] = array
- 解构对象语法 let {prop : varName = default, ...rest} = object
属性 prop 会被赋值给变量 varName，属性不存在使用默认值 default。
没有对应映射的对象属性会被复制到 rest 对象
- 智能函数参数 
```
function({
  incomingProperty: varName = defaultValue
  ...
})
```
- 从嵌套数组/对象中提取数据也是可以的，此时等号左侧必须和等号右侧有相同的结构

### 日期和时间

- 创建一个新Date对象的唯一方法是通过new 操作符，例如：let now = new Date(); 可以使用毫秒/字符串/年月日 作为参数, 可以自动校准
- Date.now()返回1970年至今的毫秒数

### Json方法

- JSON.stringify 将对象转换为 JSON。
JSON.parse 将 JSON 转换回对象。


## 函数进阶

### Reset & Spread

- ... 出现在函数参数列表的最后，就是 rest 参数，会把参数列表中剩余的参数收集到一个数组中。
-  ... 出现在函数调用或类似的表达式中，就是 spread 语法，会把一个数组展开为列表
- Rest 参数用于创建可接受任意数量参数的函数。
Spread 语法用于将数组传递给通常需要含有许多参数的列表的函数。

### 闭包

- 闭包 是指内部函数总是可以访问其所在的外部函数中声明的变量和参数，即使在其外部函数被返回了之后
JavaScript 中的函数会自动通过隐藏的 [[Environment]] 属性记住创建它们的位置，所以它们都可以访问外部变量。

### var

- var 声明的变量没有块级作用域，它们仅在当前函数内可见，或者全局可见
- var 变量声明在函数开头就会被处理（脚本启动对应全局变量）
- var是过时的东西，尽量不要使用

### 全局对象

- 全局对象包含应该在任何位置都可见的变量
- 全局对象有个通用名称 globalThis ， 更常见的是enviroment-specific名字，比如 window(浏览器）和 global (Node.js)
- 仅当值对于我们的项目而言确实是全局的时，才应将其存储在全局对象中。并保持其数量最少 
- 在浏览器中，除非使用 modules，否则使用 var 声明的全局函数和变量会成为全局对象的属性
- 应该使用直接的方式访问全局对象的属性，如 window.x

### 函数对象

- 函数的名字可以通过属性 “name” 来访问
- 函数内置属性 “length”，返回函数入参的个数
- 函数也可以增加自定义属性，可以通过 func.prop访问
- 命名函数表达式Named Function Expression）指带有名字的函数表达式.用于函数内部自调用
它允许函数在内部引用自己。
它在函数外是不可见的。
```
  let sayHi = function func(who) {
    alert(`Hello, ${who}`);
  };
  
  sayHi("John"); // Hello, John
```

### new Function

- 语法：let func = new Function ([arg1, arg2, ...argN], functionBody);
- 允许我们将任意字符串变为函数，可以用在从服务器获取动态代码
- new Function 创建的函数，它的 [[Environment]] 指向全局词法环境，而不是函数所在的外部词法环境。不能在 new Function 中直接使用外部变量

### 调度

- setTimeout：delay一定时间之后运行func
let timerId = setTimeout(func|code, [delay], [arg1], [arg2], ...) 
- 使用clearTimeout来取消调度
- setInterval：周期性运行func
let timerId = setInterval(func|code, [delay], [arg1], [arg2], ...)
- 嵌套的setTimeout比setInterval更加灵活，更精准
- 零延时调度 setTimeout(func, 0)（与 setTimeout(func) 相同）用来调度需要尽快执行的调用，会在当前脚本执行完成后进行调用。
- 浏览器会将 setTimeout 或 setInterval 的五层或更多层嵌套调用（调用五次之后）的最小延时限制在 4ms。这是历史遗留问题。

### 装饰器
```
let worker = {
  slow(min, max) {
    alert(`Called with ${min},${max}`);
    return min + max;
  }
};

function cachingDecorator(func, hash) {
  let cache = new Map();
  return function() {
    let key = hash(arguments); // (*)
    if (cache.has(key)) {
      return cache.get(key);
    }

    let result = func.call(this, ...arguments); // (**)

    cache.set(key, result);
    return result;
  };
}

function hash(args) {
  return args[0] + ',' + args[1];
}

worker.slow = cachingDecorator(worker.slow, hash);

alert( worker.slow(3, 5) ); // works
alert( "Again " + worker.slow(3, 5) ); // same (cached)
```

-  装饰器 是一个围绕改变函数行为的包装器。主要工作仍由该函数来完成
- func.call(context, arg1, arg2…)  用给定的上下文和参数调用 func
func.apply(context, args)  调用 func 将 context 作为 this 和类数组的 args 传递给参数列表。
- 概念掌握的不清楚，后续

### 函数绑定

- 方法 func.bind(context, ...args) 返回函数 func 的“绑定的（bound）变体”，它绑定了上下文 this 和第一个参数（如果给定了）。
- 通常应用 bind 来绑定对象方法的 this，以便把它们传递到其他地方使用。例如，给 setTimeout
- 当绑定现有的函数的某些参数时，绑定后的函数被称为 partially applied 或 partial。

### 箭头函数

- 没有this
- 没有arguments
- 不能用new调用
- 没有super

## 对象属性

- 对象属性（properties），除 value 外，还有三个特殊的特性（attributes）：writable enumerable configurable

- Object.getOwnPropertyDescriptor 
Object.defineProperties

- 访问器属性由 “getter” 和 “setter” 方法表示

## 原型 继承

### 原型继承

- 所有的对象都有一个隐藏的 [[Prototype]] 属性，它要么是另一个对象，要么就是 null， 可以使用 obj.__proto__ 访问它
- [[Prototype]] 引用的对象被称为“原型”。
当读取 obj 的属性或者方法不存在，JavaScript 会尝试在原型中查找
- 写/删除操作直接在对象上进行，不使用原型
- 调用 obj.method()，而且 method 是从原型中获取的，this 仍然会引用 obj。方法始终与当前对象一起使用，即使方法是继承的。
- for..in 循环在其自身和继承的属性上进行迭代。所有其他的键/值获取方法仅对对象本身起作用

### F.prototype

- 如果F.prototype 是一个对象，那么 new 操作符会使用它为新对象设置 [[Prototype]]
- F.prototype 的值要么是一个对象，要么就是 null：其他值都不起作用。
- "prototype" 属性仅在设置了一个构造函数（constructor function），并通过 new 调用时才有用
- 默认的 "prototype" 是一个只有属性 constructor 的对象，属性 constructor 指向函数自身
- 对象和函数：对象是通过函数创建的，而函数又是一种对象，常见的对象创建方式是一种语法糖
```
  var obj={
      name:"哈哈",
      age:"18"
  }
  var obj=new Object()
  obj.name="哈哈";
  obj.age="18";
``` 

### 原生的类型

- 内建对象有相同的模式：
方法都存储在 prototype 中（Array.prototype、Object.prototype、Date.prototype 等）。
对象本身只存储数据（数组元素、对象属性、日期）。
- 原始数据类型也将方法存储在包装器对象的 prototype中

### 原型方法

- 设置和直接访问原型的现代方法
Object.create(proto, [descriptors]) 
Object.getPrototypeOf(obj)
Object.setPrototypeOf(obj, proto) 

## class

### 语法
```
class MyClass {
  prop = value; // 属性

  constructor(...) { // 构造器
    // ...
  }

  method(...) {} // method

  get something(...) {} // getter 方法
  set something(...) {} // setter 方法

  [Symbol.iterator]() {} // 有计算名称（computed name）的方法（此处为 symbol）
  // ...
}
```

- 类的方法之间没有逗号
- 类是一种函数,又与函数存在重大差异

### 类继承

- class Child extends Parent：
- 在使用 this 之前，必须在 Child 的 constructor 中将父 constructor 调用为 super()
- 可以在一个 Child 方法中使用 super.method() 来调用 Parent 方法
- 方法在内部的 [[HomeObject]] 属性中记住了它们的类/对象。将一个带有 super 的方法从一个对象复制到另一个对象是不安全的。

### 静态方法/静态属性
```
class MyClass {
  static property = ...;

  static method() {
    ...
  }
}
```

- 用static标记
```
  class MyClass {
    static property = ...;
  
    static method() {
      ...
    }
  }
```  

- 静态方法被用于实现属于整个类的功能，与具体的类实例无关
- 静态属性被用于想要存储类级别的数据，而不是绑定到实例。
- 静态属性和方法是可被继承的

### 私有/受保护的属性/方法

- 受保护的字段以 _ 开头，这是一个众所周知的约定，不是在语言级别强制执行的。应该只通过它的类和从它继承的类中访问以 _ 开头的字段。
- 通过设置setter/getter可以限制外部读写
- 私有字段以 # 开头。JavaScript 确保我们只能从类的内部访问它们。

### 扩展内建类

- 原生的类也是可以扩展的，使用原生类的扩展类时候，内建方法返回的是扩展类，不过可以通过 Symbol.species 返回原生类
- 内建类没有静态方法继承

### 类型检查

- typeof  原始类型数据 返回 string
- {}.toString  原始数据类型，内建对象，包含Symbol.toStringTag属性的对象，返回 string
- instanceof 对象 返回 true/false
- 语法：obj instanceof Class

### Mixin

- 一个包含其他类的方法的类
- 使用mixin作为一种通过添加多种行为来扩充类的方法

## 错误处理
```
try {
  // 执行此处代码
} catch(err) {
  // 如果发生错误，跳转至此处
  // err 是一个 error 对象
} finally {
  // 无论怎样都会在 try/catch 之后执行
}
```

- Error 对象包含下列属性 ：
message — 人类可读的 error 信息。
name — 具有 error 名称的字符串（Error 构造器的名称）。
stack（没有标准，但得到了很好的支持）— Error 发生时的调用栈。

- 可以从 Error 和其他内建的 error 类中进行继承

## Promise，async/await

### Promise

- callback在处理disposal的时候必须存在，并且只能有一个
- Promises 允许我们按照自然顺序进行编码,先运行 excutor然后运行 .then 来处理结果，并且可以多次调用.then来处理
- .then（或 catch/finally 都可以）处理程序（handler）返回一个 promise，那么链的其余部分将会等待，直到它状态变为 settled。当它被 settled 后，其 result（或 error）将被进一步传递下去
- .catch 处理 promise 中的各种 error：在 reject() 调用中的，或者在处理程序（handler）中thrown error。
- 应该将 .catch 准确地放到我们想要处理 error，并知道如何处理这些 error 的地方，没有办法从 error 中恢复的话，不使用 .catch 也可以
- Promise.all(promises) —— 等待所有 promise 都 resolve 时，返回存放结果的数组。如果给定的任意一个 promise 为 reject，那么它就会变成 Promise.all 的 error，所有其他 promise 的结果都会被忽略。
- Promise.race(promises) —— 等待第一个 settle 的 promise，并将其 result/error 作为结果。
Promise.resolve(value) —— 使用给定 value 创建一个 resolved 的 promise。
Promise.reject(error) —— 使用给定 error 创建一个 rejected 的 promise

### Async/await

- 关键字 async 让函数总是返回一个 promise，并允许在该函数内使用await
- Promise前的await使JS引擎等待该promise settle

### generator

- 通过 generator 函数 function* f(…) {…} 创建
- 在 generator（仅在）内部，存在 yield 操作。
外部代码和 generator 可能会通过 next/yield 调用交换结果
- 异步Iterable通过Symbol.asyncIterator
实现

## 模块

- 一个模块就是一个文件。浏览器需要使用 `<script type="module">` 以使 import/export 可以工作

- 模块具有自己的本地顶级作用域，并可以通过 import/export 交换功能

### 模块始终使用 use strict

- 模块代码只执行一次。导出仅创建一次，然后会在导入之间共享

- 导出导入

- 在声明一个 class/function/… 之前:

```
export [default] class/function/variable ...
独立的导出：
export {x [as y], ...}.
重新导出：
export {x [as y], ...} from "module"
export * from "module"（不会重新导出默认的导出）。
export {default [as y]} from "module"（重新导出默认的导出）。
- 模块中命名的导出：
import {x [as y], ...} from "module"
默认的导出：
import x from "module"
import {default as x} from "module"
所有：
import * as obj from "module"
导入模块（它的代码，并运行），但不要将其赋值给变量：
import "module"
```

### 动态导入

- import(module) 表达式加载模块并返回一个 promise，该 promise resolve 为一个包含其所有导出的模块对象。我们可以在代码中的任意位置调用这个表达式

## 杂项

### pxoxy

- Proxy 是对象的包装器，将代理上的操作转发到对象，并可以选择捕获其中一些操作
```
let proxy = new Proxy(target, {
  /* trap */
});
```
### eval

- 调用 eval(code) 会运行代码字符串，并返回最后一条语句的结果
- 在现代 JavaScript 编程中，很少使用它，通常也不需要使用它
- 需要从外部作用域获取数据，请使用 new Function，并将数据作为参数传递给函数

### 柯里化

- 柯里化 是一种转换，将 f(a,b,c) 转换为可以被以 f(a)(b)(c) 的形式进行调用。JavaScript 实现通常都保持该函数可以被正常调用，并且如果参数数量不足，则返回偏函数

### Reference Type

- Reference Type 是语言内部的一个类型。
读取一个属性，例如在 obj.method() 中，. 返回的准确来说不是属性的值，而是一个特殊的 “Reference Type” 值，其中储存着属性的值和它的来源对象。
这是为了随后的方法调用 () 获取来源对象，然后将 this 设为它