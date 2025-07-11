# ---------------------------------------------------------------------------
# 📚 THEORETICAL CHEAT-SHEET ── STACK & QUEUE (using a plain Python list)
# ---------------------------------------------------------------------------
# ▸ A *stack* is a **LIFO** (Last-In-First-Out) structure.
#     • Think of a stack of plates: the last plate you put on is the first you take off.
#     • Core operations:
#         – push(item): add item to the “top”.
#         – pop()      : remove & return the item from the “top”.
#     • With a Python list:
#         – list.append(x)  → O(1) average, perfect for push.
#         – list.pop()      → O(1) average, perfect for pop.
#     • Uses: undo history, call stack, DFS, expression evaluation (postfix/infix).
#
# ▸ A *queue* is a **FIFO** (First-In-First-Out) structure.
#     • Think of people in a ticket line: first person in is served first.
#     • Core operations:
#         – enqueue(item): add item to the “rear”.
#         – dequeue()    : remove & return item from the “front”.
#     • With a Python list:
#         – list.append(x)  → add at the rear in O(1).
#         – list.pop(0)     → remove at index 0 (front).  ⚠ O(n) because items shift.
#         – Better choice for heavy queues: collections.deque (O(1) for both ends).
#     • Uses: task scheduling, BFS, printer job queue, I/O buffers.
#
# ▸ API DESIGN CHOICES (simple console demo below)
#     • Single shared list can simulate either structure, but keeping separate
#       lists makes intent clearer.
#     • Provide a text menu:
#         1. Push (stack)
#         2. Pop  (stack)
#         3. Enqueue (queue)
#         4. Dequeue (queue)
#         5. Exit
#     • Handle underflow: popping/dequeuing from an empty structure should warn
#       the user instead of crashing.
#
# ▸ BIG-O SUMMARY (list-based)
#     • Stack  : push O(1) | pop O(1)
#     • Queue  : enqueue O(1) | dequeue O(n)  (⇢ use deque for O(1)/O(1))
#
# ▸ KEY TAKEAWAYS
#     • Choose the structure that matches order requirements: LIFO vs FIFO.
#     • Python lists are fine for stacks, mediocre for queues if you dequeue a lot.
#     • APIs hide implementation; focus on behavior, not storage details.
#
# ---------------------------------------------------------------------------
# Minimal runnable demonstration below ⬇ (focus on theory; code kept tiny)
# ---------------------------------------------------------------------------

stack = []
while True:
    choice = input("enter 1 push 2 pop 3 display: ")
    if choice=="1":
        num = int(input("Enter a number: "))
        stack.append(num)
    elif choice=="2":
        if(len(stack)==0):
            print("stack is empty")
            continue
        print(f"Deleted element is: {stack.pop()}")
    elif choice=="3":
        if(len(stack)==0):
            print("stack is empty")
            continue
        print(f"elements of stack are: {stack}")
    else:
        print("invalid choice")
        break


queue = []
while True:
    choice = input("enter 1 eqQ 2 deQ 3 display")
    if choice=="1":
        num = int(input("Enter a number: "))
        queue.append(num)
    elif choice=="2":
        if(len(queue)==0):
            print("queue is empty")
            continue
        print(f"Deleted element is: {queue.pop(0)}")
    elif choice=="3":
        if(len(queue)==0):
            print("queue is empty")
            continue
        print(f"elements of queue are: {queue}")
    else:
        print("invalid choice")
        break

