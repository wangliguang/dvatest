const userModel = {};

userModel.namespace = 'user';

userModel.state = {
  name: 'GG',
  age: '18',
};

userModel.reducers = {
  saveUser(state, { payload }) {
    return {
      ...state,
      ...payload,
    };
  },
}


export default userModel;