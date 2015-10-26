function validateTextField( form, fieldName, userFriendlyFieldName ){
    var fieldValue = form[fieldName].value;
    if ( fieldValue == null || fieldValue == ""){
        alert( userFriendlyFieldName + " is a mandatory field");
        return false;
    }
    return true;
}

function validateForm(){
    var form = document.forms["event_guest_data"];
    if( !validateTextField(form, "event_guest_first_name", "First name") ){
        return false;
    }
    if( !validateTextField(form, "event_guest_lastname", "Last name") ){
        return false;
    }
    var guestEmail = form["event_guest_email"].value;
    if ( guestEmail == null || guestEmail =="" ){
        alert("Email is a mandatory field");
        return false;
    }
    if( guestEmail.indexOf("@") <= 0 ){
        alert("Invalid email");
        return false;
    }
    if( !validateTextField(form, "event_guest_company", "Company") ){
        return false;
    }
    return true;
}