---
tag: 0DT0TCV75N
kind: definition
name: Set difference
msc: ["03E20"]
defines: 05WTQ6FFPS
uses: [0SJ3RX9TXA, 0EZ758XE73, 0XR7A7RSXB]
sources:
  - url: https://en.wikipedia.org/wiki/Complement_(set_theory)
    locator: Relative complement
---

## Definition

Let $A$ and $B$ be [[sets|0SJ3RX9TXA]].
The set difference of $A$ and $B$ is the set
$$A \setminus B = \{x \in A \mid x \notin B\}.$$
It is also called the relative complement of $B$ in $A$.

## Remarks

Another notation is $A - B$.
Example: $\{1, 2, 3\} \setminus \{2, 4\} = \{1, 3\}$.
The set $B$ need not be a subset of $A$.
In general, $A \setminus B \neq B \setminus A$.

## Explanations

### L1 human

To compute $A \setminus B$, start with $A$ and remove each element that is also in $B$.
Elements of $B$ that are not in $A$ do not matter.
