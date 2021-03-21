$(document).on('click','#delete_master_category',function(){
    var master_category_id=$(this).data('master_category_id');
    $("#mastercategory_id").val(master_category_id);
    $("#master_category_model").modal('toggle');
})

$(document).on('click','#delete_category',function(){
    var category_id=$(this).data('category_id');
    $("#category_id").val(category_id);
    $("#category_model").modal('toggle');
})

$(document).on('click','#delete_subcategory',function(){
    var subcategory_id=$(this).data('subcategory_id');
    $("#subcat_id").val(subcategory_id);
    $("#subcategory_model").modal('toggle');
})