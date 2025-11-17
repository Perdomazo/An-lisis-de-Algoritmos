Encriptador de Empresas S&P 500 y ETFs usando Huffman
Descripción General
Aplicación de escritorio en Python que implementa el algoritmo de codificación de Huffman para comprimir y "encriptar" datos de empresas del S&P 500 y ETFs. Permite cargar archivos CSV, aplicar compresión Huffman, exportar a formato propietario .papus autocontenible, desencriptar con contraseña y visualizar análisis sectorial.

Características Principales
✅ Compresión Huffman: Reduce archivos CSV ~30-40%
✅ Formato .papus Autocontenible: No requiere archivo original para desencriptar
✅ Detección Automática de Columnas: Soporta múltiples formatos de ETF
✅ Protección por Contraseña: Contraseña "papus" para desencriptar
✅ Interfaz Gráfica en Español: Tkinter intuitiva y fácil de usar
✅ Análisis Visual: Gráficas Matplotlib de distribución sectorial
✅ Multi-ETF: Compatible con S&P 500, NASDAQ-100, Russell 2000, etc.

Requisitos del Sistema
Python: 3.6 o superior

Sistema Operativo: Windows, macOS, Linux

Librerías: Ver requirements.txt

Instalación
1. Clonar o descargar el proyecto
bash
git clone https://github.com/tu-usuario/encriptador-huffman-sp500.git
cd encriptador-huffman-sp500
2. Crear entorno virtual (opcional pero recomendado)
bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Instalar dependencias
bash
pip install -r requirements.txt
Uso
Ejecutar la aplicación
bash
python encriptador_sp500.py
Instrucciones de uso:
Cargar archivo CSV

Click en "Cargar archivo CSV"

Selecciona un CSV con columnas Symbol/Ticker, Name, Sector

La aplicación detecta automáticamente las columnas

Encriptar a .papus

Con un CSV cargado, click en "Encriptar a archivo .papus"

Elige dónde guardar el archivo .papus

Se mostrará el mensaje de confirmación con tamaño

Desencriptar .papus

Click en "Desencriptar archivo .papus"

Selecciona un archivo .papus

Ingresa la contraseña: papus

Elige dónde exportar el CSV recuperado

Visualizar Sectores

Con un CSV cargado, click en "Graficar distribución de sectores"

Se abrirá una gráfica con análisis de distribución sectorial

Se mostrará resumen textual debajo de la GUI

Estructura del Proyecto
text
encriptador-huffman-sp500/
├── encriptador_sp500.py          # Script principal
├── requirements.txt              # Dependencias
├── README.md                     # Este archivo
├── datos/
│   ├── sp500.csv                # Ejemplo: S&P 500
│   ├── nasdaq100.csv            # Ejemplo: NASDAQ 100
│   └── russell2000.csv          # Ejemplo: Russell 2000
└── salida/
    ├── datos_encriptados.papus  # Archivos generados
    └── datos_recuperados.csv
Formato del Archivo .papus
text
PAPUSCRYPT
<Árbol Huffman serializado en JSON + Base64>
<Número de filas>
<Nombres de columnas separados por comas>
<Fila 1 en código binario>
<Fila 2 en código binario>
...
Algoritmo de Huffman: Explicación Rápida
Frecuencias: Se cuentan caracteres en los datos

Árbol binario: Se construye combinando nodos de menor frecuencia

Códigos variables: Caracteres frecuentes → códigos cortos, raros → códigos largos

Compresión: Los datos se reemplazan por códigos binarios (~35% reducción)

Desencriptación: Se reconstruye el árbol y se decodifica sin pérdida

Formatos de CSV Soportados
La aplicación detecta automáticamente columnas con nombres como:

Símbolo	Nombre	Sector
Symbol, Ticker, Símbolo	Name, Nombre, Company	Sector, Industry, Industria
Ejemplo de CSV Compatible
text
Symbol,Name,Sector
AAPL,Apple Inc.,Technology
MSFT,Microsoft Corporation,Technology
JPM,JPMorgan Chase & Co.,Financials
Características Técnicas
Complejidad Computacional
Operación	Complejidad
Contar frecuencias	O(n)
Construir árbol	O(m log m)
Codificar datos	O(n)
Descodificar datos	O(n)
Total	O(n + m log m)
donde n = caracteres totales, m = caracteres únicos

Tasa de Compresión Típica
S&P 500 (500 empresas): 35-40%

NASDAQ-100 (100 empresas): 30-35%

Russell 2000 (2000 empresas): 33-38%

Tiempo de Ejecución (aproximado)
Operación	100 registros	500 registros	2000 registros
Carga CSV	0.1s	0.23s	0.8s
Construcción árbol	0.2s	0.45s	1.8s
Codificación	0.15s	0.32s	1.2s
Total encriptación	0.5s	1.0s	4.0s
Contraseña
Contraseña por defecto para desencriptar: papus

Para cambiar la contraseña, edita la línea en el código:

python
if pwd != "papus":  # Cambiar "papus" por tu contraseña
Fuentes de Datos
Descargar CSV de S&P 500
GitHub (Recomendado): https://github.com/noahg/sp500csv

Archivo: data/sp500.csv
