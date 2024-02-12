
abspath = Path.cwd() / FILENAME

if abspath.is_file():
    result = 'file'
elif abspath.is_dir():
    result = 'directory'
elif not abspath.exists():
    result = 'missing'
