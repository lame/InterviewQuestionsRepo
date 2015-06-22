(function(){

    angular.module('TrueCarApp').factory('searchVsnService', searchVsnService);
    searchVsnService.$inject = ['$http', 'TrueCar_Config'];

    var base_url = TrueCar_Config.apiUrl + 'api/sitters';

    function searchVsnService($http, TrueCar_Config){
        var searchVsnService = {
            getVsn: getVsn,
        };
        return searchVsnService;

    function getVsn(vsn){
        var url = [base_url, vsn].join('/');
        return $http.get(url);
    }

    }

})();
