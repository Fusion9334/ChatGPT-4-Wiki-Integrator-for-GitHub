import os
import subprocess
from tiktoken import tiktoken

class GitHubWikiIntegrator:
    def __init__(self, clone_url, model_name='gpt-4'):
        self.clone_url = clone_url
        self.model_name = model_name
        self.encoding = tiktoken.encoding_for_model(model_name)
        self.token_limit = 1800000  # 90% of 2 million tokens
        self.supported_extensions = ['.md', '.txt']
        self.repo_dir = ""  # Will be set after cloning

    def clone_repo(self):
        repo_name = self.clone_url.split('/')[-1]
        if repo_name.endswith('.wiki.git'):
            self.repo_dir = repo_name[:-len('.wiki.git')]
        else:
            self.repo_dir = repo_name
        subprocess.run(["git", "clone", self.clone_url])
        os.chdir(self.repo_dir)

    def combine_files(self):
        combined_content = ""
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(tuple(self.supported_extensions)):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                        combined_content += "\n" + file_content
        return combined_content

    def split_and_save(self, content):
        tokens = self.encoding.encode(content)
        if len(tokens) <= self.token_limit:
            self.save_content(content, "master_file.txt")
        else:
            self.split_content(tokens)

    def split_content(self, tokens):
        chunk = tokens[:self.token_limit]
        remaining = tokens[self.token_limit:]
        file_index = 1

        while chunk:
            decoded_chunk = self.encoding.decode(chunk)
            self.save_content(decoded_chunk, f"split_file_{file_index}.txt")
            file_index += 1
            chunk = remaining[:self.token_limit]
            remaining = remaining[self.token_limit:]

    def save_content(self, content, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

    def process_wiki(self):
        self.clone_repo()
        combined_content = self.combine_files()
        self.split_and_save(combined_content)
        os.chdir("..")  # Return to the original directory

if __name__ == "__main__":
    clone_url = input("Enter the GitHub Wiki repository clone URL: ")
    integrator = GitHubWikiIntegrator(clone_url)
    integrator.process_wiki()
