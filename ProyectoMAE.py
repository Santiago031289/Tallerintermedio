"""
===============================================================
🌎 INFORME DEL ANÁLISIS DE TEMPERATURA – ECUADOR / GLOBAL
===============================================================

Autor: Santiago Jumbo
Fecha: 2025-10-18
Proyecto: Análisis de temperatura 2m (ERA5 / NetCDF)
Archivo principal: analisis_ecuador.py

---------------------------------------------------------------
1️⃣ OBJETIVO
---------------------------------------------------------------
Este script realiza el análisis automatizado de datos climáticos
de temperatura superficial o del aire provenientes de archivos
NetCDF (como los productos ERA5 del servicio Copernicus).

El objetivo es identificar y visualizar el comportamiento térmico
promedio de la región ecuatoriana o, en caso de ausencia de datos,
extender el análisis a la región global disponible.

---------------------------------------------------------------
2️⃣ DESCRIPCIÓN DEL PROCESO
---------------------------------------------------------------
El código ejecuta las siguientes etapas:

🟩 *Lectura y procesamiento del archivo NetCDF*
    - Detección automática de la variable principal.
    - Conversión de Kelvin a °C (si corresponde).
    - Ajuste de coordenadas de longitud (0–360 → -180–180).

🟦 *Selección de región de análisis (Ecuador o fallback global)*
    - Latitud: -6° a 3° 
    - Longitud: -92° a -74°
    - Si no se encuentran datos válidos, se selecciona 
      automáticamente la región con valores reales más cercanos.

🟨 *Cálculo estadístico y visualización*
    - Promedio, máximo y mínimo de temperatura.
    - Mapa promedio espacial (usando Cartopy y CMOcean).
    - Serie temporal del promedio (si existe dimensión temporal).

🟧 *Exportación automática*
    - `mapa_promedio.png` → mapa de distribución térmica.
    - `serie_temporal.png` → serie temporal del promedio.
    - `estadisticas_ecuador.csv` → tabla de resumen numérico.

---------------------------------------------------------------
3️⃣ RESULTADOS ESPERADOS
---------------------------------------------------------------
El análisis genera representaciones visuales del patrón térmico
en la región ecuatorial, útiles para:

 Evaluación de variabilidad térmica.
 Identificación de anomalías y gradientes.
 Uso educativo o de monitoreo ambiental.
 Incorporación en informes, dashboards o visores geoespaciales.

---------------------------------------------------------------
4️⃣ RECOMENDACIONES
---------------------------------------------------------------
- Asegurar que los archivos .nc contengan variables válidas 
  (ej. `t2m`, `sst
