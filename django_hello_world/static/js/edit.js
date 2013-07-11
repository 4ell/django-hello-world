statout = null

function qs() {
	return document.querySelector.apply(document, arguments)
}

function show_photo() {
	var input = qs('#id_photo')
	if (input.files && input.files[0]) {
		var reader = new FileReader()

		reader.onload = function (e) {
			qs('img.photo').src = e.target.result
		}

		reader.readAsDataURL(input.files[0])
	}
}

function show_status(msg, color, timeout) {
	color = color || ''
	timeout = timeout || 15
	var code = '<div class="status '+color+'">'+msg+'</div>'

	$('#menu .status').remove()
	$('#menu').append(code)

	window.clearTimeout(statout)
	statout = window.setTimeout(function() {
		$('#menu .status').remove()
	}, timeout * 1000)
}

function show_errors(errors) {
	// body...
	console.log(errors)
}

$(document).ready(function() {
	// bind 'myForm' and provide a simple callback function 
	$('form#bio').ajaxForm({
		beforeSubmit: function() {
			show_status('Sending...')
		},
		success: function(response) {
			if(response.saved) {
				show_status('Saved', 'success')
			} else {
				show_status('Error', 'error')
				show_errors(response.errors)
			}
		},
		timeout: 1500
	})
})