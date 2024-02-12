
def get_files(path: Path) -> Iterator[Path]:
    yield from path.glob(f'*.py')
    yield from path.glob(f'*.rst')
