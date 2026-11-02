---
tag: N470JF7ZJX
kind: example
name: Ackermann function
msc: [03D20]
instance_of: [KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Ackermann_function
same_as:
  wikidata: Q341835
  wikipedia: Ackermann function
---

## Example

The Ackermann function, in the two-argument form of Rózsa Péter, is the function $A \colon \N \times \N \to \N$ given by
$$A(0, n) = n + 1, \qquad A(m + 1, 0) = A(m, 1), \qquad A(m + 1, n + 1) = A(m, A(m + 1, n)).$$
It is a total [[computable function|KZSB5E471K]].
Each right-hand side calls $A$ at a pair that is smaller in the lexicographic order on $\N \times \N$.
This order is a well-order, so the recursion stops on every input and gives an algorithm for $A$.

## Remarks

By induction on $n$, one gets $A(1, n) = n + 2$, $A(2, n) = 2n + 3$ and $A(3, n) = 2^{n+3} - 3$.
Then $A(4, 0) = A(3, 1) = 13$ and $A(4, 1) = A(3, 13) = 2^{16} - 3 = 65533$.
The function $A$ is not [[primitive recursive|5NVA2JRHPV]], see [[Ackermann function is not primitive recursive|97QF3KHSBY]].

## Explanations

### L1 human

The Ackermann function is a simple rule that produces enormous numbers very quickly.
Its first argument chooses the operation: adding, then something like multiplying, then something like taking powers, and so on.
The values $A(4, n)$ are already huge: $A(4, n) + 3$ is a tower of $n + 3$ twos, such as $A(4, 1) + 3 = 2^{2^{2^2}}$.
It was built to show that some computable functions cannot be defined with bounded loops alone.
