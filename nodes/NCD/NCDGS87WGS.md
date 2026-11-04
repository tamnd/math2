---
tag: NCDGS87WGS
kind: statement
role: proposition
name: Powers and inverse of a matrix factored as P D P^{-1}
msc: [15A20]
uses: [07SQCNV233, 0EB9N0S33C, 044JNC7ZAA]
about: [0TNR9BQ871]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section4-3.xml#L953
    locator: src/section4-3.xml:953
---

## Statement

Let $A$ be a square matrix with $A = P D P^{-1}$, where $P$ is an [[invertible matrix|0EB9N0S33C]] and $D$ is a [[diagonal matrix|044JNC7ZAA]]. This is a factoring of a [[diagonalisable matrix|07SQCNV233]].

Then $A^k = P D^k P^{-1}$ for every integer $k \ge 1$.

If $A$ is also invertible, then $D$ is invertible and $A^{-1} = P D^{-1} P^{-1}$.

## Remarks

In the product $(P D P^{-1})(P D P^{-1})\cdots$, each inner pair $P^{-1} P$ is the identity, so only one $P$ and one $P^{-1}$ remain.

The power $D^k$ is the diagonal matrix whose entries are the $k$-th powers of the entries of $D$.

When $A$ is invertible, no diagonal entry of $D$ is zero, and $D^{-1}$ has the reciprocals of the entries of $D$ on its diagonal.
