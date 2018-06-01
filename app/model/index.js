import userModel from './UserModel';

export default registerModel = (app) => {
  app.model(userModel);
};

export const USER_SAVEUSER = 'user/saveUser';