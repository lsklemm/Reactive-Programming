from rx.subject import Subject
subject_test = Subject()
subject_test.subscribe(
   on_error = lambda e: print("Error : {0}".format(e))
)
subject_test.subscribe(
   on_error = lambda e: print("Error : {0}".format(e))
)
subject_test.on_error(Exception('There is an Error!'))