$( document ).ready(function() {

    $('button[type="submit"]').click(function() {
        var data = [];
        var valid = true;
        $( 'input[type="checkbox"]').each( function() {
            data.push(this.id + "=" + this.checked);
        });

        $( 'input[type="text"], input[type="number"]' ).each(function() {
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

            $.ajax("/prediction" + dataStr)
                .done(function(result) {
                    $('#prediction').text(result);
                })
                .fail(function() {
                    alert("Request failed.")
                });
        }
    })
});