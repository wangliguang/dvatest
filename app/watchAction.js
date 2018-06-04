import { call, put, takeEvery, select } from 'redux-saga/effects'

function* wathActionAndLogger() {
  yield takeEvery('*', function* (action) {
    const state = yield select()
    console.log('action', action);
    console.log('state', state);

  });
}


export default function* rootSaga() {
  yield [wathActionAndLogger()];
}