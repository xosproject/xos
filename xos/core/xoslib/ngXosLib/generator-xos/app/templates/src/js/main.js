/* global angular */
/* eslint-disable dot-location*/

// TODO
// - Add Cache
// - Refactor routing with ui.router and child views (share the navigation and header)

'use strict';

angular.module('xos.<%= name %>', [
  'ngResource',
  'ngRoute',
  'ngCookies',
  'ngLodash',
  'xos.xos'
])
.config(($interpolateProvider, $routeProvider, $resourceProvider) => {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');

  // NOTE http://www.masnun.com/2013/09/18/django-rest-framework-angularjs-resource-trailing-slash-problem.html
  $resourceProvider.defaults.stripTrailingSlashes = false;

  $routeProvider
  .when('/', {
    template: '<users-list></users-list>',
  })

  .otherwise('/');
})
// TODO move this in xos.service module
.config(function($httpProvider){
  // add X-CSRFToken header for update, create, delete (!GET)
  $httpProvider.interceptors.push('SetCSRFToken');
})
.factory('SetCSRFToken', function($cookies){
  return {
    request: function(request){

      // if request is not HTML
      if(request.url.indexOf('.html') === -1){
        request.url += '?no_hyperlinks=1';
      }

      if(request.method !== 'GET'){
        // request.headers['X-CSRFToken'] = $cookies.get('csrftoken');
        request.headers['X-CSRFToken'] = $cookies.get('xoscsrftoken');
      }
      return request;
    }
  };
})
// ENDTODO
.directive('usersList', function(xos){
  return {
    restrict: 'E',
    scope: {},
    bindToController: true,
    controllerAs: 'vm',
    templateUrl: 'templates/users-list.tpl.html',
    controller: function(){
      // creating the API object
      const api = new xos({domain: ''});

      // retrieving user list
      api.User_List_GET()
      .then((users) => {
        this.users = users;
      })
      .catch((e) => {
        throw new Error(e);
      });
    }
  };
});