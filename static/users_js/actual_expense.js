// function PaymentCategoryFunction(){
//     var payment_category=$("#payment_category").val();
//     if (payment_category=='expense'){
//         $("#dynamic_expense_span").show();
//         $("#dynamic_income_span").hide();
//     }else{
//         $("#dynamic_expense_span").hide();
//         $("#dynamic_income_span").show();
//     }
// }
function PaymentTypeFunction(){
    var payment_type=$("#payment_type").val();
    if (payment_type=="bank"){
        $("#credit_span").hide();
        $("#bank_span").show();
    }
    if (payment_type=="credit"){
        $("#bank_span").hide();
        $("#credit_span").show();
    }
     if (payment_type=="cash"){
        $("#bank_span").hide();
        $("#credit_span").hide();
    }
}
function MasterCategoryFunction(){
    var actual_master_category=$("#actual_master_category").val();
    $.ajax({
            url: '/actualexpenses/getcategory',
            method: 'POST',
            data: {
                'actual_master_category' : actual_master_category,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
               $("#category_span").empty();
               $("#category_span").append(result);
            }
        });
}
function GetsubcategoryFunction(){
    var actual_category=$("#actual_category").val();
    $.ajax({
            url: '/actualexpenses/getsubcategory',
            method: 'POST',
            data: {
                'actual_category' : actual_category,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
               $("#subcategory_span").empty();
               $("#subcategory_span").append(result);
            }
        });
}
$(document).on('click','#delete_expense',function(){
    var expense_id=$(this).data('expense_id');
    var month_name=$(this).data('month_name');
    $("#expenseid").val(expense_id);
    $("#month_name").val(month_name);
    $("#expense_delete_model").modal('toggle');
})











