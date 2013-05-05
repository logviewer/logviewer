$('#logStreams').change(function() {
    try{
        var selected = this.value;
    }
    catch(err){
        selected = "datefilter";
    }
    document.write("deneme");
    var selectedStream = document.getElementById(selected+ 'columns');
    var columnNames = selectedStream.InnerHTML.split(",");
    document.getElementById('filterform').innerHTML = "aaaaaa";
    /*if (selected == "datefilter"){
        var table = document.getElementById('dateform').innerHTML;
        document.getElementById('filterform').innerHTML = table;
        $(function() {
            $( "#startdatepicker" ).datepicker();
        });
        $(function() {
            $( "#enddatepicker" ).datepicker();
        });
    }
    else if (selected == "ipfilter"){
        var table = document.getElementById('ipform').innerHTML;
        document.getElementById('filterform').innerHTML = table;
    }
    else if (selected == "regexfilter"){
        var table = document.getElementById('regexform').innerHTML;
        document.getElementById('filterform').innerHTML = table;
    }
    else if (selected == "servicefilter"){
        var table = document.getElementById('serviceform').innerHTML;
        document.getElementById('filterform').innerHTML = table;
    }
    else if (selected == "actionfilter"){
        var table = document.getElementById('actionform').innerHTML;
        document.getElementById('filterform').innerHTML = table;
    }
    else if (selected == "urlfilter"){
        var table = document.getElementById('urlform').innerHTML;
        document.getElementById('filterform').innerHTML = table;
    }
    else if (selected == "wordfilter"){
        var table = document.getElementById('wordform').innerHTML;
        document.getElementById('filterform').innerHTML = table;
    }
    else{
        alert("Error!")
    }*/
});

