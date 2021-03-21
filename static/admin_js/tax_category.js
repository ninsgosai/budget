$(document).on('click','#delete_tax_category',function(){
    var tax_cat_id=$(this).data('tax_cat_id');
    $("#tax_category_id").val(tax_cat_id)
    $("#tax_category_model").modal('toggle');
})