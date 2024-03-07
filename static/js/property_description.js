$(document).ready(function() {
    $('#description').summernote({
        minHeight: 400,
        toolbar: [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['para', ['ul', 'ol']],
            ['view', ['help']]
        ]
    });
});