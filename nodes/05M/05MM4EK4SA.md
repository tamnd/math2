---
tag: 05MM4EK4SA
kind: statement
role: corollary
name: Groups of prime order are cyclic
msc: [20D60]
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
