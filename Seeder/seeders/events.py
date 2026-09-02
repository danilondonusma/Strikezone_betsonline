
# seeder/seeders/events.py
import random
from datetime import date
from ..utils.helpers import (
    DEPORTES, TIPO_EVENTO_MAP, LIGAS, PARTICIPANTES_POR_DEPORTE,
    TIPOS_MERCADO, fake
)

def seed_participantes(cursor):
    sql = '''INSERT INTO PARTICIPANTES (Nombre, Tipo) VALUES (%s, %s)'''
    todos = set()
    for deporte, (lista, tipo) in PARTICIPANTES_POR_DEPORTE.items():
        for nombre in lista:
            todos.add((nombre[:20], tipo))
    cursor.executemany(sql, list(todos))
    print(f'  [OK] {len(todos)} participantes insertados')

def seed_eventos(cursor, n=60):
    sql = '''
        INSERT INTO EVENTO (Deporte, Tipo_Evento, Fecha, Liga_torneo, Resultado)
        VALUES (%s, %s, %s, %s, %s)
    '''

    def rand_resultado(deporte):
        if deporte in ('Fútbol', 'Baloncesto'):
            return f'{random.randint(0,4)}-{random.randint(0,4)}'
        elif deporte == 'Tenis':
            return f'{random.randint(0,3)}-{random.randint(0,3)}'
        elif deporte == 'MMA':
            return random.choice(['KO R1', 'Decisión unánime', 'Sumisión R2', 'TKO R3'])
        elif deporte == 'Ciclismo':
            return random.choice(['Etapa 1', 'Etapa 2', 'Etapa 3'])

    for _ in range(n):
        dep   = random.choice(DEPORTES)
        tipo  = TIPO_EVENTO_MAP[dep]
        liga  = random.choice(LIGAS[dep])
        fecha = fake.date_between(start_date='-6m', end_date='+1m')
        res   = rand_resultado(deporte=dep) if fecha <= date.today() else None
        cursor.execute(sql, (dep, tipo, fecha, liga, res))
    print(f'  [OK] {n} eventos insertados')

def seed_mercados(cursor, ids_evento):
    sql = '''
        INSERT INTO MERCADO (ID_Evento, Tipo_mercado, Cuota_actual)
        VALUES (%s, %s, %s)
    '''
    for eid in ids_evento:
        for tipo in random.sample(TIPOS_MERCADO, k=random.randint(2, 3)):
            cuota = round(random.uniform(1.20, 10.00), 2)
            cursor.execute(sql, (eid, tipo, cuota))
    print('  [OK] Mercados insertados')

def seed_participante_evento(cursor, ids_evento, ids_mercado):
    sql = '''
        INSERT INTO PARTICIPANTE_EVENTO
            (ID_Evento, ID_Mercado, ID_Participantes)
        VALUES (%s, %s, %s)
    '''
    for eid in ids_evento:
        cursor.execute("SELECT Deporte FROM EVENTO WHERE ID_Evento=%s", (eid,))
        row = cursor.fetchone()
        if not row:
            continue
        deporte = row[0]

        if deporte not in PARTICIPANTES_POR_DEPORTE:
            continue
        lista, tipo = PARTICIPANTES_POR_DEPORTE[deporte]

        cursor.execute(
            "SELECT ID_Participantes FROM PARTICIPANTES WHERE Tipo=%s AND Nombre IN ({})".format(
                ','.join(['%s'] * len(lista))
            ),
            (tipo, *[n[:20] for n in lista])
        )
        ids_correctos = [r[0] for r in cursor.fetchall()]

        if len(ids_correctos) < 2:
            continue

        mid = random.choice(ids_mercado)
        for pid in random.sample(ids_correctos, 2):
            cursor.execute(sql, (eid, mid, pid))

    print('  [OK] Participante_Evento insertados con consistencia por deporte')