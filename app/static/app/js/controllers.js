'use strict';

/* Controllers */

var elevendanceControllers = angular.module('elevendanceControllers', []);

elevendanceControllers.controller('NavController', ['$scope',
  function($scope) {
    $scope.orgs = [
      {name: 'Beyond Blues'},
      {name: 'Lindy and Blues'},
      {name: 'Austin Blues Society'},
      {name: 'Portland Blues and Jazz'}
    ];

    $scope.username = 'pmandel';
  }]);

elevendanceControllers.controller('RegistrationController', ['$scope',
  function($scope) {
    $scope.message = "Hello, world!";

    $scope.attendees = [
      {name: 'Paul Mandel', paid: '5'},
      {name: 'Brenda Russell', paid: '5'},
      {name: 'Nicole Trissell', paid: '0', comp: true}
    ];

  }]);

elevendanceControllers.controller('PhoneDetailCtrl', ['$scope', '$routeParams', 'Phone',
  function($scope, $routeParams, Phone) {
    $scope.phone = Phone.get({phoneId: $routeParams.phoneId}, function(phone) {
      $scope.mainImageUrl = phone.images[0];
    });

    $scope.setImage = function(imageUrl) {
      $scope.mainImageUrl = imageUrl;
    };
  }]);
