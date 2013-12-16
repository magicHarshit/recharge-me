'use strict';

angular.module('RechargeApp')
  .controller('MainCtrl', function($scope) {
    $scope.panes = [
      { title:'My numbers', content:'/static/app/views/mynumbers.html', active: true },
      { title:'Add money', content:'/static/app/views/addmoney.html'},
      { title:'Add phone numbers', content:'/static/app/views/addnumbers.html'}
    ];
  });
