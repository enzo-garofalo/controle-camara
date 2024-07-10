document.addEventListener("DOMContentLoaded", function() {
    function inputNumber(el) {
        var min = el.attr('min') || false;
        var max = el.attr('max') || false;

        var dec = el.siblings('.input-number-decrement');
        var inc = el.siblings('.input-number-increment');

        dec.on('click', function() {
            var value = parseInt(el.val());
            value--;
            if (!min || value >= min) {
                el.val(value);
            }
        });

        inc.on('click', function() {
            var value = parseInt(el.val());
            value++;
            if (!max || value <= max) {
                el.val(value);
            }
        });
    }

    $('.input-number').each(function() {
        inputNumber($(this));
    });
});
