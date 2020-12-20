app.controller('loginCtrl', function($scope, $http){

    $scope.username = "";

    $scope.password = "";

    $scope.errorMsg = "";

    $scope.showError = false;
    
    $scope.userData = {};

    // localStorage.setItem("userid", "");
    // var currentUser = localStorage.getItem("userid");
    // console.log(currentUser)

	$scope.loginAccount = function(){
		$scope.showError = false;
		if (($scope.username != undefined && $scope.username !="" && $scope.username != null) && 
			($scope.password != undefined && $scope.password !="" && $scope.password != null)){
			var dataObj = {"username" :$scope.username, "password":$scope.password};
			console.log(dataObj);
			$http ({
	    		url : '/loginaccount',
	    		headers: {'Content-Type': 'application/json','Access-Control-Allow-Origin': '*'},
	    		method : 'POST',
	    		data: JSON.stringify(dataObj),
	    	}).then(function(response) {
	    		console.log(response);
	    		if (response.data.status == "Success"){
	    			$scope.userData = response.data.userdetail;
	    			localStorage.setItem("userid", $scope.userData.userid);
	    			localStorage.setItem("username", $scope.userData.username);
	    			localStorage.setItem("apikey", $scope.userData.apikey);
	    			localStorage.setItem("usertype", $scope.userData.usertype);
	    			window.location = "/blogs"
	    		}
	    		else{
	    			$scope.showError = true;
	    			$scope.errorMsg = response.data.message;
	    		}
	    		
	    	})
		}
		else{
			$scope.showError = true;
			$scope.errorMsg = "Incorrect details";
		}
	}
})
