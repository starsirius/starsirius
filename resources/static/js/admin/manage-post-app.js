'use strict';

/* App Module */

var module = angular.module('managePost', ['managePost.controllers', 'managePost.directives'], function ($interpolateProvider) {
    $interpolateProvider.startSymbol('<[');
    $interpolateProvider.endSymbol(']>');
});
