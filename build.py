import PyInstaller.__main__


def main() -> None:
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--console'
    ])


if __name__ == "__main__":
    main()
