import qs from 'qs';
import axios from 'axios';
import Jsona from 'jsona';


const url = process.env.VUE_APP_API_BASE_URL;
const jsona = new Jsona();


function list(params) {
    const options = {
      params: params,
      paramsSerializer: function (params) {
        return qs.stringify(params, {encode: false});
      }
    };
  
    return axios.get(`${url}/roles`, options)
      .then(response => {
        return {
          list: jsona.deserialize(response.data),
          meta: response.data.meta
        };
      });
  }
  
  function get(id) {
    const options = {
      headers: {
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
      }
    };
  
    return axios.get(`${url}/roles/${id}`, options)
      .then(response => {
        let user = jsona.deserialize(response.data);
        delete user.links;
        return user;
      });
  }
  
  function add(user) {
    const payload = jsona.serialize({
      stuff: user,
      includeNames: null
    });
  
    const options = {
      headers: {
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
      }
    };
  
    return axios.post(`${url}/roles`, payload, options)
      .then(response => {
        return jsona.deserialize(response.data);
      });
  }
  
  function update(user) {
    const payload = jsona.serialize({
      stuff: user,
      includeNames: []
    });
  
    const options = {
      headers: {
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
      }
    };
  
    return axios.patch(`${url}/roles/${user.id}`, payload, options)
      .then(response => {
        return jsona.deserialize(response.data);
      });
  }
  
  function destroy(id) {
    const options = {
      headers: {
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
      }
    };
  
    return axios.delete(`${url}/roles/${id}`, options);
  }
  

  
  export default {
    list,
    get,
    add,
    update,
    destroy
  };