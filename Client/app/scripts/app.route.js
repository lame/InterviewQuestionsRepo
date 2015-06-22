(function() {
  'use strict';
  angular.module('TrueCarApp')
  .config(['$stateProvider','$urlRouterProvider', '$locationProvider',
           function ($stateProvider, $urlRouterProvider, $locationProvider) {
    $urlRouterProvider.otherwise('landing');

    $stateProvider
    .state('search-vsn', {
      url:'/search-vsn',
      templateUrl: 'views/search_vsn.html',
      controller: 'searchVsnController'
    })

    .state('landing', {
      url:'/landing',
      templateUrl: 'views/landing.html'
    })

  }]);
})();
