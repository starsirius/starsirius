'use strict';

/* Directives */

angular.module('managePost.directives', [])
    // Register the 'idleTime' directive factory method.
    // We inject $timeout and dateFilter service since the factory method is DI.
    .directive('idleTime', function($timeout) {
        return function(scope, element, attrs) {
            var timeoutId;

            scope.start = new Date().getTime();
            scope.$watch('start', function(newValue, oldValue) {
                updateTime();
            });

            function updateTime() {
                var now = new Date().getTime(), 
                    elapsedTime = now - scope.start;
                element.text(elapsedTime);
            }

            // schedule update in one second
            function updateLater() {
                // save the timeoutId for canceling
                timeoutId = $timeout(function() {
                    updateTime();
                    updateLater(); // schedule another update
                }, 1000);
            }

            // listen on DOM destroy (removal) event, and cancel the next UI update
            // to prevent updating time after the DOM element was removed.
            element.on('$destroy', function() {
                $timeout.cancel(timeoutId);
            });

            $(document).on("mousemove keypress", function() {
                scope.$apply(function () {
                    scope.start = new Date().getTime();
                });
            });

            updateLater(); // kick off the UI update process.
        };
    });
