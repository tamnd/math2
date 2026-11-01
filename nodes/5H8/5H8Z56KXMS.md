---
tag: 5H8Z56KXMS
kind: statement
role: theorem
name: Lasker–Noether theorem
msc: ["13A15", "13E05"]
uses: [0MVH4Y1CRZ, 0MYSA6MYNA, M2VPVJH33K, V026AAV8E6, 437YRCNYRJ, 1RJJ33KKSS]
about: [ZD34THCXQ0, ERFZ6S8X0X]
sources:
  - url: https://en.wikipedia.org/wiki/Primary_decomposition
---

## Statement

Let $R$ be a commutative [[Noetherian ring|0MVH4Y1CRZ]] and let $I \ne R$ be an [[ideal|0MYSA6MYNA]] of $R$.

1. $I$ has a minimal [[primary decomposition|M2VPVJH33K]] $I = Q_1 \cap \cdots \cap Q_n$.
2. In every minimal primary decomposition of $I$, the set of prime ideals $\set{\sqrt{Q_1}, \dots, \sqrt{Q_n}}$ is the same: it is the set of [[associated primes|1RJJ33KKSS]] of $R/I$.
3. If $\sqrt{Q_i}$ is minimal in this set, then the component $Q_i$ is the same in every minimal primary decomposition of $I$.

## Remarks

For existence, call an ideal irreducible if it is not the intersection of two strictly larger ideals.
By the [[Noetherian|0670T59HGE]] property, every proper ideal is a finite intersection of [[irreducible ideals|7PDWB550C9]], and in a Noetherian ring every irreducible ideal is primary.
Removing redundant terms and joining terms with the same radical gives a minimal decomposition.
For example, in $k[x, y]$ the ideal $(x^2, xy)$ has the minimal decompositions $(x) \cap (x^2, y)$ and $(x) \cap (x^2, xy, y^2)$.
In both, the primes are $(x)$ and $(x, y)$, and the component $(x)$ at the minimal prime is the same, while the [[embedded|RVKPM94MDF]] component changes.
Without the Noetherian hypothesis, existence can fail.
In the product ring $R = \prod_{i \in \N} \F_2$, every prime ideal is maximal and there are infinitely many, such as the kernels of the projections.
If $0 = Q_1 \cap \cdots \cap Q_n$ with $Q_i$ primary, then every prime contains some $\sqrt{Q_i}$, so $R$ would have at most $n$ prime ideals.

## Explanations

### L1 human

In a Noetherian ring every ideal can be written as an intersection of finitely many primary ideals.
The pieces are not always unique, but the primes behind them are.
This extends the unique factorisation of integers into prime powers.

### L2 human

The primes in the theorem are the associated primes, and the minimal ones among them are the minimal primes over $I$.
For an ideal of a polynomial ring, they describe the irreducible components of the zero set and the embedded points.
The same theorem holds for submodules of finitely generated modules over a Noetherian ring.
The uniqueness of the isolated components comes from localization: $Q_i$ is the preimage of $I R_P$ in $R$, for $P = \sqrt{Q_i}$ minimal.
