---
tag: EHH9KQHYFA
kind: definition
name: Karatsuba algorithm
msc: [68W30, 68W40, 11Y16]
defines: CD5Y77KGYA
uses: [9DMSG5HAQX, G9NFJ55KCX]
sources:
  - url: https://en.wikipedia.org/wiki/Karatsuba_algorithm
---

## Definition

Fix an integer base $B \ge 2$.
The *Karatsuba algorithm* is the recursive [[algorithm|9DMSG5HAQX]] that computes the product $xy$ of two non-negative integers $x, y$ as follows.

1. If $x < B$ or $y < B$, compute $xy$ directly.
2. Otherwise, let $k \ge 1$ be the least integer with $x, y < B^{2k}$, and write $x = x_1 B^k + x_0$ and $y = y_1 B^k + y_0$ with $0 \le x_0, y_0 < B^k$.
3. Compute recursively $z_2 = x_1 y_1$, $z_0 = x_0 y_0$ and $z_3 = (x_1 + x_0)(y_1 + y_0)$.
4. Return $z_2 B^{2k} + (z_3 - z_2 - z_0) B^k + z_0$.

The output is correct because $z_3 - z_2 - z_0 = x_1 y_0 + x_0 y_1$, so the returned number equals $(x_1 B^k + x_0)(y_1 B^k + y_0)$.

## Remarks

Example: with $B = 10$, $x = 12$, $y = 34$ and $k = 1$, one gets $z_2 = 3$, $z_0 = 8$ and $z_3 = 3 \cdot 7 = 21$.
The result is $3 \cdot 100 + (21 - 3 - 8) \cdot 10 + 8 = 408 = 12 \cdot 34$.

Non-example: computing the four products $x_1 y_1$, $x_1 y_0$, $x_0 y_1$, $x_0 y_0$ recursively is also correct, but it is not the Karatsuba algorithm.
Its cost satisfies $T(n) = 4 T(n/2) + O(n)$, which gives only $O(n^2)$.

For $n$-digit inputs with $k$ about $n/2$, the cost of the Karatsuba algorithm satisfies $T(n) = 3 T(n/2) + O(n)$.
By the [[master theorem|3WNSDAEMQQ]], $T(n) = O(n^{\log_2 3})$ in asymptotic notation.
