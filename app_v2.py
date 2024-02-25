import os
from tiktoken import tiktoken
from git import Repo

class GitHubWikiIntegrator:
    def __init__(self, clone_url, model_name='gpt-4', token_limit=1800000):
        self.clone_url = clone_url
        self.model_name = model_name
        self.encoding = tiktoken.encoding_for_model(model_name)
        self.supported_extensions = ['.md', '.txt']
        self.repo_dir = ""  # Will be set after cloning
        self.token_limit = token_limit

    def clone_repo(self):
        repo_name = os.path.basename(self.clone_url)
        if repo_name.endswith('.wiki.git'):
            self.repo_dir = repo_name[:-len('.wiki.git')]
        else:
            self.repo_dir = repo_name
        Repo.clone_from(self.clone_url, self.repo_dir)

    def combine_files(self):
        combined_content = ""
        for root, dirs, files in os.walk(self.repo_dir):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext in self.supported_extensions:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                        combined_content += "\n" + file_content
        return combined_content

    def split_and_save(self, content):
        tokens = self.encoding.encode(content)

        for file_index, chunk in enumerate(self.split_tokens(tokens), start=1):
            file_name = os.path.join(self.repo_dir, f"split_file_{file_index}.txt")
            self.save_content(chunk, file_name)

    def split_tokens(self, tokens):
        while tokens:
            yield tokens[:self.token_limit]
            tokens = tokens[self.token_limit:]

    def save_content(self, content, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

    def process_wiki(self):
        self.clone_repo()
        combined_content = self.combine_files()
        with os.scandir(self.repo_dir) as original_dir:
            self.split_and_save(combined_content)

if __name__ == "__main__":
    clone_url = input("Enter the GitHub Wiki repository clone URL: ")
    integrator = GitHubWikiIntegrator(clone_url)
    integrator.process_wiki()
