# 🧼 Advanced PDF Branding Remover

An intelligent PDF processing tool that removes brand elements, logos, and company information using AI-powered detection and replacement.

## ✨ Features

- **🤖 AI-Powered Detection**: Uses GPT-4o to identify brand elements, logos, and company information
- **🎨 Intelligent Logo Replacement**: Automatically replaces detected logos with custom images
- **🏢 Company Section Removal**: Removes "About Us", policies, and administrative content
- **📄 Smart Page Cleanup**: Automatically removes pages with no meaningful content
- **💰 Cost Tracking**: Real-time OpenAI API cost calculation with detailed breakdown
- **🎨 Smart Color Protection**: Preserves generic text that shares background colors with brand elements
- **⚡ Parallel Processing**: Fast processing with multi-threaded page handling

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd pdf_editor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Add replacement logo**
   - Place your replacement logo as `IMG_1916.png` in the project root
   - Or update the `REPLACEMENT_LOGO_PATH` in `app.py`

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🌐 Free Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and main branch
   - Set app path to `app.py`
   - Click "Deploy"

3. **Add environment variables**
   - In your Streamlit Cloud dashboard
   - Go to Settings → Secrets
   - Add your OpenAI API key:
   ```toml
   OPENAI_API_KEY = "your_api_key_here"
   ```

### Option 2: Render

1. **Create Render account**
   - Sign up at [render.com](https://render.com)

2. **Create new Web Service**
   - Connect your GitHub repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

3. **Add environment variables**
   - Add `OPENAI_API_KEY` in the Environment section

### Option 3: Railway

1. **Create Railway account**
   - Sign up at [railway.app](https://railway.app)

2. **Deploy from GitHub**
   - Connect your repository
   - Railway will auto-detect it's a Python app
   - Add environment variables in the Variables tab

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

### Replacement Logo

- **Path**: Update `REPLACEMENT_LOGO_PATH` in `app.py`
- **Format**: PNG recommended
- **Size**: Any size (will be resized automatically)

## 📊 Cost Management

The app includes comprehensive cost tracking:
- Real-time API cost calculation
- Per-page cost breakdown
- Model usage statistics
- Processing time tracking

**Estimated costs per page:**
- GPT-4o-mini: ~$0.001-0.005 per page
- GPT-4o (logo classification): ~$0.01-0.02 per page

## 🛠️ Technical Details

### Dependencies

- **Streamlit**: Web interface
- **OpenAI**: AI-powered detection and classification
- **PyMuPDF**: PDF processing
- **OpenCV**: Image processing and inpainting
- **EasyOCR**: Text detection
- **Pillow**: Image manipulation

### Processing Pipeline

1. **PDF Conversion**: Convert PDF to images
2. **Brand Analysis**: Extract comprehensive brand information
3. **Element Detection**: Find all brand elements, logos, and company sections
4. **Intelligent Removal**: 
   - Replace logos with custom images
   - Inpaint branding text and backgrounds
   - Remove company sections
5. **Page Cleanup**: Remove empty or logo-only pages
6. **Color Protection**: Preserve generic text colors

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter issues:
1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

## 🔒 Security Notes

- Never commit your `.env` file or API keys
- Use environment variables for sensitive data
- The app processes files locally and doesn't store them permanently 