var rechargeAppControllers = angular.module('rechargeAppControllers',[]);


rechargeAppControllers.controller('NumberListController',function($scope,$http){
    $http.get('/api/numbers/?format=json').success(function(data){
        $scope.numbers = data
    });
});

rechargeAppControllers.controller('AddNumberController',function($scope,$routeParams, $http){

    $scope.save = function(){
        $http.post('/api/numbers/',{'phnumber':$scope.phnumber}).
            success(function(data){
                $scope.phnumber = '';
                $scope.number = data;
                $scope.error = false
            }).
            error(function(data,status,confiq,header){
                $scope.error = data
            })
    }
});


rechargeAppControllers.controller('AddMoneyController',function($scope,$http){
    $http.get('/api/account/?format=json').success(function(data){
        $scope.account = data
    });
    $scope.addMoney = function(){
        $http.post('/account/update/',{'balance':$scope.balance}).
            success(function(data){
                $scope.balance = '';
                $scope.new_balance = data
            }).
            error(function(data){
                $scope.error = data
            })
    }
});

rechargeAppControllers.controller('RechargeController',function($scope,$routeParams,$http){
   $http.get('/api/number/'+ $routeParams.numberId+'/?format=json').success(function(data){
      $scope.number = data
   });

   $scope.recharge = function(number){
       $http.post('/account/update/',{'balance':$scope.recharge_amount,'action':'Recharge'}).
           success(function(data){
               $http.put('/api/number/'+number.id+'/',{'is_successful':true,'phnumber':number.phnumber}).
                   success(function(data){
                       $scope.status = 'Success'
                   });
               $scope.recharge_amount= '';
           })
   }
});
