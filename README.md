# GitHub Wiki to ChatGPT-4 Document Integrator

The GitHub Wiki to ChatGPT-4 Document Integrator is an advanced Python utility designed to streamline the conversion of GitHub Wiki content into documents optimized for OpenAI's ChatGPT-4. This tool is essential for developers, researchers, and educators leveraging GitHub for documentation, facilitating enriched interactions with ChatGPT-4 through well-prepared content.

## Features

- **Automated GitHub Wiki Cloning**: Facilitates the cloning of any GitHub Wiki repository with just the clone URL.
- **Content Optimization for ChatGPT-4**: Formats documentation to be easily ingestible by ChatGPT-4, enhancing user interaction.
- **Intelligent Document Processing**: Combines and intelligently splits text-based documentation (.md, .txt) to adhere to ChatGPT-4's token limits, ensuring no content is too lengthy for upload.
- **Advanced Token Limit Management**: Utilizes the `tiktoken` library to accurately manage and optimize content size, making sure documents fit within ChatGPT-4's upload constraints.

## Getting Started

### Prerequisites

- Python 3.6 or later
- Git

### Installation

```bash
pip install tiktoken  # For token counting and content size optimization
```

### Usage

1. Start the script and input the GitHub Wiki repository's clone URL as prompted.
2. The tool will handle the cloning, content processing, and document preparation for ChatGPT-4 compatibility.

```bash
python app_v2.py  # Initiates the script
```

## How It Works

After fetching the GitHub Wiki using the clone URL, the tool scans for `.md` and `.txt` files, compiling them into a unified document. Should the content surpass ChatGPT-4's token limits, it automatically segments it into smaller, manageable documents.

## Contributions

Contributions are encouraged! If you have ideas for enhancements or have discovered bugs, feel free to fork the repository, implement your changes, and submit a pull request.

## License

Licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This tool significantly simplifies the integration of GitHub Wiki documentation with ChatGPT-4, promoting comprehensive discussions and a deeper understanding of the content.
