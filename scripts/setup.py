import os
import subprocess
import sys
import time

def check_docker_installed():
    """Verifica si Docker está instalado"""
    try:
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE)
        print("✅ Docker está instalado")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Docker no está instalado. Por favor, instala Docker antes de continuar.")
        return False

def check_docker_compose_installed():
    """Verifica si Docker Compose está instalado"""
    try:
        subprocess.run(["docker-compose", "--version"], check=True, stdout=subprocess.PIPE)
        print("✅ Docker Compose está instalado")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Docker Compose no está instalado. Por favor, instala Docker Compose antes de continuar.")
        return False

def start_monitoring_system():
    """Inicia el sistema de monitoreo"""
    print("🚀 Iniciando sistema de monitoreo...")
    try:
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        print("✅ Sistema de monitoreo iniciado correctamente")
        
        print("\n📊 Servicios disponibles:")
        print("  - Aplicación Flask: http://localhost:5000")
        print("  - Prometheus: http://localhost:9090")
        print("  - Grafana: http://localhost:3000 (usuario: admin, contraseña: admin)")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al iniciar el sistema: {e}")
        return False

def stop_monitoring_system():
    """Detiene el sistema de monitoreo"""
    print("🛑 Deteniendo sistema de monitoreo...")
    try:
        subprocess.run(["docker-compose", "down"], check=True)
        print("✅ Sistema de monitoreo detenido correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al detener el sistema: {e}")
        return False

def check_system_status():
    """Verifica el estado de los servicios"""
    print("🔍 Verificando estado de los servicios...")
    try:
        result = subprocess.run(["docker-compose", "ps"], check=True, stdout=subprocess.PIPE)
        print(result.stdout.decode())
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al verificar el estado: {e}")
        return False

def main():
    """Función principal"""
    if not check_docker_installed() or not check_docker_compose_installed():
        sys.exit(1)
    
    if len(sys.argv) < 2:
        print("Uso: python setup.py [start|stop|status]")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "start":
        start_monitoring_system()
    elif command == "stop":
        stop_monitoring_system()
    elif command == "status":
        check_system_status()
    else:
        print(f"Comando desconocido: {command}")
        print("Uso: python setup.py [start|stop|status]")
        sys.exit(1)

if __name__ == "__main__":
    main()