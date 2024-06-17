import os
import shutil
import subprocess

def init_profile(profile):
    # Simulate cloning a repository by copying files from a template directory
    source_dir = os.path.join('templates', profile)
    dest_dir = os.path.join(os.getcwd(), profile)
    
    if os.path.exists(dest_dir):
        print(f"Profile directory {dest_dir} already exists")
        return
    
    shutil.copytree(source_dir, dest_dir)
    print(f"Initialized profile at {dest_dir}")

def start_infra():
    # Run docker-compose up -d
    subprocess.run(['docker-compose', 'up', '-d'], check=True)
    print("Infrastructure started")

def stop_infra():
    # Run docker-compose down
    subprocess.run(['docker-compose', 'down'], check=True)
    print("Infrastructure stopped")

def start_api():
    # Assuming your FastAPI app is started with uvicorn
    subprocess.run(['uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', '8000', '--reload'], check=True)
    print("API started")

def stop_api():
    # Stopping FastAPI app, you can implement based on your actual need
    print("API stopped (implement actual stop logic as needed)")

def build_env(name):
    # Create the Conda environment
    subprocess.run(['conda', 'create', '-n', name, 'python=3.11', '-y'], check=True)
    print(f"Conda environment '{name}' created")
    
    # Activate the Conda environment and install requirements
    # This step varies slightly between shells (bash, zsh, cmd.exe, powershell)
    if os.name == 'nt':
        activate_command = f'conda activate {name} && pip install -r requirements.txt'
    else:
        activate_command = f'conda activate {name} && pip install -r requirements.txt'
    
    subprocess.run(activate_command, shell=True, check=True, executable="/bin/bash")
    print(f"Conda environment '{name}' activated and requirements installed")
