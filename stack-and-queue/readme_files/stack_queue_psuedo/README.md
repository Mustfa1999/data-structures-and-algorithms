# Stack Queue Psuedo

> [Back to main](../../README.md)

---

# Challenge Summary

Build a class that build a queue from 2 stacks

## Pull Request

> [PR 2](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/10)

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

enqueue: just push the value to the stack 1

dequeue: empty the stack 1 inside 2 then pop the last item in 2 

Big(o) for both time and space in enqueue is o(1),and in dequeue is o(n) 

## Solution

```
class PseudoQueue:
    """
    Implements a Queue using two Stacks.
    """
    
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """
        Inserts value into the PseudoQueue, using a first-in, first-out approach.
        """

        self.stack1.push(value)

    def dequeue(self):
        """
        Extracts a value from the PseudoQueue, using a first-in, first-out approach.
        """
        
        if not self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        if not self.stack1.is_empty():
            return self.stack1.pop()
        else:
            raise(Exception("Pseudo Queue is empty !"))


    def is_empty(self):
        return True if self.stack1.is_empty() and self.stack2.is_empty() else False

    
    def size(self):
        return self.stack1.size() + self.stack2.size()

    def front(self):
        if not self.stack2.is_empty():
            return self.stack2.peek()
        elif not self.stack1.is_empty():
            return self.stack1.reverse().peek()
        else:
            raise(Exception("Pseudo Queue is empty !"))
```

## tests

```
def test_enqueue():
    pseudoQ = PseudoQueue()
    [pseudoQ.enqueue(i) for i in ["Mustafa", "Zaid", "Barham"]]
    assert pseudoQ.dequeue() == "Barham"

def test_dequeue(my_pseudo_queue):
    assert my_pseudo_queue.dequeue() == "Barham"

def test_dequeue_empty():
    with pytest.raises(Exception):
        PseudoQueue().dequeue()

# =============================================
# =============================================
# =============================================

@pytest.fixture
def my_pseudo_queue():
    q = PseudoQueue()
    [q.enqueue(i) for i in ["Mustafa", "Zaid", "Barham"]]
    return q

```

