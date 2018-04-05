///////////////////////////
// CSRF PROTECTION SETUP //
///////////////////////////
let csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protectionco
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            console.log('Before send working as well!')
        }
    }
});

/////////////////////////////////
// MAKE INITIAL DATA AVAILABLE //
/////////////////////////////////
$("#chartContainer").load("ajax/charts/initial/", {'inditr_pk':6});

////////////////////////////
// DROPDOWNS SEARCH SETUP //
////////////////////////////
$("select").on("change", function (event) {
    let dropDownID = event.target.id;
    if (dropDownID === 'FormSelectCategory') {
        fsCategory(event, dropDownID)
    } else if (dropDownID === 'FormSelectCountry') {
        fsCountry(event, dropDownID)
    } else if (dropDownID === 'FormSelectSeries') {
        fsSeries(event, dropDownID)
    }
});

function fsCategory(e, dropdown_id) {
    let value_id = e.target.value;
    let results = getSearchEntries(dropdown_id, value_id);
    let formId = $('#FormSelectCountry');
    formId.find('option').remove();
    formId.append('<option value="" selected disabled hidden>Country</option>');
    results.then(function (data) {
        $.each(data, function (i, item) {
            formId.append($('<option>', {
                value: item.pk,
                text: item.fields.name
            }));
        });
    });
    formId.removeAttr('disabled');

    let attr = $('#FormSelectSeries');
    let check = attr.attr('disabled');
    // For some browsers, `attr` is undefined; for others,
    // `attr` is false.  Check for both.
    if (typeof check !== typeof undefined && check !== false) {
        // do noting!!!
    } else {
        attr.attr('disabled', '');
    }
}

function fsCountry(e, dropdown_id) {
    let value_id = e.target.value;
    let category = $('#FormSelectCategory').val();
    let results = getSearchEntriesIndicators(dropdown_id, value_id, category);
    let formId = $('#FormSelectSeries');
    formId.find('option').remove();
    formId.append('<option value="" selected disabled hidden>Series</option>');
    results.then(function (data) {
        $.each(data, function (i, item) {
            formId.append($('<option>', {
                value: item.pk,
                text: item.fields.name
            }));
        });
    });
    formId.removeAttr('disabled')
}

function fsSeries(e) {
    console.log(e.target.id)
}

async function getSearchEntries(dropdown_id, value_id) {
    let result;
    try {
        result = await $.ajax({
            url: '/ajax/search/',
            type: "GET",
            data: {
                dropdown_id: dropdown_id,
                value_id: value_id
            }
        });
        return result
    } catch (error) {
        console.error(error);
    }
}

async function getSearchEntriesIndicators(dropdown_id, value_id, category) {
    let result;
    try {
        result = await $.ajax({
            url: '/ajax/search/',
            type: "GET",
            data: {
                dropdown_id: dropdown_id,
                value_id: value_id,
                category: category
            }
        });
        return result
    } catch (error) {
        console.error(error);
    }
}


///////////////////////////
// SUBMIT REFRESH BUTTON //
///////////////////////////
function submitRefreshButton(e) {
    let catry_text = $("#FormSelectCategory").find("option:selected").text();
    let catry_id = $("#FormSelectCategory").find("option:selected").val();

    let country_text = $("#FormSelectCountry").find("option:selected").text();
    let country_id = $("#FormSelectCountry").find("option:selected").val();

    let indtr_text = $("#FormSelectSeries").find("option:selected").text();
    let indtr_id = $("#FormSelectSeries").find("option:selected").val();

    e.preventDefault();
    let warning = $('#selectWarningModal');
    if (catry_text !== 'Data Category' && country_text !== 'Country' && indtr_text !== 'Series') {
        e.stopPropagation();    // Prevent the modal from popping up
        $("#chartContainer").empty();
        $("#chartContainer").load("ajax/charts/initial/", {'inditr_pk': indtr_id});
    } else {
        console.log('working');
        warning.addClass('show');
        warning.css({'display': 'block', 'padding-right': '15px'});
    }
    warning.removeClass('show');
    warning.css({'display': 'none', 'padding-right': ''});
}

//////////////////////////////////////
// SUBMIT CONTACT FORM - SEND EMAIL //
//////////////////////////////////////
$('.myContactForm').on('submit', function (event) {
    event.preventDefault();
    $.ajax({
        url: ".", // the endpoint
        type: "POST", // http method
        data: {email: $('#id_email').val(), subject: $('#id_subject').val(), message: $('#id_message').val()}, // data sent with the post request

        // handle a successful response
        success: function (json) {
            //$('#post-text').val(''); // remove the value from the input
            console.log(json['form']); // log the returned json to the console
            $('#id_email').blur()
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});
