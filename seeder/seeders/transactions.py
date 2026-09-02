
# seeder/seeders/transactions.py
import random
from datetime import time
from ..utils.helpers import RANGOS_TRANSACCION, fake

def seed_transacciones(cursor, ids_usuario, ids_metodo, ids_apuesta, n=600):
    tipos   = ['DEPOSITO', 'RETIRO', 'APUESTA', 'GANANCIA', 'AJUSTE']
    pesos_t = [0.35,        0.20,     0.25,      0.10,       0.10]
    sql = '''
        INSERT INTO TRANSACCION
            (ID_Usuario, ID_Apuesta, ID_Metodo_pago,
             Tipo_transaccion, Fecha, Hora, Valor)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    omitidos = 0

    for _ in range(n):
        uid   = random.choice(ids_usuario)
        tipo  = random.choices(tipos, weights=pesos_t)[0]

        if tipo in ('RETIRO', 'APUESTA'):
            cursor.execute(
                "SELECT Saldo_disponible FROM SALDO_CUENTA WHERE ID_Usuario=%s", (uid,))
            row   = cursor.fetchone()
            saldo = row[0] if row else 0
            if saldo <= 0:
                omitidos += 1
                print(f"  [SI] Saldo insuficiente — usuario {uid} | saldo: ${saldo:,.0f} COP | tipo: {tipo}")
                continue

        ap_id = (random.choice(ids_apuesta)
                 if tipo in ('APUESTA', 'GANANCIA') else None)
        mid   = random.choice(ids_metodo)
        fecha = fake.date_between(start_date='-1y', end_date='today')
        hora  = time(random.randint(0, 23), random.randint(0, 59))
        minv, maxv = RANGOS_TRANSACCION[tipo]
        valor = round(random.uniform(minv, maxv), -3)
        cursor.execute(sql, (uid, ap_id, mid, tipo, fecha, hora, valor))

    print(f'  [OK] {n} transacciones procesadas — {omitidos} omitidas por saldo insuficiente')