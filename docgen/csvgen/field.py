import random
import string
import pandas as pd
from . import config

from . import utils



def nomer_dokumen():
    pass

def nomer_faktur():
    pass

def tanggal_faktur():
    pass

# ====== identitas pemilik ====== #

def degree(name, csv_path = None):
    if csv_path == None:
        csv_path = config.csv_gelar
    dframe = pd.read_csv(csv_path)
    sample = dframe.sample().reset_index(drop=True)
    sample = sample['singkatan'][0]
    sample = sample.strip()
    out = f'{name}, {sample}'
    
    return out

def abbrev_insert(name, is_gelar):
    abjad = string.ascii_uppercase
    abb = random.choices(abjad, k=1)[0]
    
    name_list = name.split(" ")
    name_len = len(name_list)
    middle_index = name_len // 2
    
    if is_gelar:
        name_list.insert(middle_index, abb)
    else:
        ridx = utils.random_choice(data=[middle_index, name_len], weight=[0.5,0.5])
        if ridx==0:
            ridx = name_len 
        name_list.insert(ridx, abb)
        
    name_combined = ' '.join(name_list)
    
    return name_combined
    
    
def name(gender='male', degree_prob=0.1, abbrev_prob=0.2, csv_path = None):
    if csv_path == None:
            csv_path = config.csv_nama
    dframe = pd.read_csv(csv_path)
    dframe = dframe[dframe['gender'] == gender]
    sampled_name = dframe.sample().reset_index(drop=True)
    sampled_name = sampled_name['name'][0]
    
    use_gelar = False
    if utils.coin_toss(p=degree_prob):
        sampled_name = degree(sampled_name)
        use_gelar = True
        
    if utils.coin_toss(p=abbrev_prob):
        sampled_name = abbrev_insert(sampled_name, use_gelar)
        
    return sampled_name


def clean_kab_text(text):
    if text.startswith('KOTA ADM.'):
        text = text.replace('KOTA ADM. ','')
    if text.startswith("KAB."):
        text = text.replace('KAB. ','KABUPATEN ')
    if text.startswith("KAB"):
        text = text.replace('KAB ','KABUPATEN ')
    return text

def wilayah(kode_wilayah=None, csv_path=None):
    if csv_path == None:
        csv_path = config.csv_wilayah
    
    df = pd.read_csv(csv_path)
    
    if kode_wilayah != None:
       df = wilayah_filter(df, kode_wilayah)
    
    dfkel = df[df['kode'].str.len()>8]
    kel_sample = dfkel.sample().reset_index(drop=True)
    
    kode_kel, nama_kel = kel_sample['kode'][0], kel_sample['nama'][0]
    kode_prov, kode_kab, kode_kec, kode_kel = kode_kel.split('.')
    nama_prov = df[df['kode']==f'{kode_prov}'].iloc[0]['nama']
    nama_kab = df[df['kode']==f'{kode_prov}.{kode_kab}'].iloc[0]['nama']
    nama_kec = df[df['kode']==f'{kode_prov}.{kode_kab}.{kode_kec}'].iloc[0]['nama']

    nama_kab = clean_kab_text(nama_kab)

    dout = {
        'prov':{'kode':kode_prov, 'nama': nama_prov},
        'kab': {'kode': kode_kab, 'nama': nama_kab},
        'kec': {'kode': kode_kec, 'nama': nama_kec},
        'kel': {'kode': kode_kel, 'nama': nama_kel},
    }

    
    return dout


def wilayah_filter(dframe, kode):
    if type(kode) == str:
        dframe = dframe[dframe['kode'].str.startswith(str(kode))]
    elif type(kode) == list:
        frames = [dframe[dframe['kode'].str.startswith(str(kd))] for kd in kode]
        dframe= pd.concat(frames)
    else:
        raise ValueError("Kode value must be string of number or list of string of number!")
    
    return dframe



def alamat():
    pass

def nik(kp, kb, kl, kd, km, ky):
    no_komp = str(random.randint(0, 9999)).zfill(4)
    nik_gen = f'{kp}{kb}{kl}{kd}{km}{ky}{no_komp}'
    return nik_gen

def no_tdp():
    pass

def no_ktp_tdp():
    pass

# ==== Identitas Kendaraan ==== #

def merk():
    pass

def vehicle_type():
    pass

def jenis():
    pass

def model():
    pass

def tahun_pembuatan():
    pass

def isi_silinder():
    pass

def warna():
    pass

def no_rangka_nik_vin():
    pass

def no_mesin():
    pass

def bahan_bakar():
    pass

def harga():
    pass




# ========== data pendukung ============ #

def nomer_formulir():
     pass
 
def nomer_pib():
    pass

def nomer_tpt():
    pass

def nomer_sut():
    pass

def nomer_srut():
    pass
 
 
