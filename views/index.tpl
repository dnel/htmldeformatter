<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Home &middot; MyApp</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<!-- Bootstrap -->
		<link href="{{ get_url('css', filename='bootstrap.css') }}" rel="stylesheet" media="screen">
		<style type="text/css">
		body {
        padding-bottom: 40px;
        background-color: #f5f5f5;
		}
		</style>
	</head>
	<body>
		<script src="http://code.jquery.com/jquery.js"></script>
		<script src="{{ get_url('js', filename='bootstrap.min.js') }}"></script>

		<div class="container">
		<h1>HTML Text De-formatter</h1>
		<p class="text-muted">Convert HTML to Plaintext in one click!</p>
		<p class="text-warning">Please note: Complex formatting such as tables etc may not render well in plaintext.</p>
%if converted_text:		
		<form class="form-horizontal" role="form" action="/" method="get">
			<div class="form-group">
				<textarea class="form-control" rows="30">{{converted_text}}</textarea>
			</div>
			<div class="form-group">
				<button class="btn btn-large btn-danger" type="submit">Reset</button>
			</div>
		</form>
%else:
		<form class="form-horizontal" role="form" action="/" method="post">
			<div class="form-group">
				<textarea class="form-control" rows="30" placeholder="Paste your HTML-infested text in here." name="html_content"></textarea>
			</div>
			<div class="form-group">
				<button class="btn btn-large btn-primary" type="submit">Convert</button>
			</div>
		</form>
		</div>
	</body>

</html>
