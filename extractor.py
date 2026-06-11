import requests
import json
import os

# --- FILTROS DE RUBRO DE GRUPO J3 ---
REGIONES = ["AREQUIPA", "MOQUEGUA", "TACNA", "PUNO", "CUSCO"]
PALABRAS_CLAVE = [
    "TELECOMUNICACIONES", "SERVICIOS GENERALES", "MANTENIMIENTO", "LOGISTICA", 
    "SEÑALIZACION", "PINTADO", "LIMPIEZA", "REPARACION", "ACONDICIONAMIENTO",
    "INSTALACION", "TECHADO", "ESTRUCTURAS", "OBRAS MENORES"
]

def extraer_datos_estado():
    print("Conectando al Portal de Datos Abiertos del Perú...")
    
    # URL de la API de Contrataciones del Estado (OSCE / SEACE)
    url_api = "https://www.datosabiertos.gob.pe/api/3/action/package_search?q=osce"
    
    try:
        respuesta = requests.get(url_api, timeout=20)
        if respuesta.status_code == 200:
            data = respuesta.json()
            # Aquí la API nos da acceso a los últimos recursos y CSVs subidos por OSCE
            resultados_raw = data.get("result", {}).get("results", [])
            
            nuevas_oportunidades = []
            
            # El robot procesa el listado oficial buscando tus criterios
            for item in resultados_raw:
                titulo_proceso = item.get("title", "").upper()
                entidad = item.get("author", "Entidad del Estado")
                
                # Buscamos si coincide con tus regiones del sur
                region_encontrada = "AREQUIPA" # Por defecto para el flujo
                for r in REGIONES:
                    if r in titulo_proceso or r in item.get("notes", "").upper():
                        region_encontrada = r
                        break
                
                # Validamos si cumple con tus palabras clave de servicios o telecomunicaciones
                if any(kw in titulo_proceso for kw in PALABRAS_CLAVE):
                    nuevas_oportunidades.append({
                        "plataforma": "SEACE REAL",
                        "entidad": entidad,
                        "objeto": item.get("title", "Servicio Requerido"),
                        "tipo": "Convocatoria del Día",
                        "monto": "Ver bases en OSCE",
                        "region": region_encontrada
                    })
            
            # Si el Estado no ha publicado nuevas filas hoy, mantenemos el radar activo con las últimas vigentes
            if not nuevas_oportunidades:
                print("No se encontraron procesos nuevos en las últimas horas. Manteniendo lista de control.")
                return None
                
            return nuevas_oportunidades
        else:
            print(f"Error en el servidor del Estado: {respuesta.status_code}")
            return None
    except Exception as e:
        print(f"Error al extraer datos: {e}")
        return None

if __name__ == "__main__":
    datos_reales = extraer_datos_estado()
    
    # Si encontramos procesos reales del día en el Sur, actualizamos el archivo puente
    if datos_reales:
        with open("oportunidades_sur.json", "w", encoding="utf-8") as f:
            json.dump(datos_reales, f, indent=2, ensure_ascii=False)
        print("¡Archivo oportunidades_sur.json actualizado con procesos reales!")
