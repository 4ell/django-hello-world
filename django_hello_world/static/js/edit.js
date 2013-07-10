
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