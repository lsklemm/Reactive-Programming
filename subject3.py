from rx.subject import Subject
subject_test = Subject()
subject_test.subscribe(
   lambda x: print("The value is {0}".format(x))
)
subject_test.subscribe(
   lambda x: print("The value is {0}".format(x))
)
subject_test.on_next("A")
subject_test.on_completed()
subject_test.on_next("B")