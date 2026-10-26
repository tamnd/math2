---
tag: ~f0fe5a7f
kind: statement
role: theorem
name: Addition formula for Fibonacci numbers
msc: [11B39]
uses: [~bc16f766]
sources:
  - url: https://en.wikipedia.org/wiki/Fibonacci_sequence
    locator: Other identities
---

## Statement

Let $m$ and $n$ be natural numbers, and let $F_k$ be the [[Fibonacci numbers|~bc16f766]].
Then
$$F_{m+n+1} = F_m F_n + F_{m+1} F_{n+1}.$$

## Remarks

With $m = n$ it gives $F_{2n+1} = F_n^2 + F_{n+1}^2$.
An equivalent form is $F_{m+n} = F_{m-1} F_n + F_m F_{n+1}$ for $m \ge 1$.
The formula is the basis of fast algorithms that compute $F_n$ with $O(\log n)$ arithmetic operations.

## Explanations

### L1 human

To get a Fibonacci number with a large index, you can combine Fibonacci numbers with smaller indices.
For example, with $m = 2$ and $n = 3$: $F_6 = F_2 F_3 + F_3 F_4 = 1 \cdot 2 + 2 \cdot 3 = 8$.
