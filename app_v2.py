import os
import json
import logging
import re
import requests
from git import Repo
import argparse

# Setup basic logging configuration
logging.basicConfig(filename='integrator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_github_url(url):
    """Validate the GitHub repository URL."""
    pattern = r'https://github\.com/[\w-]+/[\w-]+(\.wiki\.git)?$'
    if not re.match(pattern, url):
        logging.error(f'Invalid GitHub URL: {url}')
        return False
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True
        else:
            logging.error(f'GitHub URL not accessible: {url}')
            return False
    except requests.RequestException as e:
        logging.error(f'Error checking URL {url}: {str(e)}')
        return False

def detect_repo_type(clone_url):
    """Detect if the URL is for a wiki or code repository."""
    if '.wiki.git' in clone_url:
        return 'wiki'
    else:
        return 'code'

def parse_arguments():
    """Parse command line arguments for the script."""
    parser = argparse.ArgumentParser(description='GitHub Wiki to ChatGPT-4 Document Integrator')
    parser.add_argument('--url', help='GitHub repository clone URL (wiki or code)', default=None)
    parser.add_argument('--output', help='Output JSON file name', default='output.json')
    parser.add_argument('--token-limit', type=int, help='Token limit for the processed content', default=1800000)
    parser.add_argument('--extensions', help='Comma-separated list of supported file extensions', default='.md,.txt,.py,.js,.html')
    args = parser.parse_args()

    if not args.url:
        args.url = input("Enter the GitHub repository clone URL (wiki or code): ").strip()

    return args

class GitHubWikiIntegrator:
    def __init__(self, clone_url, output_file, token_limit, supported_extensions):
        self.clone_url = clone_url
        self.output_file = output_file
        self.token_limit = token_limit
        self.supported_extensions = supported_extensions.split(',')
        self.repo_dir = ""

    def clone_repo(self):
        """Clone a GitHub repository."""
        repo_type = detect_repo_type(self.clone_url)
        try:
            repo_name = os.path.basename(self.clone_url)
            if repo_name.endswith('.git'):
                repo_name = repo_name[:-4]  # Remove '.git' from the end
            self.repo_dir = f"cloned_repos/{repo_name}"
            os.makedirs(self.repo_dir, exist_ok=True)
            Repo.clone_from(self.clone_url, self.repo_dir)
            logging.info(f'Successfully cloned {self.clone_url}')
            return repo_type
        except Exception as e:
            logging.error(f'Failed to clone {self.clone_url}: {str(e)}')
            raise

    def process_contents(self, repo_type):
        """Process and structure the contents of the cloned repository."""
        documents = []

        for root, _, files in os.walk(self.repo_dir):
            for file in files:
                file_path = os.path.join(root, file)
                _, ext = os.path.splitext(file)
                if ext in self.supported_extensions:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        document = {
                            "path": file_path.replace(f"{self.repo_dir}/", ""),
                            "type": repo_type,
                            "extension": ext,
                            "content": content
                        }
                        documents.append(document)
        self.save_content_as_json(documents)

    def save_content_as_json(self, documents):
        """Save the structured documents into a JSON file."""
        try:
            with open(self.output_file, 'w', encoding='utf-8') as file:
                json.dump(documents, file, ensure_ascii=False, indent=4)
            logging.info(f'Successfully saved content to {self.output_file}')
        except Exception as e:
            logging.error(f'Failed to save content to {self.output_file}: {str(e)}')
            raise

if __name__ == "__main__":
    args = parse_arguments()

    if validate_github_url(args.url):
        integrator = GitHubWikiIntegrator(args.url, args.output, args.token_limit, args.extensions)
        repo_type = integrator.clone_repo()
        integrator.process_contents(repo_type)
        print(f"Processing completed. Content is structured and saved in {args.output}")
    else:
        print("The provided URL is invalid. Please check the URL and try again.")
