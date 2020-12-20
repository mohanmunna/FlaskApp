app.controller('blogDetailCtrl', function($scope, $http){

    $scope.customComment = "";
    $scope.editComment = false
    $scope.blogsResult = {};
    $scope.blogsResult = JSON.parse(localStorage.getItem("blogDetails"));
    console.log($scope.blogsResult);

})
