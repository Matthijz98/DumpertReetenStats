$( document ).ready(function() {
    let hiero =  $('#hiero');



    // get the json data
    $.getJSON('../api/json/top10', function(data) {
        $.each(data, function (key, entry) {
            hiero.append($('<div class="col-md-4"><div class="card">'+
                '<div class="card-header">'+ entry.name +'</div>'+
                '<div class="card-body zeropadding">'+
                '<table class="table table-striped">'+
                 $.map(entry.data, function(entry, key) {
                     return '<tr><td>' + entry.key + '</td><td>' + entry.value + '</td></tr>'
                 }).join('')+
                '</table></div>'+
            '</div>'+
        '</div>'+
        '</div>'))
        })
    });
});