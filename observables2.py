import rx
from rx import operators as ops

obs1 = rx.from_([1, 2, 3, 4])
obs2 = rx.from_([5, 6, 7, 8])

obs_list = [obs1, obs2]

res = rx.merge(*obs_list)
res.subscribe(print)