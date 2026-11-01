---
tag: S8Y8RVZY79
kind: definition
name: Divisible group
msc: [20K40, 20K25]
defines: ZXVBEPMTCN
uses: [082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Divisible_group
---

## Definition

Let $A$ be an [[abelian group|082GHNPJ53]], written additively.
The group $A$ is *divisible* if for every $a \in A$ and every integer $n \ge 1$ there is $x \in A$ with $nx = a$.

## Remarks

Example: $\Q$ is divisible: given $a \in \Q$ and $n \ge 1$, take $x = a/n$.
Example: $\Q/\Z$ is divisible, as a quotient of the divisible group $\Q$.

Non-example: $\Z$ is not divisible, since there is no integer $x$ with $2x = 1$.
A nonzero finite abelian group is not divisible either: if $\abs{A} = m$ and $a \neq 0$, then $mx = 0 \neq a$ for every $x$.

An abelian group is divisible if and only if it is an [[injective|85H7PRHDPZ]] $\Z$-module.
It is enough to check the condition for $n$ prime.
Every divisible group is isomorphic to a direct sum of copies of $\Q$ and of the [[Prüfer groups|F0XAMM2PPS]] $\Z(p^\infty)$, for various primes $p$.
