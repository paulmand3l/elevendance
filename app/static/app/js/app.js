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
        templateUrl: '/static/app/partials/home.html',
        controller: 'PhoneListCtrl'
      }).
      when('/registration', {
        templateUrl: '/static/app/partials/registration.html',
        controller: 'RegistrationController'
      }).
      when('/scheduling', {
        templateUrl: '/static/app/partials/scheduling.html',
        controller: 'SchedulingController'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);
