<?php
error_reporting(0);
include "koneksi.php";


$auth = $_GET['auth']; //888
$perintah = $_GET['perintah'];

//------Supplier------
$id_supplier = $_GET['id_supplier'];
$nama_supplier = $_GET['nama_supplier'];
$no_telp = $_GET['no_telp'];
$alamat = $_GET['alamat'];

//------ barang--------
$id_barang = $_GET['id_barang'];
$kode_barang = $_GET['kode_barang'];
$nama_barang = $_GET['nama_barang'];
$harga = $_GET['harga'];
$stok = $_GET['stok'];
$id_supplier = $_GET['id_supplier'];

//-------Pembeli--------
$id_pembeli = $_GET['id_pembeli'];
$nama_pembeli = $_GET['nama_pembeli'];
$jk = $_GET['jk'];
$no_telp = $_GET['no_telp'];
$alamat = $_GET['alamat'];

//-------Transaksi------
$id_transaksi = $_GET['id_transaksi'];
$id_barang = $_GET['id_barang'];
$id_pembeli = $_GET['id_pembeli'];
$tanggal = $_GET['tanggal'];
$keterangan = $_GET['keterangan'];

//-----Pembayaran-------
$id_pembayaran = $_GET['id_pembayaran'];
$tgl_bayar = $_GET['tgl_bayar'];
$total_bayar = $_GET['total_bayar'];
$id_transaksi = $_GET['id_transaksi'];

//-----Login-------
$username = $_GET['username'];
$password = $_GET['password'];


//=======insert======
//insert===barang===

if($auth == "888"){

if(!empty($_GET) && $perintah=="insert"){

    $sql = "INSERT INTO barang (nama_barang, id_barang, kode_barang, harga, stok) VALUES ('". $nama_barang. "','".$id_barang."','".$kode_barang."','".$harga."', '".$stok."')";
    echo"<br>";
    echo $sql;

    if (mysqli_query($conn, $sql)) {
        echo "<br>";
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }


}

//insert===supplier===

if($auth == "888"){

if(!empty($_GET) && $perintah=="insert"){

    $sql = "INSERT INTO supplier (id_supplier, nama_supplier, no_telp, alamat) VALUES ('". $id_supplier. "','".$nama_supplier."','".$no_telp."', '".$alamat."')";
    echo"<br>";
    echo $sql;

    if (mysqli_query($conn, $sql)) {
        echo "<br>";
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }


}

//insert===pembeli===

if($auth == "888"){

if(!empty($_GET) && $perintah=="insert"){

    $sql = "INSERT INTO pembeli (id_pembeli, nama_pembeli, jk,  no_telp, alamat) VALUES ('". $id_pembeli. "','".$nama_pembeli."','".$jk."','".$no_telp."', '".$alamat."')";
    echo"<br>";
    echo $sql;

    if (mysqli_query($conn, $sql)) {
        echo "<br>";
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }


}

//insert===transaksi===

if($auth == "888"){

if(!empty($_GET) && $perintah=="insert"){

    $sql = "INSERT INTO transaksi (id_transaksi, id_barang, id_pembeli,  tanggal, keterangan) VALUES ('". $id_transaksi. "','".$id_barang."','".$id_pembeli."','".$tanggal."', '".$keterangan."')";
    echo"<br>";
    echo $sql;

    if (mysqli_query($conn, $sql)) {
        echo "<br>";
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }


}

//insert===tb_login===

if($auth == "888"){

if(!empty($_GET) && $perintah=="insert"){

    $sql = "INSERT INTO tb_login (username, password) VALUES ('". $username. "', '".$password."')";
    echo"<br>";
    echo $sql;

    if (mysqli_query($conn, $sql)) {
        echo "<br>";
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }


}

//update===barang===

if(!empty($_GET) && $perintah=="update"){

    $sql = "update barang set nama_barang='".$nama_barang."' where kode_barang='".$kode_barang."'";
    echo"<br>";
    echo $sql;

    if (mysqli_query($conn, $sql)) {
        echo "<br>";
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }


}

//delete===barang===

if(!empty($_GET) && $perintah=="delete"){

    $sql = "delete from barang where kode_barang=".$kode_barang;
    echo"<br>";
    echo $sql;

    if (mysqli_query($conn, $sql)) {
        echo "<br>";
        echo "Record has been deleted";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }


}


//===select===

$return_arr = array();
//$sql = "SELECT kode_barang, nama_barang, harga, stok FROM barang";
$sql = "select kode_barang, nama_barang, harga, stok from barang";
$result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            //echo "<br>";
            //echo "kode_barang= ". $row["kode_barang"]. ", nama_barang= ". $row["nama_barang"]. ", harga = ".$row["harga"]. ", stok = ".$row["stok"];
            //echo "kd_barang = $row['kode_barang'] , nama_barang= $row['barang']";
            
            $row_array['kode_barang'] = $row['kode_barang'];
            $row_array['nama_barang'] = $row['nama_barang'];
            $row_array['harga'] = $row['harga'];
            $row_array['stok'] = $row['stok'];

            array_push($return_arr,$row_array);
        }
        echo json_encode($return_arr);
    } else {
            echo "0 results";
    }



$conn->close();

}
?>