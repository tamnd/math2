---
tag: 0YBVKMYX0W
kind: statement
role: theorem
name: Identity theorem
aliases: [uniqueness-theorem-for-holomorphic-functions]
msc: [30C15]
uses: [0DG0Z72CQD, 097KNJFJ7V, 0K83KEJ43P]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Identity_theorem
    locator: Proof
same_as:
  wikidata: Q1038716
  wikipedia: Identity theorem
inventory: [WV3SN733GH]
---

## Statement

Let $D \subseteq \mathbb{C}$ be a [[domain|097KNJFJ7V]] and let $f, g : D \to \mathbb{C}$ be [[holomorphic|0DG0Z72CQD]] on $D$.
Let $S = \{z \in D : f(z) = g(z)\}$.
Assume that $S$ has an accumulation point in $D$. This means that there is $z_0 \in D$ such that each disc with center $z_0$ contains a point of $S$ other than $z_0$.
Then $f(z) = g(z)$ for each $z \in D$.

## Remarks

Proof idea: apply the [[isolated zeros theorem|0K83KEJ43P]] to $f - g$. The set of points near which $f - g = 0$ is open, closed in $D$ and not empty, so it is $D$ because $D$ is connected.
For example, if $f$ is entire and $f(1/n) = 0$ for each $n \ge 1$, then $f = 0$.
The connectedness of $D$ is necessary: on the union of two disjoint discs, a function can be $0$ on one disc and $1$ on the other.
The theorem makes [[analytic continuation|0M3YQJ81NB]] unique.

## Explanations

### L1 human

Two holomorphic functions on a domain that agree on a small piece, even on a convergent sequence of points with its limit, agree everywhere.
So a holomorphic function is fixed everywhere by its values on a small disc.
