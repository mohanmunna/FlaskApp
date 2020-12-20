app.controller('signupCtrl', function($scope, $http){

    $scope.username = "";

    $scope.password = "";

    $scope.errorMsg = "";

    $scope.successMsg = "";

    $scope.showError = false;

    $scope.success = false;
    
    $scope.userData = {};

    // localStorage.setItem("userid", "");
    // var currentUser = localStorage.getItem("userid");
    // console.log(currentUser)

	$scope.signup = function(){
		$scope.successMsg = "";
		$scope.errorMsg = "";
		$scope.showError = false;
		$scope.success = false;

		if ($scope.username && $scope.password){
			var dataObj = {"username" :$scope.username, "password":$scope.password};
			console.log(dataObj);
			$http ({
	    		url : '/createaccount',
	    		headers: {'Content-Type': 'application/json','Access-Control-Allow-Origin': '*'},
	    		method : 'POST',
	    		data: JSON.stringify(dataObj),
	    	}).then(function(response) {
	    		console.log(response);
	    		if (response.data.status == "Success"){
	    			$scope.success = true;
	    			$scope.successMsg = "Successfully created, Please Login";
	    		}
	    		else{
	    			$scope.showError = true;
	    			$scope.errorMsg = response.data.message;
	    		}
	    		
	    	})
		}
	}
})
