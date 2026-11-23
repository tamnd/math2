---
tag: WXHVSE066S
kind: example
name: The standard model is a model of Robinson arithmetic
msc: ["03F30", "03C62"]
topics: [QHCRN4JVG0]
audience: grad
instance_of: [3K1AKGXF8A]
illustrates: [MVCH6N9SNW]
uses: [TT8MXRTVBM, 329ZG1Z0G5, WP27CABPA4, VM8TQ70CVJ, 0AK9TGSNXY]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
  - book: isbn:9780521857840
---

## Example

The ordinary natural numbers satisfy every axiom of Robinson arithmetic, and that one fact makes the theory consistent.
Let $\mathfrak{N}$ be the [[standard model|WP27CABPA4]] of the language of arithmetic, with domain $\mathbb{N}$.
We check that $\mathfrak{N}$ satisfies each axiom of [[Robinson arithmetic|TT8MXRTVBM]], so $\mathfrak{N}$ is a [[model|MVCH6N9SNW]] of $\mathsf{Q}$.
Let $m, n \in \mathbb{N}$ be any values of the variables.

1. $\mathsf{Q}1$: $S^{\mathfrak{N}}(m) = m + 1 \ge 1$, so $m + 1 \ne 0$.
2. $\mathsf{Q}2$: if $m + 1 = n + 1$, then $m = n$, by cancelling $1$.
3. $\mathsf{Q}3$: if $m \ne 0$, then $m \ge 1$, and $k = m - 1 \in \mathbb{N}$ satisfies $m = k + 1$.
4. $\mathsf{Q}4$: $m + 0 = m$.
5. $\mathsf{Q}5$: $m + (n + 1) = (m + n) + 1$, by the associativity of addition.
6. $\mathsf{Q}6$: $m \cdot 0 = 0$.
7. $\mathsf{Q}7$: $m \cdot (n + 1) = m n + m$, by distributivity.
8. $\mathsf{Q}8$: if $m < n$, then $v = n - m - 1 \in \mathbb{N}$ satisfies $v + (m + 1) = n$.
   Conversely, $v + (m + 1) = n$ gives $n \ge m + 1 > m$.

So every axiom of $\mathsf{Q}$ holds in $\mathfrak{N}$ for all values of its variables.

## Remarks

The example gives the [[consistency|VM8TQ70CVJ]] of $\mathsf{Q}$, because a theory with a model proves no contradiction, by soundness.
It also bounds what $\mathsf{Q}$ proves from above: every theorem of $\mathsf{Q}$ is true in $\mathfrak{N}$.

Notice that steps 5 and 7 use associativity and distributivity, laws of $\mathbb{N}$ that $\mathsf{Q}$ itself does not prove.
The check happens outside the theory, in ordinary mathematics, where these laws are available.
The converse bound fails: $\mathsf{Q}$ does not prove everything that is true in $\mathfrak{N}$, as [[a model in which addition is not commutative|PR8Z1YPJDK]] shows.

## Explanations

### L1 human

The rules of Robinson arithmetic are true for the ordinary numbers $0, 1, 2, \ldots$.
For example, rule 7 says $m \cdot (n + 1) = m \cdot n + m$, and this is how multiplication works: $3 \cdot 5 = 3 \cdot 4 + 3$.
So the ordinary numbers are one world in which all the rules hold.

### L2 human

We test $\mathsf{Q}7$ and $\mathsf{Q}8$ on specific numbers.
For $\mathsf{Q}7$ with $m = 3$ and $n = 4$, both sides give 15:
$$3 \cdot 5 = 15, \qquad 3 \cdot 4 + 3 = 12 + 3 = 15.$$
For $\mathsf{Q}8$ with $m = 2$ and $n = 7$, the fact $2 < 7$ matches the witness $v = 4$, since $4 + 3 = 7$.
For $\mathsf{Q}8$ with $m = 7$ and $n = 2$, the fact that $7 < 2$ is false matches the fact that $v + 8 = 2$ has no solution in $\mathbb{N}$.

The typical use of this example is to prove that $\mathsf{Q}$ is consistent.
Watch out: it does not follow that $\mathsf{Q}$ proves every truth about $\mathfrak{N}$.
A theory can be true in a model and still be far from complete.
