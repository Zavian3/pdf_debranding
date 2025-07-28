#!/usr/bin/env python3
"""
Download required models at runtime to avoid Git LFS issues
"""

import os
import streamlit as st
from pathlib import Path

@st.cache_resource
def download_easyocr_models():
    """Download EasyOCR models if they don't exist"""
    try:
        import easyocr
        
        # Create models directory if it doesn't exist
        models_dir = Path("models")
        models_dir.mkdir(exist_ok=True)
        
        # EasyOCR will automatically download models to its default location
        # We just need to initialize it once
        reader = easyocr.Reader(['en'], download_enabled=True)
        
        return reader
    except Exception as e:
        st.error(f"Failed to download models: {str(e)}")
        return None

if __name__ == "__main__":
    print("Testing model download...")
    reader = download_easyocr_models()
    if reader:
        print("✅ Models downloaded successfully!")
    else:
        print("❌ Model download failed") 