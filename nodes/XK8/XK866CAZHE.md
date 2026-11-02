---
tag: XK866CAZHE
kind: object
name: Hilbert scheme
msc: [14C05, 14D22]
instance_of: [FJZRW9P0K3]
uses: [FJZRW9P0K3, A4H4CZ2V35, ZT9A6JK8QF, 5M6KS8F47R, 9537RKBZPP, SWWW9X4A3N, KCCHH87H6E, 5FR6JX04RS]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_scheme
same_as:
  wikidata: Q5761225
  wikipedia: Hilbert scheme
---

## Description

Let $k$ be a field and let $X \subset \mathbb{P}^n_k$ be a closed subscheme of [[projective space|ZT9A6JK8QF]], for example a [[projective variety|A4H4CZ2V35]].
The *Hilbert functor* of $X$ sends a $k$-scheme $T$ to the set of closed subschemes $Z \subset X \times_k T$ such that the projection $Z \to T$ is [[flat|5M6KS8F47R]] and [[proper|9537RKBZPP]].
Grothendieck proved that this functor is [[representable|KCCHH87H6E]].
So there are a $k$-scheme $\operatorname{Hilb}(X)$ and a universal flat family $\mathcal{Z} \subset X \times \operatorname{Hilb}(X)$.
Every family $Z \subset X \times T$ as above is the pullback of $\mathcal{Z}$ along a unique morphism $T \to \operatorname{Hilb}(X)$.
This is the *Hilbert scheme* of $X$.
It is a disjoint union $\operatorname{Hilb}(X) = \coprod_P \operatorname{Hilb}^P(X)$ over the [[Hilbert polynomials|5FR6JX04RS]] $P$ of the fibers, and each $\operatorname{Hilb}^P(X)$ is a projective scheme.
So the Hilbert scheme is a fine [[moduli space|FJZRW9P0K3]] for closed subschemes of $X$, in the sense of the [[functor of points|SWWW9X4A3N]].

## Remarks

The hypersurfaces of degree $d$ in $\mathbb{P}^n$ are the zero sets of nonzero homogeneous polynomials of degree $d$ up to scalars.
Their Hilbert scheme is the projective space $\mathbb{P}^N$ with $N = \binom{n+d}{d} - 1$, whose points are these polynomials up to scaling.
The Hilbert scheme also exists for quasi-projective $X$, with quasi-projective components.
The Hilbert scheme of $m$ points in the plane, $\operatorname{Hilb}^m(\mathbb{A}^2)$, is smooth and irreducible of dimension $2m$ by a theorem of Fogarty.
It resolves the singularities of the symmetric product of $m$ copies of $\mathbb{A}^2$.

## Explanations

### L1 human

The Hilbert scheme is a space whose points are the subvarieties of a fixed projective variety, together with their degenerate limits.
Families of subvarieties become curves or surfaces inside this space.
For example, the lines in $\mathbb{P}^3$ form a four-dimensional Hilbert scheme, the Grassmannian of lines.
It is one of the first and most important examples of a moduli space.
