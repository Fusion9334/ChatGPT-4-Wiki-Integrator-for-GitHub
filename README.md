# GitHub Wiki to ChatGPT-4 Document Integrator



The GitHub Wiki to ChatGPT-4 Document Integrator is a Python-based automation tool designed to transform GitHub Wiki content into a cohesive document optimized for interaction with OpenAI's ChatGPT-4. This tool simplifies the process of compiling and formatting GitHub Wiki pages, ensuring the final document stays within the token limits of ChatGPT-4 for seamless upload and discussion.



## Features



- **Automated GitHub Wiki Cloning**: Clone any GitHub Wiki repository directly using the provided clone URL.

- **Content Optimization for ChatGPT-4**: Ensures the documentation is in a digestible format for ChatGPT-4, facilitating more meaningful interactions.

- **Smart Document Processing**: Automatically merges text-based documentation (.md, .txt) into a single document, or splits it to adhere to token limitations.

- **Token Limit Management**: Utilizes the `tiktoken` library to accurately count tokens, optimizing content size for ChatGPT-4's upload constraints.



## Getting Started



### Prerequisites



- Python 3.6 or newer

- Git installed on your system



### Installation



```bash

pip install tiktoken  # Install the tiktoken library

```



### Usage



1. Run the script and provide the GitHub Wiki repository's clone URL when prompted.

2. The tool will clone the repository, process the content, and generate a document(s) ready for ChatGPT-4.



```bash

python app.py  # Execute the main script

```



## How It Works



The integrator fetches the GitHub Wiki repository using the provided clone URL, then scans for all `.md` and `.txt` files, compiling their contents into a single document. If the content exceeds ChatGPT-4's token limits, it's automatically divided into smaller, manageable documents.



## Contributions



Contributions are welcome! If you have suggestions for improvement, or have identified bugs, feel free to fork the repository, make your changes, and submit a pull request.



## License



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



---



This tool is particularly useful for developers, researchers, and educational professionals who leverage GitHub for documentation and seek to enhance their interactive experience with ChatGPT-4, ensuring comprehensive subject matter understanding and discussion.
