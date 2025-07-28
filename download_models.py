#!/usr/bin/env python3
"""
Script to download EasyOCR models locally for deployment.
This avoids runtime model downloads in production.
"""
import easyocr
import os
import shutil
from pathlib import Path

def download_easyocr_models():
    """Download EasyOCR models to local models directory"""
    print("🔄 Downloading EasyOCR models...")
    
    # Create models directory if it doesn't exist
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    
    try:
        # Initialize EasyOCR reader to trigger model downloads
        # This will download models to the default cache location
        print("📥 Initializing EasyOCR reader (this will download models)...")
        reader = easyocr.Reader(['en'], gpu=False, download_enabled=True)
        print("✅ EasyOCR models downloaded successfully")
        
        # Find the EasyOCR model cache directory using different approaches
        possible_cache_dirs = [
            Path.home() / ".EasyOCR",
            Path.home() / ".cache" / "easyocr",
            Path.home() / "AppData" / "Local" / "easyocr",  # Windows
            Path("/tmp") / "easyocr",  # Linux
        ]
        
        model_storage_path = None
        for cache_dir in possible_cache_dirs:
            if cache_dir.exists():
                print(f"📂 Found EasyOCR cache at: {cache_dir}")
                model_storage_path = cache_dir
                break
        
        # Also check if we can get the path from the reader object
        if hasattr(reader, 'model_storage_directory'):
            model_storage_path = Path(reader.model_storage_directory)
        elif hasattr(reader, 'detector') and hasattr(reader.detector, 'model_path'):
            model_storage_path = Path(reader.detector.model_path).parent
        
        if model_storage_path and model_storage_path.exists():
            print(f"📂 Using model cache location: {model_storage_path}")
            print("📋 Copying models to local directory...")
            
            # Copy all model files
            copied_files = 0
            for model_file in model_storage_path.rglob("*"):
                if model_file.is_file() and model_file.suffix in ['.pth', '.zip', '.pkl', '.onnx']:
                    relative_path = model_file.relative_to(model_storage_path)
                    target_path = models_dir / relative_path
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(model_file, target_path)
                    print(f"✅ Copied: {relative_path}")
                    copied_files += 1
            
            print(f"🎉 {copied_files} model files copied to {models_dir.absolute()}")
            
            # Also save a config file to help the app locate models
            config_file = models_dir / "easyocr_config.txt"
            with open(config_file, 'w') as f:
                f.write(f"EasyOCR models copied from: {model_storage_path}\n")
                f.write(f"Total files: {copied_files}\n")
            print(f"📝 Config saved to {config_file}")
            
        else:
            print("❌ Could not locate EasyOCR model cache directory")
            print("📂 Searching common locations...")
            # List what we can find
            for cache_dir in possible_cache_dirs:
                if cache_dir.exists():
                    print(f"  Found: {cache_dir}")
                    for item in cache_dir.iterdir():
                        print(f"    - {item.name}")
                else:
                    print(f"  Not found: {cache_dir}")
            
    except Exception as e:
        print(f"❌ Error downloading models: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    download_easyocr_models() 