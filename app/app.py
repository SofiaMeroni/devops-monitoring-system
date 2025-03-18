from flask import Flask, Response
import time
import random
import prometheus_client
from prometheus_client import Counter, Histogram, Gauge

# Inicializar la aplicación Flask
app = Flask(__name__)

# Crear métricas Prometheus
REQUEST_COUNT = Counter(
    'app_request_count', 
    'Contador de solicitudes HTTP', 
    ['method', 'endpoint', 'status']
)
REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds', 
    'Tiempo de respuesta de solicitudes HTTP', 
    ['method', 'endpoint']
)
ACTIVE_REQUESTS = Gauge(
    'app_active_requests', 
    'Número de solicitudes activas'
)
MEMORY_USAGE = Gauge(
    'app_memory_usage', 
    'Uso de memoria simulado'
)

@app.route('/')
def home():
    """Endpoint de página principal"""
    ACTIVE_REQUESTS.inc()
    start_time = time.time()
    
    # Simular procesamiento
    time.sleep(random.uniform(0.01, 0.5))
    
    # Simular uso de memoria
    MEMORY_USAGE.set(random.uniform(100, 500))
    
    # Registrar métricas
    REQUEST_COUNT.labels('GET', '/', '200').inc()
    REQUEST_LATENCY.labels('GET', '/').observe(time.time() - start_time)
    ACTIVE_REQUESTS.dec()
    
    return "Aplicación de ejemplo para monitoreo DevOps"

@app.route('/api/data')
def api_data():
    """Endpoint de API de datos"""
    ACTIVE_REQUESTS.inc()
    start_time = time.time()
    
    # Simular procesamiento con latencia variable
    time.sleep(random.uniform(0.1, 0.9))
    
    # Simular uso de memoria
    MEMORY_USAGE.set(random.uniform(200, 800))
    
    # Registrar métricas
    REQUEST_COUNT.labels('GET', '/api/data', '200').inc()
    REQUEST_LATENCY.labels('GET', '/api/data').observe(time.time() - start_time)
    ACTIVE_REQUESTS.dec()
    
    return {"data": "Datos de ejemplo", "timestamp": time.time()}

@app.route('/api/error')
def api_error():
    """Endpoint que ocasionalmente genera errores"""
    ACTIVE_REQUESTS.inc()
    start_time = time.time()
    
    # Simular procesamiento
    time.sleep(random.uniform(0.1, 0.3))
    
    # Simular un error aleatorio (30% de probabilidad)
    if random.random() < 0.3:
        REQUEST_COUNT.labels('GET', '/api/error', '500').inc()
        REQUEST_LATENCY.labels('GET', '/api/error').observe(time.time() - start_time)
        ACTIVE_REQUESTS.dec()
        return "Error interno", 500
    
    # Registrar métricas para solicitudes exitosas
    REQUEST_COUNT.labels('GET', '/api/error', '200').inc()
    REQUEST_LATENCY.labels('GET', '/api/error').observe(time.time() - start_time)
    ACTIVE_REQUESTS.dec()
    
    return "Operación exitosa"

@app.route('/metrics')
def metrics():
    """Endpoint para exponer métricas de Prometheus"""
    return Response(prometheus_client.generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    # Inicializar el servidor en modo desarrollo
    app.run(host='0.0.0.0', port=5000, debug=True)