statout = null

$(document).ready(function() {
	// bind 'myForm' and provide a simple callback function 
	$('form#bio').ajaxForm({
		beforeSubmit: function() {
			ui.status.show('Sending...')
			$("form#bio :input").attr("disabled", true);
		},
		success: function(response) {
			if(response.saved) {
				ui.status.show('Saved', 'success')
				ui.errors.hide()
			} else {
				ui.status.show('Error', 'error')
				ui.errors.show(response.errors)
			}
		},
		uploadProgress: function (event, position, total, percentComplete) {
			var percentVal = percentComplete + '%';
			ui.status.show('Uploading '+percentVal+'...')
		},
		complete: function (xhr) {
			if(xhr.status != 200) {
				ui.status.show('Unknown error', 'error')
			}
			$("form#bio :input").attr("disabled", false);
		}
	})
})
