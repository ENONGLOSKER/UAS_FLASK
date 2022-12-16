from flask import Flask, render_template,request,redirect, flash
import mysql.connector

#database-------------------------
app = Flask(__name__)
app.secret_key = '2v2Yp7XSS9cC5WcbGk3l7PijY5bW4zwJ'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="py_flask"
)

# prodi-------------------------
# @app.route('/cari', methods=['GET', 'POST'])
# def cari():
#     if request.method == 'POST':
#         data = request.form
#         cari = data['cari']
#         cursor = db.cursor()
        
#         query = f" SELECT * FROM tb_nilai WHERE nama = cari='{cari}'"
#         cursor.execute(query)
#         db.commit()
#         return redirect('/khs', code=302, Response=None)

#     return render_template('form.html')

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_jurusan")
    result = cursor.fetchall()
    print(result)

    return render_template('prodi.html', data=result)

#insert
@app.route('/addpd', methods=['GET', 'POST'])
def addprodi():
    if request.method == 'POST':
        data = request.form
        kode_jurusan = data['kode_jurusan']
        nama_jurusan = data['nama_jurusan']
        kaprodi = data['kaprodi']

        cursor = db.cursor()
        query = f"INSERT INTO tb_jurusan VALUES('{kode_jurusan}', '{nama_jurusan}', '{kaprodi}')"
        cursor.execute(query)
        db.commit()
        return redirect('/', code=302, Response=None)

    return render_template('inprodi.html')

#edit
@app.route("/edit/<kode_jurusan>", methods=["GET", "POST"])
def edit(kode_jurusan):
    cursor = db.cursor(buffered=True)
    cursor.execute(f"select * from tb_jurusan WHERE kode_jurusan= '{kode_jurusan}'")
    data = cursor.fetchone()
    if request.method == "POST":
        kode_jurusan = request.form['kode_jurusan']
        nama_jurusan = request.form['nama_jurusan']
        kaprodi = request.form['kaprodi']

        sql = (f"UPDATE tb_jurusan SET kode_jurusan='{kode_jurusan}', nama_jurusan='{nama_jurusan}', kaprodi='{kaprodi}' WHERE kode_jurusan='{kode_jurusan}'")
        cursor.execute(sql)
        db.commit()
        cursor.close()
        flash('Data updated successfully','success')
        return redirect('/') 
    else:
        return render_template('editprodi.html', data=data, code=302, Response=None)
        
#hapus data
@app.route('/hapus/<kode_jurusan>')
def Hapusprd(kode_jurusan):
    cursor = db.cursor()
    query = f"DELETE FROM tb_jurusan WHERE kode_jurusan='{kode_jurusan}'"
    cursor.execute(query)
    db.commit()

    return redirect('/', code=302, Response=None)

#mahasiswa -------------------------------------------------
@app.route('/mahasiswa')
def mahasiswa():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_mahasiswa order by nama desc")
    result = cursor.fetchall()
    print(result)

    return render_template('mahasiswa.html', data=result)

#insert
@app.route('/addmh', methods=['GET', 'POST'])
def addmh():
    if request.method == 'POST':
        data = request.form
        nim = data['nim']
        nama = data['nama']   
        jenis_kelamin = data['jenis_kelamin']
        tempat_lahir = data['tempat_lahir']
        tanggal_lahir = data['tanggal_lahir']
        alamat = data['alamat']
        kode_prodi = data['kode_prodi']
        
        cursor = db.cursor()
        query = f"INSERT INTO tb_mahasiswa VALUES ('{nama}','{nim}','{jenis_kelamin}','{tempat_lahir}','{tanggal_lahir}','{alamat}','{kode_prodi}')"
        cursor.execute(query)
        db.commit()
        return redirect('/mahasiswa', code=302, Response=None)

    return render_template('inmhs.html')

#edit mh
@app.route("/editmh/<nim>", methods=["GET", "POST"])
def editmh(nim):
    cursor = db.cursor(buffered=True)
    cursor.execute(f"select * from tb_mahasiswa WHERE nim= '{nim}'")
    data = cursor.fetchone()
    if request.method == "POST":
        nim = request.form['nim']
        nama = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        tempat_lahir = request.form['tempat_lahir']
        tgl_lahir = request.form['tgl_lahir']
        alamat = request.form['alamat']
        kode_jurusan = request.form['kode_jurusan']

        sql = (f"UPDATE tb_mahasiswa SET nim='{nim}', nama='{nama}',jenis_kelamin='{jenis_kelamin}',tempat_lahir='{tempat_lahir}',tgl_lahir='{tgl_lahir}', alamat='{alamat}',kode_jurusan='{kode_jurusan}' WHERE nim='{nim}'")
        cursor.execute(sql)
        db.commit()

        flash('Data updated successfully','success')
        return redirect('/mahasiswa') 
    else:
        return render_template('editmhs.html', data=data, code=302, Response=None)

#hapus mh
@app.route('/hapusmh/<nim>')
def Hapusmh(nim):
    cursor = db.cursor()
    query = f"DELETE FROM tb_mahasiswa WHERE nim='{nim}'"
    cursor.execute(query)
    db.commit()

    return redirect('/mahasiswa', code=302, Response=None)

#dosen-------------------------
@app.route('/dosen')
def dosen():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_dosen")
    result = cursor.fetchall()
    print(result)

    return render_template('dosen.html', datas=result)

#addosen
@app.route('/addosen', methods=['GET', 'POST'])
def addosen():
    if request.method == 'POST':
        data = request.form
        nidn = data['nidn']
        nama = data['nama']   
        jenis_kelamin = data['jenis_kelamin']
        tempat_lahir = data['tempat_lahir']
        tgl_lahir = data['tgl_lahir']
        alamat = data['alamat']
        
        cursor = db.cursor()
        query = f"INSERT INTO tb_dosen VALUES ('{nama}','{nidn}','{jenis_kelamin}','{tempat_lahir}','{tgl_lahir}','{alamat}')"
        cursor.execute(query)
        db.commit()
        return redirect('/dosen', code=302, Response=None)

    return render_template('indosen.html')

#edit dosen
@app.route("/editdosen/<nidn>", methods=["GET", "POST"])
def editdosen(nidn):
    cursor = db.cursor(buffered=True)
    cursor.execute(f"select * from tb_dosen WHERE nidn= '{nidn}'")
    data = cursor.fetchone()
    if request.method == "POST":
        nidn = request.form['nidn']
        nama = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        tempat_lahir = request.form['tempat_lahir']
        tgl_lahir = request.form['tgl_lahir']
        alamat = request.form['alamat']

        sql = (f"UPDATE tb_dosen SET nidn='{nidn}', nama='{nama}',jenis_kelamin='{jenis_kelamin}',tempat_lahir='{tempat_lahir}',tgl_lahir='{tgl_lahir}', alamat='{alamat}' WHERE nidn='{nidn}'")
        cursor.execute(sql)
        db.commit()

        flash('Data updated successfully','success')
        return redirect('/dosen') 
    else:
        return render_template('editdosen.html', data=data, code=302, Response=None)

#hapus dosen
@app.route('/hapusdosen/<nidn>')
def hpuasdosen(nidn):
    cursor = db.cursor()
    query = f"DELETE FROM tb_dosen WHERE nidn='{nidn}'"
    cursor.execute(query)
    db.commit()

    return redirect('/dosen', code=302, Response=None)

#MK ---------------------------
@app.route('/mk')
def mk():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_matakuliah order by kode_mk desc ")
    result = cursor.fetchall()
    print(result)

    return render_template('mk.html', datas=result)

#insert mk
@app.route('/addmk', methods=['GET', 'POST'])
def addmk():
    if request.method == 'POST':
        data = request.form
        kode_mk = data['kode_mk']
        nama_mk = data['nama_mk']
        sks = data['sks']
        nidn = data['nidn']

        cursor = db.cursor()
        query = f"INSERT INTO `tb_matakuliah` (`kode_mk`, `nidn`, `nama_mk`, `sks`) VALUES ('{kode_mk}','{nidn}','{nama_mk}','{sks}')"
        cursor.execute(query)
        db.commit()
        return redirect('/mk', code=302, Response=None)

    return render_template('inmk.html')

#edit mk
@app.route("/editmk/<kode_mk>", methods=["GET", "POST"])
def editmk(kode_mk):
    cursor = db.cursor(buffered=True)
    cursor.execute(f"select * from tb_matakuliah WHERE kode_mk= '{kode_mk}'")
    data = cursor.fetchone()
    if request.method == "POST":
        kode_mk = request.form['kode_mk']
        nama_mk = request.form['nama_mk']
        sks = request.form['sks']
        nidn = request.form['nidn']

        sql = (f"UPDATE tb_matakuliah SET kode_mk='{kode_mk}', nama_mk='{nama_mk}', sks='{sks}', nidn='{nidn}' WHERE kode_mk='{kode_mk}'")
        cursor.execute(sql) 
        db.commit()
        cursor.close()
        flash('Data updated successfully','success')
        return redirect('/mk') 
    else:
        return render_template('editmk.html', data=data, code=302, Response=None)
        
#hapus mk
@app.route('/hapusmk/<kode_mk>')
def hapusmk(kode_mk):
    cursor = db.cursor()
    query = f"DELETE FROM tb_matakuliah WHERE kode_mk='{kode_mk}'"
    cursor.execute(query)
    db.commit()

    return redirect('/mk', code=302, Response=None)


#nilai----------------
@app.route('/nilai')
def nilai():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_nilai order by nim desc ")
    result = cursor.fetchall()
    print(result)

    return render_template('nilai.html', data=result)

#insert nilai
@app.route('/addnilai', methods=['GET', 'POST'])
def addnilai():
    if request.method == 'POST':
        data = request.form
        # id_nilai = data['id_nilai']
        nim = data['nim']
        kode_mk = data['kode_mk']
        absen = data['absen']
        tugas = data['tugas']
        uts = data['uts']
        uas = data['uas']

        cursor = db.cursor()
        query = f"INSERT INTO `tb_nilai` (`nim`, `kode_mk`, `absen`, `tugas`, `uts`, `uas`) VALUES ('{nim}','{kode_mk}','{absen}','{tugas}','{uts}','{uas}');"
        # query = f"INSERT INTO tb_nilai VALUES ('{id_nilai}',{nim}','{kode_mk}','{absen}','{tugas}','{uts}','{uas}')"
        cursor.execute(query)
        db.commit()
        return redirect('/nilai', code=302, Response=None)

    return render_template('innilai.html')

#edit nilai
@app.route("/editnilai/<nim>", methods=["GET", "POST"])
def editnilai(nim):
    cursor = db.cursor(buffered=True)
    cursor.execute(f"select * from tb_nilai WHERE nim= '{nim}'")
    data = cursor.fetchone()
    if request.method == "POST":
        data = request.form
        nim = data['nim']
        kode_mk = data['kode_mk']
        absen = data['absen']
        tugas = data['tugas']
        uts = data['uts']
        uas = data['uas']

        sql = (f"UPDATE tb_nilai SET nim='{nim}', kode_mk='{kode_mk}', absen='{absen}', tugas='{tugas}', uts='{uts}', uas='{uas}' WHERE nim='{nim}'")
        cursor.execute(sql) 
        db.commit()
        cursor.close()
        flash('Data updated successfully','success')
        return redirect('/nilai') 
    else:
        return render_template('editnilai.html', data=data, code=302, Response=None)

#hapus nilai
@app.route('/hapusnilai/<nim>')
def hapusnilai(nim):
    cursor = db.cursor()
    query = f"DELETE FROM tb_nilai WHERE nim='{nim}'"
    cursor.execute(query)
    db.commit()

    return redirect('/nilai', code=302, Response=None)  

@app.route('/khs', methods=["GET", "POST"] )
def khs():
    if request.method == 'GET': 
        cursor = db.cursor()
        cari= (f"SELECT nim,nama FROM tb_mahasiswa")
        cursor.execute(cari)
        result = cursor.fetchall()

        return render_template('khs.html',cari=result)

    else:
        nim = request.form ['nim']
        cursor = db.cursor()
        cursor.execute(f"""
        SELECT tb_mahasiswa.nim,tb_mahasiswa.nama,tb_jurusan.nama_jurusan, tb_matakuliah.sks,tb_matakuliah.nama_mk,tb_dosen.nama,tb_nilai.absen,tb_nilai.tugas,tb_nilai.uts,tb_nilai.uas,(0.1*tb_nilai.absen)+(0.2*tb_nilai.tugas)+(0.3*tb_nilai.uts)+(0.4*tb_nilai.uas) as total FROM (select * from tb_nilai where nim = {nim} ) as tb_nilai
        join tb_mahasiswa on (tb_mahasiswa.nim = tb_nilai.nim)
        join tb_matakuliah on (tb_matakuliah.kode_mk = tb_nilai.kode_mk)
        join tb_dosen on (tb_dosen.nidn = tb_matakuliah.nidn)
        join tb_jurusan on (tb_jurusan.kode_jurusan = tb_mahasiswa.kode_jurusan);
        """)
        khs = cursor.fetchall()
        
        cursor.execute(f"SELECT * FROM tb_mahasiswa WHERE nim={nim}")
        mhs=cursor.fetchone()
        cursor.execute(f"SELECT nim,nama FROM tb_mahasiswa")
        mh=cursor.fetchall() 
        print(mh)
        print(mhs)
        print(khs)

        context = {
             'cari' : mh,
             'data' : khs,
             'mhs' :mhs
        }


        return render_template('khs.html', data=context)

if __name__ == "__main__":
    app.run(debug=True)
