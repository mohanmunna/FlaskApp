app.controller('bloglistCtrl', function($scope, $http){

    $scope.editComment = false;

    $scope.customComment = "";

    $scope.blogsResult = [];

    $scope.noresult = false;

    $scope.isAdmin = false;

    $scope.apikey = localStorage.getItem("apikey");
    $scope.userid = localStorage.getItem("userid");
    $scope.username = localStorage.getItem("username");
    $scope.usertype = localStorage.getItem("usertype");
    if ($scope.usertype == "ADMIN"){
        $scope.isAdmin = true;        
    }
    console.log($scope.apikey)
    console.log($scope.userid)
    console.log($scope.username)
    console.log($scope.usertype)

	$scope.getBlogs = function(){
		// var dataObj = {"userid" :$scope.userid};
        var dataObj = {"userid" :""};
		console.log(dataObj);
		$http ({
    		url : '/getbloglist',
    		headers: {'Content-Type': 'application/json','Access-Control-Allow-Origin': '*', 'x-api-key': $scope.apikey},
    		method : 'POST',
    		data: JSON.stringify(dataObj),
    	}).then(function(response) {
    		console.log(response);
    		if ("bloglist" in response.data && response.data.status == "Success"){
    			$scope.blogsResult = response.data.bloglist;
    		}else{
                $scope.noresult = true;
            }
    	})
	}


	$scope.commentCRUD = function(post, type){

        console.log(post)
        console.log(type)

        var dataObj = {}
        if (type == "ADD"){
            dataObj = {"postid" :post.postid, "comment":$scope.customComment, "userid": $scope.userid, "username":$scope.username};
        }
        else if(type == "UPDATE"){
            dataObj = {"postid":post.cmntpostid, "comment": post.msg, "userid":$scope.userid, "id":post.cmntid, "username":$scope.username};
        } 

        console.log(dataObj);

        if (dataObj){
            $http ({
                url : '/commentcrud',
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


    $scope.deleteComment = function(post){
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

    $scope.updateBlog = function(post){
        localStorage.setItem('updateObj', JSON.stringify(post));
        window.location = "/updateblog";
    }


    $scope.deleteBlog = function(post){
        console.log(post);
        var dataObj = {"userid":$scope.userid, "postid": post.postid};
        console.log(dataObj);
        
        $http ({
            url : '/deleteblog',
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

    $scope.detail = function(post){
        localStorage.setItem('blogDetails', JSON.stringify(post));
        window.location = "/blogdetail";
    }


	$scope.getBlogs()
	
})
