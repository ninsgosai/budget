$(document).on('click','#delete_saving_category',function(){
    alert();
    var saving_category_id=$(this).data('saving_category_id');
    $("#saving_catid").val(saving_category_id)
    $("#saving_category_model").modal('toggle');
})