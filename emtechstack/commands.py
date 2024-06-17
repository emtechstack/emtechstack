import os
import shutil
import subprocess
import requests
import zipfile
import yaml
from io import BytesIO
from tabulate import tabulate
from termcolor import colored
import pkg_resources  # to retrieve the package version


def init_profile(profile, name=None):
    repo_url = 'https://github.com/emtechstack/infra-profiles/archive/refs/heads/main.zip'
    temp_dir = 'emtechstack_temp_profile_download'
    
    try:
        # Step 1: Download the repo
        response = requests.get(repo_url)
        if response.status_code != 200:
            print(f"Failed to download profile from {repo_url}")
            return
        
        # Step 2: Unzip the repo
        zip_file = zipfile.ZipFile(BytesIO(response.content))
        zip_file.extractall(temp_dir)
        
        profile_path = os.path.join(temp_dir, 'infra-profiles-main', 'profiles', profile)
        if not os.path.exists(profile_path):
            print(f"Profile '{profile}' not found in the repository.")
            return
        
        # Step 3: Create the destination directory
        repo_name = name if name else profile
        dest_dir = os.path.join(os.getcwd(), repo_name)
        
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        # Copy all files from the profile directory to the destination directory
        for root, dirs, files in os.walk(profile_path):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.move(src_file, dest_dir)
        
        # Step 5: Clean up the downloaded zip and extracted files
        shutil.rmtree(temp_dir)
        print(f"Initialized profile at {dest_dir}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)


def start_infra():
    subprocess.run(['docker-compose', 'up', '-d'], check=True)
    print("Infrastructure started")
    display_services()

def stop_infra():
    subprocess.run(['docker-compose', 'down'], check=True)
    print("Infrastructure stopped")

def start_api():
    subprocess.run(['uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', '8000', '--reload'], check=True)
    print("API started")

def stop_api():
    print("API stopped (implement actual stop logic as needed)")

def build_env(name=None):
    try:
        if name is None:
            name = os.path.basename(os.getcwd())
        
        # Create the Conda environment
        subprocess.run(['conda', 'create', '-n', name, 'python=3.8', '-y'], check=True)
        print(f"Conda environment '{name}' created")

        # Write a temporary shell script to activate the environment and install requirements
        script_content = f"""
        #!/bin/bash
        source $(conda info --base)/etc/profile.d/conda.sh
        conda activate {name}
        pip install -r requirements.txt
        """
        script_path = 'temp_script.sh'
        with open(script_path, 'w') as script_file:
            script_file.write(script_content)

        # Make the script executable
        os.chmod(script_path, 0o775)

        # Run the script using /bin/bash
        subprocess.run(['/bin/bash', script_path], check=True)
        
        # Clean up the temporary script
        os.remove(script_path)
        
        print(f"Conda environment '{name}' activated and requirements installed")
        display_services()
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while building the environment: {e}")


def display_services():
    try:
        with open('docker-compose.yml', 'r') as file:
            docker_compose = yaml.safe_load(file)
        
        services = docker_compose.get('services', {})
        table_data = []
        
        for service, details in services.items():
            ports = details.get('ports', [])
            for port in ports:
                table_data.append([service, port.split(':')[0], port.split(':')[1]])
        
        if table_data:
            # Retrieve the package version
            version = pkg_resources.get_distribution('emtechstack').version
            
            # Print the title
            title = colored(f"EmTechStack AI Dev Tools (Version {version})", 'cyan', attrs=['bold'])
            print(title)
            print("=" * len(title))
            
            # Print the table
            print(colored(tabulate(table_data, headers=['Service', 'Port Local', 'Port Docker'], tablefmt='grid'), 'green'))
        else:
            print(colored("No services found in the docker-compose.yml file.", 'red'))
    
    except FileNotFoundError:
        print(colored("docker-compose.yml file not found.", 'red'))
    except yaml.YAMLError as exc:
        print(colored(f"Error reading docker-compose.yml file: {exc}", 'red'))
    except pkg_resources.DistributionNotFound:
        print(colored("emtechstack package not found. Ensure it is installed properly.", 'red'))

def clean_code():
    subprocess.run(['black', '.'], check=True)