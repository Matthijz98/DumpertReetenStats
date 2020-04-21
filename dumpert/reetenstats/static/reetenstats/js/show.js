$( document ).ready(function() {
    let table_inner =  $('#reeting-card-body');
    let ratings_table = $('#ratings-table');
    let show_id = document.getElementById('show_id').textContent;

    console.log('Lets go');

    // set the card body to the loading state
    // table_inner.append('<h1>Loading</h1>');

    // get the json data
    $.getJSON('../api/json/ratingsinshow?show=' + show_id, function(data) {
        $.each(data, function (key, entry) {
            ratings_table.append($('<tr> <td>'+ entry.title +'</td><td>Omschrijving: ' + entry.description +'</td><td>' +
                $.map(entry.ratings, function(entry, key) {
                    return '' + entry.by + ' ' + entry.rating_amount + '<br><br>'
                }).join('') +'</td></tr>'));
        })
    });
});