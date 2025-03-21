# Sistema de Monitoreo DevOps

## 📊 Visión General

Este proyecto implementa un sistema completo de monitorización de aplicaciones utilizando herramientas modernas de DevOps. Proporciona una solución end-to-end para instrumentar, recolectar y visualizar métricas de una aplicación web, todo containerizado y listo para implementarse con un solo comando.

## 🧩 Componentes

El sistema está compuesto por tres servicios principales:

### 1. Aplicación Flask Instrumentada
- API web con endpoints para demostración (`/`, `/api/data`, `/api/error`)
- Endpoint `/metrics` que expone métricas para Prometheus
- Instrumentación completa con métricas como:
  - Contador de solicitudes HTTP por método, endpoint y código de estado
  - Latencia de respuesta de solicitudes
  - Solicitudes activas en tiempo real
  - Simulación de uso de memoria

### 2. Prometheus
- Recolector y almacenamiento de series temporales
- Configurado para obtener métricas de la aplicación cada 15 segundos
- Punto central para la agregación de datos de monitoreo

### 3. Grafana
- Visualización interactiva de métricas con dashboards preconfigados
- Alertas basadas en umbrales para latencia de solicitudes
- Paneles para todas las métricas clave de la aplicación

## 🔧 Tecnologías Utilizadas

- **Containerización**: Docker, Docker Compose
- **Backend**: Python 3.9, Flask, Gunicorn
- **Monitorización**: Prometheus, Grafana
- **Instrumentación**: prometheus_client para Python
- **CI/CD**: GitHub Actions
- **Pruebas**: Scripts de generación de tráfico para simular carga

## 🚀 Instalación y Uso

### Requisitos Previos
- Docker y Docker Compose
- Git
- Python 3.6+ (solo para scripts de utilidad)

### Configuración Rápida

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/devops-monitoring-system.git
   cd devops-monitoring-system
   ```

2. **Iniciar el sistema**:
   ```bash
   python scripts/setup.py start
   ```

3. **Verificar el estado**:
   ```bash
   python scripts/setup.py status
   ```

4. **Generar tráfico de prueba** (opcional):
   ```bash
   python scripts/load-generator.py --duration 120 --rps 10
   ```

5. **Detener el sistema**:
   ```bash
   python scripts/setup.py stop
   ```

## 🖥️ Acceso a los Servicios

Una vez en funcionamiento, puedes acceder a los servicios en:

- **Aplicación Flask**: [http://localhost:5000](http://localhost:5000)
- **Prometheus**: [http://localhost:9090](http://localhost:9090)
- **Grafana**: [http://localhost:3000](http://localhost:3000)
  - Usuario: `admin`
  - Contraseña: `admin`

## 📈 Métricas y Dashboard

El dashboard de Grafana preconfigurado incluye:

- **Panel de Latencia**: Tiempo promedio de respuesta por endpoint con alertas
- **Tasa de Solicitudes**: Solicitudes por segundo, segregadas por código de estado
- **Solicitudes Activas**: Gauge en tiempo real de solicitudes en proceso
- **Uso de Memoria**: Tendencia de consumo de memoria simulado

## 🔄 Integración Continua

El proyecto incluye un flujo de trabajo de GitHub Actions que:

1. Verifica la sintaxis de Python con Flake8
2. Valida la configuración de Docker Compose
3. Construye las imágenes Docker
4. Está listo para publicar las imágenes en un registro de contenedores (requiere configuración adicional)

## 🛠️ Estructura del Proyecto

```
devops-monitoring-system/
├── app/                      # Aplicación Flask
│   ├── app.py                # Código de la aplicación con métricas
│   ├── Dockerfile            # Instrucciones para construir la imagen
│   └── requirements.txt      # Dependencias de Python
├── prometheus/               # Configuración de Prometheus
│   ├── Dockerfile
│   └── prometheus.yml        # Configuración de recopilación
├── grafana/                  # Configuración de Grafana
│   ├── datasource.yml        # Configuración de fuente de datos
│   └── dashboards/           # Dashboards preconfigados
│       ├── dashboard.yml
│       └── dashboard.json
├── scripts/                  # Scripts de utilidad
│   ├── setup.py              # Script para gestionar el sistema
│   └── load-generator.py     # Generador de tráfico para pruebas
└── docker-compose.yml        # Orquestación de los servicios
```
