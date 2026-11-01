---
tag: XBDB3YNV9S
kind: definition
name: Schnirelmann density
msc: [11B05, 11B13]
defines: QHH8RY9XCZ
uses: [0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Schnirelmann_density
---

## Definition

Let $A$ be a subset of the [[natural numbers|0MWKJ44V5A]].
For each integer $n \ge 1$, let $A(n)$ be the number of elements $a \in A$ with $1 \le a \le n$.
The *Schnirelmann density* of $A$ is
$$\sigma(A) = \inf_{n \ge 1} \frac{A(n)}{n}.$$

## Remarks

Always $0 \le \sigma(A) \le 1$, and $A(n) \ge \sigma(A)\, n$ for every $n \ge 1$.
The element $0$, if present, does not count.
One has $\sigma(A) = 1$ if and only if $A$ contains every positive integer.

Example: for the set $A$ of odd positive integers, $A(n)/n = 1/2$ for even $n$ and $A(n)/n = (n+1)/(2n) > 1/2$ for odd $n$; so $\sigma(A) = 1/2$.
Contrast: for the even positive integers, $A(1)/1 = 0$, so $\sigma(A) = 0$, although their [[natural density|RVG9Z8NYA6]] is $1/2$.

Schnirelmann's inequality: if $0 \in A$ and $0 \in B$, then $\sigma(A + B) \ge \sigma(A) + \sigma(B) - \sigma(A)\sigma(B)$, where $A + B = \set{a + b : a \in A, b \in B}$.
