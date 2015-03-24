# Create a custom widget here
import django.forms

class FileUploader(django.forms.FileInput):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)	# do some custom widget code here


	def render(self, name, value, attrs=None):
		return super().render(name, value, attrs)+ ("""
			<script>
				$(function() {
					$('#id_%s').off('change.uploader').on('change.uploader', function() {
						var fd = new FormData();
						var file = this.files[0];
						fd.append("upload", file);
						$.ajax({
							url: '/homepage/uploader.upload/',
							type: 'POST',
							contentType: false,
							processData: false,
							data: fd,
							xhr: function() {
								var xhr = jQuery.ajaxSettings.xhr();
								if (xhr.upload) {
									xhr.upload.addEventListener('progress', function(evt) {
										if (evt.lengthComputable) {
											// update the progress bar
											var percentComplete = evt.loaded / evt.total;
											$('.bar').show();
											$('.progress-bar').css('width',(percentComplete)*100+'%%');
						 					$('.progress-bar').text(Math.floor((percentComplete)*100)+'%%');
										}//if
									}, false);//add event listener
								}//if
								return xhr;
							},//xhr
							success: function(data) {
								// save the name to be uploaded with the main form
								$('#id_upload_fullname').val(data);
								console.log("Success");
							},//success
							error: function(data) {
								console.log("Error");
								console.log(err);
							},//error
						});//ajax
					});//change
					$('#id_%s').closest('form').off('submit.uploader').on('submit.uploader', function() {
						$('#id_%s').remove();
					});//submit
				});//ready
			</script>
		""" % (name, name, name))