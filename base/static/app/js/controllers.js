'use strict';

/* Controllers */

var elevendanceControllers = angular.module('elevendanceControllers', []);

elevendanceControllers.controller('navController', ['$scope',
  function($scope) {
    $scope.orgs = [
      {name: 'Beyond Blues'},
      {name: 'Lindy and Blues'},
      {name: 'Austin Blues Society'},
      {name: 'Portland Blues and Jazz'}
    ];

    $scope.username = 'pmandel';
  }]);

elevendanceControllers.controller('PhoneDetailCtrl', ['$scope', '$routeParams', 'Phone',
  function($scope, $routeParams, Phone) {
    $scope.phone = Phone.get({phoneId: $routeParams.phoneId}, function(phone) {
      $scope.mainImageUrl = phone.images[0];
    });

    $scope.setImage = function(imageUrl) {
      $scope.mainImageUrl = imageUrl;
    }
  }]);
