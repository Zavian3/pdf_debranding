# Models Directory

This directory is for storing AI models used by the PDF debranding application.

## Current Status

**Models have been moved to runtime download** to avoid Git LFS deployment issues.

### Previous Issues
- The original `.pth` model files were stored using Git LFS
- Streamlit Cloud had trouble downloading Git LFS files during deployment
- This caused repeated deployment failures

### Current Solution
- Models are now downloaded automatically when needed
- This happens at runtime using the `download_models.py` script
- No large files stored in the repository

### Re-enabling Advanced Features
When you're ready to add back full PDF processing:

1. Uncomment the packages in `requirements.txt`:
   ```
   PyMuPDF>=1.23.0
   Pillow>=10.0.0
   openai>=1.0.0
   numpy>=1.24.0
   easyocr>=1.7.0
   # etc.
   ```

2. Update `app.py` to use actual PDF processing instead of placeholders

3. Models will be downloaded automatically by EasyOCR when first used

### Files
- `easyocr_config.txt` - Configuration for EasyOCR model settings
- Models will be stored here when downloaded at runtime 