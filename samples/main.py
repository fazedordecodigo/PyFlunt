import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ]
)


log = logging.getLogger(__name__)


def time_me(function):
    def wrap(*arg):
        start = time.time()
        r = function(*arg)
        end = time.time()
        log.info(f"{function.__name__} ({(end-start)*1000:0.3f} ms)")
        return r
    return wrap

# Not Existing
@time_me
def with_try(iterations):
    d = {"somekey": 123}
    for _i in range(iterations):
        try:
            d["notexist"]
        except:  # noqa: E722
            pass

@time_me
def with_try_exc(iterations):
    d = {"somekey": 123}
    for _i in range(iterations):
        try:
            d["notexist"]
        except Exception as e:  # noqa: F841
            pass

@time_me
def without_try(iterations):
    d = {"somekey": 123}
    for _i in range(iterations):
        if "notexist" in d:
            pass
        else:
            pass

@time_me
def without_try_not(iterations):
    d = {"somekey": 123}
    for _i in range(iterations):
        if "notexist" not in d:
            pass
        else:
            pass

# Existing
@time_me
def exists_with_try(iterations):
    d = {"somekey": 123}
    for _i in range(iterations):
        try:
            d["somekey"]
        except:  # noqa: E722
            pass

@time_me
def exists_unsafe(iterations):
    d = {"somekey": 123}
    for _i in range(iterations):
        d["somekey"]

# @time_me
# def exists_with_try_exc(iterations):
#     d = {"somekey": 123}
#     for _i in range(iterations):
#         try:
#             d["somekey"]
#         except Exception:
#             pass

@time_me
def exists_without_try(iterations):
    d = {"somekey": 123}
    for _i in range(iterations):
        if "somekey" in d:
            d["somekey"]
        else:
            pass

@time_me
def exists_without_try_not(iterations):
    d = {"somekey": 123}
    for _i in range(iterations):
        if "somekey" not in d:
            pass
        else:
            d["somekey"]

# log.info("The case where the key does not exist:\n")
# log.info("100 iterations:")
# with_try(100)
# with_try_exc(100)
# without_try(100)
# without_try_not(100)

# log.info("\n")
# log.info("1,000,000 iterations:")
# with_try(1_000_000)
with_try_exc(1_000_000)
# without_try(1_000_000)
# without_try_not(1_000_000)

# log.info("\n")
# log.info("The case where the key does exist:\n")

# log.info("100 iterations:")
# exists_unsafe(100)
# exists_with_try(100)
# exists_with_try_exc(100)
# exists_without_try(100)
# exists_without_try_not(100)


# log.info("\n")
# log.info("1,000,000 iterations:")
# exists_unsafe(1_000_000)
# exists_with_try(1_000_000)
# exists_with_try_exc(1_000_000)
# exists_without_try(1_000_000)
# exists_without_try_not(1_000_000)
