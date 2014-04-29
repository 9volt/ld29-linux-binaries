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
    $scope.osFilter =  function(input){
        if($scope.os.length > 0){
            for(var o in $scope.os){
                for(var b in input.binaries){
                    if(input.binaries[b] == $scope.os[o]){
                        return true;
                    }
                }
            }
            return false;
        } else {
            return true;
        }
    };
    $scope.games = angular.fromJson(game_json);
}
