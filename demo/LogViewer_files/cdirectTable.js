(function ($) {
	var datatable = {
		"sPaginationType": "bootstrap",
		"sDom": "<'row-fluid'<'well cddt-bottom-0'lp>>t<'row-fluid'i>"
	};

	var dt;
	var methods = {
		initStyles : function( selector ) {
			$(selector).attr('border', '').attr('class', 'table table-bordered table-striped dataTable');
		},
		buildCustomTableHeaders : function( selector ) {
			var filterBuilder = '<tr class="cddt-filter">';
			
			$(selector + ' thead tr th').each(function() {
				filterBuilder += '<td><input type="text" style="width:90%;" /></td>';
			});
			
			filterBuilder += '</tr>';
			
			$(selector).children('th').attr('class', 'cddt-sort2');			
			$(selector).children('thead').append(filterBuilder);
		},
		updateSortUI : function() {
			$(".cddt-sort2 th").each(function(){
				var pos = $(".cddt-sort2 th").index(this);
				var targetElement = $(".cddt-sort td:nth-child(" + (pos + 1) + ")");
				
				var classes = targetElement.attr('class');
				$(this).attr('class', classes);
			});
		},
		initDatatable : function( selector ) {
			dt = $(selector).dataTable( datatable );
		},
		initEvents : function() {
			$(".cddt-sort2 th").click(function(){
				var pos = $(".cddt-sort2 th").index(this);
				$(".cddt-sort td:nth-child(" + (pos + 1) + ")").click();
				
				this.updateSortUI();
			});
			
			$(".cddt-filter input").keyup(function(){
				var pos = $(".cddt-filter td").index($(this).parent());
				dt.fnFilter($(this).val(), pos);
			});
		},
		init : function( selector ) {
			this.initStyles(selector);
			this.initDatatable(selector);
			this.buildCustomTableHeaders(selector);
			this.updateSortUI();
			this.initEvents();
		}
	};
	
	$.fn.cdirectTable = function( options ) {
		if(options && options.datatable)
			$.extend( datatable, options.datatable );
			
		var selector = this.attr('id');
		selector = selector ? '#' + selector : ( this.attr('class') ? '.' + this.attr('class') : false );
		selector = selector ? selector : 'table';
		methods.init(selector);		
		
	};


})(jQuery);
