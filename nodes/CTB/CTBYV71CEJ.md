---
tag: CTBYV71CEJ
kind: definition
name: Affine scheme
msc: [14A15]
defines: B3V3XJ2W8G
uses: [B7FPT8JTXR, FB45BHHA2J, 0310REJJY8, 8SQK7RTB63, 4C1AE84N5N, X6JD4AG973, TB6TM6R4MD]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_of_a_ring
---

## Definition

Let $A$ be a [[commutative ring|0310REJJY8]] with identity, and let $X = \operatorname{Spec} A$ be its [[spectrum|FB45BHHA2J]] with the [[Zariski topology|8SQK7RTB63]].
For $f \in A$, write $D(f) = \set{\mathfrak{p} \in X : f \notin \mathfrak{p}}$; these sets form a basis of open sets of $X$.
Let $A_f$ be the [[localization|4C1AE84N5N]] of $A$ at the powers of $f$.
The *structure sheaf* $\mathcal{O}_X$ is the unique [[sheaf|TB6TM6R4MD]] of rings on $X$ with $\mathcal{O}_X(D(f)) = A_f$ for every $f \in A$.
Its restriction maps $A_f \to A_g$ for $D(g) \subseteq D(f)$ are the natural maps.
Its stalk at $\mathfrak{p}$ is the [[localization at the prime ideal|X6JD4AG973]] $A_{\mathfrak p}$, which is a local ring.

An *affine scheme* is a [[locally ringed space|B7FPT8JTXR]] isomorphic to $(\operatorname{Spec} A, \mathcal{O}_{\operatorname{Spec} A})$ for some commutative ring $A$.

## Remarks

Example: $\operatorname{Spec} \Z$ is an affine scheme; its points are $(0)$ and $(p)$ for the primes $p$, and $\mathcal{O}(D(n)) = \Z[1/n]$ for $n \ne 0$.
Example: the affine $n$-space over a ring $R$ is $\mathbb{A}^n_R = \operatorname{Spec} R[x_1, \ldots, x_n]$.
Non-example: for a field $k$, the open subset $U = \mathbb{A}^2_k \setminus \set{(x, y)}$ of the plane, with the restricted sheaf, is a locally ringed space but not an affine scheme.
Its ring of global functions is $k[x, y]$, so if it were affine it would be $\operatorname{Spec} k[x, y]$, which also contains the origin $(x, y)$.
The ring is recovered as $A \cong \mathcal{O}_X(X)$, the global sections.
