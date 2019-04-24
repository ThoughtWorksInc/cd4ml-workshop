$( document ).ready(function() {
    $('#date').datepicker({
      dateFormat: "yy-mm-dd"
    });

    $('button[type="submit"]').click(function() {
        var data = [];
        var valid = true;
        $( 'input[type="text"], select' ).each(function() {
            if (this.id === 'date' && !/[12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])/.test($(this).val())) {
                alert("Invalid date format");
                valid = false;
                return false;
            } else if (!$(this).val()) {
                alert("Need to provide a value for " + $(this).prev().text());
                valid = false;
                return false;
            } else {
                data.push(this.id + "=" + $(this).val());
            }
        });

        if (valid) {
            var dataStr = '?' + data.join('&');
            var prefix = (window.location.pathname == "/" ? "" : window.location.pathname)
            $.ajax(prefix + "/prediction" + dataStr, {
                    beforeSend: function() {
                      $('#prediction').text('loading...')
                      $('button[type="submit"]').attr("disabled", "true")
                    }
                })
                .done(function(result) {
                    $('#prediction').text(result);
                    $('button[type="submit"]').removeAttr("disabled")
                })
                .fail(function() {
                    alert("Request failed.")
                    $('button[type="submit"]').removeAttr("disabled")
                });
        }
    })
});
