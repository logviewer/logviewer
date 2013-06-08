function showfilterform(){
    var selectbox = document.getElementById("current_filters");
    var selected = selectbox.options[selectbox.selectedIndex].value;

    var filterform = document.getElementById("filterform");
    filterform.innerHTML = document.getElementById(selected).innerHTML;
}

function deletefilter(){
    var selectbox = document.getElementById("current_filters");
    var selected = selectbox.options[selectbox.selectedIndex].value;
    var agree=confirm("Are you sure you want to delete "+selected+"?");
    if (agree){
        //delete selected filter from selectbox
        $("#current_filters option[value='"+selected+"']").remove();
        $.get(
          "/managefilters/deletefilter",
            {filter_name : selected},
            function(data) {
                
                alert(data);
            }
        );      
    }
}

function editfilterget(input_id, val){
    var selectbox = document.getElementById("current_filters");
    var selected = selectbox.options[selectbox.selectedIndex].value;
    
    var inputs = document.getElementById(selected).getElementsByTagName("input");
    for (var i = 0; i < inputs.length; i++) {
        if(inputs[i].getAttribute('name') == input_id){
            inputs[i].value = val;      
            $.get(
            "/managefilters/editfilter",
                {filter_name : selected,
                column_name : inputs[i].getAttribute('name'),   
                //regex : inputs[i].getAttribute('value'),   
                regex : val,   
                },
                function(data) {
                    alert(data);
                }
            ); 
        }
    }
        
}

