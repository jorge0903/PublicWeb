<html>
  <body>  
    <h1><?php echo ">------ DONE -------->" ?></h1>
    <?php
       // Comment
       $url    = $_POST["url"];
       $format = $_POST["fileType"];
       $app    = $_POST["app"];
       $shared = $_POST["shared"];
       
       
       echo $url    . " ";
       echo $format . " ";
       echo $app    . " ";
       echo $shared . " ";


       $myfile = fopen("PHP-FILE.txt", "a+");
       fwrite($myfile, $url . " ");
       fwrite($myfile, $format . " ");
       fwrite($myfile, $app . " ");
       fwrite($myfile, $shared . "\n");
       fwrite($myfile, "\n");

       $cmd = "python process.py {$url} {$format} {$app} {$shared} & ";
       //echo $cmd;
       
       $output = shell_exec($cmd);
       echo "<pre>$output</pre>";
       
       ?>
  </body>
</html>
