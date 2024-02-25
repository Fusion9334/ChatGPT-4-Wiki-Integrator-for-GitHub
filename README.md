# ChatGPT-4 Wiki Integrator for GitHub

The ChatGPT-4 Wiki Integrator for GitHub is a sophisticated Python utility designed to consolidate text-based documentation from GitHub Wiki pages into a unified document. This utility is tailored specifically for enhancing the interaction with OpenAI's ChatGPT-4 by preparing comprehensive documentation in a format that's easily digestible by the model. It's an essential tool for developers and researchers aiming to facilitate detailed discussions with ChatGPT-4 about complex projects or topics that the model might not fully understand from its pre-existing knowledge base.

## Key Features

- **Optimized for ChatGPT-4**: Tailored to prepare documentation for seamless processing and understanding by ChatGPT-4.
- **Automated Documentation Consolidation**: Combines `.md` and `.txt` files from GitHub Wikis into a single or multiple documents, based on token count.
- **Intelligent Token Handling**: Leverages the `tiktoken` library to manage token counts efficiently, ensuring the final document stays within the ChatGPT-4 token limit for optimal interaction.
- **Flexible File Support**: Focuses on `.md` and `.txt` files, the most common formats for GitHub Wikis, ensuring wide applicability.

## Installation

Ensure you have Python 3.6 or later installed on your system. You can install the ChatGPT-4 Wiki Integrator using pip:

```bash
pip install tiktoken  # Dependency
# Clone or download this repository to your local machine.
```

## Usage

1. Clone the GitHub Wiki repository you wish to process.
2. Run the ChatGPT-4 Wiki Integrator script, specifying the path to the cloned Wiki directory:

```bash
python chatgpt4_wiki_integrator.py <path_to_cloned_wiki>
```

3. The script will produce a `master_file.txt` or multiple split files, ready for upload and discussion with ChatGPT-4.

## Areas for Improvement

- **Extended File Format Support**: Future versions could include support for additional file formats found in GitHub Wikis.
- **GUI for Ease of Use**: Implementing a graphical user interface (GUI) could make the tool more accessible to non-technical users.
- **Automated Wiki Cloning**: Integrating the capability to automatically clone GitHub Wikis by URL would streamline the process further.

## Contribution

Contributions are welcome! Whether it's adding new features, improving documentation, or reporting issues, your input is highly valued. Please feel free to fork the repository, make changes, and submit pull requests.

This tool opens up new possibilities for leveraging the vast knowledge stored in GitHub Wikis in conversations with ChatGPT-4, making it a valuable addition to any developer's or researcher's toolkit.
