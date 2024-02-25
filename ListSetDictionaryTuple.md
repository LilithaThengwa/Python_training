# Sets
- Unordered
- Iterable.
- Mutable.
- No duplicate elements.
- Collection is enclosed by curly braces.
- Major advantage over a list is that it has a highly optimized method for checking whether a specific element is contained in the set. This is based on a data structure known as a hash table. - Since sets are unordered, we cannot access items using indexes like with lists.
- Declaration: myset = set() or myset = {}
- Cannot assign or change a value once the set is created. We can only add or delete items in the set.
- Has the following methods: add(), union(), intersection(), difference(), clear()
- Not sequence.

# Lists
- Ordered, mutable, and allow duplicates.
- Indexed, starting at zero.
- Can be declared: mylist = list() or mylist = []
- Some methods: pop() removes the last item, by index. Changes the original array. Slicing doesn't change the original array. Remove and append mutate it as well. Remove removes a specific item.
- Iterable and sequence.

# Dictionaries
- Ordered(version 3.7), mutable and no duplicates.
- A data structure, used to store values in key:value format.
- Declaration: mydict = dict() or mydict = {"":""}
- Keys must be unique.
- ** unpacking operator for dictionaries.
- get() doesn't throw an error if the value is not found.
- Iterable only.
