$lastLog = '20000101010101';
$columns = '';
var page = '';

/*
var html = '';

html += '<thead>'
html += '<th>' + 'LOGDATE' + '</th>'; 
html += '<th>' + 'PROTO' + '</th>'; 
html += '<th>' + 'ACTION' + '</th>'; 
html += '<th>' + 'SOURCE IP' + '</th>'; 
html += '<th>' + 'DESTINATION IP' + '</th>'; 
html += '</thead>';
html += '<tbody></tbody>';
*/
$(document).ready(function(){
    page = document.location.pathname.replace('search', 'dsearch');
    if(page == ''){
        page = '/dsearch/network/';
    } 

$.ajax( {
    "url": page + $lastLog,
    "success": function ( json ) {
        /*table = '<thead><tr>';
        for(var k in json.column){
            table += '<th>'+ json.column[k] + '</th>';   
        }
        table += '</tr></thead><tbody>';        
        var myDataTable = $('#example').dataTable();      
        myDataTable.append(table);*/
        //$('#example').append(table);        
        for(var i in json.data){    
            var retArr = [];
            
            for(var j in json.column)
            {
                var temp = eval('json.data[i].'+json.column[j]);
                if(json.column[j] == 'logdate'){
                    temp = temp.substring(0, 4) + "/" + temp.substring(4, 6) + "/" + temp.substring(6,8) + " " + temp.substring(8,10) + ":" + temp.substring(10,12) + ":" + temp.substring(12,14);
                }
                retArr.push(temp);
            }

            $('#example').dataTable().fnAddData( 
            retArr);
            if(json.data[i].logdate > $lastLog) {
                $lastLog = json.data[i].logdate;     
            } 
        }
    },
    "dataType": "json"
} );
});




setInterval( function(){
$.ajax( {
    "url": page + $lastLog,
    "success": function ( json ) { 
        for(var i in json.data){    
            if(json.data[i].logdate > $lastLog) {
                var retArr = [];
                for(var j in json.column){
                    var temp = eval('json.data[i].'+json.column[j]);
                    if(json.column[j] == 'logdate'){
                    temp = temp.substring(0, 4) + "/" + temp.substring(4, 6) + "/" + temp.substring(6,8) + " " + temp.substring(8,10) + ":" + temp.substring(10,12) + ":" + temp.substring(12,14);
                    }
                    retArr.push(temp);
                }
                $('#example').dataTable().fnAddData(retArr);
                $lastLog = json.data[i].logdate;     
            } 
        }
    },
    "dataType": "json"
} );


},3000);
