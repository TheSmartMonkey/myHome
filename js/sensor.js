
// var fs = require('fs');

$( document ).ready(function() {

//     function generateJsonFile() {
//         var dict = {"one" : [15, 4.5]};
//         // alert("imported")
//         var dictstring = JSON.stringify(dict);
    
        
//         fs.writeFile("sensor.json", dictstring, function(err, _result) {
//             if(err) console.log('error', err);
//         });
//     }

//     $('#toggle-event').on('click',function() {
//         if($(this).is(':checked')) {
//             generateJsonFile();
//         } else {
//             generateJsonFile();
//         }
//     })

var dict = {"one" : [15, 4.5]};

var json = $.getJSON("sensor.json");

var data = eval("(" +json.responseText + ")");

document.write(data["a"]);

});

