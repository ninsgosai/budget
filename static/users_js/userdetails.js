//for inserting bank details
$(document).on('click','#insert_bank_details',function(){
    var bank_name=$("#bank_name").val();
    var account_number=$("#account_number").val();
    var od_token=$("#od_token").val();
    var current_balance=$("#current_balance").val();
    var intrest_time_period=$("#intrest_time_period").val();
    var intrest_type=$("#intrest_type").val();
    var intrest_rate=$("#intrest_rate").val();
    if (bank_name=="" || account_number=="" || od_token=="" || current_balance=="" ||intrest_rate=="" || intrest_time_period==0 || intrest_type==0){
            $("#bank_detail_error").show();
    }else{
            $("#bank_detail_error").hide();
             $.ajax({
                    url: '/userdetails/insertbankdetails',
                    method: 'POST',
                    data: {
                        'bank_name' : bank_name,
                        'account_number' : account_number,
                        'od_token' : od_token,
                        'current_balance' : current_balance,
                        'intrest_time_period' : intrest_time_period,
                        'intrest_type' : intrest_type,
                        'intrest_rate' : intrest_rate,
                         csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                    },
                    success:function(result)
                    {
                        Swal.fire(
                              'Bank Details Inserted!',
                              'fill form again if you have more than one bank account',
                              'success'
                            ).then((value) => {
                                $("#bank_name").val("");
                                $("#account_number").val("");
                                $("#od_token").val("");
                                $("#current_balance").val("");
                                $("#intrest_time_period").val("--select time period--");
                                $("#intrest_type").val("--select intrest type--");
                                $("#intrest_rate").val("");
                                $("#bank_dynamic_div").empty();
                                $("#bank_dynamic_div").append(result);
                                location.reload();
                            });
                    }
            });
    }
});
$("#account_number").keypress(function (e) {
 if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           return false;
  }
});
$("#current_balance").keypress(function (e) {
 if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           return false;
  }
});
$("#intrest_rate").keypress(function (e) {
 if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           return false;
  }
});
$(document).on('click','#delete_bank_details',function(){
 var bank_id=$(this).data('bank_id');
  $.ajax({
            url: '/userdetails/deletebankdetails',
            method: 'POST',
            data: {
                'bank_id' : bank_id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
                     location.reload();
                    $("#bank_dynamic_div").empty();
                    $("#bank_dynamic_div").append(result);
            }
        });
})
$(document).on('click','#update_bank_details',function(){
    var bank_hidden_id=$("#bank_hidden_id").val();
    var bank_name=$("#bank_name").val();
    var account_number=$("#account_number").val();
    var od_token=$("#od_token").val();
    var current_balance=$("#current_balance").val();
    var intrest_time_period=$("#intrest_time_period").val();
    var intrest_type=$("#intrest_type").val();
    var intrest_rate=$("#intrest_rate").val();
    if (bank_name=="" || account_number=="" || od_token=="" || current_balance=="" ||intrest_rate=="" || intrest_time_period==0 || intrest_type==0){
            $("#edit_bank_error").show();
    }else{
            $("#edit_bank_error").hide();
             $.ajax({
                url: '/userdetails/updatebankdetails',
                method: 'POST',
                data: {
                    'bank_hidden_id' : bank_hidden_id,
                    'bank_name' : bank_name,
                    'account_number' : account_number,
                    'od_token' : od_token,
                    'current_balance' : current_balance,
                    'intrest_time_period' : intrest_time_period,
                    'intrest_type' : intrest_type,
                    'intrest_rate' : intrest_rate,
                     csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                },
                success:function(result)
                {
                    Swal.fire({
                          position: 'top-end',
                          icon: 'success',
                          title: 'bank details updated',
                          showConfirmButton: false,
                          timer: 1500
                        })
                }
            });
    }
})


// for inserting credit card details
$(document).on('click','#insert_credit_card_details',function(){
    var credit_card_number=$("#credit_card_number").val();
    var credit_limit=$("#credit_limit").val();
    var charges_and_fees=$("#charges_and_fees").val();
    var due_date=$("#due_date").val();
    var overdue=$("#overdue").val();
    var intrest_on_payable=$("#intrest_on_payable").val();
    var payment_made=$("#payment_made").val();
    if (credit_card_number=="" || credit_limit=="" || charges_and_fees=="" ||  intrest_on_payable=="" || payment_made==""){
            $("#creditcard_error").show();
    }else{
            $("#creditcard_error").hide();
            $.ajax({
                    url: '/userdetails/insertcreditcarddetails',
                    method: 'POST',
                    data: {
                        'credit_card_number' : credit_card_number,
                        'credit_limit' : credit_limit,
                        'charges_and_fees' : charges_and_fees,
                        'due_date' : due_date,
                        'overdue' : overdue,
                        'intrest_on_payable' : intrest_on_payable,
                        'payment_made' : payment_made,
                         csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                    },
                    success:function(result)
                    {
                         Swal.fire(
                              'Credit Card Details Inserted!',
                              'fill form again if you have more than one credit card',
                              'success'
                            ).then((value) => {
                                $("#credit_card_number").val("");
                                $("#credit_limit").val("");
                                $("#charges_and_fees").val("");
                                $("#due_date").val("");
                                $("#overdue").val("");
                                $("#intrest_on_payable").val("");
                                $("#payment_made").val("");
                                $("#credit_card_dynamic_div").empty();
                                $("#credit_card_dynamic_div").append(result);
                                location.reload();
                            });
                    }
                });
    }
})
$("#credit_card_number").keypress(function (e) {
 if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           return false;
  }
});
$("#credit_limit").keypress(function (e) {
 if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           return false;
  }
});
$("#charges_and_fees").keypress(function (e) {
 if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           return false;
  }
});
$("#intrest_on_payable").keypress(function (e) {
 if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           return false;
  }
});
$("#payment_made").keypress(function (e) {
 if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           return false;
  }
});
$(document).on('click','#delete_credit_card',function(){
 var credit_card_id=$(this).data('credit_card_id');
  $.ajax({
            url: '/userdetails/deletecreditcard',
            method: 'POST',
            data: {
                'credit_card_id' : credit_card_id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
                     location.reload();
                    $("#credit_card_dynamic_div").empty();
                    $("#credit_card_dynamic_div").append(result);
            }
        });
})
$(document).on('click','#update_credit_card',function(){
      var credit_hidden_val=$("#credit_hidden_val").val();
      var credit_card_number=$("#credit_card_number").val();
      var credit_limit=$("#credit_limit").val();
      var charges_and_fees=$("#charges_and_fees").val();
      var due_date=$("#due_date").val();
      var overdue=$("#overdue").val();
      var intrest_on_payable=$("#intrest_on_payable").val();
      var payment_made=$("#payment_made").val();
      if (credit_card_number=="" || credit_limit=="" || charges_and_fees=="" ||  intrest_on_payable=="" || payment_made==""){
             $("#edit_creditcard_error").show();
      }else{
             $("#edit_creditcard_error").hide();
             $.ajax({
                    url: '/userdetails/updatecreditcard',
                    method: 'POST',
                    data: {
                        'credit_hidden_val' : credit_hidden_val,
                        'credit_card_number' : credit_card_number,
                        'credit_limit' : credit_limit,
                        'charges_and_fees' : charges_and_fees,
                        'due_date' : due_date,
                        'overdue' : overdue,
                        'intrest_on_payable' : intrest_on_payable,
                        'payment_made' : payment_made,
                         csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                    },
                    success:function(result)
                    {
                        Swal.fire({
                              position: 'top-end',
                              icon: 'success',
                              title: 'credit card details updated',
                              showConfirmButton: false,
                              timer: 1500
                            })
                    }
                });
      }
})



//for inserting other loans
$(document).on('click','#insert_other_loans',function(){
    var loan_name=$("#loan_name").val();
    var loan_amount=$("#loan_amount").val();
    var roi_percentage_type=$("#roi_percentage_type").val();
    var roi_percentage=$("#roi_percentage").val();
    var other_due_date=$("#other_due_date").val();
    var other_intrest_type=$("#other_intrest_type").val();
    var loan_duration=$("#loan_duration").val();
    if (loan_name=="" || loan_amount=="" || roi_percentage_type==0 || other_due_date=="" || other_intrest_type==0 || loan_duration==""){
            $("#other_loans_error").show();
    }else{
            $("#other_loans_error").hide();
            $.ajax({
                url: '/userdetails/insertotherloans',
                method: 'POST',
                data: {
                    'loan_name' : loan_name,
                    'loan_amount' : loan_amount,
                    'roi_percentage_type' : roi_percentage_type,
                    'roi_percentage' : roi_percentage,
                    'other_due_date' : other_due_date,
                    'other_intrest_type' : other_intrest_type,
                    'loan_duration' : loan_duration,
                     csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                },
                success:function(result)
                {
                  Swal.fire(
                          'Details Inserted!',
                          'fill form again if you have more than one loans',
                          'success'
                        ).then((value) => {
                            $("#loan_name").val("");
                            $("#loan_amount").val("");
                            $("#roi_percentage_type").val("--select time period--");
                            $("#roi_percentage").val("");
                            $("#other_due_date").val("");
                            $("#other_intrest_type").val("--intrest type--");
                            $("#loan_duration").val("");
                            $("#loans_dynamic_div").empty();
                            $("#loans_dynamic_div").append(result);
                             location.reload();
                        });
                }
            });
    }
})
$("#loan_amount").keypress(function (e) {
 if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           return false;
  }
});
$("#roi_percentage").keypress(function (e) {
 if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           return false;
  }
});
$("#loan_duration").keypress(function (e) {
 if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           return false;
  }
});
$(document).on('click','#update_otherloans',function(){
     var other_loan_hidden_id=$("#other_loan_hidden_id").val();
     var loan_name=$("#loan_name").val();
     var loan_amount=$("#loan_amount").val();
     var roi_percentage_type=$("#roi_percentage_type").val();
     var roi_percentage=$("#roi_percentage").val();
     var other_due_date=$("#other_due_date").val();
     var other_intrest_type=$("#other_intrest_type").val();
     var loan_duration=$("#loan_duration").val();
     if (loan_name=="" || loan_amount=="" || roi_percentage_type==0 || other_due_date=="" || other_intrest_type==0 || loan_duration==""){
            $("#edit_other_loans_error").show();
     }else{
            $("#edit_other_loans_error").hide();
            $.ajax({
                    url: '/userdetails/updateotherloans',
                    method: 'POST',
                    data: {
                        'other_loan_hidden_id' : other_loan_hidden_id,
                        'loan_name' : loan_name,
                        'loan_amount' : loan_amount,
                        'roi_percentage_type' : roi_percentage_type,
                        'roi_percentage' : roi_percentage,
                        'other_due_date' : other_due_date,
                        'other_intrest_type' : other_intrest_type,
                        'loan_duration' : loan_duration,
                         csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                    },
                    success:function(result)
                    {
                       Swal.fire({
                              position: 'top-end',
                              icon: 'success',
                              title: 'data updated',
                              showConfirmButton: false,
                              timer: 1500
                            })

                    }
                });
     }
})


$(document).on('click','#delete_saving_category',function(){
  alert();
  var saving_category_id=$(this).data('saving_category_id');
  $("#saving_catid").val(saving_category_id)
  $("#saving_category_model").modal('toggle');
})













