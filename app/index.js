import HomePage from './container/HomePage';
import React from 'react';
import { create } from 'dva-core';
import { Provider } from 'react-redux';
import createLoading from 'dva-loading';
import registerModel from './model';


// 支持的hook
// const hooks = [
//   'onError',
//   'onStateChange',
//   'onAction',
//   'onHmr',
//   'onReducer',
//   'onEffect',
//   'extraReducers',
//   'extraEnhancers',
//   '_handleActions',
// ];

export default function () {
  const app = create({
    ...createLoading({ effects: true }),
    onReducer: (reducer) => {
      // 可以拦截发送的reducer
      return (state, action) => {
        return { ...action.payload };
      }
    },
  });
  registerModel(app);
  app.start();
  const store = app._store;
  return (
    <Provider store={store}>
      <HomePage/>
    </Provider>
  )
}
