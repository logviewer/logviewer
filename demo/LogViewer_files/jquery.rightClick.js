var menu3 = [
  {'Show Alert':{
          onclick:function(menuItem,menu) { alert("You clicked me!"); },
              className:'menu3-custom-item',
                  hoverClassName:'menu3-custom-item-hover',
                      title:'This is the hover title'
                            }
  }
];
$(function() {
      $('.deneme0303').contextMenu(menu3,{});
});
