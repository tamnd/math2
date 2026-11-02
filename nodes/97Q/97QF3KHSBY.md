---
tag: 97QF3KHSBY
kind: statement
role: theorem
name: Ackermann function is not primitive recursive
msc: [03D20]
uses: [5NVA2JRHPV, KZSB5E471K]
about: [N470JF7ZJX, 5NVA2JRHPV]
sources:
  - url: https://en.wikipedia.org/wiki/Ackermann_function
---

## Statement

Let $A \colon \N \times \N \to \N$ be the [[Ackermann function|N470JF7ZJX]], given by $A(0, n) = n + 1$, $A(m + 1, 0) = A(m, 1)$ and $A(m + 1, n + 1) = A(m, A(m + 1, n))$.
Then $A$ is a total [[computable function|KZSB5E471K]] that is not [[primitive recursive|5NVA2JRHPV]].

## Remarks

The key lemma is a domination result.
For every primitive recursive $f \colon \N^k \to \N$ there is $m \in \N$ such that $f(\bar x) < A(m, \max \bar x)$ for all $\bar x \in \N^k$.
It is proved by induction on the construction of $f$, using that $A$ is increasing in each argument.
If $A$ were primitive recursive, so would be $g(n) = A(n, n)$.
Then some $m$ would give $A(n, n) < A(m, n)$ for all $n$, which fails at $n = m$.

The theorem shows that the class of primitive recursive functions is strictly smaller than the class of total computable functions.
Computability of $A$ follows from the fact that the recursion decreases the pair $(m, n)$ in the lexicographic order.

## Explanations

### L1 human

Primitive recursive functions are those computed by programs whose loops have bounds fixed before they start.
The Ackermann function can be computed, but it grows so fast that no such program keeps up with it.
So bounded loops are not enough to compute everything computable.

### L2 human

Each primitive recursive function is dominated by one level $n \mapsto A(m, n)$ of the Ackermann function.
The diagonal $n \mapsto A(n, n)$ escapes every level, so it is outside the class.
This is a diagonal argument, like the one that shows that no effective list of total computable functions contains all of them.
To reach all computable functions one adds unbounded search, which gives the [[general recursive functions|HBK5QHC1GC]].
