import PyInstaller.__main__
import toml
import platform


def main() -> None:
    with open("pyproject.toml") as f:
        file = toml.load(f)
    ver = str(file['tool']['poetry']['version'])
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--console',
        f'--name=numbguess-{ver}-{platform.uname().system}'
    ])


if __name__ == "__main__":
    main()
