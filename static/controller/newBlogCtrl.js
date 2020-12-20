app.controller('newblogCtrl', function($scope, $http){

    $scope.title = "";

    $scope.shortDesp = "";

    $scope.longDesp = "";

    $scope.image = "";

    $scope.editComment = false;

    $scope.blogsResult = [];

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


	$scope.blogCRUD = function(){

        var dataObj = {}
        dataObj = {"userid" :$scope.userid, "username":$scope.username, "title":$scope.title,"short_description":$scope.shortDesp,"long_description":$scope.longDesp};
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

    $scope.updateBlog = function(post){
        var dataObj = {"userid":post.cmntuserid, "postid": post.cmntpostid, "id":post.cmntid};
        if (dataObj){
            $http ({
                url : '/deletecomment',
                headers: {'Content-Type': 'application/json','Access-Control-Allow-Origin': '*', 'x-api-key': $scope.apikey},
                method : 'POST',
                data: JSON.stringify(dataObj),
            }).then(function(response) {
                console.log(response);
                $scope.customComment = "";
                if (response.data.status == "Success"){
                    $scope.blogsResult = response.data.bloglist;
                    $scope.getBlogs();
                }
            })
        }
    }


	$scope.getBlogs()
	
})
