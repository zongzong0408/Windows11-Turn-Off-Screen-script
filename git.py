from datetime import datetime
import sys
import os

def main() -> None:

    current_time        = datetime.now()
    show_time           = current_time.strftime("%Y/%m/%d %H:%M")
    
    repository_path     = os.getcwd()
    repository_branch   = "main"
    commit_message      = ""

    commit_message = input("system ENTER (commit message): ")
    if commit_message == "":
        commit_message = show_time

    sys.stdout.write(f"system INFO:\t now times is:\t{show_time}\n")
    sys.stdout.write(f"system INFO:\t repository path is:\t{repository_path}\n")
    sys.stdout.write(f"system INFO:\t repository branch is:\t{repository_branch}\n")
    sys.stdout.write(f"system INFO:\t commit message is:\t{commit_message}\n")
    if input("system ENTER (are you sure you want commit all files ? y or n): ") == "n" or "":
        return

    sys.stdout.write("system INFO:\t starting git process...\n\n")
    os.chdir(repository_path)
    os.system("git add .")
    os.system(f'git commit -m "{commit_message}"')
    os.system(f"git push origin {repository_branch}")
    
    sys.stdout.write("\n\nsystem OK:\t git commit all & push all successful!\n")
    os.system("pause")

    return

main()