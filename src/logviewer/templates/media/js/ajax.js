var timerID = 0;
$(document).ready(function () {
     //$('#example').cdirectTable();
    //if(typeof $('#example') == undefined){
    /*$('#example').dataTable({
    'bProcessing': true,
    'bFilter': true,
    'sPaginationType': "full_numbers",
    'sAjaxSource': '/dsearch/network/0',
    //'sAjaxSource': http://www.datatables.net/examples/examples_support/server_processing.php,
    'bServerSide': true,
    'bDestroy': true,
    'bRetrieve':true
    //'bJQueryUI': true    
    });
    //dataTable.fnClearTable(this);
    //logtable.fnDraw()
    //}*/
    $('#example').cdirectTable();
    //$("<button id=\"startStop\" Class=\"btn btn-primary\" name=\"start\" value=\"start\" style=\"alignment:center;\" onclick=\"startStopLogs()\">Start</button>").appendTo('#example_length');
    $("<input type=\"submit\" id=\"startStop\" Class=\"btn-danger\" value=\"Stop\" onclick=\"startStopLogs()\">").appendTo('#example_length');    
    
    timerID = setInterval( function(){
        $('#example').dataTable().fnClearTable();
    },3000);
    /*$(document).bind("contextmenu", function(event) {
        $("<div class='custom-menu'>Custom menu</div>")
        .appendTo("body")
        .css({top: event.pageY + "px", left: event.pageX + "px"
        });
    });
*/   
    var rightClickDiv = "<div id=\"menu2\" style=\"display:none;width:200px;background-color:white;border:1px solid black;padding:5px;\"> \"This is my custom context menu\"</div>";
    var menu1 = [ 
        {'Search':{ 
            onclick:function(menuItem,menu) { alert("You clicked me!"); }, 
            className:'menu3-custom-item',
            //padding:'3px',
            //font-size:'16px !important', 
            title:'This is the hover title' } }
    ]; 
    $(function(){ 
        $('#example').contextMenu(menu1,{theme:'vista'});
    });

});


//fnDraw();
/*

$lastLog = '20000101010101';
$columns = '';
var page = '';


$(document).ready(function(){
    page = document.location.pathname.replace('search', 'dsearch');
    if(page == ''){
        page = '/dsearch/network/';
    } 
/*
$.ajax( {
    "url": page + $lastLog,
    //'sAjaxSource': '/dsearch/network/0'
    "success": function ( json ){    
        for(var i in json.aaData){    
            var retArr = [];
            
            for(var j in json.column)
            {
                var temp = eval('json.aaData[i].'+json.column[j]);
                if(json.column[j] == 'logdate'){
                    temp = temp.substring(0, 4) + "/" + temp.substring(4, 6) + "/" + temp.substring(6,8) + " " + temp.substring(8,10) + ":" + temp.substring(10,12) + ":" + temp.substring(12,14);
                }
                retArr.push(temp);
            }

            $('#example').dataTable().fnAddData( 
            retArr);
            if(json.aaData[i].logdate > $lastLog) {
                $lastLog = json.aaData[i].logdate;     
            } 
        }
    },
    "dataType": "json"
} );
});*/
/*
$lastLog = '20000101010101';
$columns = '';
var page = '';

page = document.location.pathname.replace('search', 'dsearch');
if(page == ''){
    page = '/dsearch/network/';
}
*/


/*
//setInterval( function(){  
/*$.ajax( {
    "url": page + $lastLog,
    "success": function ( json ) { 
        for(var i in json.aaData){    
            if(json.aaData[i].logdate > $lastLog) {
                var retArr = [];
                for(var j in json.column){
                    var temp = eval('json.aaData[i].'+json.column[j]);
                    if(json.column[j] == 'logdate'){
                    temp = temp.substring(0, 4) + "/" + temp.substring(4, 6) + "/" + temp.substring(6,8) + " " + temp.substring(8,10) + ":" + temp.substring(10,12) + ":" + temp.substring(12,14);
                    }
                    retArr.push(temp);
                }
                $('#example').dataTable().fnAddData(retArr);
                $lastLog = json.aaData[i].logdate;     
            } 
        }
    },
    "dataType": "json"
} );*/


  


    //$('#example').dataTable().bProcessing = 'false';
    //var retArr = ['', '', '', '' , '', '', ''];
    //$('#example').dataTable().fnAddData();
  //  $('#example').dataTable().fnClearTable();
//},3000);






function startStopLogs(){
    //var startStop = document.getElementById('startStop');
    if(timerID == 0){
        timerID = setInterval( function(){
            $('#example').dataTable().fnClearTable();
        },3000);
        $(function(){
            $("#startStop").val('Stop');
            $("#startStop").attr("Class","btn-danger");
        });
    }
    else{
        clearInterval(timerID);
        timerID = 0;
        $(function(){
            $("#startStop").val('Start');
            $("#startStop").attr("Class", "btn-success");
        });    
        //this.value = 'Start';
    }
    
}


