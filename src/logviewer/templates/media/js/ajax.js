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
    $.get(
          "/managefilters/getfilters",
          {},
              function(data) {
                var buttons = '<center><table id="streaminputs" border="0"><tr>';
                buttons += '<td valign="top" width="200"><input type="submit" id="startStop" Class="btn-danger" style="height: 30px;" value="Stop" onclick="startStopLogs()"></td>';
                buttons += '<td valign="top">'+data+'</td>';
                buttons += '<td valign="top" width=200><input type="submit" id="applyFilter" Class="btn-success" value="Apply" style="height: 30px;" onclick="applyFilter()"></td>';
                buttons += '<td valign="top" ><input type="text" id="filterName" class="input-small" style="float:right;"></td>';
                buttons += '<td valign="top" ><input type="submit" id="SaveFilter" Class="btn-success" style="height: 30px;" value="SaveFilter" onclick="saveFilter()"></td>';
                buttons += '</tr></table></center>';
                $(buttons).appendTo('#example_length');
             }
    );


    //$("<input type=\"submit\" id=\"startStop\" Class=\"btn-danger\" value=\"Stop\" onclick=\"startStopLogs()\">").appendTo('#example_length');    
    //$("<input type=\"submit\" id=\"applyFilter\" Class=\"btn-danger\" value=\"Apply\" onclick=\"applyFilter()\">").appendTo('#example_length');    
    //$("<select><option value=\"choose\">Choose</option></select>").appendTo('#example_length');
    //$("<input type=\"submit\" id=\"SaveFilter\" Class=\"btn-danger\" style=\"float:right;\" value=\"SaveFilter\" onclick=\"saveFilter()\">").appendTo('#example_length');
    //$("<input type=\"text\" id=\"filterName\" class=\"input-small\" style=\"float:right;\">").appendTo('#example_length');

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

function applyFilter(){
    /*var filterIndexes = [1];
    var deneme  = "deneme";
    var oDataTable = $('#example').dataTable();
    $('thead .cddt-filter').each( function ( i ) {
         $('td:eq(1) input', this).val($('#filterName').val());
         var searchText = $('#filterName').val();
         oDataTable.fnFilter(searchText, 1);
    });*/
    var oDataTable = $('#example').dataTable();
    var e = document.getElementById('filterdropdown')
    $.get
    (
     "/managefilters/getfilterinfo",
     {filter_name : e.options[e.selectedIndex].value},
     function(data){
        var filterTuple = data.split(";");
        for(var i = 0; i < filterTuple.length; i++){
            var fname = filterTuple[i].split(',')[0];
            var finfo = filterTuple[i].split(',')[1];
            
            var cnumber = -1;
            $('thead tr th').each( function ( i ) {
                    if($(this).text() == fname){
                        cnumber = i;
                    }
           });            

            $('thead .cddt-filter').each( function ( i ) {
                $('td:eq('+String(cnumber)+') input', this).val(finfo);
                var searchText = finfo;
                oDataTable.fnFilter(searchText, cnumber);
            });
        }
     }
    );
}

function saveFilter(){
        var searchText = new Array();
        var searchIndex = new Array();
        var searchColumns = new Array();
        var oDataTable = $('#example').dataTable();
        $('thead .cddt-filter td').each( function ( i ) {
            var tempText = $('input', this).val();
            if(tempText != "")
            {
                searchIndex.push(i);
                searchText.push(tempText);
            }
        });

        $('thead tr th').each( function ( i ) {
            //if(jQuery.inArray(i, searchIndex)){
            for(var j = 0; j < searchIndex.length; j++){
                if(i == searchIndex[j]){
                searchColumns.push($(this).text());
                }
            }
        });

        var filterText = document.getElementById('filterName').value;
        var filterInfo = "";
        for(var i = 0; i < searchIndex.length; i++){
            filterInfo += searchColumns[i] + "," + searchText[i];
            if(i != searchIndex.length - 1){
                filterInfo += ";";
            }
        }

        if(filterText == ""){
            alert("Enter a filter name!")
        }
        else if(filterInfo == ""){
            alert("Enter a filter");
        }
        else{
           $.get(
            "/managefilters/savefilter",
            {filter_name : filterText,
             filter_info : filterInfo},
            function(data) {
                alert(data);
            }
        ); 
        }       
}

