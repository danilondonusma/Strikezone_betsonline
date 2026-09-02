
# seeder/seeders/users.py
import random
from datetime import timedelta, date
from ..utils.helpers import fake, CIUDADES, GENEROS, PESOS_GENERO, TIPOS_METODO_PAGO

def seed_usuarios(cursor, n=300):
    estados_kyc = ['PENDIENTE', 'VERIFICADO', 'RECHAZADO']
    pesos_kyc   = [0.2, 0.7, 0.1]

    sql = '''
        INSERT INTO USUARIO
            (Nombre, Apellido, Email, Numero_telefono,
             Direccion, Fecha_registro, Estado_KYC,
             Ciudad, Genero, Fecha_nacimiento)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    for _ in range(n):
        nombre   = fake.first_name()
        apellido = fake.last_name()
        email    = fake.unique.email()
        tel      = fake.phone_number()[:20]
        dir_     = fake.address()[:100]
        fecha    = fake.date_between(start_date='-3y', end_date='today')
        estado   = random.choices(estados_kyc, weights=pesos_kyc)[0]
        ciudad   = random.choice(CIUDADES)
        genero   = random.choices(GENEROS, weights=PESOS_GENERO)[0]
        fecha_max_nac = fecha - timedelta(days=18*365)
        fecha_min_nac = date.today() - timedelta(days=70*365)
        fecha_nacimiento = fake.date_between(
            start_date=fecha_min_nac,
            end_date=fecha_max_nac
        )

        cursor.execute(sql, (nombre, apellido, email, tel, dir_,
                             fecha, estado, ciudad, genero, fecha_nacimiento))
    print(f'  [OK] {n} usuarios insertados')

def seed_saldos(cursor, ids_usuario):
    sql = '''INSERT INTO SALDO_CUENTA (ID_Usuario, Saldo_disponible)
             VALUES (%s, %s)'''
    for uid in ids_usuario:
        saldo = round(random.uniform(10000, 2000000), -3)
        cursor.execute(sql, (uid, saldo))
    print(f'  [OK] {len(ids_usuario)} saldos insertados')

def seed_metodos_pago(cursor, ids_usuario):
    sql = '''INSERT INTO METODO_PAGO (ID_Usuario, Tipo_pago)
             VALUES (%s, %s)'''
    for uid in ids_usuario:
        tipo = random.choice(TIPOS_METODO_PAGO)
        cursor.execute(sql, (uid, tipo))
    print('  [OK] Métodos de pago insertados')