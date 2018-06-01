import React, { Component } from 'react';
import { connect } from 'react-redux';
import {
  Platform,
  StyleSheet,
  Text,
  View
} from 'react-native';

import * as reducerType from '../model'

type Props = {};
class HomePage extends Component<Props> {

  componentDidMount() {
    this.props.setUserInfo(reducerType.USER_SAVEUSER, { name: '王立广', age: 26 });
  }

  render() {
    return (
      <View style={styles.container}>
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
  console.log(state);
  return {
    loading,
    User,
  }
}

const mapDispatchToProps = (dispatch) => ({
  setUserInfo: (type, payload) => {
    dispatch({
      type,
      payload,
    });
  }
});

export default connect(mapStateToProps, mapDispatchToProps)(HomePage);