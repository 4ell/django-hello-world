
var ui = {
	photo : {show: null},
	status: {show: null},
	errors: {show: null, hide: null}
}

ui.photo.show = function() {
	var input = qs('#id_photo')
	if (input.files && input.files[0]) {
		var reader = new FileReader()

		reader.onload = function (e) {
			qs('img.photo').src = e.target.result
		}

		reader.readAsDataURL(input.files[0])
	}
}

ui.status.show = function(msg, color, timeout) {
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

ui.errors = {
	show: function(errors) {
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
	},

	hide: function() {
		$('#form-error').hide()
	}
}
