---
tag: SPT1JD267Q
kind: definition
name: Bimetric gravity
msc: [83D05]
defines: HGGX6W1XNX
uses: [384JFR3K6X, BY4QYYS788, ZHX2VYQDZ3, 63FAKMYZ2E, 0X5QVCF06N, Y4SHDZSCZ4]
sources:
  - url: https://en.wikipedia.org/wiki/Bimetric_gravity
---

## Definition

A *bimetric theory of gravity* is an [[alternative to general relativity|384JFR3K6X]] with two gravitational fields.
These are two [[Lorentzian metrics|BY4QYYS788]] $g$ and $f$ on the same four-dimensional manifold.
In the ghost-free bimetric theory of Hassan and Rosen, both metrics are dynamical, and the action is
$$S = \frac{M_g^2}{2}\int R(g)\sqrt{-g}\,d^4x + \frac{M_f^2}{2}\int R(f)\sqrt{-f}\,d^4x - m^2 M_g^2 \int \sum_{n=0}^{4} \beta_n\, e_n\!\left(\sqrt{g^{-1}f}\right)\sqrt{-g}\,d^4x + S_m[g, \psi],$$
where:

1. $R(g)$ and $R(f)$ are the [[scalar curvatures|ZHX2VYQDZ3]] of $g$ and $f$, and $M_g, M_f > 0$ are mass scales;
2. $\sqrt{g^{-1}f}$ is the [[matrix square root|63FAKMYZ2E]] $S$ of the matrix $g^{\mu\lambda}f_{\lambda\nu}$, defined by $S^\mu{}_\lambda S^\lambda{}_\nu = g^{\mu\lambda}f_{\lambda\nu}$;
3. $e_n(S)$ is the $n$-th [[elementary symmetric polynomial|0X5QVCF06N]] of the eigenvalues of $S$, $m$ is a mass scale and the $\beta_n$ are real constants;
4. matter fields $\psi$ couple only to $g$.

## Remarks

The special combination of the $e_n$ in the potential is what removes the Boulware–Deser ghost; normalizations of $m$, $M_g$ and $M_f$ vary between authors.
Example: let $f = c^2 g$ with a constant $c > 0$.
Then $S = c\,\mathrm{id}$ and the potential is a constant times $\sqrt{-g}$.
Solutions of this kind behave like general relativity with a cosmological constant.
Non-example: general relativity has a single metric, so it is not a bimetric theory.
The [[massive gravity|Y4SHDZSCZ4]] theory of de Rham, Gabadadze and Tolley has a second metric $f$ without kinetic term.
It arises from the Hassan–Rosen action in the limit $M_f \to \infty$ with $f$ held fixed.
Rosen's bimetric theory of 1940 is an older theory of the first kind, with $f$ a fixed flat metric.

## Explanations

### L1 human

Bimetric gravity gives spacetime two metrics, each with its own Einstein–Hilbert term, tied together by a potential.
The potential is built from the eigenvalues of a square root that compares the two metrics.
