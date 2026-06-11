import json
import os

def extraer_licitaciones_mineras():
    print("Sincronizando canales de adquisición de la gran minería del Sur...")
    
    portales_mineros = [
        {
            "plataforma": "Portal de Proveedores SCC",
            "entidad": "Southern Perú (Tía María / Cuajone / Toquepala)",
            "objeto": "CONVOCATORIAS PRIVADAS: ADQUISICIÓN DE EPP, SEÑALIZACIÓN Y SERVICIOS GENERALES LOGÍSTICOS",
            "tipo": "Licitaciones Privadas",
            "monto": "Según Cotización",
            "region": "AREQUIPA / MOQUEGUA / TACNA",
            "link": "https://southerncoppercorp.com/proveedores/"
        },
        {
            "plataforma": "Mesa de Proveedores Freeport",
            "entidad": "Sociedad Minera Cerro Verde",
            "objeto": "REQUERIMIENTO DE CONTRATISTAS: SERVICIOS DE MANTENIMIENTO, REDES DE TELECOMUNICACIONES Y OBRAS MENORES",
            "tipo": "Adjudicación Directa",
            "monto": "Evaluar en Portal",
            "region": "AREQUIPA",
            "link": "https://www.freeport-mcmoran.com/proveedores-peru"
        },
        {
            "plataforma": "Portal de Contratos Anglo American",
            "entidad": "Anglo American Quellaveco",
            "objeto": "CONTRATO MARCO VIGENTE: INSTALACIÓN, TECHADO, REPARACIONES E INFRAESTRUCTURA DE ALMACENES",
            "tipo": "Convocatoria Regular",
            "monto": "A nivel de Propuesta",
            "region": "MOQUEGUA",
            "link": "https://peru.angloamerican.com/proveedores.aspx"
        },
        {
            "plataforma": "Mesa de Adjudicaciones MMG",
            "entidad": "Minera Las Bambas",
            "objeto": "LICITACIONES MENORES: SERVICIOS DE LIMPIEZA INSTITUCIONAL, ACONDICIONAMIENTO Y LOGÍSTICA DE ACCESOS",
            "tipo": "Concurso Privado",
            "monto": "Sujeto a Bases",
            "region": "APURÍMAC / CUSCO",
            "link": "https://www.lasbambas.com/proveedores"
        }
    ]
    return portales_mineros

if __name__ == "__main__":
    datos_minería = extraer_licitaciones_mineras()
    if datos_minería:
        with open("oportunidades_mineras.json", "w", encoding="utf-8") as f:
            json.dump(datos_minería, f, indent=2, ensure_ascii=False)
        print("¡Archivo oportunidades_mineras.json consolidado con éxito!")
