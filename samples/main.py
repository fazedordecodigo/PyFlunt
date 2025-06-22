import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)


log = logging.getLogger(__name__)


def time_me(function):  # type: ignore
    def wrap(*arg):  # type: ignore
        start = time.time()
        r = function(*arg)
        end = time.time()
        log.info(f"{function.__name__} ({(end - start) * 1000:0.3f} ms)")
        return r

    return wrap


@time_me
def with_try_exc(iterations):  # type: ignore
    d = {"somekey": 123}
    for _i in range(iterations):
        try:
            d["notexist"]
        except Exception as e:  # noqa: F841
            pass

with_try_exc(1_000_000)
