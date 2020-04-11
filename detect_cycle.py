def has_cycle(head):
    fp = head.next
    if fp:
        fp = fp.next
    sp = head
    cycle = False
    while fp != None:
        if fp == sp or fp.next == sp:
            cycle = True
            break
        sp = sp.next
        fp = fp.next
        if fp:
            fp = fp.next
    return cycle