angular.module('TrueCarApp').controller('SearchVsnController', ["$scope", "$element", "$compile", "$http", "$q", "searchVsnService", function($scope, $element, $compile, $http, $q, searchVsnService){

    var vm = this;

    vm.getMatches = function(vsn) {

        searchVsnService.getVsn(vsn)
            .success(function(data, status, headers, config) {
                console.log('success', status);
                console.log('matches data', data);
                vm.matches = data
            })
            .error(function(data, status, headers, config) {
                console.log('error', status);
            });
        return $scope.matches
    };
}]);
