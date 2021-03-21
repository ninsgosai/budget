//##############################################for income##############################################################
$("#income").keypress(function (e) {
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
               return false;
      }
});
$(document).on('click','#edit_income',function(){
   var edit_income_id=$(this).data('edit_income_id');
   $.ajax({
            url: '/monthlyexpenses/editincome',
            method: 'POST',
            data: {
                'edit_income_id' : edit_income_id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
                $("#dynamic_income_form_body").empty();
                $("#dynamic_income_form_body").append(result);
                $("#income_edit_model").modal('toggle');
            }
        });
});

$(document).on('click','#update_income',function(){
    var name=$("#edit_name").val();
    var income=$("#edit_income_field").val();
    var hidden_income_id=$("#hidden_income_id").val();
    var hidden_month_name=$("#hidden_month_name").val();
    var income_category = $("#income_category_in").val();
    $.ajax({
            url: '/monthlyexpenses/updateincome',
            method: 'POST',
            data: {
                'name' : name,
                'income' : income,
                'hidden_income_id' : hidden_income_id,
                'hidden_month_name' : hidden_month_name,
                'income_category_in' : income_category,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
                $("#income_edit_model").modal('toggle');
                Swal.fire(
                  'income data updated',
                  '',
                  'success'
                ).then((value) => {
                    location.reload();
                });
            }
        });
})




//###################################################################for tax#############################################
$("#tax_per").keypress(function (e) {
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
               return false;
      }
});
$(document).on('click','#edit_tax',function(){
 var tax_id=$(this).data('tax_id');
  $.ajax({
            url: '/monthlyexpenses/edittax',
            method: 'POST',
            data: {
                'tax_id' : tax_id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
                $("#dynamic_tax_form_body").empty();
                $("#dynamic_tax_form_body").append(result);
                $("#tax_edit_model").modal('toggle');
            }
        });
})
$(document).on('click','#update_tax',function(){
  var edit_tax_id=$("#edit_tax_id").val();
  var edit_month_name=$("#edit_month_name").val();
  var edit_tax_category=$("#edit_tax_category").val();
  var edit_member_name=$("#edit_member_name").val();
  var edit_tax_per=$("#edit_tax_per").val();
  var edit_tax_amt=$("#edit_tax_amt").val();
  $.ajax({
            url: '/monthlyexpenses/updatetax',
            method: 'POST',
            data: {
                'edit_tax_id' : edit_tax_id,
                'edit_month_name' : edit_month_name,
                'edit_tax_category' : edit_tax_category,
                'edit_member_name' : edit_member_name,
                'edit_tax_per' : edit_tax_per,
                'edit_tax_amt' : edit_tax_amt,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
                $("#tax_edit_model").modal('toggle');
                Swal.fire(
                  'tax data updated',
                  '',
                  'success'
                ).then((value) => {
                    location.reload();
                });
            }
        });
})



//################################################for savings###########################################################
$("#saving_per").keypress(function (e) {
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
               return false;
      }
});
$(document).on('click','#edit_saving',function(){
  var saving_id=$(this).data('saving_id');
  $.ajax({
            url: '/monthlyexpenses/editsavings',
            method: 'POST',
            data: {
                'saving_id' : saving_id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
                $("#dynamic_savings_form_body").empty();
                $("#dynamic_savings_form_body").append(result);
                $("#savings_edit_model").modal('toggle');
            }
        });
})

$(document).on('click','#update_savings',function(){
    var edit_savings_id=$("#edit_savings_id").val();
    var edit_month_name=$("#edit_month_name").val();
    var edit_saving_category=$("#edit_saving_category").val();
    var edit_family_member_name=$("#edit_family_member_name").val();
    var edit_savings_per=$("#edit_savings_per").val();
    var edit_savings_amt=$("#edit_savings_amt").val();
    $.ajax({
              url: '/monthlyexpenses/updatesavings',
              method: 'POST',
              data: {
                  'edit_savings_id' : edit_savings_id,
                  'edit_month_name' : edit_month_name,
                  'edit_saving_category' : edit_saving_category,
                  'edit_family_member_name' : edit_family_member_name,
                  'edit_savings_per' : edit_savings_per,
                  'edit_savings_amt' : edit_savings_amt,
                   csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
              },
              success:function(result)
              {
                  $("#savings_edit_model").modal('toggle');
                  Swal.fire(
                    'savings data updated',
                    '',
                    'success'
                  ).then((value) => {
                      location.reload();
                  });
              }
          });
  })

//###################################################expenses code start#######################################
$("#total_expenses").keypress(function (e) {
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
               return false;
      }
});
function MastercategoryFunction(){
  var master_category_id=$("#master_category_id").val();
  $.ajax({
            url: '/monthlyexpenses/getcategory',
            method: 'POST',
            data: {
                'master_category_id' : master_category_id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
               $("#category_span").empty();
               $("#category_span").append(result);
            }
        });
}
function CategoryFunction(){
    var category_id=$("#category_id").val();
    $.ajax({
            url: '/monthlyexpenses/getsubcategory',
            method: 'POST',
            data: {
                'category_id' : category_id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
               $("#subcategory_span").empty();
               $("#subcategory_span").append(result);
            }
        });
}
$(document).on('click','#edit_expense',function(){
    var expense_id=$(this).data('expense_id');
    $.ajax({
            url: '/monthlyexpenses/editexpense',
            method: 'POST',
            data: {
                'expense_id' : expense_id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
                $("#dynamic_expense_body").empty();
                $("#dynamic_expense_body").append(result);
                $("#expense_model").modal('toggle');
            }
        });
})
$(document).on('click','#edit_expense',function(){

    var edit_expenses_id=$("#edit_expenses_id").val();
    var edit_month_name=$("#edit_month_name").val();
    var edit_master_category_id=$("#edit_master_category_id").val();
    var edit_category=$("#edit_category").val();
    var edit_subcategory=$("#edit_subcategory").val();
    var edit_total_expenses=$("#edit_total_expenses").val();
    $.ajax({
            url: '/monthlyexpenses/updateexpensedata',
            method: 'POST',
            data: {
                'edit_expenses_id' : edit_expenses_id,
                'edit_month_name' : edit_month_name,
                'edit_master_category_id' : edit_master_category_id,
                'edit_category' : edit_category,
                'edit_subcategory' : edit_subcategory,
                'edit_total_expenses' : edit_total_expenses,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
                $("#expense_model").modal('toggle');
                Swal.fire(
                  'expense data updated',
                  '',
                  'success'
                ).then((value) => {
                    location.reload();
                });
            }
        });
})


//////////////for second module/////////////////////////////////////////////////
$(".income").keypress(function (e) {
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
               return false;
      }
});
function UpdateincomeFunction(id){
  var income=$("#income"+id+"").val();
  $.ajax({
        url: '/monthlyexpenses/updateincome_income',
        method: 'POST',
        data: {
            'income' : income,
            'id' : id,
             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(result)
        {
        }
    });
}

//tax
function ChangetaxFunction(id){
    var tax_category=$("#tax_category"+id+"").val();
     $.ajax({
            url: '/monthlyexpenses/updatetaxcat',
            method: 'POST',
            data: {
                'tax_category' : tax_category,
                'id' : id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
            }
        });
}
function TaxperFunction(id){
  var tax_per=$("#tax_per"+id+"").val();
   $.ajax({
            url: '/monthlyexpenses/tax_update',
            method: 'POST',
            data: {
                'tax_per' : tax_per,
                'id' : id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
            }
        });
}

//savings
function ChangesavingsFunction(id){
  var saving_category_id=$("#saving_category_id"+id+"").val();
   $.ajax({
            url: '/monthlyexpenses/saving_catupdate',
            method: 'POST',
            data: {
                'saving_category_id' : saving_category_id,
                'id' : id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
            }
        });
}

function UpdatesavingperFunction(id){
  var saving_per=$("#saving_per"+id+"").val();
  $.ajax({
            url: '/monthlyexpenses/saving_per_udpate',
            method: 'POST',
            data: {
                'saving_per' : saving_per,
                'id' : id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
            }
        });
}




//=================================Third Module=========================================================================
function saveFunction(){
 location.reload();
}
//income
function SaveIncomeFunction(){
    var name=$("#new_name").val();
    $.ajax({
            url: '/monthlyexpenses/savename',
            method: 'POST',
            data: {
                'name' : name,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
                location.reload();
            }
        });
}
function InsertincomeFunction(count){
   var income_id=$("#income_id"+count+"").val();
   var income=$("#income"+count+"").val();
   $.ajax({
        url: '/monthlyexpenses/insertincome',
        method: 'POST',
        data: {
            'income_id' : income_id,
            'income' : income,
             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(result)
        {

        }
    });
}
function UpdateNameFunction(is_row){
    var name=$("#name"+is_row+"").val();
    $.ajax({
            url: '/monthlyexpenses/updatename',
            method: 'POST',
            data: {
                'is_row' : is_row,
                'name' : name,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {

            }
        });
}
function NewincomeFunction(count){
    $("#income"+count+"").val('');
    $("#income_errors").show();
    setTimeout(function(){
      $("#income_errors").hide();
     }, 4000);
}




//tax
function SaveTaxNameFunction(){
   var family_member_name_tax=$("#family_member_name_tax").val();
   $.ajax({
        url: '/monthlyexpenses/inserttaxname',
        method: 'POST',
        data: {
            'family_member_name_tax' : family_member_name_tax,
             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(result)
        {
            location.reload();
        }
    });
}
function SavetaxcatFunction(count){
 var tax_category_id=$("#tax_category_id"+count+"").val();
 var tax_id=$("#tax_id"+count+"").val();
 $.ajax({
        url: '/monthlyexpenses/updatetaxcategory',
        method: 'POST',
        data: {
            'tax_category_id' : tax_category_id,
            'tax_id' : tax_id,
             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(result)
        {

        }
    });
}
function EditTaxFunction(count){
    var tax_per=$("#tax_per"+count+"").val();
    var tax_id=$("#tax_id"+count+"").val();
    $.ajax({
            url: '/monthlyexpenses/edittaxper',
            method: 'POST',
            data: {
                'tax_per' : tax_per,
                'tax_id' : tax_id,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {

            }
        });
}
function UpdatetaxNameFunction(tax_row){
  var member_name=$("#member_name"+tax_row+"").val();
  $.ajax({
            url: '/monthlyexpenses/updatemembername',
            method: 'POST',
            data: {
                'member_name' : member_name,
                'tax_row' : tax_row,
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result)
            {
                 location.reload();
            }
        });
}



//savings
function InsertSavingsnameFunction(){
 var family_member_name=$("#family_member_name").val();
 $.ajax({
        url: '/monthlyexpenses/savesavingsname',
        method: 'POST',
        data: {
            'family_member_name' : family_member_name,
             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(result)
        {
           location.reload();
        }
    });
}
function SaveSavingperFunction(count){
  var saving_category_id=$("#saving_category_id"+count+"").val();
  var saving_id=$("#saving_id"+count+"").val();
  $.ajax({
        url: '/monthlyexpenses/insertsavingsper',
        method: 'POST',
        data: {
            'saving_category_id' : saving_category_id,
            'saving_id' : saving_id,
             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(result)
        {

        }
    });
}
function EditsavingperFunction(count){
  var saving_per=$("#saving_per"+count+"").val();
  var saving_id=$("#saving_id"+count+"").val();
   $.ajax({
        url: '/monthlyexpenses/updatesavingper',
        method: 'POST',
        data: {
            'saving_per' : saving_per,
            'saving_id' : saving_id,
             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(result)
        {

        }
    });
}
function UpdatesavingprFunction(saving_row){
  var family_member_names=$("#family_member_names"+saving_row+"").val();
  $.ajax({
        url: '/monthlyexpenses/updatesavingname',
        method: 'POST',
        data: {
            'family_member_names' : family_member_names,
            'saving_row' : saving_row,
             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(result)
        {
            location.reload();
        }
    });
}
























