# Language-Translator-Huggingface

A powerful translation engine built with Streamlit, LangChain, and Hugging Face models that supports multiple languages for seamless text translation.

## Features

- 🌍 **Multi-language Support**: Translate between English, Hindi, French, Telugu, Tamil, Japanese, and Urdu
- 🤖 **AI-Powered**: Uses Qwen2.5-7B-Instruct model from Hugging Face for accurate translations
- 💬 **User-Friendly Interface**: Built with Streamlit for an intuitive web-based UI
- ⚡ **Fast Processing**: Leverages LangChain for efficient prompt handling and model interaction

## Supported Languages

- English
- Hindi
- French
- Telugu
- Tamil
- Japanese
- Urdu

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yashpalsaini01/Language-Translator-Huggingface.git
   cd Language-Translator-Huggingface
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Environment Variables

Create a `.env` file in the root directory with your Hugging Face API credentials:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
```

You can get your API token from [Hugging Face Hub](https://huggingface.co/settings/tokens).

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### How to Use

1. Enter the text you want to translate in the text area
2. Select the **source language** (the language of your input text)
3. Select the **target language** (the language you want to translate to)
4. Click the **Translate** button
5. View your translated text below

## Technical Details

### Dependencies

- **streamlit**: Web application framework
- **langchain-huggingface**: Integration between LangChain and Hugging Face models
- **python-dotenv**: Load environment variables from `.env` file

### Model Information

- **Model**: Qwen/Qwen2.5-7B-Instruct
- **Task**: Text Generation
- **Provider**: Hugging Face Hub

## Project Structure

```
Language-Translator-Huggingface/
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (not tracked)
└── README.md          # Project documentation
```

## How It Works

1. The application initializes a Hugging Face endpoint using the Qwen2.5-7B-Instruct model
2. User inputs text along with source and target language preferences
3. A translation prompt is constructed and sent to the LLM
4. The model processes the request and returns the translated text
5. Results are displayed in the Streamlit interface

## Error Handling

- If the text area is empty, a warning message "Translation failed" is displayed
- If the translation fails, the application returns "Translation failed"

## Limitations

- Translation accuracy depends on the underlying model's capabilities
- Requires internet connection to access Hugging Face API
- API rate limits may apply based on your Hugging Face account tier

## Future Enhancements

- Add support for additional languages
- Implement caching for repeated translations
- Add batch translation support
- Implement custom API key management
- Add language detection feature

## Contributing

Contributions are welcome! Feel free to:
- Report bugs by opening an issue
- Suggest features through discussions
- Submit pull requests with improvements

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions:
1. Check the [Hugging Face documentation](https://huggingface.co/docs)
2. Review the [LangChain documentation](https://python.langchain.com/)
3. Open an issue on this repository

## Author

**Yashpal Saini**

---

**Happy Translating! 🚀**
