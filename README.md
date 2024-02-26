# GitHub Wiki to ChatGPT-4 Document Integrator

The GitHub Wiki to ChatGPT-4 Document Integrator is a powerful Python utility designed to convert GitHub Wiki content into documents optimized for OpenAI's ChatGPT-4. This tool is ideal for developers, researchers, and educators who use GitHub for documentation and wish to enhance their interaction with ChatGPT-4.

## Getting Started

### Automated Setup with start.bat

For a quick and easy setup, use the `start.bat` script. This script automates the environment setup, including checking for Python, creating a virtual environment, installing dependencies, and running the application.

1. **Run start.bat**: Double-click the `start.bat` file in the project's root directory. This initiates the automated setup process.
    - If Python is not installed or not found in the system's PATH, the script will prompt you to install Python and ensure it's added to PATH.
    - If a virtual environment named `venv` does not exist, the script will create it, activate it, and install the necessary dependencies from `requirements.txt`.
    - Finally, the script runs the `app_v2.py` script to start the application.

This method is recommended for most users for its simplicity.

### Manual Installation

If you prefer to set up the environment manually, follow these steps:

1. **Check Python Installation**: Ensure that Python 3.6 or later is installed on your system and that Python and pip are added to your system's PATH.
2. **Clone the Repository**: Clone this repository to your local machine.
3. **Create a Virtual Environment**: Navigate to the cloned repository's directory and create a virtual environment.
    ```bash
    python -m venv venv
    ```
4. **Activate the Virtual Environment**: 
    - On Windows, activate the virtual environment by running:
    ```bash
    .\venv\Scripts\activate
    ```
    - On macOS and Linux, use:
    ```bash
    source venv/bin/activate
    ```
5. **Install Dependencies**: Install all required dependencies using pip.
    ```bash
    pip install -r requirements.txt
    ```
6. **Run the Application**: Start the application with Python.
    ```bash
    python app_v2.py
    ```

### Prerequisites

- **Python 3.6 or later**: Ensure Python is installed and accessible from your system's PATH.
- **Git**: Required for cloning the repository if using manual installation.

## Features

- Automated GitHub Wiki Cloning
- Content Optimization for ChatGPT-4
- Intelligent Document Processing
- Advanced Token Limit Management

## Contributions

Contributions are welcome! If you have suggestions for improvement or have identified bugs, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
