---
tag: 0D0SMQYEJA
kind: statement
role: fact
name: Fibonacci recurrence
msc: [11B39]
uses: [0GA9K57A39]
sources:
  - url: https://en.wikipedia.org/wiki/Fibonacci_sequence
    locator: Definition
---

## Statement

Let $n$ be a natural number, and let $F_m$ be the [[Fibonacci numbers|0GA9K57A39]].
Then
$$F_{n+2} = F_{n+1} + F_n.$$

## Remarks

With the values $F_0 = 0$ and $F_1 = 1$, the recurrence determines the whole sequence.
The recurrence extends to negative indices with $F_{-n} = (-1)^{n+1} F_n$.

## Explanations

### L1 human

To get the next Fibonacci number, add the last two.
From $3$ and $5$ you get $8$, and from $5$ and $8$ you get $13$.
