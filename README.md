# GitHub Wiki to ChatGPT-4 Document Integrator

The GitHub Wiki to ChatGPT-4 Document Integrator is a meticulously designed Python tool aimed at transforming GitHub Wiki repositories into comprehensive documents that are seamlessly compatible with OpenAI's ChatGPT-4. This innovative tool bridges the gap between the extensive, often fragmented documentation stored in GitHub Wikis and the conversational, interactive capabilities of ChatGPT-4, enabling users to engage with the content in a dialogue-based format. It's the perfect solution for software developers, academic researchers, and educational professionals who rely on GitHub for documentation and seek to leverage the advanced AI-driven insights of ChatGPT-4 for a deeper understanding of their projects and topics.

## Core Features

- **Automated GitHub Wiki Cloning**: With just the clone URL of a GitHub Wiki, the tool automatically clones the repository for local processing, removing the manual overhead of content retrieval.

- **Content Optimization for ChatGPT-4**: The integrator smartly formats the cloned Wiki content, ensuring it is in a digestible format for ChatGPT-4. This includes restructuring content for coherence and breaking down complex documentation into conversational pieces that are easier for users to interact with.

- **Intelligent Document Processing**: Beyond mere content aggregation, the tool analyses and merges text-based documentation files (.md, .txt) within the cloned Wiki. It automatically combines these files into a singular document or splits them into multiple documents if necessary, to meet the token limitations imposed by ChatGPT-4, ensuring the entire repository content is accessible without information loss.

- **Advanced Token Limit Management**: Leveraging the `tiktoken` library, the tool precisely counts and manages the token count of the processed documentation. This feature ensures that the final document(s) are optimized for upload to ChatGPT-4, adhering to its token constraints and maximizing the efficiency of AI interaction.

## Enhanced User Experience

This tool not only simplifies the process of integrating GitHub Wiki content with ChatGPT-4 but also enhances the user's experience by providing a streamlined, automated workflow for document preparation and optimization. By eliminating the manual challenges associated with content compilation and formatting, it allows users to focus more on the interaction and less on the preparation. Whether you're looking to discuss code documentation, research findings, or educational material, the GitHub Wiki to ChatGPT-4 Document Integrator ensures your content is ready for an engaging, insightful conversation with ChatGPT-4.

## Getting Started

The integrator is designed to be user-friendly, with minimal setup required to get started. Whether you prefer a one-click automated setup via the provided `start.bat` file or a manual setup process, you'll find the steps straightforward and easy to follow. 

### Automated Setup

Ideal for users seeking a quick start, this method uses `start.bat` to automate environment setup, dependencies installation, and application launch. Simply double-click the `start.bat` file in the project's root directory to initiate the setup. The script will guide you through the process, including checking for Python installation, setting up the virtual environment, and running the application.

### Manual Setup

For those who prefer more control over their setup environment, manual setup instructions are as follows:

1. **Check Python Installation**: Ensure Python 3.6 or later is installed on your system and accessible via the system's PATH.

2. **Clone the Repository**: Use Git to clone the repository to your local machine.

    ```bash
    git clone https://github.com/Fusion9334/ChatGPT-4-Wiki-Integrator-for-GitHub.git
    ```

3. **Create a Virtual Environment**: Navigate to the cloned repository directory and create a virtual environment.

    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment**:
    - On Windows, run:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS and Linux, run:
      ```bash
      source venv/bin/activate
      ```

5. **Install Dependencies**: Install the required dependencies using pip.

    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Application**: Start the application with the following command:

    ```bash
    python app_v2.py
    ```

## Prerequisites

- **Python 3.6 or later**: Ensure Python is installed and accessible from your system's PATH.
- **Git**: Required for cloning the repository if using manual installation.

## Contributions

We welcome contributions from the community! If you have suggestions for improvement or have identified bugs, please fork the repository, make your changes, and submit a pull request. We appreciate your input in making this tool more efficient and useful for everyone.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

By providing a comprehensive guide from getting started through contributions, this README ensures users have all the information they need to successfully utilize the GitHub Wiki to ChatGPT-4 Document Integrator.
