$(function() {
    // checkbox display number of players
    let playerSet = new Set();
    $('input').change(function () {
	if (this.checked) {
	    playerSet.add($(this).attr('data-id'));
	} else {
	    playerSet.delete($(this).attr('data-id'));
	}
	let playerStr = '';
	let separator = '';
	let playerArr = Array.from(playerSet);

	let pLen = playerArr.length;
	for (i = 0; i < pLen; i++) {
	    playerStr += separator;
	    playerStr += playerArr[i];
	    separator = ", ";
	}
	if (playerStr === '') {
	    $('h3').text(String.fromCharCode(160));
	} else {
	    $('h3').text(playerStr);
	}
    });

    // Search when button is clicked
    $('#search-button').click(function () {
	let playerList = Array.from(playerSet);
	let postDict = {};
	postDict['players'] = playerList;
	$.ajax({
	    type: 'POST',
	    url: '/gameList/',
	    data: JSON.stringify(postDict),
	    dataType: 'json',
	    contentType: 'application/json',
	    success: function (result) {
		$('article').remove();
		for (let game in result) {
		    let structure = [
			'<article class="col-xs-12">',
			'<div class="game-name">',
			'<h2>' + result[game].name + '</h2>',
			'</div>',
			'<div class="information">',
			'<div class="num-players col-sm-3 col-xs-12">',
			'<img class="col-sm-12 col-xs-4" src="https://cdn2.iconfinder.com/data/icons/user-interface-essentials-outline/48/ui-49-128.png" alt="player icon" aria-hidden="true">',
			'<p class="col-sm-12 col-xs-8">' + result[game].num_player + ' Players </p>',
			'</div>',
			'<div class="directions col-sm-9 col-xs-12">',
			'<p>' + result[game].description + '</p>',
			'</div>',
			'</div>',
			'</article>'
		    ];
		    $(structure.join('')).appendTo('#idv-games');
		}
	    },
	    error: function (error) {
		alert("An error occured: " + error.status + " " + error.statusText);
	    }
	});
    });
})
