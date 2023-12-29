import os
import sys
import subprocess

comfy_path = '../..'
if sys.argv[0] == 'install.py':
    sys.path.append('.')  # for portable version

print("### ComfyUI-ownimage: Check dependencies")

if "python_embeded" in sys.executable or "python_embedded" in sys.executable:
    pip_install = [sys.executable, '-s', '-m', 'pip', 'install']
else:
    pip_install = [sys.executable, '-m', 'pip', 'install']


def ensure_pip_packages():
    try:
        import cython
    except Exception:
        my_path = os.path.dirname(__file__)
        requirements_path = os.path.join(my_path, "requirements.txt")
        subprocess.check_call(pip_install + ['-r', requirements_path])


def install():
    ensure_pip_packages()
