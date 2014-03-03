'use strict';

/* App Module */

var elevendanceApp = angular.module('elevendanceApp', [
  'ngRoute',
  'elevendanceControllers',
  'elevendanceFilters',
  'elevendanceFactories'
]);

elevendanceApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'partials/home.html',
        controller: 'PhoneListCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);
