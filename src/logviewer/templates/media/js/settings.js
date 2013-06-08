$(document).ready(function(){
    $("#server_settings_l").click(function(event){
        $('#server_info').remove()
        $('#settings_ul li').map(function(i,n) {
            $(n).attr('class', '');
        });
        $('#settings_div').children('div').map(function(i,n) {
            $(n).attr('style', 'visibility:hidden');
            $('#main_div').append($(n));
        });
        $("#server_settings_l").attr('class', 'active');
        $('#settings_div').append($('#server_settings'));
        $('#server_settings').attr('style', 'visibility:show');
    });
    $("#log_settings_l").click(function(event){
        $('#log_types').empty()
        $.get("get_log_types").done(function(data) {
            for(var i in data['log_types'])
            {
                $('#log_types').append(
                                   '<li><a href="#" onclick="choose_log(\''+data['log_types'][i]+'\');">'+data['log_types'][i]+'</a></li>'
                                  );
            }
        });
        $('#server_info').remove()
        $('#settings_ul li').map(function(i,n) {
            $(n).attr('class', '');
        });
        $('#settings_div').children('div').map(function(i,n) {
            $(n).attr('style', 'visibility:hidden');
            $('#main_div').append($(n));
        });
        $("#log_settings_l").attr('class', 'active');
        $('#settings_div').append($('#log_settings'));
        $('#log_settings').attr('style', 'visibility:show');
    });
});

function save_server(ip){
    $.get("save_server", { 'ip': $('#server_ip').val() }).done(function(data) {
        $('#server_info').remove()
        if(data['success'])
        {
            $('#settings_div').append(
                                      '<div id="server_info" class="alert alert-success">'+data['success']+'</div>'
                                     );
        }
        else
        {
            $('#settings_div').append(
                                      '<div id="server_info" class="alert alert-error"><strong>Error!</strong>'+data['error']+'</div>'
                                     );
        }
    });
}

function choose_log(log_type){
    $('#log_dropdown').text(log_type);
    $.get("get_log_settings/", { 'log_type': log_type }).done(function(data) {
        $('#settings_index').val(data['default'])
        $('#settings_delimiter').val(data['delimiter'])
        $('#settings_shown').val(data['shown_columns'])
        $('#settings_filter').val(data['filter_columns'])
    });
}

function save_log_settings(){
    $.get("save_log_settings", { 'log_type': $('#log_dropdown').text(),
                                 'default': $('#settings_index').val(),
                                 'delimiter': $('#settings_delimiter').val(),
                                 'shown_columns': $('#settings_shown').val(),
                                 'filter_columns': $('#settings_filter').val() }).done(function(data) {
        $('#log_info').remove()
        if(data['success'])
        {
            $('#settings_div').append(
                                      '<div id="log_info" class="alert alert-success">'+data['success']+'</div>'
                                     );
        }
        else
        {
            $('#settings_div').append(
                                      '<div id="log_info" class="alert alert-error"><strong>Error!</strong>'+data['error']+'</div>'
                                     );
        }
    });

}
