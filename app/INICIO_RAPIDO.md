# 🚀 INICIO RÁPIDO - AIRA

## Opción 1: Ejecución Automática (Windows)

1. Haz doble clic en `run.bat`
2. ¡Listo! La aplicación se abrirá automáticamente

## Opción 2: Ejecución Manual

### Paso 1: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 2: Iniciar la aplicación
```bash
streamlit run app.py
```

### Paso 3: Abrir en navegador
La aplicación se abrirá automáticamente en: `http://localhost:8501`

## ⚡ Comandos Útiles

- **Detener la aplicación**: Presiona `Ctrl + C` en la terminal
- **Reinstalar dependencias**: `pip install -r requirements.txt --force-reinstall`
- **Limpiar caché**: En la app, presiona `C` y luego `Enter`

## 📁 Estructura de Archivos

```
app/
├── app.py                  ⭐ Archivo principal (ejecutar este)
├── config.py              📝 Configuración
├── utils.py               🛠️ Utilidades
├── visualizations.py      📊 Gráficos
├── requirements.txt       📦 Dependencias
├── README.md              📚 Documentación completa
├── run.bat                🚀 Inicio rápido (Windows)
└── pages/                 📂 Módulos de páginas
    ├── inicio.py
    ├── origen_datos.py
    ├── eda.py
    ├── ml_clustering.py
    └── conclusiones.py
```

## 🔧 Solución de Problemas

### Error: "No module named 'streamlit'"
**Solución**: Instala las dependencias con `pip install -r requirements.txt`

### Error: "FileNotFoundError: Data/AIRAData_final.csv"
**Solución**: Verifica que el archivo CSV esté en la carpeta `Data/` un nivel arriba de `app/`

### La aplicación no se abre automáticamente
**Solución**: Abre manualmente en tu navegador: `http://localhost:8501`

### Error de puerto ocupado
**Solución**: Usa un puerto diferente: `streamlit run app.py --server.port 8502`

## 💡 Consejos

- **Rendimiento**: La primera carga puede tardar unos segundos
- **Navegación**: Usa el menú lateral para cambiar de sección
- **Interactividad**: Todos los gráficos son interactivos (zoom, filtrado)
- **Descarga**: Puedes descargar gráficos y tablas usando los botones
- **Actualización**: Los cambios en el código se reflejan automáticamente al guardar

## 📞 Soporte

- Consulta el [README.md](README.md) para documentación completa
- Revisa los comentarios en el código
- Verifica que Python 3.8+ esté instalado: `python --version`

---

**¡Disfruta explorando los datos AIRA! 🏥📊**
