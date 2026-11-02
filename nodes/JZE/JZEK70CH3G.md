---
tag: JZEK70CH3G
kind: statement
role: theorem
name: Kontsevich quantization formula
msc: [53D55, 53D17]
uses: [A2KQ49Y4NF, 033WGN00BF]
about: [A2KQ49Y4NF]
sources:
  - url: https://en.wikipedia.org/wiki/Kontsevich_quantization_formula
same_as:
  wikidata: Q6430406
  wikipedia: Kontsevich quantization formula
---

## Statement

Let $U \subseteq \R^d$ be open and let $\pi^{ij} = -\pi^{ji}$, $1 \le i, j \le d$, be smooth functions on $U$.
Assume that $\{f, g\} = \sum_{i,j} \pi^{ij} \partial_i f \, \partial_j g$ satisfies the Jacobi identity.
So $U$ is a [[Poisson manifold|A2KQ49Y4NF]] with Poisson bivector $\pi$.
For $n \ge 0$, let $G_n$ be the set of admissible graphs.
Such a graph has aerial vertices $1, \ldots, n$, ground vertices $L$ and $R$, and $2n$ directed edges.
Each aerial vertex is the source of exactly two edges, labeled first and second.
No edge goes from a vertex to itself, and no two edges have the same source and target.
To $\Gamma \in G_n$ attach:

1. the bidifferential operator $B_\Gamma$. Place a copy of $(\pi^{ij})$ at each aerial vertex, $f$ at $L$ and $g$ at $R$. Let each edge act as a partial derivative $\partial_i$ on the object at its target, and sum over all indices;
2. the weight $w_\Gamma$ defined below.

Let $C_n$ be the space of configurations of $n$ distinct points in the upper half-plane $\mathbb{H}$, and put $L = 0$ and $R = 1$.
Let $e_k^1$ and $e_k^2$ be the edges leaving vertex $k$.
For an edge $e$, let $\phi_e$ be the angle at the source of $e$, in the hyperbolic metric of $\mathbb{H}$.
It goes from the geodesic to $\infty$ to the geodesic to the target of $e$.
Then
$$w_\Gamma = \frac{1}{n! \, (2\pi)^{2n}} \int_{C_n} \bigwedge_{k=1}^n \left( d\phi_{e_k^1} \wedge d\phi_{e_k^2} \right).$$

Let $C^\infty(U)[\![\hbar]\!]$ be the space of [[formal power series|033WGN00BF]] in $\hbar$ with coefficients in $C^\infty(U)$.
Extend the following product $\hbar$-bilinearly to it:
$$f \star g = \sum_{n \ge 0} \hbar^n \sum_{\Gamma \in G_n} w_\Gamma \, B_\Gamma(f, g).$$
Then $\star$ is associative, and $f \star g = fg + \hbar \{f, g\} + O(\hbar^2)$.
So $\star$ is a deformation quantization of $(U, \pi)$.

## Remarks

Kontsevich obtained the formula from his formality theorem: there is an $L_\infty$ quasi-isomorphism from polyvector fields to polydifferential operators on $\R^d$.
The formula is its explicit form, and associativity follows from Stokes' theorem on compactified configuration spaces, where the boundary terms either cancel or vanish by the Jacobi identity $[\pi, \pi] = 0$.
For a constant Poisson bivector only graphs without edges between aerial vertices contribute, and the formula gives the Moyal product.
With the formality theorem and a globalization argument, Kontsevich showed that every Poisson manifold has a deformation quantization.
He also showed that equivalence classes of star products correspond bijectively to equivalence classes of formal Poisson structures.

## Explanations

### L1 human

In quantum mechanics observables do not commute, while in classical mechanics they do.
A deformation quantization replaces the ordinary product of functions by a new associative product.
The new product depends on a small parameter $\hbar$, Planck's constant, and its first correction is the Poisson bracket.
Kontsevich's formula writes such a product explicitly for any Poisson structure on a piece of $\R^d$, as a sum over pictures of graphs with numerical weights given by integrals.

### L2 human

Before Kontsevich, star products were known for symplectic manifolds, by work of De Wilde and Lecomte and of Fedosov, but not for general Poisson manifolds.
The weights $w_\Gamma$ are hard to compute in general.
Cattaneo and Felder later explained the formula as a perturbative expansion of a topological field theory, the Poisson sigma model, on a disc.
