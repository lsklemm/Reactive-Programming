import rx, operator as op

obs1 = rx.from_([1, 2, 3, 4])
obs2 = rx.from_([5, 6, 7, 8])

res = rx.merge(obs1, obs2)
res.subscribe(print)