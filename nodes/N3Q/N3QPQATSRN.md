---
tag: N3QPQATSRN
kind: statement
role: theorem
name: Serre duality
msc: [14F06, 14F08]
uses: [A4H4CZ2V35, EXKGG9X6J0, P4DZM975BV, W05VYY4HBR, PQ6Q143ARJ]
about: [PQ6Q143ARJ, W05VYY4HBR]
sources:
  - url: https://en.wikipedia.org/wiki/Serre_duality
same_as:
  wikidata: Q11095962
  wikipedia: Serre duality
---

## Statement

Let $k$ be a field and let $X$ be a [[projective variety|A4H4CZ2V35]] over $k$ of dimension $n$.
Assume that $X$ is [[smooth|EXKGG9X6J0]] and geometrically connected, with [[canonical bundle|W05VYY4HBR]] $\omega_X$.
Then there is a trace isomorphism $H^n(X, \omega_X) \cong k$.
Let $\mathcal{E}$ be a [[vector bundle|P4DZM975BV]] on $X$ with dual $\mathcal{E}^\vee$, and let $0 \le i \le n$.
Then the cup product followed by the trace,
$$H^i(X, \mathcal{E}) \times H^{n-i}(X, \mathcal{E}^\vee \otimes \omega_X) \to H^n(X, \omega_X) \cong k,$$
is a perfect pairing of finite-dimensional vector spaces.
So $H^i(X, \mathcal{E}) \cong H^{n-i}(X, \mathcal{E}^\vee \otimes \omega_X)^\vee$, where $H^i$ is [[sheaf cohomology|PQ6Q143ARJ]].

## Remarks

The idea of the proof: first treat $\mathbb{P}^N_k$, where the cohomology of the sheaves $\mathcal{O}(d)$ is computed explicitly by Čech cohomology and the pairing is visible on monomials.
For $X \subseteq \mathbb{P}^N_k$ of codimension $r$, the dualizing sheaf of $X$ is $\mathcal{E}xt^r(\mathcal{O}_X, \omega_{\mathbb{P}^N})$, and for smooth $X$ this sheaf is $\omega_X$.

Example: for a smooth projective curve $X$ of genus $g$ and $\mathcal{E} = \mathcal{O}_X$, duality gives $h^1(X, \mathcal{O}_X) = h^0(X, \omega_X) = g$.
Combined with Riemann–Roch it gives $\deg \omega_X = 2g - 2$.

Properness is necessary: for $X = \mathbb{A}^1_k$, $H^0(X, \mathcal{O}_X) = k[t]$ is infinite-dimensional while $H^1(X, \omega_X) = 0$ by affine vanishing.
More generally the statement holds for projective Cohen–Macaulay schemes of pure dimension $n$, with $\omega_X$ replaced by the dualizing sheaf.

## Explanations

### L1 human

Serre duality says that the cohomology of a vector bundle in degree $i$ and the cohomology of a twisted dual bundle in the complementary degree $n - i$ carry the same information.
The twist is by the canonical bundle.
It halves the work in many computations and links the top cohomology to global sections, which are easier to understand.

### L2 human

Serre duality is the algebraic analogue of Poincaré duality for compact oriented manifolds.
It is used constantly with the Riemann–Roch theorem: on a curve, $h^1(L) = h^0(K - L)$, which turns Riemann–Roch into a statement about global sections only.
Its general form, valid for proper morphisms and complexes of sheaves, is Grothendieck duality.
