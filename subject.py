import rx
import rx.operators as ops
from rx.subject import Subject


def component_a(input):
    return input.pipe(
        ops.map(lambda i: i*2)
    )


def component_b(input):
    input.subscribe(
        on_next=lambda i: print("item: {}".format(i)),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("Done")
    )
    return rx.from_([1, 2, 3])


b_in_proxy = Subject()
b_out = component_b(b_in_proxy)
a_out = component_a(b_out)
a_out.subscribe(b_in_proxy)