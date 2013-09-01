'use strict';

/* Controllers */

angular.module('managePost.controllers', [])
    .controller('PortfolioController', ['$scope', '$http', function($scope, $http) {
        /******
        * Local variables
        *****************/

        /******
        * Data models
        *****************/
        $scope.works = [
            {
                id: 1, 
                title: "Title 1", 
                post: {
                    content: "Content of work 1"
                }, 
                published: "2013-04-13 04:56pm"
            }, 
            {
                id: 2, 
                title: "Title 2", 
                post: {
                    content: "Content of work 2"
                }, 
                published: "2013-04-24 13:36pm"
            } 
        ];

        /******
        * Functions
        *****************/

    }])
    .controller('NewController', [function() {
        /******
        * Local variables
        *****************/

        /******
        * Data models
        *****************/

        /******
        * Functions
        *****************/
    }]);
