#!/usr/bin/env python3
import requests
import time
import random
import threading
import argparse
from datetime import datetime

# URLs de los endpoints
BASE_URL = "http://localhost:5000"
ENDPOINTS = [
    "/",
    "/api/data",
    "/api/error"
]

def send_request(endpoint):
    """Envía una solicitud HTTP al endpoint especificado"""
    url = f"{BASE_URL}{endpoint}"
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        duration = time.time() - start_time
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = response.status_code
        
        print(f"[{timestamp}] {url} - Status: {status} - Tiempo: {duration:.4f}s")
        return True
    except requests.RequestException as e:
        print(f"Error al acceder a {url}: {e}")
        return False

def request_worker(endpoint, success_counter, fail_counter):
    """Ejecuta una solicitud y actualiza los contadores globales."""
    if send_request(endpoint):
        success_counter.append(1)  # Usamos una lista para mantener la referencia
    else:
        fail_counter.append(1)

def generate_traffic(duration, requests_per_second):
    """Genera tráfico a la aplicación durante el tiempo especificado"""
    start_time = time.time()
    end_time = start_time + duration
    
    successful_requests = []
    failed_requests = []
    
    print(f"Generando tráfico: {requests_per_second} solicitudes/segundo durante {duration} segundos")
    
    while time.time() < end_time:
        threads = []
        for _ in range(requests_per_second):
            if time.time() >= end_time:
                break
                
            # Seleccionar un endpoint aleatorio
            endpoint = random.choice(ENDPOINTS)
            
            # Crear un hilo para enviar la solicitud
            thread = threading.Thread(target=request_worker, args=(endpoint, successful_requests, failed_requests))
            threads.append(thread)
            thread.start()
        
        # Esperar a que todos los hilos terminen
        for thread in threads:
            thread.join()
        
        # Esperar para mantener el ritmo de solicitudes por segundo
        time_to_sleep = 1 - (time.time() % 1)
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)
    
    total_duration = time.time() - start_time
    print(f"\nResumen:")
    print(f"Duración total: {total_duration:.2f} segundos")
    print(f"Solicitudes exitosas: {len(successful_requests)}")
    print(f"Solicitudes fallidas: {len(failed_requests)}")
    print(f"Tasa de solicitudes: {(len(successful_requests) + len(failed_requests)) / total_duration:.2f} solicitudes/segundo")

def main():
    parser = argparse.ArgumentParser(description="Generador de tráfico para la aplicación de monitoreo")
    parser.add_argument("--duration", type=int, default=60, help="Duración de la prueba en segundos (default: 60)")
    parser.add_argument("--rps", type=int, default=5, help="Solicitudes por segundo (default: 5)")
    args = parser.parse_args()
    
    # Verificar que la aplicación esté en funcionamiento
    try:
        response = requests.get(f"{BASE_URL}/metrics", timeout=5)
        if response.status_code != 200:
            print(f"La aplicación no está respondiendo correctamente. Código de estado: {response.status_code}")
            return
    except requests.RequestException:
        print("No se puede conectar a la aplicación. Asegúrate de que esté en funcionamiento.")
        return
    
    generate_traffic(args.duration, args.rps)

if __name__ == "__main__":
    main()
