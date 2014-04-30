function ListCtrl($scope){
    $scope.oses = ["web", "windows", "osx", "linux"];
    $scope.os = [];
    $scope.toggle = function(input){
        if($scope.os.indexOf(input) > -1){
            $scope.os.splice($scope.os.indexOf(input), 1);
        } else {
            $scope.os.push(input);
        }
    };
    $scope.osActive = function(input){
        return $scope.os.indexOf(input) > -1;
    };
    $scope.hasOS = function(game, test_os){
        for(var b in game.binaries){
            if(game.binaries[b] == test_os){
                return true;
            }
        }
        return false;
    };
    $scope.osURL = function(game, test_os){
        for(var b in game.binaries){
            if(game.binaries[b] == test_os){
                return game.binary_url[b];
            }
        }
        return "";
    };
    $scope.osFilter =  function(input){
        if($scope.os.length > 0){
            for(var o in $scope.os){
                if(typeof input.binaries == 'undefined' || input.binaries.indexOf($scope.os[o]) == -1){
                    return false;
                }
            }
            return true;
        } else {
            return true;
        }
    };
    $scope.games = angular.fromJson(game_json);
}
