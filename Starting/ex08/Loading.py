import shutil


def ft_tqdm(lst: range) -> None:
    """
    Simulate a progress bar for iterating through a range.

    Args:
        lst (range): The range to iterate through.

    Yields:
        Any: The current item from the range.
        is a keyword in Python used in the context of creating generators.
        Generators are a way to create iterators, which are objects used to
        iterate over a sequence of values without having to store all those
        values in memory at once. Instead of generating allvalues and returning
        them in one go, a generator yields one value at a time whenever the
        yield statement is encountered.
    """
    total = len(lst)
    progress_bar_width = shutil.get_terminal_size().columns - 40

    for i, item in enumerate(lst, start=1):
        progress = int(i / total * progress_bar_width)
        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        progress_percentage = progress * 100 // progress_bar_width

        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        print(f"\r{progress_info}", end="", flush=True)

        yield item
