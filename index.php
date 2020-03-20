<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8'>
  <?php
    $json_url = "URL"; # set URL for getting JSON data
    $crl = curl_init();
    curl_setopt($crl, CURLOPT_URL, $json_url);
    curl_setopt($crl, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($crl, CURLOPT_SSL_VERIFYPEER, FALSE); 
    $php_json = curl_exec($crl);
    curl_close($crl);
  ?>
  <script>
    var js_json = <?php echo $php_json; ?>;
    console.log(js_json["items"][0]["example"]); # refered value in the JSON data
  </script>
</head>
<body>
  underconstruction
</body>
</html>