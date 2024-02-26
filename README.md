# 🌟 GitHub Wiki to ChatGPT-4 Document Integrator 🌟

The GitHub Wiki to ChatGPT-4 Document Integrator is a Python-based tool designed to facilitate the integration of GitHub Wiki or code repository content into a structured JSON format suitable for processing with OpenAI's ChatGPT-4. This tool automatically clones the specified repository, processes its contents based on whether it's a wiki or a code repository, and outputs a structured JSON document.

## Features

- **Automatic Repository Cloning**: Clones GitHub Wiki or code repositories based on the provided URL.
- **Content Detection**: Automatically detects whether the provided repository is a Wiki or code repository and processes the content accordingly.
- **Structured JSON Output**: Outputs the processed repository content into a structured JSON file, making it compatible for further processing or analysis.
- **Interactive Prompts**: Offers an interactive mode that prompts users for input if necessary, enhancing usability.
- **Command-Line Arguments**: Supports command-line arguments for easy automation and integration into workflows.

## Installation

### Automated Setup with `start.bat`

For Windows users, a `start.bat` file is provided to automate the setup process, including environment setup, dependencies installation, and application execution.

- Double-click the `start.bat` file.
- Follow the on-screen instructions to complete the setup.

### Prerequisites

- Python 3.6 or later.
- `git` installed and accessible from the command line.
- Internet access for cloning GitHub repositories.

### Setup

1. **Clone the Repository**:

```bash
git clone https://github.com/yourusername/yourrepositoryname.git
cd yourrepositoryname
```

2. **Create a Virtual Environment (Optional)**:

```bash
python -m venv venv
```

- Activate the virtual environment:
  - On Windows: `.\venv\Scripts\activate`
  - On macOS/Linux: `source venv/bin/activate`

3. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

## Usage

### Command-Line Arguments

```bash
python app_v2.py --url <REPOSITORY_URL> --output <OUTPUT_FILE_NAME> --token-limit <TOKEN_LIMIT> --extensions <FILE_EXTENSIONS>
```

- `--url`: The GitHub repository clone URL (required).
- `--output`: The name of the output JSON file (optional, default `output.json`).
- `--token-limit`: The token limit for the processed content (optional, default 1800000).
- `--extensions`: Comma-separated list of supported file extensions (optional, default `.md,.txt,.py,.js,.html`).

### Interactive Mode

If no arguments are provided, the script will prompt you interactively for the GitHub repository URL.

## Contributions

Contributions are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Remember to replace `https://github.com/yourusername/yourrepositoryname.git` with your actual repository URL. This README provides a comprehensive guide for users to get started with your tool, install it, and understand how to use it effectively.
