import queue;

# スタック
stack = [];
stack.append(3);
stack.append(5);
stack.append(2);
print(stack.pop());
print(stack.pop());
print(stack.pop());

# キュー
q = queue.Queue();
q.put(3);
q.put(5);
q.put(2);
print(q.get());
print(q.get());
print(q.get());
