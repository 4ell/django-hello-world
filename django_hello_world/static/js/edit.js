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
	var code = ''
	for(err in errors) {
		code += '<li>'
		var val = errors[err]
		if(typeof err === 'string')
			code += err + ': '
		if(val instanceof Array)
			code += val.join()
		else
			code += val
		code += '</li>\n'
	}
	$('#form-error ul').html(code)
	$('#form-error').show()
}

function hide_errors() {
	$('#form-error').hide()
}

$(document).ready(function() {
	// bind 'myForm' and provide a simple callback function 
	$('form#bio').ajaxForm({
		beforeSubmit: function() {
			show_status('Sending...')
			$("form#bio :input").attr("disabled", true);
		},
		success: function(response) {
			if(response.saved) {
				show_status('Saved', 'success')
				hide_errors()
			} else {
				show_status('Error', 'error')
				show_errors(response.errors)
			}
		},
		uploadProgress: function (event, position, total, percentComplete) {
			var percentVal = percentComplete + '%';
			show_status('Uploading '+percentVal+'...')
		},
		complete: function (xhr) {
			if(xhr.status != 200) {
				show_status('Unknown error', 'error')
			}
			$("form#bio :input").attr("disabled", false);
		}
	})
})