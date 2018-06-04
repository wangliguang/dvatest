import React, { Component } from 'react';
import { connect } from 'react-redux';
import {
  Platform,
  StyleSheet,
  Text,
  View,
  Button
} from 'react-native';
import * as reducerType from '../model'

type Props = {};
class HomePage extends Component<Props> {

  componentDidMount() {
    this.props.setUserInfo(reducerType.USER_SAVEUSER, { name: '王立广', age: 26 });
    this.props.login(reducerType.USER_LOGIN, { phone: '13121529304', pwd: '1234' });
  }

  render() {
    return (
      <View style={styles.container}>
        <Button onPress={() => {
          this.props.login(reducerType.USER_LOGIN, { phone: '13121529304', pwd: '1234' });
        }} title={'发送登录请求'}/>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'orange',
  },
});

const mapStateToProps = (state) => {
  const { loading, User } = state;
  return {
    loading,
    User,
  }
}

const mapDispatchToProps = (dispatch) => ({
  setUserInfo: (type, payload) => {
    dispatch({ type,payload });
  },
  login: (type, payload) => {
    dispatch({ type, payload });
  }
});

export default connect(mapStateToProps, mapDispatchToProps)(HomePage);