function processJSON() {
  var p;
  alert(p);
  $.getJSON('https://api.thingspeak.com/channels/1344250/feed/last.json?api_key=SKF96HHC05WSCCXA', function(data) { 
  p = data.field8;
  
  if(data==1) location.href('Sano.html');
  if(data==2) location.href('Media.html');
  if(data==3) location.href('Moderada.html');
  if(data==4) location.href('Grave.html');});
};

  

 







