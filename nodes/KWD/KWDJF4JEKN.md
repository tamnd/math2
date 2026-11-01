---
tag: KWDJF4JEKN
kind: definition
name: Real closure
msc: [12J15, "12D15"]
defines: 778KFSM09P
uses: [010JCV9J4E, X32TSWJSYT, 09EYMKMSB9, 0MB4TGMXG6]
sources:
  - url: https://en.wikipedia.org/wiki/Real_closed_field
---

## Definition

A field $R$ is *real closed* if $R$ is [[formally real|X32TSWJSYT]] and no [[algebraic extension|09EYMKMSB9]] $R' \ne R$ of $R$ is formally real.
Let $(F, \le)$ be an [[ordered field|010JCV9J4E]].
A *real closure* of $(F, \le)$ is an algebraic extension $R$ of $F$ such that:

1. $R$ is real closed;
2. the ordering of $R$, in which the nonnegative elements are the squares, restricts to $\le$ on $F$.

## Remarks

A real closed field has exactly one ordering, given by $a \ge 0$ if and only if $a$ is a square, so clause 2 makes sense.
Equivalently, $R$ is real closed if and only if two things hold.
It has an ordering in which every positive element is a square, and every polynomial of odd degree over $R$ has a root in $R$.
Every ordered field has a real closure, and it is unique up to a unique isomorphism over $F$ that respects the orderings.
Example: the field of real [[algebraic numbers|0MB4TGMXG6]] is a real closure of $\Q$.
Non-example: $\R$ is real closed, but it is not a real closure of $\Q$, because it is not algebraic over $\Q$.
