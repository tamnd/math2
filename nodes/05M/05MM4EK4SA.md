---
tag: 05MM4EK4SA
kind: statement
role: corollary
name: Groups of prime order are cyclic
msc: [20D60]
about: [0KVGH0J5B3, 01826KMG2H, 0B85S2V2DR]
uses: [3C53TD, 0B85Q41RP6, 031M8HX7DA]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange's_theorem_(group_theory)
    locator: Applications
---

## Statement

Let $p$ be a prime number and let $G$ be a [[group|G5S1M9]] of order $p$.
Then $G$ is [[cyclic|0KVGH0J5B3]], and each element of $G$ other than the identity generates $G$.

## Remarks

If $g \neq e$, then the order of $\langle g \rangle$ is greater than $1$ and divides $p$ by [[Lagrange's theorem|3C53TD]], so it is $p$.
Thus each group of order $p$ is isomorphic to $\mathbb{Z}/p\mathbb{Z}$.
A group of prime order has no subgroups except $\{e\}$ and itself.

## Explanations

### L1 human

When the size of a group is a prime, there is no room for proper subgroups other than the trivial one.
Any element other than the identity generates a subgroup larger than $1$, so it generates everything.
Thus, for example, each group with $7$ elements is a clock with $7$ hours.

### L2 agent

A prime $p$ has only the divisors $1$ and $p$. With Lagrange's theorem, this leaves a group of order $p$ no room for subgroups other than $\{e\}$ and the whole group.

The proof is short:

1. Let $g \in G$ with $g \ne e$.
2. The order of $g$ divides $p$, so it is $1$ or $p$.
3. Only $e$ has order $1$. Thus $\operatorname{ord}(g) = p$.
4. Thus $\langle g \rangle$ has $p$ elements, and it is all of $G$.

A worked example with $p = 5$ and $G = \mathbb{Z}/5\mathbb{Z}$:

1. Take $g = 2$. Its multiples are $2, 4, 1, 3, 0$.
2. All five elements occur, so $2$ generates $G$.
3. The same is true for $1$, $3$ and $4$, as the result states.

A consequence is that, up to isomorphism, there is exactly one group of each prime order $p$, namely $\mathbb{Z}/p\mathbb{Z}$. Thus the groups of order $2$, $3$, $5$ and $7$ are all cyclic and abelian.

The hypothesis that $p$ is prime is necessary. The Klein four-group has order $4$, and it is not cyclic. The group $S_3$ has order $6$, and it is not even abelian.

A common error is to think that the result also gives a generator for groups of prime power order. A group of order $p^2$ is abelian, but it need not be cyclic, as $\mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/p\mathbb{Z}$ shows.
