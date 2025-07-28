#!/usr/bin/env python3
"""
PDF Branding Remover - Minimal test version for deployment debugging
"""

import streamlit as st

# Start with absolute minimal app
st.set_page_config(page_title="PDF Branding Remover - Debug", layout="wide")
st.title("Debug Mode - Basic App Test")

try:
    st.success("✅ Streamlit is working!")
    
    # Test basic imports one by one
    st.markdown("### Testing Imports...")
    
    try:
        import sys
        st.success("✅ sys imported")
    except Exception as e:
        st.error(f"❌ sys failed: {str(e)}")
    
    try:
        import os
        st.success("✅ os imported")
    except Exception as e:
        st.error(f"❌ os failed: {str(e)}")
    
    try:
        import numpy as np
        st.success("✅ numpy imported")
    except Exception as e:
        st.error(f"❌ numpy failed: {str(e)}")
    
    try:
        from PIL import Image
        st.success("✅ PIL imported")
    except Exception as e:
        st.error(f"❌ PIL failed: {str(e)}")
    
    try:
        import cv2
        st.success("✅ opencv imported")
    except Exception as e:
        st.error(f"❌ opencv failed: {str(e)}")
    
    try:
        import fitz
        st.success("✅ PyMuPDF imported")
    except Exception as e:
        st.error(f"❌ PyMuPDF failed: {str(e)}")
    
    try:
        import openai
        st.success("✅ openai imported")
    except Exception as e:
        st.error(f"❌ openai failed: {str(e)}")
    
    try:
        import easyocr
        st.success("✅ easyocr imported")
    except Exception as e:
        st.error(f"❌ easyocr failed: {str(e)}")
    
    # Test basic functionality
    st.markdown("### Basic Tests")
    
    if st.button("Test Basic Functionality"):
        try:
            # Test numpy
            import numpy as np
            arr = np.array([1, 2, 3])
            st.success(f"✅ Numpy array: {arr}")
            
            # Test PIL
            from PIL import Image
            img = Image.new('RGB', (100, 100), color='red')
            st.success("✅ PIL image created")
            st.image(img, width=100)
            
        except Exception as e:
            st.error(f"❌ Basic functionality failed: {str(e)}")
    
    # Environment info
    st.markdown("### Environment Info")
    st.code(f"Python version: {sys.version}")
    st.code(f"Working directory: {os.getcwd()}")
    
    # File check
    st.markdown("### File Check")
    files_to_check = ['requirements.txt', 'packages.txt', 'IMG_1916.png']
    for file_path in files_to_check:
        if os.path.exists(file_path):
            st.success(f"✅ {file_path} exists")
        else:
            st.warning(f"⚠️ {file_path} not found")
    
    # API Key check
    st.markdown("### API Key Check")
    env_key = os.getenv("OPENAI_API_KEY")
    if env_key:
        st.success(f"✅ OPENAI_API_KEY found in environment (length: {len(env_key)})")
    else:
        st.warning("⚠️ OPENAI_API_KEY not found in environment")
    
    try:
        if hasattr(st, 'secrets') and st.secrets:
            secrets_key = st.secrets.get("OPENAI_API_KEY")
            if secrets_key:
                st.success(f"✅ OPENAI_API_KEY found in Streamlit secrets (length: {len(secrets_key)})")
            else:
                st.warning("⚠️ OPENAI_API_KEY not found in Streamlit secrets")
        else:
            st.info("ℹ️ Streamlit secrets not available")
    except Exception as e:
        st.error(f"❌ Error checking Streamlit secrets: {str(e)}")
    
    st.markdown("---")
    st.markdown("### Instructions")
    st.info("""
    **If you can see this page with green checkmarks:**
    The basic app is working and we can identify which specific component is failing.
    
    **If you still see 'Oh no' error:**
    The issue is in the basic Streamlit setup, requirements, or deployment configuration.
    """)

except Exception as e:
    st.error(f"Error in main app: {str(e)}")
    import traceback
    st.code(traceback.format_exc())
