<?php
if(isset($_POST['submit'])) {
  $target_dir = "uploads/"; // directorio donde se guardarán los archivos cargados
  $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
  $uploadOk = 1;
  $imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

  // Comprobar si el archivo ya existe
  if (file_exists($target_file)) {
    echo "El archivo ya existe.";
    $uploadOk = 0;
  }

  // Limitar el tamaño del archivo
  if ($_FILES["fileToUpload"]["size"] > 500000) {
    echo "Lo siento, tu archivo es demasiado grande.";
    $uploadOk = 0;
  }

  // Permitir solo ciertos tipos de archivos
  if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
  && $imageFileType != "gif" ) {
    echo "Lo siento, solo se permiten archivos JPG, JPEG, PNG y GIF.";
    $uploadOk = 0;
  }

  // Comprobar si $uploadOk está configurado en 0 por un error
  if ($uploadOk == 0) {
    echo "Lo siento, tu archivo no fue cargado.";
  // Si todo está bien, intenta subir el archivo
  } else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
      echo "El archivo ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " ha sido cargado.";
    } else {
      echo "Lo siento, hubo un error al cargar tu archivo.";
    }
  }
}
?>
