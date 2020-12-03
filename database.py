import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=kehadiran user=pi")
        self.cur = self.conn.cursor()

    def Insert(self, task):
        cmd = """INSERT INTO siswa (nama,kelas,umur,nis,foto) VALUES(%s, %s, %s, %s, %s)"""
        self.cur.execute(cmd, task)
        self.conn.commit()

    def Kehadiran(self,task):
        cmd = """INSERT INTO kehadiran (nama, nis, kelas, suhu,waktu) VALUES(%s, %s, %s, %s, %s)"""
        self.cur.execute(cmd, task)
        self.conn.commit()

    def showAll(self):
        self.cur.execute("SELECT * FROM siswa")
        show = self.cur.fetchall()
        print(show)

    def getNama(self, nis):
        self.cur.execute("SELECT nama FROM siswa WHERE nis='{}'".format(nis))
        nama = self.cur.fetchall()
        return nama

    def getAllImage(self):
        self.cur.execute("SELECT foto FROM siswa;")
        img = self.cur.fetchall()
        return img

    def getNis(self):
        self.cur.execute("SELECT nis FROM siswa;")
        nis = self.cur.fetchall()
        return nis

    def getAll(self, nis):
        self.cur.execute("SELECT * FROM siswa WHERE nis='{}'".format(nis))
        nama = self.cur.fetchall()
        return nama

    def getImage(self, nis):
        self.cur.execute("SELECT foto FROM siswa WHERE nis = {}".format(nis))

    def Delete(self, nis):
        self.cur.execute("DELETE FROM siswa WHERE nis = {}".format(nis))
        self.conn.commit()


