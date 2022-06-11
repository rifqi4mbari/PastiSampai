CREATE SCHEMA dbpastisampai;
USE dbPastiSampai;

CREATE TABLE tblPastiSampai(
id_pengiriman INT(30) PRIMARY KEY,
tanggal_pengiriman VARCHAR(30),
jenis_pengiriman VARCHAR(40),
jenis_barang VARCHAR(80),
asal_pengiriman VARCHAR(40),
tujuan_pengiriman VARCHAR(40),
status_pengiriman VARCHAR(40));