$( document ).ready(function() {
    let showsdeck = $('#shows-deck');

    // set the card body to the loading state
    // table_inner.append('<h1>Loading</h1>');

    // get the json data
    $.getJSON('../api/json/shows', function (data) {
        $.each(data, function (key, entry) {
            showsdeck.append($('<div class="col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12 zeropadding">\n' +
                '                <div class="card show_card">\n' +
                '                    <div class="card-header zeropadding">\n' +
                '                        <img alt="'+entry.title+'" src="https://img.youtube.com/vi/'+entry.youtube_id+'/sddefault.jpg" class="header-img">\n' +
                '                    </div>\n' +
                '                    <div class="card-body">\n' +
                '                        <div class="row">\n' +
                '                            <div class="col-md-4 col-sm-4 col-xs-4">\n' +
                '                                <div class="show_stat">\n' +
                '                                    <i class="material-icons md-48">people</i>\n' +
                '                                    <p>'+entry.gasten_count+'</p>\n' +
                '                                </div>\n' +
                '                            </div>\n' +
                '                            <div class="col-md-4 col-sm-4 col-xs-4">\n' +
                '                                <div class="show_stat">\n' +
                '                                    <img src="./static/reetenstats/img/reet/reet-64.png" alt="reet">\n' +
                '                                    <p>'+parseFloat(entry.rating_sum).toString()+'</p>\n' +
                '                                </div>\n' +
                '                            </div>\n' +
                '                            <div class="col-md-4 col-sm-4 col-xs-4">\n' +
                '                                <div class="show_stat">\n' +
                '                                    <i class="material-icons md-48">movie</i>\n' +
                '                                    <p>'+entry.video_count+'</p>\n' +
                '                                </div>\n' +
                '                            </div>\n' +
                '                        </div>\n' +
                '                    </div>\n' +
                '                    <div class="card-footer">\n' +
                '                        '+entry.date+'' +
                '                        <a href="/show/dumperteeten-'+entry.id+'" title="'+entry.title+'">See more</a>\n' +
                '                    </div>\n' +
                '                </div>\n' +
                '            </div>'))
        });
    });
});
