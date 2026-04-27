# Configuración de Despliegue en Render

## 🔧 Variables de Entorno Requeridas

En el panel de Render, ve a **Settings → Environment** y agrega estas variables:

### Variables Esenciales
```
SECRET_KEY=django-insecure-tu-secret-key-aqui-genera-una-nueva
DEBUG=False
ALLOWED_HOSTS=tu-dominio.onrender.com
```

### Variable de Base de Datos (Render la proporciona automáticamente)
```
DATABASE_URL=postgresql://user:password@host:port/dbname
```

## 🚀 Proceso de Despliegue

1. **Sube los cambios a GitHub**
   ```bash
   git add .
   git commit -m "Fix deployment configuration for Render"
   git push origin main
   ```

2. **Configura las variables de entorno en Render**
   - Ve a tu servicio en Render
   - Settings → Environment → Add Environment Variable
   - Agrega las variables mencionadas arriba

3. **Trigger manual del despliegue**
   - Ve a la pestaña "Events" en Render
   - Click en "Manual Deploy" → "Deploy Latest Commit"

## 🔍 Solución de Problemas

### Error 502 Bad Gateway
Si sigues viendo este error:

1. **Verifica los logs en Render**
   - Ve a la pestaña "Logs" en tu servicio
   - Busca errores de Django o de la base de datos

2. **Variables de entorno incorrectas**
   - Asegúrate que SECRET_KEY esté configurada
   - Verifica que DEBUG=False en producción

3. **Problemas con la base de datos**
   - La variable DATABASE_URL debe ser proporcionada por Render
   - Si usas SQLite, puede haber problemas de permisos

4. **Build script fallido**
   - Revisa que el build.sh se ejecute correctamente
   - Verifica que el super admin se cree sin errores

## 📋 Checklist de Despliegue

- [ ] SECRET_KEY configurada en variables de entorno
- [ ] DEBUG=False en producción
- [ ] ALLOWED_HOSTS incluye tu dominio de Render
- [ ] Build script actualizado
- [ ] Super admin se crea automáticamente
- [ ] Django check --deploy pasa sin errores
- [ ] Login funciona correctamente

## 🛠️ Comandos Útiles

### Generar una nueva SECRET_KEY
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Verificar configuración localmente
```bash
python manage.py check --deploy
```

### Probar el script de super admin
```bash
python scripts/create_superuser_deploy.py
```

## 🔐 Credenciales del Super Admin

- **Username**: `fsuarez120`
- **Email**: `fsuarez120@unab.edu.co`
- **Password**: `Qwerty123456*`

Estas credenciales se crearán automáticamente durante el despliegue.
