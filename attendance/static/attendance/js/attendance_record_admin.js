(function($) {
    $(document).ready(function() {
        var $isAbsentField = $('#id_is_absent');
        var $checkInField = $('#id_check_in_time').closest('.form-row');
        var $checkOutField = $('#id_check_out_time').closest('.form-row');

        function toggleTimeFields() {
            if ($('input[name="isAbsentField"]:checked').val() === 'absent') {
                $checkInField.hide();
                $checkOutField.hide();
            } else {
                $checkInField.show();
                $checkOutField.show();
            }
        }

        $isAbsentField.change(toggleTimeFields);
        toggleTimeFields();  // Initial state
    });
})(django.jQuery);
