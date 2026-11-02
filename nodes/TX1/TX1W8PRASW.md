---
tag: TX1W8PRASW
kind: definition
name: Čech cohomology
msc: [55N05, 14F06]
defines: 97MYM5X7N5
uses: [0CQHFPGJ45, 049PXYHW1T, TB6TM6R4MD, 082GHNPJ53, WQ82C0M3QB, PQ6Q143ARJ]
sources:
  - url: https://en.wikipedia.org/wiki/Čech_cohomology
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]], and let $\mathcal{F}$ be a [[sheaf|TB6TM6R4MD]] of [[abelian groups|082GHNPJ53]] on $X$.
Let $\mathfrak{U} = (U_i)_{i \in I}$ be an [[open cover|049PXYHW1T]] of $X$ with $I$ a well-ordered set.
For $i_0, \dots, i_p \in I$ write $U_{i_0 \dots i_p} = U_{i_0} \cap \dots \cap U_{i_p}$.
The *Čech complex* is the [[cochain complex|WQ82C0M3QB]] with
$$C^p(\mathfrak{U}, \mathcal{F}) = \prod_{i_0 < \dots < i_p} \mathcal{F}(U_{i_0 \dots i_p})$$
and differential $d \colon C^p \to C^{p+1}$ given by
$$(d\alpha)_{i_0 \dots i_{p+1}} = \sum_{j=0}^{p+1} (-1)^j \, \alpha_{i_0 \dots \widehat{i_j} \dots i_{p+1}}|_{U_{i_0 \dots i_{p+1}}},$$
where the hat means that the index is omitted.
The *Čech cohomology* of $\mathcal{F}$ with respect to $\mathfrak{U}$ is $\check{H}^p(\mathfrak{U}, \mathcal{F}) = H^p(C^\bullet(\mathfrak{U}, \mathcal{F}))$.
The Čech cohomology of $X$ with coefficients in $\mathcal{F}$ is the direct limit $\check{H}^p(X, \mathcal{F}) = \varinjlim_{\mathfrak{U}} \check{H}^p(\mathfrak{U}, \mathcal{F})$ over refinements of covers.

## Remarks

The sheaf axioms give $\check{H}^0(\mathfrak{U}, \mathcal{F}) = \mathcal{F}(X)$ for every cover.

Example: let $X = S^1$, covered by two open arcs $U_0, U_1$ whose intersection has two components, and let $\mathcal{F} = \underline{\Z}$ be the constant sheaf.
Then $C^0 = \Z^2$, $C^1 = \underline{\Z}(U_{01}) = \Z^2$, and $d(a, b) = (b - a, b - a)$.
So $\check{H}^0 = \Z$ and $\check{H}^1 = \Z^2 / \set{(c, c)} \cong \Z$.

Non-example: a family of open sets that does not cover $X$ is not allowed; then $\check{H}^0$ would be the sections over the union, not over $X$.

There is a natural map $\check{H}^p(\mathfrak{U}, \mathcal{F}) \to H^p(X, \mathcal{F})$ to [[sheaf cohomology|PQ6Q143ARJ]].
It is an isomorphism when $H^q(U_{i_0 \dots i_p}, \mathcal{F}) = 0$ for all $q > 0$ and all finite intersections (Leray's theorem), for example for a quasi-coherent sheaf on a separated scheme and an affine open cover.
