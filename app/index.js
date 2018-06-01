import HomePage from './container/HomePage';
import React from 'react';
import { create } from 'dva-core';
import { Provider } from 'react-redux';

/* =============Model=============  */
const UserModel = {
  namespace: 'User',
  state: {},
  reducers: {
    saveUser(state, { payload }) {
      return {
        ...state,
        ...payload,
      };
    },
  }
}

export default function () {
  const app = create({
    onError: (error) => { alert(error);},
  });
  app.model(UserModel);
  app.start();

  const store = app._store;
  return (
    <Provider store={store}>
      <HomePage/>
    </Provider>
  )
}
