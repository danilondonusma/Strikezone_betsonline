
# seeder/main.py
from seeder.config import get_conn
from seeder.utils.helpers import validar_datos_maestros, obtener_ids
from seeder.seeders.users import seed_usuarios, seed_saldos, seed_metodos_pago
from seeder.seeders.events import (
    seed_participantes, seed_eventos, seed_mercados, seed_participante_evento
)
from seeder.seeders.bets import seed_apuestas_y_cuotas, seed_historial_cuotas
from seeder.seeders.transactions import seed_transacciones

def reset_db(cursor):
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    tablas = [
        'HISTORIAL_CUOTA', 'HISTORIAL_APUESTA', 'TRANSACCION',
        'CUOTA', 'APUESTA', 'PARTICIPANTE_EVENTO', 'MERCADO',
        'EVENTO', 'PARTICIPANTES', 'METODO_PAGO', 'SALDO_CUENTA', 'USUARIO'
    ]
    for tabla in tablas:
        cursor.execute(f"TRUNCATE TABLE {tabla}")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    print('  [OK] Tablas limpiadas')

def main():
    conn = get_conn()
    cursor = conn.cursor()
    try:
        print('--- INICIANDO POBLACIÓN DE DATOS ---')
        reset_db(cursor)
        conn.commit()
        validar_datos_maestros()

        seed_usuarios(cursor, n=300)
        conn.commit()
        ids_u = obtener_ids(cursor, 'USUARIO', 'ID_Usuario')

        seed_saldos(cursor, ids_u)
        seed_metodos_pago(cursor, ids_u)
        conn.commit()

        seed_participantes(cursor)
        conn.commit()

        seed_eventos(cursor, n=60)
        conn.commit()
        ids_e = obtener_ids(cursor, 'EVENTO', 'ID_Evento')

        seed_mercados(cursor, ids_e)
        conn.commit()
        ids_m = obtener_ids(cursor, 'MERCADO', 'ID_Mercado')

        seed_participante_evento(cursor, ids_e, ids_m)
        conn.commit()

        seed_apuestas_y_cuotas(cursor, ids_u, ids_e, ids_m, n=500)
        conn.commit()

        ids_c = obtener_ids(cursor, 'CUOTA', 'ID_Cuota')
        seed_historial_cuotas(cursor, ids_c)
        conn.commit()

        ids_ap = obtener_ids(cursor, 'APUESTA', 'ID_Apuesta')
        ids_mp = obtener_ids(cursor, 'METODO_PAGO', 'ID_Metodo_pago')
        seed_transacciones(cursor, ids_u, ids_mp, ids_ap, n=600)
        conn.commit()

        print('--- POBLACIÓN COMPLETADA CON ÉXITO ---')

    except Exception as e:
        conn.rollback()
        print(f'ERROR: {e}')
        raise
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    main()