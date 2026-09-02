
# seeder/utils/helpers.py
import random
from datetime import date, timedelta, time
from faker import Faker

# --- Faker & Seed ---
fake = Faker('es_CO')
random.seed(42)

# --- Master Data ---
DEPORTES = ['Fútbol', 'Baloncesto', 'Tenis', 'MMA', 'Ciclismo']

LIGAS = {
    'Fútbol':     ['Liga BetPlay', 'Premier League', 'La Liga', 'Champions League'],
    'Baloncesto': ['NBA', 'EuroLeague'],
    'Tenis':      ['ATP Masters', 'Roland Garros', 'Wimbledon'],
    'MMA':        ['UFC', 'Bellator'],
    'Ciclismo':   ['Tour de France', 'Vuelta a España'],
}

TIPO_EVENTO_MAP = {
    'Fútbol':     'PARTIDO',
    'Baloncesto': 'PARTIDO',
    'Tenis':      'TORNEO',
    'MMA':        'COMBATE',
    'Ciclismo':   'CARRERA',
}

EQUIPOS_FUTBOL = [
    'Millonarios', 'América de Cali', 'Atlético Nacional', 'Junior',
    'Santa Fe', 'Deportivo Cali', 'Barcelona SC', 'Boca Juniors',
    'River Plate', 'Real Madrid', 'Barcelona', 'Manchester City',
]

EQUIPOS_BALONCESTO = [
    'Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Chicago Bulls',
    'Real Madrid BC', 'Bayern Munich BC', 'Valencia Basket', 'Olympiakos BC',
]

JUGADORES_TENIS = [
    'Carlos Alcaraz', 'Novak Djokovic', 'Jannik Sinner', 'Daniil Medvedev',
    'Alexander Zverev', 'Holger Rune',
]

LUCHADORES_MMA = [
    'Jon Jones', 'Islam Makhachev', 'Alex Pereira', 'Leon Edwards',
    'Dricus du Plessis', "Sean O'Malley",
]

CICLISTAS = [
    'Egan Bernal', 'Rigoberto Uran', 'Nairo Quintana',
    'Tadej Pogacar', 'Jonas Vingegaard',
]

PARTICIPANTES_POR_DEPORTE = {
    'Fútbol':     (EQUIPOS_FUTBOL,     'EQUIPO'),
    'Baloncesto': (EQUIPOS_BALONCESTO, 'EQUIPO'),
    'Tenis':      (JUGADORES_TENIS,    'DEPORTISTA'),
    'MMA':        (LUCHADORES_MMA,     'DEPORTISTA'),
    'Ciclismo':   (CICLISTAS,          'DEPORTISTA'),
}

TIPOS_MERCADO = [
    'GANADOR', 'TOTAL_ANOTACIONES', 'HANDICAP',
    'AMBOS_ANOTAN', 'RESULTADO_EXACTO',
]

RANGOS_TRANSACCION = {
    'DEPOSITO': (10000,    2000000),
    'RETIRO':   (10000,    1000000),
    'APUESTA':  (1000,     5000000),
    'GANANCIA': (1000,     20000000),
    'AJUSTE':   (-500000,  500000),
}

TIPOS_METODO_PAGO = [
    'TARJETA_CREDITO', 'TARJETA_DEBITO',
    'TRANSFERENCIA', 'BILLETERA_DIGITAL', 'CONSIGNACION_BANCARIA'
]

CIUDADES = [
    'Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena',
    'Bucaramanga', 'Pereira', 'Manizales', 'Santa Marta', 'Cúcuta'
]

GENEROS = ['MASCULINO', 'FEMENINO', 'OTRO']
PESOS_GENERO = [0.62, 0.35, 0.03]

RANGOS_APUESTA = [
    (1000,    5000),
    (5000,    50000),
    (50000,   500000),
    (500000,  5000000),
]
PESOS_APUESTA = [0.30, 0.45, 0.20, 0.05]

# --- Helper Functions ---
def rand_monto_apuesta():
    minv, maxv = random.choices(RANGOS_APUESTA, weights=PESOS_APUESTA)[0]
    return round(random.uniform(minv, maxv), -3)

def validar_datos_maestros():
    deportes = set(DEPORTES)
    assert deportes == set(LIGAS.keys()), \
        f'LIGAS no cubre: {deportes - set(LIGAS.keys())}'
    assert deportes == set(TIPO_EVENTO_MAP.keys()), \
        f'TIPO_EVENTO_MAP no cubre: {deportes - set(TIPO_EVENTO_MAP.keys())}'
    assert deportes == set(PARTICIPANTES_POR_DEPORTE.keys()), \
        f'PARTICIPANTES_POR_DEPORTE no cubre: {deportes - set(PARTICIPANTES_POR_DEPORTE.keys())}'
    print('  [OK] Datos maestros consistentes')

def obtener_ids(cursor, tabla, pk):
    cursor.execute(f'SELECT {pk} FROM {tabla}')
    return [row[0] for row in cursor.fetchall()]