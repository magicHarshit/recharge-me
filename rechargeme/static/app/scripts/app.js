'use strict';

var RechargeApp = angular.module('RechargeApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'ui.bootstrap.tabs'
], function ($interpolateProvider){
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

RechargeApp.config(function ($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: '/static/app/views/main.html',
      controller: 'MainCtrl'
    })
    .when('/recharge/:id',{
      templateUrl: '/static/app/views/recharge.html',
      controller: 'RechargeController'
    })
    .when('/showmynumbers/',{
      templateUrl: '/static/app/views/mynumbers.html',
      controller: 'NumbersController'
    })
    .when('/addmoney/',{
      templateUrl: '/static/app/views/addmoney.html',
      controller: 'AddMoneyController'
    })
    .otherwise({
      redirectTo: '/'
    });
});

RechargeApp.run(function ($http, $cookies) {
  $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});
