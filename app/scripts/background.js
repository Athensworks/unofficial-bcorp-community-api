'use strict';
$=jQuery;
//function urlRegEx()
//{
	//var urlrex = rex + str + rex;
	//return rex;

//}








function ifgoogle (Id,url)
{
	$.getJSON('scripts/data.json',function(result) {
		var rex;
		for (var i = 0; i < result.length; i++) {
			rex = new RegExp('.*'+ result[i].website + '.*');
			if (rex.test(url))   {
				chrome.pageAction.show(Id);
				return;
			}
		}
	});
		
}

function onQuery(tabs)
{
	var tab = tabs[0];
	console.log(typeof tab.url);
	console.log(tab.url);
	ifgoogle(tab.id,tab.url);
}
	
	


function getCurrentTab() {
	 /*Query filter to be passed to chrome.tabs.query - see
	  *https://developer.chrome.com/extensions/tabs#method-query
	  */
	var queryInfo = {
      active: true,
      currentWindow: true
	  };
	chrome.tabs.query(queryInfo,function(tabs){onQuery(tabs);});
}

chrome.tabs.onUpdated.addListener(function() {
	getCurrentTab();
});

console.log('\'Allo \'Allo! Event Page for Page Action');
