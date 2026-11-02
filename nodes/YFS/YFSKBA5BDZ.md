---
tag: YFSKBA5BDZ
kind: definition
name: Malcev completion
msc: ["22E25", "22E40", 20F18]
defines: V9GRK3QANS
uses: [DK87YN458D, BTYF5Y5PFY, 0Q7MMQHC1P, ZZYCV5EX9J]
sources:
  - url: https://en.wikipedia.org/wiki/Nilmanifold
---

## Definition

Let $\Gamma$ be a finitely generated, torsion-free [[nilpotent group|0Q7MMQHC1P]].
A *Malcev completion* of $\Gamma$ is a pair $(N, \iota)$ with three properties.

1. $N$ is a connected and simply connected [[nilpotent Lie group|DK87YN458D]].
2. $\iota \colon \Gamma \to N$ is an injective group homomorphism.
3. $\iota(\Gamma)$ is a [[lattice|BTYF5Y5PFY]] in $N$: it is discrete and $N/\iota(\Gamma)$ is compact.

## Remarks

Malcev proved that a Malcev completion exists and is unique up to a unique isomorphism compatible with $\iota$.
More generally, each homomorphism between two such groups $\Gamma$ extends uniquely to a continuous homomorphism of their completions.

Example: $\Gamma = \Z^n$ with $N = \R^n$ and $\iota$ the inclusion.
The group $\R^n$ is abelian, hence nilpotent, and simply connected; $\Z^n$ is discrete, and $\R^n/\Z^n$ is the compact torus.
In the same way, the integer [[Heisenberg group|ZZYCV5EX9J]] has the real Heisenberg group as Malcev completion.

Non-example: $\Gamma = \Z$ with $N = \R^2$ and $\iota(k) = (k, 0)$.
Clauses 1 and 2 hold, but $\R^2/\iota(\Z)$ is a cylinder, which is not compact, so clause 3 fails.

The name is also used for the rational Malcev completion of $\Gamma$.
It is a torsion-free nilpotent group containing $\Gamma$ in which each element has a unique $k$-th root for each $k \ge 1$.
Moreover, some positive power of each of its elements lies in $\Gamma$.
