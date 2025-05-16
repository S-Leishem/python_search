# Web Search Application

A powerful and user-friendly web search application built with Python that provides instant web search results through both command-line and graphical interfaces.

## 🚀 Key Features

- 🔍 Real-time web search capabilities
- 💻 Dual Interface Options:
  - Modern graphical interface
  - Simple command-line interface
- 🎯 High-quality, relevant search results
- 🔗 Clickable links (GUI version)
- 🌐 Direct browser integration
- 🛡️ Secure API handling

## 📋 Requirements

- Python 3.8 or higher
- Internet connection
- SerpAPI key (get from [SerpAPI](https://serpapi.com))

## 🔧 Setup

1. Install required packages:
```bash
pip install flet google-search-results python-dotenv
```

2. Configure your API key:
   - Create a file named `.env` in the program directory
   - Add your SerpAPI key:
   ```
   SERPAPI_KEY=your_api_key_here
   ```

## 📱 Using the Application

### Graphical Interface
Run the GUI version:
```bash
python search_flet.py
```

Features:
- Clean, modern search interface
- Type your search query and press Enter or click Search
- Click any result to open in your browser
- Progress indicator while searching
- Error notifications if something goes wrong

### Command Line Interface
Run the CLI version:
```bash
python search.py
```

Features:
- Fast, lightweight interface
- Type your search query when prompted
- View numbered results with titles and links
- Copy-paste links directly from terminal

## 💎 Premium Features

### Standard Package
- 100 searches per month
- Basic search functionality
- CLI interface
- Email support

### Professional Package
- Unlimited searches
- Full GUI access
- Priority support
- Advanced filters
- Bulk search capability

For pricing and premium access: contact@yourdomain.com

## ⚠️ Troubleshooting

Common solutions:
- Ensure your API key is correctly set in `.env`
- Check your internet connection
- Verify Python version (3.8+ required)
- Make sure all dependencies are installed

## 🔒 Security

Your searches and API key are protected through:
- Secure environment variable storage
- Local-only configuration
- Encrypted API communications

---

Made with ❤️ by Soubam Leishem
Contact: soubamleishem4@gmail.com
