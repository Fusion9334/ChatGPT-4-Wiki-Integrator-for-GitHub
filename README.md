---

# 🌟 GitHub to ChatGPT-4 Document Integrator 🌟

The GitHub to ChatGPT-4 Document Integrator is a cutting-edge Python tool crafted to seamlessly integrate content from any GitHub repository—be it a Wiki or a codebase—into a structured JSON format. This innovative tool stands ready to automatically clone the repository you specify, intelligently process its contents, and deliver a JSON document primed for interaction with OpenAI's ChatGPT-4. Whether you're dealing with detailed documentation or intricate code, this tool ensures your content is ChatGPT-4 ready.

## Features

- **Automatic Repository Cloning**: Effortlessly clones any GitHub repository directly from the URL you provide.
- **Content Detection**: With keen insight, it determines whether your repository is a Wiki or code-based and tailors the processing accordingly.
- **Structured JSON Output**: Produces a meticulously structured JSON document from your repository content, optimized for further processing or deep analysis.
- **Interactive Prompts**: Engages you with interactive prompts to ensure a smooth and user-friendly experience, even in the absence of initial command-line arguments.
- **Command-Line Arguments**: Offers full support for command-line arguments, facilitating straightforward automation and workflow integration.

## Installation

### 🚀 Automated Setup with `start.bat`

Windows users, rejoice! The `start.bat` file is your shortcut to getting everything up and running. It automates the entire setup process, including the environment setup, dependencies installation, and application execution. Just give it a double-click and follow the simple on-screen instructions.

### Prerequisites

- Ensure Python 3.6 or later is installed and ready to wield its magic.
- Have `git` installed and within reach from your command line.
- A connection to the vast digital ocean (internet access) for cloning GitHub repositories.

### 🔧 Manual Setup

1. **Summon the Repository**:

    ```bash
    git clone https://github.com/yourusername/yourrepositoryname.git
    cd yourrepositoryname
    ```

2. **Conjure a Virtual Environment (Optional)**:

    ```bash
    python -m venv venv
    ```

    - Awaken the virtual environment:
      - Windows: `.\venv\Scripts\activate`
      - macOS/Linux: `source venv/bin/activate`

3. **Gather the Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Navigate the realms of GitHub documentation and code with ease:

### Command-Line Arguments

```bash
python app_v2.py --url <REPOSITORY_URL> --output <OUTPUT_FILE_NAME> --token-limit <TOKEN_LIMIT> --extensions <FILE_EXTENSIONS>
```

Details for the command-line adventurers:
- `--url`: Your chosen GitHub repository's clone URL.
- `--output`: Name your adventure's outcome (the output JSON file, defaulting to `output.json`).
- `--token-limit`: Set the boundaries of your quest with a token limit (optional, with a default of 1800000).
- `--extensions`: Choose your path by specifying the file extensions to include (optional, defaults to `.md,.txt,.py,.js,.html`).

### Interactive Mode

Should you embark without command-line companions, worry not! The script will engage you in a dialogue, asking for the GitHub repository URL to begin its magic.

## Contributions

Your spells and incantations (enhancements and fixes) are most welcome in this grand tome. Fork the repository, cast your enhancements, and conjure a pull request to share your magic.

## License

This mystical tool is bound by the MIT License - consult the LICENSE scroll for the ancient texts.

Dive into the GitHub to ChatGPT-4 Document Integrator experience, where every GitHub repository's story is ready to be told, explored, and understood in the enchanting world of ChatGPT-4. 🌌

---
