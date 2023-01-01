from typing import Optional, Iterator, List, Callable, Dict, Generator, Iterable, Union

from HW_23.function import limit_query, map_query, sort_query, unique_query, regex_query, filter_query

CMD_TO_FUNCTIONS: Dict[str, Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'regex': regex_query,
}


def read_file(filename: str) -> Generator[str, None, None]:
    with open(filename) as file:
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        prepared_data: Union[Generator, Iterable[str]] = read_file(file_name)
    else:
        prepared_data = data
    result: Iterable[str] = CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data)
    return list(result)
