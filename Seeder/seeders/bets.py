
# seeder/seeders/bets.py
import random
from datetime import time
from ..utils.helpers import (
    PARTICIPANTES_POR_DEPORTE, CIUDADES, rand_monto_apuesta, fake
)

def seed_apuestas_y_cuotas(cursor, ids_usuario, ids_evento, ids_mercado, n=500):
    estados = ['PENDIENTE', 'GANADA', 'PERDIDA', 'ANULADA']
    pesos_e = [0.10, 0.40, 0.45, 0.05]

    sql_ap = '''
        INSERT INTO APUESTA
            (ID_Usuario, ID_Evento, ID_Mercado, Valor_apostado,
             Estado, ID_Participantes, Fecha_hora, Ciudad)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    sql_cu = '''
        INSERT INTO CUOTA (ID_Mercado, ID_Apuesta, Valor_cuota)
        VALUES (%s, %s, %s)
    '''
    for _ in range(n):
        uid    = random.choice(ids_usuario)
        eid    = random.choice(ids_evento)
        mid    = random.choice(ids_mercado)
        monto  = rand_monto_apuesta()
        estado = random.choices(estados, weights=pesos_e)[0]
        ciudad = random.choice(CIUDADES)

        fecha_hora = fake.date_time_between(start_date='-6m', end_date='now')

        cursor.execute("SELECT Deporte FROM EVENTO WHERE ID_Evento=%s", (eid,))
        row = cursor.fetchone()
        id_part = None
        if row:
            deporte = row[0]
            if deporte in PARTICIPANTES_POR_DEPORTE:
                lista, tipo = PARTICIPANTES_POR_DEPORTE[deporte]
                cursor.execute(
                    "SELECT ID_Participantes FROM PARTICIPANTES WHERE Tipo=%s AND Nombre IN ({})".format(
                        ','.join(['%s'] * len(lista))
                    ),
                    (tipo, *[n[:20] for n in lista])
                )
                ids_correctos = [r[0] for r in cursor.fetchall()]
                if ids_correctos:
                    id_part = random.choice(ids_correctos)

        cursor.execute(sql_ap, (uid, eid, mid, monto,
                                estado, id_part, fecha_hora, ciudad))
        ap_id = cursor.lastrowid
        cuota = round(random.uniform(1.10, 10.00), 2)
        cursor.execute(sql_cu, (mid, ap_id, cuota))

    print(f'  [OK] {n} apuestas + cuotas insertadas')

def seed_historial_cuotas(cursor, ids_cuota):
    sql = '''
        INSERT INTO HISTORIAL_CUOTA
            (ID_Cuota, Cuota_anterior, Cuota_nueva, Fecha, Hora)
        VALUES (%s, %s, %s, %s, %s)
    '''
    for cid in ids_cuota:
        num_cambios  = random.randint(1, 5)
        cuota_actual = round(random.uniform(1.10, 10.00), 2)
        for _ in range(num_cambios):
            cuota_ant = cuota_actual
            delta     = round(random.uniform(-0.5, 0.5), 2)
            cuota_nva = max(1.01, round(cuota_actual + delta, 2))
            fecha     = fake.date_between(start_date='-3m', end_date='today')
            hora      = time(random.randint(0, 23), random.randint(0, 59))
            cursor.execute(sql, (cid, cuota_ant, cuota_nva, fecha, hora))
            cuota_actual = cuota_nva
    print('  [OK] Historial de cuotas insertado')