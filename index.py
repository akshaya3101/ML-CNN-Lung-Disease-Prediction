index.html file

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Classification</title>
</head>
<body>
    <h1>Upload an Image for Prediction</h1>
    <form action="{{ url_for('predict') }}" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Predict</button>
    </form>
</body>
</html>
