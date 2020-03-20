<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <?php
      $json_url = "URL"; # URL for getting JSON data
      $php_json = file_get_contents($json_url);
      # $php_arr = json_decode($php_json, true); if convert JSON to array on PHP
    ?>
    <script>
      var js_json = <?php echo $php_json; ?>;
      console.log(js_json["items"][0]["example"]); // refered value in the JSON data
    </script>
  </head>
  <body>
    <br>
  </body>
</html>
