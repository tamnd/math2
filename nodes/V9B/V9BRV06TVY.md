---
tag: V9BRV06TVY
kind: definition
name: Unital
msc: ["51E05", "51E15", 05B05]
defines: V051BD0CZG
uses: [4JCSS2Z1BA, 7BPSC4T4M3, DANFNN8C4Y, 48P4A1CX85, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Unital_(geometry)
---

## Definition

Let $n \ge 2$ be an integer.
A *unital of order $n$* is a [[block design|4JCSS2Z1BA]] $(X, \mathcal{B})$ such that:

1. the point set $X$ has $n^3 + 1$ elements;
2. every block $B \in \mathcal{B}$ has $n + 1$ elements;
3. any two distinct points of $X$ lie in exactly one common block.

## Remarks

Equivalently, a unital of order $n$ is a [[Steiner system|7BPSC4T4M3]] $S(2, n + 1, n^3 + 1)$.

Let $\Pi$ be a [[projective plane|DANFNN8C4Y]] of order $n^2$.
A unital is *embedded* in $\Pi$ if $X$ is a set of points of $\Pi$ and the blocks are the intersections of $X$ with lines that have size $n + 1$.
In that case every line of $\Pi$ meets $X$ in $1$ or $n + 1$ points.

Example: let $q$ be a prime power and let $\F_{q^2}$ be the [[finite field|0ZXZ82FTX2]] with $q^2$ elements.
In $\mathrm{PG}(2, q^2)$, the Hermitian curve $x^{q+1} + y^{q+1} + z^{q+1} = 0$, the set of isotropic points of a non-degenerate [[Hermitian form|48P4A1CX85]], has $q^3 + 1$ points.
Each line meets it in $1$ or $q + 1$ points, so with the secant lines as blocks it is a unital of order $q$.

Non-example: in the Fano plane, blocks have size $3$ and any two points lie in exactly one block.
But it has $7$ points rather than $2^3 + 1 = 9$, so clause 1 fails.
