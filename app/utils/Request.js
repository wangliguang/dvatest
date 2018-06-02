
const checkStatus = (response) =>{
  if (response.status >= 200 && response.status < 300) {
    return response;
  }
  const error = new Error(response.statusText||'');
  error.response = response;
  throw error;
};

const QueryString = (obj) =>{
  return obj ? Object.keys(obj).sort().map(function (key) {
    var val = obj[key];
    if (Array.isArray(val)) {
      return val.sort().map(function (val2) {
        return encodeURIComponent(key) + '[]=' + encodeURIComponent(val2);}).join('&');
    }
    return encodeURIComponent(key) + '=' + encodeURIComponent(val);
  }).join('&') : '';
};

const getNormalHost = () => 'http://www.wiringdata.com/';

const getHost = () => getNormalHost()+'api/v1.';

const request = (host,url, method, body)=>{
  var opts = {
    method:method,
    timeout:6*1000,
    headers:{
      'Content-Type': 'application/json;charset=UTF-8',
    },
  };
  url = host? getHost() + url:url;
  if (method!='get') {
    opts.body=JSON.stringify(body);
  }else{
    url=url+(body&&'?'+QueryString(body)||'');
  }
  return new Promise((resolve, reject) => {
    fetch(url,opts)
      .then(checkStatus)
      .then(response => response.json())
      .then((responseData) => {
        resolve(responseData);
      })
      .catch((error) => {
        reject(error);
      });
  });
};

export default {
  request,
  getNormalHost,
  getHost
};


