from .command_execution import execute_command

def run_script(script_path, args=None):
    command = f"python {script_path}"
    if args:
        command += f" {' '.join(args)}"
    return execute_command(command)
