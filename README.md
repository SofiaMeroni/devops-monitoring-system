# Sistema de Monitoreo DevOps

Este repositorio contiene un sistema completo de monitoreo de aplicaciones utilizando herramientas DevOps modernas. El proyecto implementa un stack de monitoreo que incluye:

- **Aplicación Flask** con métricas instrumentadas
- **Prometheus** para recolección y almacenamiento de métricas
- **Grafana** para visualización y alertas

## Arquitectura

El sistema está compuesto por tres componentes principales:

1. **Aplicación Flask**: Una API web simple que expone métricas de Prometheus.
2. **Prometheus**: Recopila métricas de la aplicación y las almacena.
3. **Grafana**: Visualiza las métricas recopiladas en dashboards interactivos.

![Arquitectura del Sistema](https://raw.githubusercontent.com/prometheus/prometheus/main/documentation/images/architecture.svg)

## Métricas Monitorizadas

La aplicación Flask instrumentada proporciona las siguientes métricas:

- **Contador de solicitudes**: Total de solicitudes HTTP por método, endpoint y código de estado
- **Latencia de solicitudes**: Tiempo de respuesta de las solicitudes HTTP
- **Solicitudes activas**: Número de solicitudes siendo procesadas en un momento dado
- **Uso de memoria**: Simulación de uso de memoria de la aplicación

## Requisitos previos

- Docker
- Docker Compose
- Python 3.6+

## Instalación y Uso

### Configuración inicial

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/devops-monitoring-system.git
   cd devops-monitoring-system
   ```

2. Ejecuta el script de configuración:
   ```
   python scripts/setup.py start
   ```

### Acceso a los servicios

Una vez iniciado, los servicios estarán disponibles en:

- **Aplicación Flask**: http://localhost:5000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (usuario: admin, contraseña: admin)

### Comandos útiles

- **Iniciar el sistema**: `python scripts/setup.py start`
- **Detener el sistema**: `python scripts/setup.py stop`
- **Verificar estado**: `python scripts/setup.py status`

## Implementación CI/CD

Este proyecto incluye un flujo de trabajo de GitHub Actions que realiza:

1. Verificación de sintaxis de Python
2. Validación de la configuración de Docker Compose
3. Construcción de imágenes Docker
4. (Preparado para) Publicación de imágenes a registro de contenedores

## Personalización

Para personalizar este sistema:

1. Modifica `app/app.py` para ajustar las métricas que deseas recopilar
2. Actualiza `prometheus/prometheus.yml` para cambiar la configuración de recopilación
3. Modifica o agrega dashboards en `grafana/dashboards/`

4. borrar