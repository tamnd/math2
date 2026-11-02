---
tag: B76G1KR3SB
kind: definition
name: Motive
msc: [14C15, 14F42]
defines: K1AZ4YF2RE
uses: [A4H4CZ2V35, 9VFWPZEVGN, K76N026JFK, EBEF6PEK4N, 4HV4WTAX9P]
sources:
  - url: https://en.wikipedia.org/wiki/Motive_(algebraic_geometry)
---

## Definition

Let $k$ be a field, and let $\mathcal{V}$ be the class of smooth [[projective varieties|A4H4CZ2V35]] over $k$.
Let $X, Y \in \mathcal{V}$ with $X$ irreducible of dimension $d$, and let $r \in \Z$.
The group of *correspondences of degree $r$* is $\operatorname{Corr}^r(X, Y) = CH^{d + r}(X \times Y) \otimes \Q$,
where $CH^\bullet$ is the [[Chow group|EBEF6PEK4N]] graded by codimension, that is, [[algebraic cycles|9VFWPZEVGN]] modulo [[rational equivalence|K76N026JFK]].
For general $X$, sum over the irreducible components of $X$.
The composition of $f \in \operatorname{Corr}^r(X, Y)$ and $g \in \operatorname{Corr}^s(Y, Z)$ is
$$g \circ f = (p_{XZ})_*\big(p_{XY}^* f \cdot p_{YZ}^* g\big) \in \operatorname{Corr}^{r+s}(X, Z),$$
where the $p$ are the projections from $X \times Y \times Z$ and the product is the [[intersection product|4HV4WTAX9P]].

The category of *Chow motives* over $k$ with rational coefficients is defined as follows.

1. Its objects, the *motives*, are triples $(X, p, m)$ with $X \in \mathcal{V}$, $p \in \operatorname{Corr}^0(X, X)$ such that $p \circ p = p$, and $m \in \Z$.
2. Its morphisms are $\Hom\big((X, p, m), (Y, q, n)\big) = q \circ \operatorname{Corr}^{n - m}(X, Y) \circ p$.
3. Composition is the composition of correspondences.

The *motive of* $X$ is $h(X) = (X, \Delta_X, 0)$, where $\Delta_X$ is the class of the diagonal.

## Remarks

The class $\Delta_X$ is the identity of $\operatorname{Corr}^0(X, X)$.
The *unit motive* is $\mathbb{1} = h(\operatorname{Spec} k)$ and the *Lefschetz motive* is $\mathbb{L} = (\operatorname{Spec} k, \id, -1)$.
Example: for $X = \mathbb{P}^1$, let $e_0 = [\mathrm{pt} \times \mathbb{P}^1]$ and $e_2 = [\mathbb{P}^1 \times \mathrm{pt}]$ in $\operatorname{Corr}^0(X, X) = CH^1(X \times X)_\Q$.
They are orthogonal idempotents, and $\Delta_X = e_0 + e_2$ because the diagonal and $e_0 + e_2$ both have bidegree $(1, 1)$ in $CH^1(\mathbb{P}^1 \times \mathbb{P}^1) \cong \Z^2$.
This gives $h(\mathbb{P}^1) = (X, e_0, 0) \oplus (X, e_2, 0) \cong \mathbb{1} \oplus \mathbb{L}$.
Non-example: $(X, 2\Delta_X, 0)$ is not a motive when $X$ is nonempty, since $2\Delta_X \circ 2\Delta_X = 4\Delta_X \ne 2\Delta_X$, so clause 1 fails.
Replacing rational equivalence by homological or numerical equivalence gives other categories of pure motives.
