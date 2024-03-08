from argparse import Namespace


class TypedNamespace(Namespace):
    read: str
    output: str
    url_base: str
    times: int
    timeout: int
    retry_times: int
    sentences: bool
    proxies: dict | None
    languages: list[str]
    cookies: str | None
    max_thread_cnt: int
    separator: str
