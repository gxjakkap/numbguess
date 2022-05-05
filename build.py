import shutil
import PyInstaller.__main__
import toml
import platform
import os
import shutil


def main() -> None:
    # open pyproject.toml to get version number
    with open("pyproject.toml") as f:
        file = toml.load(f)
    # get version number and filename
    ver = str(file['tool']['poetry']['version'])
    name = f'numbguess-{ver}-{platform.uname().system.lower()}'
    # build an excutable
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--console',
        f'--name={name}',
        '-p /gamemode/*.py'
    ])
    # cleanup build cache
    os.remove(f'./{name}.spec')
    shutil.rmtree(f'build/{name}')


if __name__ == "__main__":
    main()
