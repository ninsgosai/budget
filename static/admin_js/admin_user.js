// for adding users
$(document).on('click','#delete_users',function(){
    var user_id=$(this).data('user_id');
    $("#userid").val(user_id);
    $("#user_conformation_model").modal('toggle')
});

$("#age").keypress(function (e) {
if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
    return false;
  }
});

$("#mobile").keypress(function (e) {
if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
    return false;
  }
});

$("#income").keypress(function (e) {
if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
    return false;
  }
});

$("#months").keypress(function (e) {
if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
    return false;
  }
});


// for subadmin
$(document).on('click','#delete_subadmin',function(){
    var subadmin_id=$(this).data('subadmin_id');
    $("#subadminid").val(subadmin_id);
    $("#subadmin_conformation_model").modal('toggle')
})















