app.controller('myAccountCtrl', function($scope, $http){


    $scope.apikey = localStorage.getItem("apikey");
    $scope.userid = localStorage.getItem("userid");
    $scope.username = localStorage.getItem("username");
    $scope.usertype = localStorage.getItem("usertype");



	$scope.getBlogs = function(){
        var dataObj = {"userid" :$scope.userid};
        console.log(dataObj);
        $http ({
            url : '/getbloglist',
            headers: {'Content-Type': 'application/json','Access-Control-Allow-Origin': '*', 'x-api-key': $scope.apikey},
            method : 'POST',
            data: JSON.stringify(dataObj),
        }).then(function(response) {
            console.log(response);
            if (response.data.status == "Success"){
                $scope.blogsResult = response.data.bloglist;
            }
        })
    }

    $scope.getBlogs();
	
})
