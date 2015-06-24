(function(){

    angular.module('TrueCarApp').factory('searchVsnService', searchVsnService);
    searchVsnService.$inject = ['$http', '$q', '$log', 'TrueCar_Config'];

    function searchVsnService($http, TrueCar_Config){

        var searchVsnService = {
            getVsn: getVsn,
        };
        return searchVsnService;

        function getVsn(vsn){
            var url = ["http://localhost:5000/api/vsn", vsn].join('/');
            return $http.get(url);
        }

    }

})();
