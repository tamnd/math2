---
tag: EX6YSYN7B4
kind: statement
role: theorem
name: Lefschetz hyperplane theorem
msc: [14F45, 14C30, 14F25]
uses: [A4H4CZ2V35, FHV05ZK99F, RRK8P6TXG2, 6N7BC70CX0]
about: [6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/Lefschetz_hyperplane_theorem
same_as:
  wikidata: Q6516731
  wikipedia: Lefschetz hyperplane theorem
---

## Statement

Let $X$ be a complex [[projective variety|A4H4CZ2V35]] of dimension $n$.
Let $D \subseteq X$ be an effective [[ample|RRK8P6TXG2]] [[Cartier divisor|FHV05ZK99F]], for example a hyperplane section, such that $X \setminus D$ is smooth.
Then, for [[singular cohomology|6N7BC70CX0]] with integer coefficients, the restriction map
$$H^i(X, \Z) \to H^i(D, \Z)$$
is an isomorphism for $i \le n - 2$ and injective for $i = n - 1$.

## Remarks

The idea of the proof: $X \setminus D$ is a smooth affine variety of dimension $n$.
By the Andreotti–Frankel theorem it has the homotopy type of a CW complex of real dimension at most $n$.
Lefschetz duality then gives $H^i(X, D; \Z) \cong H_{2n - i}(X \setminus D; \Z) = 0$ for $i < n$, and the long exact sequence of the pair gives the claim.
The homotopy version says that $\pi_i(D) \to \pi_i(X)$ is an isomorphism for $i \le n - 2$ and surjective for $i = n - 1$.

Example: a smooth hypersurface $X \subseteq \mathbb{P}^{n+1}_\C$ of dimension $n$ is an ample divisor in $\mathbb{P}^{n+1}$.
So $H^i(X, \Z) \cong H^i(\mathbb{P}^{n+1}, \Z)$ for $i \le n - 1$, which is $\Z$ for even $i$ and $0$ for odd $i$; in particular $X$ is simply connected when $n \ge 2$.

The bound $n - 1$ is sharp.
Let $X = \mathbb{P}^1 \times \mathbb{P}^1$, of dimension $n = 2$, embedded in $\mathbb{P}^3$ as a quadric by the Segre embedding.
A hyperplane section is a smooth conic $D \cong \mathbb{P}^1$, and $H^2(X, \Z) \cong \Z^2$ while $H^2(D, \Z) \cong \Z$.
So the map in degree $n = 2$ is not injective.

## Explanations

### L1 human

Cut a projective variety by a hyperplane.
The theorem says that the slice has the same cohomology as the whole variety in all low degrees, below the middle dimension of the slice.
So the topology of a variety is largely determined by the topology of its hyperplane sections, and new topology can only appear in the middle degree.

### L2 human

The theorem is the basis for induction on dimension in the topology of algebraic varieties, through Lefschetz pencils.
Together with Poincaré duality it shows that all the interesting cohomology of a smooth complete intersection sits in the middle degree.
It is complemented by the hard Lefschetz theorem, which describes the middle and upper degrees, and it has analogues in étale cohomology used in the proof of the Weil conjectures.
