const userModel = {};
import RequestUtil from '../utils/Request';

userModel.namespace = 'user';

userModel.state = {
  name: 'GG',
  age: '18',
};

userModel.reducers = {
  // state是上次的值， payload是本次获取到的值
  saveUser(state, { payload }) {
    return {
      ...state,
      ...payload,
    };
  },
}

userModel.effects = {
  *login ({ payload }, { put, call }) {
    try{
      let data = yield call(RequestUtil.request,true,'user/login','post',payload);
      console.log('================================');
      console.log(payload);
      console.log(data);
    }catch(error){
      console.log(error);
    }
  },
}

export default userModel;