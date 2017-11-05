$(function() {
    // Populate wheel based on prompt chosen
    $('li.prompt').click(function () {
	let promptList=[]
	let postDict = {}
	console.log("prompt: ", $(this).text())
	let to_query = $(this).text();
	promptList.push(to_query);
	postDict['prompt'] = promptList;
	$.ajax({
	    type: 'POST',
	    url: '/wheelPrompt/',
	    data: JSON.stringify(postDict),
	    dataType: 'json',
	    contentType: 'application/json',
	    success: function (result) {
		$('#first').text(result[0]);
		$('#second').text(result[1]);
		$('#third').text(result[2]);
		$('#fourth').text(result[3]);
		$('#fifth').text(result[4]);
		$('#sixth').text(result[5]);
	    },
	    error: function (error) {
		alert("An error occured: " + error.status + " " + error.statusText);
	    }
	});
    });
    $('li.players').click(function () {
	let playerList=[]
	let postDict = {}
	let to_query = $(this).text();
	playerList.push(to_query);
	postDict['num_player'] = playerList;
	$.ajax({
	    type: 'POST',
	    url: '/wheelGame/',
	    data: JSON.stringify(postDict),
	    dataType: 'json',
	    contentType: 'application/json',
	    success: function (result) {
		console.log("result: ", result)
		$('#first').text(result[0]);
		$('#second').text(result[1]);
		$('#third').text(result[2]);
		$('#fourth').text(result[3]);
		$('#fifth').text(result[4]);
		$('#sixth').text(result[5]);
	    },
	    error: function (error) {
		alert("An error occured: " + error.status + " " + error.statusText);
	    }
	});
    });
});
