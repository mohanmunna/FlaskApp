app.controller('updateBlogCtrl', function($scope, $http){

    $scope.title = "";

    $scope.shortDesp = "";

    $scope.longDesp = "";

    $scope.image = "";
    
    $scope.postId = "";
    
    $scope.userId = "";

    $scope.username = "";

    $scope.blogsResult = [];

    $scope.apikey = localStorage.getItem("apikey");
    $scope.userid = localStorage.getItem("userid");
    $scope.username = localStorage.getItem("username");
    $scope.usertype = localStorage.getItem("usertype");

    
    $scope.updateObj = JSON.parse(localStorage.getItem("updateObj"));
    console.log($scope.updateObj);

    if ("short_description" in $scope.updateObj){
        $scope.shortDesp = $scope.updateObj.short_description;
    }

    if ("long_description" in $scope.updateObj){
        $scope.longDesp = $scope.updateObj.long_description;
    }

    if ("title" in $scope.updateObj){
        $scope.title = $scope.updateObj.title;
    }
    
    if ("postid" in $scope.updateObj){
        $scope.postId = $scope.updateObj.postid;
    }

    if ("userid" in $scope.updateObj){
        $scope.userId = $scope.updateObj.userid;
    }

    if ("username" in $scope.updateObj){
        $scope.username = $scope.updateObj.username;
    }


	$scope.blogCRUD = function(){
        var dataObj = {}
        dataObj = {"postid" :$scope.postId, "userid" :$scope.userId, "username":$scope.username, "title":$scope.title,"short_description":$scope.shortDesp,"long_description":$scope.longDesp};
        console.log(dataObj)
        $http ({
            url : '/createblog',
            headers: {'Content-Type': 'application/json','Access-Control-Allow-Origin': '*', 'x-api-key': $scope.apikey},
            method : 'POST',
            data: JSON.stringify(dataObj),
        }).then(function(response) {
            console.log(response);
            if (response.data.status == "Success"){
                window.location = "/blogs"
            }
        })
	}
	
})
