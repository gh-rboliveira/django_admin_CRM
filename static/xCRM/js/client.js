$(document).ready(function(){

    company_name_field = $('#id_company_name');
    name_field = $('#id_name');

    company_name_row = $(".field-company_name");
    name_row = $(".field-name");
    
    // Hide field based in client type
    if ($("#id_client_type").val() == "I") {
        company_name_row.hide();
        toggle_field_mandatoriness(name_field);
    }
    else {
        name_row.hide();
        toggle_field_mandatoriness(company_name_field);
    }

    // Since the fields are not mandatory in the database
    // let's make the name mandatory
    
    



    $("#id_client_type").change(function(){
        if (this.value == "I") {
            name_row.show();
            company_name_row.hide();
        }
        else {
            name_row.hide();
            company_name_row.show();
        }
        toggle_field_mandatoriness(name_field);
        toggle_field_mandatoriness(company_name_field);
    });
    
});

function toggle_field_mandatoriness(field) {
    if (field.prop('required')) {
        field.prop('required', false);
        field.parent().find('label').removeClass('required');
    } else {
        field.prop('required', true);
        field.parent().find('label').addClass('required');
    }
}

//company_name_field = document.querySelector('.field-company_name');
//company_name_field.style.display = "none";

//name_field = document.querySelector('.field-name');
//name_field.style.display = "none";