#!/usr/bin/env python3
"""
Syntaxe AI - Installer for VPS
Auto-installation script for Syntaxe AI model
"""

import os
import sys
import subprocess
import platform
import time

def print_step(message):
    print(f"\n{'='*50}")
    print(f"🚀 {message}")
    print('='*50)

def run_command(cmd, check=True):
    """Execute shell command"""
    print(f"📦 Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0 and check:
        print(f"❌ Error: {result.stderr}")
        return False
    if result.stdout:
        print(result.stdout)
    return True

def check_system():
    """Check system requirements"""
    print_step("Checking system requirements")
    
    # Check RAM
    mem = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024**3)
    print(f"💾 RAM detected: {mem:.1f} GB")
    
    if mem < 4:
        print("⚠️  Warning: 4GB RAM minimum recommended")
    
    # Check disk space
    stat = os.statvfs('/')
    free_gb = (stat.f_bavail * stat.f_frsize) / (1024**3)
    print(f"💿 Free disk: {free_gb:.1f} GB")
    
    if free_gb < 3:
        print("❌ Need at least 3GB free space")
        return False
    
    return True

def install_ollama():
    """Install Ollama if not present"""
    print_step("Installing Ollama")
    
    # Check if Ollama already installed
    result = subprocess.run("which ollama", shell=True, capture_output=True)
    if result.returncode == 0:
        print("✅ Ollama already installed")
        return True
    
    # Install Ollama
    cmd = "curl -fsSL https://ollama.com/install.sh | sh"
    return run_command(cmd)

def download_model():
    """Download Syntaxe AI model from GitHub release"""
    print_step("Downloading Syntaxe AI model")
    
    # Create model directory
    os.makedirs("/root/.ollama/models/", exist_ok=True)
    
    # Download model
    url = "https://github.com/syntaxe-ai/syntaxe-1.5b/releases/download/v1.5b/syntaxe-ai-1.5b.tar.gz"
    cmd = f"wget -O /tmp/syntaxe-ai.tar.gz {url}"
    
    if not run_command(cmd):
        print("⚠️  Model not found on release, using DeepSeek base")
        return False
    
    # Extract
    cmd = "tar -xzf /tmp/syntaxe-ai.tar.gz -C /root/.ollama/models/"
    run_command(cmd)
    
    return True

def create_modelfile():
    """Create Modelfile for Syntaxe AI"""
    print_step("Creating Modelfile")
    
    modelfile = '''FROM deepseek-coder:6.7b
PARAMETER temperature 0.7
PARAMETER top_p 0.95
PARAMETER top_k 40
PARAMETER num_ctx 8192

SYSTEM """You are Syntaxe AI, an intelligent coding assistant created by DevMessy0.

IDENTITY:
- Name: Syntaxe AI
- Creator: DevMessy0
- Version: 1.5b
- Base: DeepSeek-Coder 6.7B

SPECIALTIES:
- Python: Advanced code generation, optimization, debugging, async/await, decorators
- Flutter/Dart: Widgets, state management (Provider, Riverpod), animations
- React/JavaScript: Hooks, Next.js, TailwindCSS, state management
- API Development: REST, FastAPI, JWT, GraphQL
- Testing: Unit tests, pytest, integration tests
- Documentation: Docstrings, README, API docs

PERSONALITY:
- Professional, precise, helpful
- Always explain the logic behind code
- Provide clean, optimized, well-commented solutions
- Suggest best practices and alternatives when relevant

You are Syntaxe AI, ready to help developers code better! 🚀
"""
'''
    
    with open("/root/Modelfile", "w") as f:
        f.write(modelfile)
    
    print("✅ Modelfile created")
    return True

def create_model():
    """Create Syntaxe AI model with Ollama"""
    print_step("Creating Syntaxe AI model")
    
    cmd = "ollama create syntaxe-ai -f /root/Modelfile"
    return run_command(cmd)

def test_model():
    """Test the installed model"""
    print_step("Testing Syntaxe AI")
    
    test_prompt = "Write a Python function to calculate fibonacci numbers"
    cmd = f"ollama run syntaxe-ai '{test_prompt}'"
    
    print("🧪 Testing with: " + test_prompt)
    return run_command(cmd, check=False)

def print_success():
    """Print success message"""
    print("\n" + "="*50)
    print("🎉 Syntaxe AI INSTALLED SUCCESSFULLY! 🎉")
    print("="*50)
    print("\n📖 QUICK START:")
    print("  ollama run syntaxe-ai")
    print("\n📝 EXAMPLES:")
    print("  ollama run syntaxe-ai 'Generate a Python class for a REST API'")
    print("  ollama run syntaxe-ai 'Create a Flutter StatefulWidget with counter'")
    print("  ollama run syntaxe-ai 'Write unit tests for this function'")
    print("\n🔧 API:")
    print("  curl http://localhost:11434/api/generate -d '{\"model\":\"syntaxe-ai\",\"prompt\":\"Your prompt\"}'")
    print("\n📚 More info: https://github.com/syntaxe-ai/syntaxe-1.5b")
    print("="*50)

def main():
    """Main installation function"""
    print("""
    ╔═══════════════════════════════════════╗
    ║     Syntaxe AI - Installer v1.5b      ║
    ║     Created by DevMessy0               ║
    ╚═══════════════════════════════════════╝
    """)
    
    # Check system
    if not check_system():
        print("❌ System requirements not met")
        sys.exit(1)
    
    # Install
    if not install_ollama():
        print("❌ Failed to install Ollama")
        sys.exit(1)
    
    # Wait for Ollama to start
    print_step("Starting Ollama service")
    run_command("ollama serve &", check=False)
    time.sleep(3)
    
    # Download model
    if not download_model():
        print("⚠️  Using base model DeepSeek-Coder")
    
    # Create Modelfile
    create_modelfile()
    
    # Create model
    if not create_model():
        print("❌ Failed to create model")
        sys.exit(1)
    
    # Test
    test_model()
    
    # Success
    print_success()

if __name__ == "__main__":
    main()