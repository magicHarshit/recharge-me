var rechargeApp = angular.module('rechargeApp',['ngRoute','ngCookies','rechargeAppControllers']);



rechargeApp.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});


rechargeApp.config(['$routeProvider','$httpProvider','$interpolateProvider',
    function($routeProvider,$httpProvider,$interpolateProvider){

//  it change the angular-js tag, to differentiate between django-template-tag and angular-js-tag
    $interpolateProvider.startSymbol('{{{');
    $interpolateProvider.endSymbol('}}}');

//  request.is_ajax will return True, ajax request will send the HTTP-header
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';


//    this will be used for url-routing
    $routeProvider.
        when('/numbers',{
            templateUrl:'/static/templates/number_listing.html',
            controller:'NumberListController'
        }).

        when('/number/add/',{
            templateUrl:'/static/templates/add_number.html',
            controller:'AddNumberController'
        }).
        when('/addmoney/',{
            templateUrl:'/static/templates/addmoney.html',
            controller:'AddMoneyController'
        }).
        when('/recharge/:numberId/',{
        templateUrl:'/static/templates/recharge.html',
        controller:'RechargeController'
        }).
        otherwise({
            redirectTo:'/numbers'
        });
}
]);