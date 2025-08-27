import pandas as pd
import json

def convert_to_number(value):
    """Convertir cadena a número flotante reemplazando comas por puntos. Verifica si el valor es una cadena."""
    if isinstance(value, str):  # Verificar si el valor es una cadena
        try:
            return float(value.replace(',', '.'))
        except ValueError:
            return value  # Devuelve el valor original si no puede convertirlo
    return value  # Devuelve el valor original si no es una cadena

try:
    # Cargar el archivo CSV con el delimitador adecuado (punto y coma en este caso)
    df = pd.read_csv('./../Segundo periodo/consolidadoNotas2p2Bb.csv', delimiter=';', on_bad_lines='warn')
    
    # Limpiar nombres de columnas para eliminar espacios extra
    df.columns = df.columns.str.strip()
    
    # Verificar los nombres de las columnas
    print("Columnas en el DataFrame después de limpiar:", df.columns.tolist())

    # Convertir las columnas a texto (si existen en el archivo)
    columnas_a_convertir = [
        'grupo', 'codigo', 'nombre', 'periodo','acumulado',
        'observaciones_ciencias_naturales', 'observaciones_fisica', 'observaciones_quimica', 
        'observaciones_ciencias_politicas_economicas', 'observaciones_ciencias_sociales',
        'observaciones_civica_y_constitucion', 'observaciones_educacion_artistica',
        'observaciones_educacion_cristiana', 'observaciones_educacion_etica', 
        'observaciones_educacion_fisica', 'observaciones_filosofia', 
        'observaciones_idioma_extranjero', 'observaciones_lengua_castellana', 
        'observaciones_matematicas', 'observaciones_tecnologia',
        'metas_ciencias_naturales', 'metas_fisica', 'metas_quimica', 
        'metas_ciencias_politicas_economicas', 'metas_ciencias_sociales',
        'metas_civica_y_constitucion', 'metas_educacion_artistica', 
        'metas_educacion_cristiana', 'metas_educacion_etica', 
        'metas_educacion_fisica', 'metas_filosofia', 'metas_idioma_extranjero', 
        'metas_lengua_castellana', 'metas_matematicas', 'metas_tecnologia',
        'rep_eva_ciencias_naturales', 'rep_eva_fisica', 'rep_eva_quimica', 
        'rep_eva_ciencias_politicas_economicas', 'rep_eva_ciencias_sociales', 
        'rep_eva_civica_y_constitucion', 'rep_eva_educacion_artistica', 
        'rep_eva_educacion_cristiana', 'rep_eva_educacion_etica', 
        'rep_eva_educacion_fisica', 'rep_eva_filosofia', 
        'rep_eva_idioma_extranjero', 'rep_eva_lengua_castellana', 
        'rep_eva_matematicas', 'rep_eva_tecnologia'
    ]

    for col in columnas_a_convertir:
        if col in df.columns:
            df[col] = df[col].astype(str)

    # Convertir las columnas numéricas (si existen) a números flotantes
    columnas_numericas = [
        'puesto', 'promedio', 'ciencias_naturales', 'fisica', 'quimica', 
        'ciencias_politicas_economicas', 'ciencias_sociales', 'civica_y_constitucion', 
        'educacion_artistica', 'educacion_cristiana', 'educacion_etica', 
        'educacion_fisica', 'filosofia', 'idioma_extranjero', 'lengua_castellana', 
        'matematicas', 'tecnologia'
    ]

    for col in columnas_numericas:
        if col in df.columns:
            df[col] = df[col].apply(convert_to_number)

    # Convertir el DataFrame a JSON (sin secuencias de escape)
    data_json = df.to_json(orient='records', lines=False, force_ascii=False)

    # Guardar el archivo JSON en UTF-8
    with open('CONSOLIDADO_2p2Bb.json', 'w', encoding='utf-8') as json_file:
        json.dump(json.loads(data_json), json_file, ensure_ascii=False, indent=4)

except pd.errors.ParserError as e:
    print(f"Error al analizar el archivo CSV: {e}")
except Exception as e:
    print(f"Se produjo un error: {e}")
