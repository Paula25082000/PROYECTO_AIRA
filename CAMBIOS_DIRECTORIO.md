# 📁 Cambios de Directorio - Actualización Completada

## ✅ Cambios Realizados

Se han actualizado todos los archivos para funcionar correctamente con la nueva estructura de directorios anidados:

```
C:\Users\IPP\Downloads\Bootcamp\MODULO_3\PROYECTO_AIRA\PROYECTO_AIRA\
```

### Archivos Actualizados:

#### 1. **notebooks/preprocesamiento.ipynb**
Se actualizaron las rutas absolutas en 3 celdas:
- Carga de datos: `AIRAData.csv`
- Exportación de datos limpios: `AIRAData_final.csv`
- Carga y conversión de metadata: `AIRA Metadata.xlsx`

**Antes:** `C:\Users\IPP\Downloads\Bootcamp\MODULO_3\PROYECTO_AIRA\Data\...`  
**Ahora:** `C:\Users\IPP\Downloads\Bootcamp\MODULO_3\PROYECTO_AIRA\PROYECTO_AIRA\Data\...`

#### 2. **notebooks/EDA.ipynb**
Se actualizó la ruta relativa para cargar datos:

**Antes:** `Data/AIRAData_final.csv`  
**Ahora:** `../Data/AIRAData_final.csv` (ruta relativa desde carpeta notebooks)

#### 3. **app/run.bat**
Se agregó cambio automático al directorio de la aplicación:
- El script ahora cambia automáticamente a su propio directorio antes de ejecutar
- Muestra el directorio actual para verificación

## 🚀 Cómo Ejecutar la Aplicación

### Opción 1: Usando run.bat (Recomendado para Windows)

1. Navega a la carpeta de la aplicación:
   ```
   cd C:\Users\IPP\Downloads\Bootcamp\MODULO_3\PROYECTO_AIRA\PROYECTO_AIRA\app
   ```

2. Ejecuta el archivo batch:
   ```
   run.bat
   ```
   O simplemente haz doble clic en `run.bat` desde el explorador de Windows.

### Opción 2: Ejecución Manual

1. Navega a la carpeta de la aplicación:
   ```powershell
   cd C:\Users\IPP\Downloads\Bootcamp\MODULO_3\PROYECTO_AIRA\PROYECTO_AIRA\app
   ```

2. Instala las dependencias (solo la primera vez):
   ```powershell
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```powershell
   streamlit run app.py
   ```

4. La aplicación se abrirá automáticamente en tu navegador en: `http://localhost:8501`

## 📓 Cómo Ejecutar los Notebooks

Los notebooks de Jupyter deben ejecutarse desde su propia carpeta:

1. Navega a la carpeta de notebooks:
   ```powershell
   cd C:\Users\IPP\Downloads\Bootcamp\MODULO_3\PROYECTO_AIRA\PROYECTO_AIRA\notebooks
   ```

2. Ejecuta Jupyter:
   ```powershell
   jupyter notebook
   ```
   
   O si usas VS Code, simplemente abre el notebook y ejecútalo directamente.

## 🔧 Archivos Que NO Necesitan Cambios

Los siguientes archivos ya estaban bien diseñados con rutas relativas y **NO** requirieron cambios:

- ✅ `app/config.py` - Usa `os.path` para rutas relativas
- ✅ `app/app.py` - Usa `Path(__file__).parent` para rutas relativas
- ✅ `app/utils.py` - Importa rutas desde config.py
- ✅ `notebooks/ExplicacionML.ipynb` - Solo contiene markdown, sin código

## 📂 Estructura de Directorios Actual

```
C:\Users\IPP\Downloads\Bootcamp\MODULO_3\PROYECTO_AIRA\PROYECTO_AIRA\
├── .git/                      # Repositorio Git
├── .gitattributes
├── readme.md
├── app/                       # 🎯 Aplicación Streamlit
│   ├── app.py                 # Archivo principal
│   ├── config.py              # Configuración
│   ├── utils.py
│   ├── visualizations.py
│   ├── requirements.txt
│   ├── run.bat                # ⭐ Ejecutar desde aquí
│   ├── INICIO_RAPIDO.md
│   ├── README.md
│   └── components/
│       ├── __init__.py
│       ├── inicio.py
│       ├── origen_datos.py
│       ├── eda.py
│       ├── ml_clustering.py
│       └── conclusiones.py
├── Data/                      # 📊 Datos
│   └── AIRAData_final.csv
├── docs/                      # 📚 Documentación
│   └── EDA.md
└── notebooks/                 # 📓 Jupyter Notebooks
    ├── EDA.ipynb
    ├── ExplicacionML.ipynb
    └── preprocesamiento.ipynb
```

## ✨ Ventajas de los Cambios

1. **Compatibilidad con GitHub**: La estructura anidada es común al crear repos en GitHub
2. **Rutas Relativas**: Los archivos de la app usan rutas relativas, por lo que funcionan en cualquier entorno
3. **Cambio Automático**: El `run.bat` actualizado cambia automáticamente al directorio correcto
4. **Notebooks Actualizados**: Los notebooks pueden ejecutarse correctamente con las nuevas rutas

## 🆘 Solución de Problemas

### Error: "FileNotFoundError: Data/AIRAData_final.csv"
**Causa**: Estás ejecutando la aplicación desde el directorio incorrecto  
**Solución**: Asegúrate de estar en la carpeta `app/` antes de ejecutar:
```powershell
cd C:\Users\IPP\Downloads\Bootcamp\MODULO_3\PROYECTO_AIRA\PROYECTO_AIRA\app
streamlit run app.py
```

### Error en notebooks: "No such file or directory"
**Causa**: El notebook está buscando archivos en la ruta incorrecta  
**Solución**: Los archivos ya están actualizados. Si el error persiste, reinicia el kernel del notebook.

### VS Code muestra el workspace en la raíz incorrecta
**Solución**: Abre la carpeta correcta en VS Code:
- File → Open Folder → Selecciona: `C:\Users\IPP\Downloads\Bootcamp\MODULO_3\PROYECTO_AIRA\PROYECTO_AIRA`

## 📝 Notas Adicionales

- No es necesario modificar ningún archivo de configuración de Git
- Los paths en `.gitignore` siguen siendo válidos
- Todos los imports en Python funcionan correctamente
- La aplicación Streamlit detecta automáticamente su directorio base

---

**¡Todo listo para usar! 🎉**

Si tienes algún problema, verifica que estés en el directorio correcto antes de ejecutar cualquier comando.
