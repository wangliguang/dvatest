import HomePage from './container/HomePage';
import React from 'react';
import { create } from 'dva-core';
import { Provider } from 'react-redux';
import createLoading from 'dva-loading';
import registerModel from './model';
import rootSaga from './watchAction';

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
