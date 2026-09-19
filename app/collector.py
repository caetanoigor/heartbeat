import psutil 

def get_system_metrics():
    cpu = psutil.cpu_percent(interval=0.5)
    
    memory = psutil.virtual_memory()
    
    disk = psutil.disk_usage('/')
    
    return {
        'cpu': {
            'usage_percent': cpu,
            'logical_cores': psutil.cpu_count(logical=True),
            'physical_cores': psutil.cpu_count(logical=False)
        },
        
        'memory': {
            'total_mb': int(memory.total / (1024**2)),
            'available_mb': int(memory.available / (1024**2)),
            'usage_percent': memory.percent
        },
        
        'disk': {
            'total_gb': round(disk.total / (1024**3), 2),
            'free_gb': round(disk.free / (1024**3), 2),
            'usage_percent': disk.percent
        }
    }
    
if __name__ == '__main__':
    import json
    print(json.dumps(get_system_metrics(), indent=2))    