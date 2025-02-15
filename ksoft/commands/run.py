import subprocess
from typing import List, Optional

def execute_command(command: List[str], cwd: Optional[str] = None) -> int:
    """
    Execute a shell command and return the exit code.
    
    Args:
        command: List of command arguments
        cwd: Working directory for command execution (optional)
        
    Returns:
        Exit code from the command execution
    """
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return result.returncode
    except Exception as e:
        print(f"Error executing command: {e}")
        return 1

def run(args: List[str]) -> int:
    """
    Main entry point for the run command.
    
    Args:
        args: Command line arguments
        
    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    if not args:
        print("Error: No command specified")
        return 1
        
    return execute_command(args)