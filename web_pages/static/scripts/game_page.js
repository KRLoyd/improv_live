$(function() {
    // checkbox display number of players
    let playerSet = new Set();
    $('input').change(function () {
	console.log("input text: ", $(this).attr('data-id'))
	if (this.checked) {
	    playerSet.add($(this).attr('data-id'));
	} else {
	    playerSet.delete($(this).attr('data-id'));
	}
	console.log("playerSet: ", playerSet)
	let playerStr = '';
	let separator = '';
	let playerArr = Array.from(playerSet);
	console.log("playerArr: ", playerArr);

	let pLen = playerArr.length;
	for (i = 0; i < pLen; i++) {
	    playerStr += separator;
	    playerStr += playerArr[i];
	    separator = ", ";
	}
	console.log("playerStr: ", playerStr)
	if (playerStr === '') {
	    $('h3').text(String.fromCharCode(160));
	} else {
	    $('h3').text(playerStr);
	}
    });

    // Search when button is clicked
    $('#search-button').click(function () {
	let playerList = [];
	for (let i in playerDict) {
	    playerList.push(i);
	}
	let postDict = {};
	postDict['players'] = playerList;
	$.ajax({
	    type: 'POST',
	    url: '/gameList/',
	    data: JSON.stringify(postDict),
	    dataType: 'json',
	    contentType: 'application/json',
	    success: function (result) {
		for (let i in result) {
		    let structure = [
			//structure of article
			// access info : request[i].<attr>
		    ];
		    $(structure.join('')).appendTo('section.games');
		}
	    },
	    error: function (error) {
		alert("An error occured: " + error.status + " " + error.statusText);
	    }
	});
    });
})
