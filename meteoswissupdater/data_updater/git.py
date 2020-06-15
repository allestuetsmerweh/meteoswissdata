import subprocess

def git_setup(
    name,
    email,
    branch='data',
):
    subprocess.run(f'git branch -D {branch} || exit 0', shell=True)
    subprocess.run(f'git checkout --orphan {branch}', shell=True)
    subprocess.run(f'git rm --cached -r .', shell=True)
    subprocess.run(f'rm -Rf *', shell=True)

    subprocess.run(f'git config user.email "ci-build@hatt.style"', shell=True)
    subprocess.run(f'git config user.name "ci-build"', shell=True)
    subprocess.run(f'git remote set-url --push origin https://$GITHUB_ACTOR:$GITHUB_TOKEN@github.com/$GITHUB_REPOSITORY', shell=True)

def git_push(
    commit_message,
    branch='data',
):
    subprocess.run(f'git add .', shell=True)
    subprocess.run(f'git commit -m "{commit_message}"', shell=True)
    subprocess.run(f'git push -f --set-upstream origin {branch}', shell=True)
