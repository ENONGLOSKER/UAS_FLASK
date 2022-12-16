-- phpMyAdmin SQL Dump
-- version 5.3.0-dev+20221026.4ba2a88e73
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 16 Des 2022 pada 10.04
-- Versi server: 10.4.24-MariaDB
-- Versi PHP: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `py_flask`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_dosen`
--

CREATE TABLE `tb_dosen` (
  `nidn` varchar(10) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `jenis_kelamin` enum('L','P') DEFAULT NULL,
  `tempat_lahir` varchar(50) DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `alamat` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tb_dosen`
--

INSERT INTO `tb_dosen` (`nidn`, `nama`, `jenis_kelamin`, `tempat_lahir`, `tgl_lahir`, `alamat`) VALUES
('0109303', 'Siti Puspita Hidasakti MZ, M.Cs', 'P', 'Kopang', '1988-12-10', 'Jl. Merdeka Barat No. 21 Kota Praya'),
('2002419', 'M. Khaerul Faridi, M.Kom', 'L', 'Praya', '1990-09-09', 'Jl. Merdeka No. 10 Kota Praya\r\n'),
('2002420', 'MUHAMMAD AZMI,M.Kom', 'L', 'Sepit', '1993-02-02', 'jl.L Mustiadi no.32 Sepit.Keruak'),
('2002421', 'AHMAD HARMAIN,M.Kom', 'L', 'Kalijaga', '1993-02-02', 'jl. labuan lombok no.32 kalijaga'),
('2002422', 'FITRIANI,S.Kom', 'P', 'Masbagik', '1993-02-02', 'jl.L masbagik no.32 masbagik'),
('2002423', 'ZULKARNAEN,M.Kom', 'L', 'Sukamulia', '1993-02-02', 'jl. selong no.32 selong'),
('2002424', 'NUKMAN,M.Kom', 'L', 'kalijaga', '1993-02-02', 'jl.L kalijaga no.32 kalijaga'),
('2002425', 'SRI HARDIANA DH,M.Kom', 'P', 'Selong', '1993-02-02', 'jl. selong no.32 selong'),
('2002426', 'M.ALFAN HABIB,M.Cs', 'L', 'labuan hajji', '1993-02-02', 'jl.L hajji no.32 labuan hajji'),
('2002427', 'DEDY EFENDI, S.Ag.,S.H.,M.Pd', 'L', 'Anjani', '1993-02-02', 'jl. suralaga no.32 suralaga'),
('2009408', 'IRWAN,M.Pd', 'L', 'ANJANI', '2022-12-28', 'ANJNI'),
('2009409', 'LL. Puji Indra Karisma, M.Cs', 'L', 'Selong', '1987-02-12', 'Jl. Ki Hajar Dewantara No. 20 Kota Mataram');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_jurusan`
--

CREATE TABLE `tb_jurusan` (
  `kode_jurusan` varchar(7) NOT NULL,
  `nama_jurusan` varchar(50) NOT NULL,
  `kaprodi` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tb_jurusan`
--

INSERT INTO `tb_jurusan` (`kode_jurusan`, `nama_jurusan`, `kaprodi`) VALUES
('55', 'Teknik Informatika', 'LL. Puji Indra Karisma, M.Cs'),
('57', 'Sistem Informasi ', 'Siti Puspita Hidasakti MZ, M.Cs'),
('tes', 'testing', 'testing update');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_mahasiswa`
--

CREATE TABLE `tb_mahasiswa` (
  `nim` varchar(15) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `jenis_kelamin` enum('L','P') DEFAULT NULL,
  `tempat_lahir` varchar(50) DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `alamat` text DEFAULT NULL,
  `kode_jurusan` varchar(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tb_mahasiswa`
--

INSERT INTO `tb_mahasiswa` (`nim`, `nama`, `jenis_kelamin`, `tempat_lahir`, `tgl_lahir`, `alamat`, `kode_jurusan`) VALUES
('204855009', 'rizqa ulfaturrahmis', 'P', 'sakra', '2001-10-28', 'SAKRA', '55'),
('204855033', 'ira miatun', 'P', 'masbagik', '1999-10-31', 'MASBAGIK', '55'),
('204855035', 'rabiatul adawiyah', 'P', 'sepit', '2001-10-28', 'SEPIT', '55'),
('204855090', 'novia ardani', 'P', 'sangkawati', '2001-11-07', 'LANDO', '55'),
('204855101', 'ruswanti mulyana', 'P', 'sikur', '2002-10-28', 'SIKUR', '55'),
('204855111', 'wardatul ummi', 'P', 'sukamandi', '2002-11-11', 'LENEK', '55'),
('204855113', 'Zaenul Alqusairi', 'L', 'lokon', '2001-06-20', 'lokon', '55'),
('2155481001', 'Nadia Ilham', 'P', 'Selong', '2000-09-12', 'Jl. Ki Hajar Dewantara No. 20 Kota Mataram', '57'),
('2155481004', 'Nadia', 'P', 'Kopang', '2001-12-10', 'Jl. Merdeka Barat No. 21 Kota Praya\r\n\r\n', '55'),
('2157481003', 'Muhammad Nabil Zakaria', 'L', 'Praya', '1999-09-09', 'Jl. Merdeka No. 10 Kota Praya', '55');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_matakuliah`
--

CREATE TABLE `tb_matakuliah` (
  `kode_mk` varchar(7) NOT NULL,
  `nidn` varchar(10) NOT NULL,
  `nama_mk` varchar(50) DEFAULT NULL,
  `sks` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tb_matakuliah`
--

INSERT INTO `tb_matakuliah` (`kode_mk`, `nidn`, `nama_mk`, `sks`) VALUES
('MK5579', '2009408', 'MATRIK AL-JABAR LINEAR', 3),
('MK5580', '2009408', 'elcode', 3),
('MK6670', '0109303', 'BASISDATA', 3),
('MK6671', '2002420', 'JARINGAN KOMPUTETR', 3),
('MK6672', '2002421', 'PEMROGRAMAN 111', 3),
('MK6673', '2002422', 'PENGOLHAN CITRA', 3),
('MK6674', '2002423', 'ANALISIS SISTEM', 3),
('MK6675', '2002424', 'DESAIN WEB', 3),
('MK6676', '2002425', 'PENGAMANAN DATA', 3),
('MK6677', '2002426', 'REKAYASA PERANGKAT LUNAK', 3),
('MK6678', '2002427', 'SEMINAR', 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_nilai`
--

CREATE TABLE `tb_nilai` (
  `id_nilai` int(10) NOT NULL,
  `nim` varchar(15) NOT NULL,
  `kode_mk` varchar(7) NOT NULL,
  `absen` decimal(10,0) NOT NULL,
  `tugas` decimal(10,0) NOT NULL,
  `uts` decimal(10,0) NOT NULL,
  `uas` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tb_nilai`
--

INSERT INTO `tb_nilai` (`id_nilai`, `nim`, `kode_mk`, `absen`, `tugas`, `uts`, `uas`) VALUES
(8, '2155481001', 'MK6670', 60, 50, 60, 50),
(16, '2155481004', 'MK6670', 40, 30, 50, 50),
(21, '204855113', 'MK6671', 90, 90, 90, 95),
(22, '204855113', 'MK6672', 90, 80, 90, 95),
(23, '204855113', 'MK6673', 90, 85, 85, 90),
(24, '204855113', 'MK6674', 90, 95, 85, 95),
(25, '204855113', 'MK6675', 90, 90, 90, 90),
(26, '204855113', 'MK6676', 90, 90, 85, 95),
(27, '204855113', 'MK6677', 90, 90, 95, 90),
(28, '204855113', 'MK6678', 90, 95, 95, 95);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `tb_dosen`
--
ALTER TABLE `tb_dosen`
  ADD PRIMARY KEY (`nidn`);

--
-- Indeks untuk tabel `tb_jurusan`
--
ALTER TABLE `tb_jurusan`
  ADD PRIMARY KEY (`kode_jurusan`);

--
-- Indeks untuk tabel `tb_mahasiswa`
--
ALTER TABLE `tb_mahasiswa`
  ADD PRIMARY KEY (`nim`),
  ADD KEY `kode_jurusan` (`kode_jurusan`);

--
-- Indeks untuk tabel `tb_matakuliah`
--
ALTER TABLE `tb_matakuliah`
  ADD PRIMARY KEY (`kode_mk`),
  ADD KEY `nidn` (`nidn`);

--
-- Indeks untuk tabel `tb_nilai`
--
ALTER TABLE `tb_nilai`
  ADD PRIMARY KEY (`id_nilai`),
  ADD KEY `nim` (`nim`),
  ADD KEY `kode_mk` (`kode_mk`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `tb_nilai`
--
ALTER TABLE `tb_nilai`
  MODIFY `id_nilai` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `tb_mahasiswa`
--
ALTER TABLE `tb_mahasiswa`
  ADD CONSTRAINT `tb_mahasiswa_ibfk_1` FOREIGN KEY (`kode_jurusan`) REFERENCES `tb_jurusan` (`kode_jurusan`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `tb_matakuliah`
--
ALTER TABLE `tb_matakuliah`
  ADD CONSTRAINT `tb_matakuliah_ibfk_1` FOREIGN KEY (`nidn`) REFERENCES `tb_dosen` (`nidn`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `tb_nilai`
--
ALTER TABLE `tb_nilai`
  ADD CONSTRAINT `tb_nilai_ibfk_1` FOREIGN KEY (`kode_mk`) REFERENCES `tb_matakuliah` (`kode_mk`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tb_nilai_ibfk_2` FOREIGN KEY (`nim`) REFERENCES `tb_mahasiswa` (`nim`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
