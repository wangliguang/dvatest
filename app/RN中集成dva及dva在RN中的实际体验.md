## 知识储备

| 知识点    | 需掌握的程度             |
| --------- | ------------------------ |
| generator | 了解*、yield和next的作用 |
| redux     | 深入理解                 |
| thunk     | 深入理解                 |
| saga      | 基本了解                 |
| 单元测试  | 了解基本的单元测试即可   |
| dva       | 基本了解                 |



## redux与dva的对比

|            | Redux        | Dva                                                         |
| ---------- | ------------ | ----------------------------------------------------------- |
| 集成方式   | 配置比较繁琐 | 配置更加简洁                                                |
| 学习成本   | 文档详细     | 文档也很详细，除此之外提供有知识网络和中文参考资料,示例也多 |
| saga的集成 | 较为复杂     | dva里是直接集成saga的                                       |



## thunk与saga的对比

|            | thunk                              | Saga                                       |
| ---------- | ---------------------------------- | ------------------------------------------ |
| 异步处理   | 在action中处理，使action产生副作用 | 在saga中间件处理，保证action始终没有副作用 |
| 单元测试   | 因为有副作用对aciton无法做单元测试 | 因为无副作用可以对action直接进行单元测试   |
| 异步可控性 | 异步流程不可控，并不可取消         | 异步流程可控制，并可取消                   |
| 学习成本   | 低                                 | 比较高                                     |



## dva的API介绍

| API                 | 介绍                                                         |
| ------------------- | ------------------------------------------------------------ |
| create(parm1,parm2) | dva初始化。有两个参数，并且都是对象。返回一个dva对象<br />第一个参数是指定hoock,可以对一些操作进行拦截处理(可以拦截的操作如下：onError/onStateChange/onAction/onHmr/onReducer/onEffect/extraReducers/extraEnhancers/_handleActions)，第二个参数暂时未知 |
| app.model()         | 使用create创建出来的对象注册model(action和reducer的整合)     |
| app.start()         | 启动dva，将model中的state转为store，只有执行start后, app._store才会被赋值。这个sotore跟redux中的store是一个概念 |
| app._store          | 获取全局唯一的store,  只有执行过前面三个方法，store才有值    |



## saga的API介绍

| API  | 介绍 |
| ---- | ---- |
| call |      |
|      |      |
|      |      |
|      |      |
|      |      |



## 在RN中集成dva



## QA












# effect的API

- ### call: 

  在正常写逻辑时，call可用可不用，但使用call时会帮我们返回一个对象，来标识后面的语句是做什么的，方便我们做函数的颗粒化测试

- ### redux-saga中的action为什么使用yield呢，在项目中又没有调用过generater的next方法

    我们在action中一般会做多个异步处理，比如有异步A和异步B，异步A在异步B之前条用，并且异步B要用到异步A最后获取到的数据。此时如果使用如下方式来调用：
            
      function* asyncOpertion() {      
        let resultA = yield 异步A
        yeild resultA + 1
      }
    
    saga内部的机制，会先执行一次asyncOpertion().next()，等异步A执行完之后才会执行下一次asyncOpertion().next()，执行异步B

- ### put

  相当于dispatch

## 参考资料

- [redux-saga(强烈推荐看一下提供的例子)](https://redux-saga-in-chinese.js.org/)

- [dva(提供了很多干货)](https://github.com/dvajs/dva/blob/master/README_zh-CN.md)

- [saga与thunk](https://segmentfault.com/a/1190000009928167)
- [异步方案选型saga与thunk](https://blog.csdn.net/liwusen/article/details/79677827)








