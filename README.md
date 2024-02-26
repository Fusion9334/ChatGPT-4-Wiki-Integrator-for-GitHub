# GitHub Wiki to ChatGPT-4 Document Integrator

The GitHub Wiki to ChatGPT-4 Document Integrator is a Python tool designed to transform GitHub Wiki repositories into documents that can be interacted with through OpenAI's ChatGPT-4. This tool automates the cloning of GitHub Wiki repositories and prepares the content for conversational interaction with ChatGPT-4, making it a valuable resource for software developers, academic researchers, and educational professionals.

## Core Features

- **Automated GitHub Wiki Cloning**: Automatically clones GitHub Wiki repositories using the clone URL, facilitating easy access to repository content for processing.

- **Content Aggregation**: Combines text-based documentation files (such as `.md` and `.txt`) from the cloned repository into a single document or multiple documents, depending on the size, to make the content more manageable for ChatGPT-4 interaction.

- **Basic Token Management**: Splits content into manageable parts based on a simplistic token limit to ensure compatibility with ChatGPT-4's token constraints, enhancing the efficiency of AI interactions.

## Enhanced User Experience

This tool streamlines the integration of GitHub Wiki content with ChatGPT-4, simplifying document preparation and optimization. It allows users to focus on engaging with their content through ChatGPT-4, rather than on manual content compilation and formatting.

## Getting Started

The tool is designed for easy setup, whether you prefer an automated or a manual approach.

### Automated Setup

For a quick start, an automated setup script (e.g., `start.bat`) is provided for Windows users. This script automates the environment setup, including dependencies installation and application launch. Simply double-click the `start.bat` file in the project's root directory to begin.

### Manual Setup

For manual setup, follow these steps:

1. **Check Python Installation**: Ensure Python 3.6 or later is installed and accessible via the system's PATH.

2. **Clone the Repository**: Clone the repository to your local machine using Git.

    ```bash
    git clone https://github.com/YourUsername/YourRepository.git
    ```

3. **Create a Virtual Environment**: Navigate to the cloned repository directory and set up a virtual environment.

    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment**:
    - Windows: `.\\venv\\Scripts\\activate`
    - macOS/Linux: `source venv/bin/activate`

5. **Install Dependencies**: Use pip to install the required Python packages.

    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Application**: Launch the tool with Python.

    ```bash
    python app_v2.py
    ```

## Prerequisites

- **Python 3.6 or later**: Necessary for running the script.
- **Git**: Required for cloning the GitHub Wiki repository.

## Contributions

Contributions are welcome! If you have suggestions or bug fixes, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

This revised README provides a more accurate description of the tool's functionality, aligning with the capabilities demonstrated in the provided code.
