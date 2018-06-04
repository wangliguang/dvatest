import { call, put, takeEvery } from 'redux-saga/effects'

function* wathActionAndLogger() {
  yield takeEvery('*', function* (action) {
    console.log('Logger', action);
  });
}


export default function* rootSaga() {
  yield [wathActionAndLogger()];
}