# RN中集成dva及dva在RN中的实际体验



## 知识储备

| 知识点    | 需掌握的程度             |
| --------- | ------------------------ |
| redux     | 深入理解                 |
| dva       | 基本了解                 |
| thunk     | 深入理解                 |
| saga      | 基本了解                 |
| generator | 了解*、yield和next的作用 |
| 单元测试  | 了解基本的单元测试即可   |



## redux与dva的对比

|            | Redux        | Dva                                                         |
| ---------- | ------------ | ----------------------------------------------------------- |
| 集成方式   | 配置比较繁琐 | 配置更加简洁                                                |
| 学习成本   | 文档详细     | 文档也很详细，除此之外提供有知识网络和中文参考资料,示例也多 |
| saga的集成 | 较为复杂     | dva里是直接集成saga的                                       |

## dva的API介绍

| API                 | 介绍                                                         |
| ------------------- | ------------------------------------------------------------ |
| create(parm1,parm2) | dva初始化。有两个参数，并且都是对象。返回一个dva对象<br />第一个参数是指定hoock,可以对一些操作进行拦截处理(可以拦截的操作如下：onError/onStateChange/onAction/onHmr/onReducer/onEffect/extraReducers/extraEnhancers/_handleActions)，第二个参数暂时未知 |
| app.model()         | 使用create创建出来的对象注册model(action和reducer的整合)     |
| app.start()         | 启动dva，将model中的state转为store，只有执行start后, app._store才会被赋值。这个sotore跟redux中的store是一个概念 |
| app._store          | 获取全局唯一的store,  只有执行过前面三个方法，store才有值    |




## thunk与saga的对比

|            | thunk                              | Saga                                       |
| ---------- | ---------------------------------- | ------------------------------------------ |
| 异步处理   | 在action中处理，使action产生副作用 | 在saga中间件处理，保证action始终没有副作用 |
| 单元测试   | 因为有副作用对aciton无法做单元测试 | 因为无副作用可以对action直接进行单元测试   |
| 异步可控性 | 异步流程不可控，并不可取消         | 异步流程可控制，并可取消                   |
| 学习成本   | 低                                 | 比较高                                     |


## saga的effects API介绍

eeffects API都会返回一个纯对象来描述当前的操作，会方便我们做模拟数据测试。另外这些API都是纯函数，也不会进行实际的操作，具体的操作都是saga中间件根据他们返回值来处理的。

| API        | 介绍                                                         |
| ---------- | ------------------------------------------------------------ |
| put        | 类似于dispatch                                               |
| select     | 类似于getState                                               |
| call       | 发起异步操作（阻塞调用）                                     |
| fork       | 发起异步操作（非阻塞调用）                                   |
| take       | 执行一次，只会监听一次，并且会阻塞后面的调用                 |
| takeEvery  | 执行一次,便会永久监听                                        |
| takeLatest | 监听action,   多个action时，处理最后一次发起的异步请求，如果上次未结束则会被取消 |
| cancel     | 取消一个还未返回的fork任务                                   |
| all        | 同Promise                                                    |
| race       | 同Promise                                                    |



takeEvery  可以同时执行多个action  takeLatest  多个action同时发出，只会执行最后一个

## 在RN中集成dva

```javascript
export default function () {
  const app = create({
    ...createLoading({ effects: true }),
  });
  registerModel(app);
  app.start();
  const store = app._store;
  store.runSaga(rootSaga);
  return (
    <Provider store={store}>
      <HomePage/>
    </Provider>
  )
}
```


## QA



## 参考资料

- [redux-saga(强烈推荐看一下提供的例子)](https://redux-saga-in-chinese.js.org/)

- [dva(提供了很多干货)](https://github.com/dvajs/dva/blob/master/README_zh-CN.md)

- [saga与thunk](https://segmentfault.com/a/1190000009928167)
- [异步方案选型saga与thunk](https://blog.csdn.net/liwusen/article/details/79677827)








