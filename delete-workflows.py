import os
import requests

github_token = os.getenv('GITHUB_TOKEN')
repo_owner = os.getenv('REPO_OWNER')
repo_name = os.getenv('REPO_NAME')

base_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs'

headers = {
    'Authorization': f'Token {github_token}',
    'Accept': 'application/vnd.github.v3+json'
}

def delete_workflow_runs():
    response = requests.get(base_url, headers=headers)
    runs = response.json().get('workflow_runs', [])
    
    for run in runs:
        run_id = run['id']
        delete_url = f'{base_url}/{run_id}'
        delete_response = requests.delete(delete_url, headers=headers)
        
        if delete_response.status_code == 204:
            print(f'Successfully deleted workflow run {run_id}')
        else:
            print(f'Failed to delete workflow run {run_id}: {delete_response.json()}')

if __name__ == "__main__":
    delete_workflow_runs()
