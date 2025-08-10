# React Agent with LangChain RAG Implementation

A sophisticated React Agent implementation using LangChain's ReAct (Reasoning and Acting) framework with Retrieval Augmented Generation (RAG) capabilities, designed to support an ice breaker application with grocery sales and complementary data sources.

## 🎯 Purpose

This project demonstrates the implementation of a conversational AI agent that combines reasoning with action-taking capabilities, utilizing RAG (Retrieval Augmented Generation) to provide contextually relevant responses for ice breaker conversations using grocery sales and complementary datasets.

## 🚀 Features

- **ReAct Agent Framework**: Implementation of LangChain's ReAct pattern for reasoning and action-taking
- **Custom Callback Handlers**: Real-time monitoring and debugging of LLM interactions
- **Tool Integration**: Extensible tool system for various data processing tasks
- **OpenAI Integration**: Seamless integration with OpenAI's language models
- **Environment Management**: Secure configuration management using environment variables

## 🏗️ Architecture

The project follows a modular architecture:

```
├── main.py              # Core agent implementation and execution logic
├── callbacks.py         # Custom callback handlers for LLM monitoring
├── Pipfile             # Pipenv dependency management
├── Pipfile.lock        # Locked dependency versions
├── requirements.txt    # pip-compatible dependency list
├── .env               # Environment variables (not tracked)
└── README.md          # This documentation
```

## 📋 Prerequisites

- Python 3.12 or higher
- OpenAI API key
- pipenv (recommended) or pip

## 🛠️ Installation

### Using pipenv (Recommended)

```bash
# Clone the repository
git clone <your-repository-url>
cd react-langchain

# Install dependencies using pipenv
pipenv install

# Activate the virtual environment
pipenv shell
```

### Using pip

```bash
# Clone the repository
git clone <your-repository-url>
cd react-langchain

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

2. Replace `your_openai_api_key_here` with your actual OpenAI API key.

## 🚀 Usage

Run the main application:

```bash
python main.py
```

The agent will demonstrate its capabilities by processing a sample question about text length calculation.

## 🔧 Core Components

### Agent Implementation (`main.py`)

The main script implements a ReAct agent that:
- Loads environment variables and dependencies
- Defines custom tools (e.g., text length calculation)
- Sets up the agent prompt template following ReAct format
- Executes the agent with intermediate step tracking

### Callback Handlers (`callbacks.py`)

Custom callback handlers provide:
- Real-time LLM prompt monitoring
- Response tracking and debugging
- Execution flow visibility

### Tool System

The project includes an extensible tool system:
- `get_text_length`: Calculates character count in text strings
- Easily extensible for additional RAG-related tools

## 🎓 Educational Context

This project serves as a practical implementation of advanced LangChain concepts, including:
- Agent architecture and reasoning patterns
- Custom tool development
- Callback handler implementation
- RAG system integration patterns

## 🔄 Future Enhancements

Potential improvements and extensions:
- Integration of vector databases for RAG functionality
- Implementation of grocery sales data processing tools
- Enhanced ice breaker conversation capabilities
- Web interface for user interaction
- Multi-tool agent capabilities
- Performance monitoring and analytics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

This project was originally created by **Eden Marco** (GitHub: [@emarco177](https://github.com/emarco177)) as part of his comprehensive LangChain course curriculum.

## ⚠️ Disclaimer

This project was completed as part of Eden Marco's Udemy Course on LangChain. It is intended for educational purposes and demonstrates the practical application of LangChain's ReAct agent framework with RAG capabilities. The implementation serves as a learning resource for understanding advanced AI agent architectures and their real-world applications.

## 📞 Support

For questions, issues, or contributions, please:
1. Check existing [Issues](../../issues)
2. Create a new issue if needed
3. Refer to Eden Marco's original course materials for additional context

---

*Built with ❤️ using LangChain and OpenAI*
