---
tag: 1NC789DATR
kind: statement
role: theorem
name: Base change theorems
msc: [14F06, 14D06]
uses: [ND6XEY68P4, Z5G47MQ99B, 5M6KS8F47R, KPKND0K7W6, 56RXEJ8Z6S, 963QWX2E2Z, G51E8MW7J1, PQ6Q143ARJ]
about: [PQ6Q143ARJ]
sources:
  - url: https://en.wikipedia.org/wiki/Base_change_theorems
same_as:
  wikidata: Q4866385
  wikipedia: Base change theorems
---

## Statement

Let $Y$ be a [[Noetherian scheme|ND6XEY68P4]] and let $f \colon X \to Y$ be a morphism.
For a sheaf $\mathcal{F}$ on $X$, $R^i f_* \mathcal{F}$ is the higher direct image, the sheaf on $Y$ associated to $V \mapsto H^i(f^{-1}(V), \mathcal{F})$, where $H^i$ is [[sheaf cohomology|PQ6Q143ARJ]].
For $y \in Y$ with [[residue field|G51E8MW7J1]] $k(y)$, let $X_y$ be the [[fiber|963QWX2E2Z]] and $\mathcal{F}_y$ the restriction of $\mathcal{F}$ to $X_y$.

1. (Flat base change.) Let $f$ be separated and of finite type, let $\mathcal{F}$ be [[quasi-coherent|KPKND0K7W6]], and let $u \colon Y' \to Y$ be a [[flat morphism|5M6KS8F47R]] with $Y'$ Noetherian. Let $v \colon X' = X \times_Y Y' \to X$ and $g \colon X' \to Y'$ be the projections. Then the natural maps $u^* R^i f_* \mathcal{F} \to R^i g_* (v^* \mathcal{F})$ are isomorphisms for all $i \ge 0$.

In the following, let $f$ be [[projective|Z5G47MQ99B]] and let $\mathcal{F}$ be a [[coherent sheaf|56RXEJ8Z6S]] on $X$ that is flat over $Y$.

2. (Semicontinuity.) For each $i \ge 0$, the function $y \mapsto \dim_{k(y)} H^i(X_y, \mathcal{F}_y)$ is upper semicontinuous on $Y$, and the Euler characteristic $y \mapsto \sum_i (-1)^i \dim_{k(y)} H^i(X_y, \mathcal{F}_y)$ is locally constant.
3. (Grauert.) If $Y$ is integral and $y \mapsto \dim_{k(y)} H^i(X_y, \mathcal{F}_y)$ is constant, then $R^i f_* \mathcal{F}$ is locally free and the natural map $R^i f_* \mathcal{F} \otimes k(y) \to H^i(X_y, \mathcal{F}_y)$ is an isomorphism for every $y \in Y$.
4. (Cohomology and base change.) Let $y \in Y$ and suppose that the natural map $\varphi^i(y) \colon R^i f_* \mathcal{F} \otimes k(y) \to H^i(X_y, \mathcal{F}_y)$ is surjective. Then $\varphi^i(y)$ is an isomorphism, and $\varphi^{i-1}(y)$ is surjective if and only if $R^i f_* \mathcal{F}$ is locally free in a neighbourhood of $y$.

## Remarks

The idea of the proof of parts 2 to 4: locally on an affine $Y = \operatorname{Spec} A$, there is a bounded complex $K^\bullet$ of finitely generated free $A$-modules with a special property.
For every $A$-algebra $B$, it computes the cohomology after base change: $H^i(X \times_Y \operatorname{Spec} B, \mathcal{F}_B) \cong H^i(K^\bullet \otimes_A B)$.
All statements then become facts about ranks of matrices of functions on $Y$.
Part 1 follows from the Čech complex of an affine cover, since flat base change commutes with taking cohomology of a complex.

Example: let $f \colon X \to Y$ be a flat projective family of curves over an integral base, with all fibers smooth of genus $g$.
Then $h^0(X_y, \mathcal{O}) = 1$ and $h^1(X_y, \mathcal{O}) = g$ for all $y$, so by part 3 $f_* \mathcal{O}_X$ and $R^1 f_* \mathcal{O}_X$ are locally free of ranks $1$ and $g$.

Flatness is needed in part 2.
Let $Y = \mathbb{A}^1_k$, and let $X$ be the disjoint union of $Y$ and the closed point $0$.
Let $f$ be the identity on $Y$ and the inclusion on the point, and let $\mathcal{F} = \mathcal{O}_X$.
Then $f$ is finite, hence projective, but $\mathcal{F}$ is not flat over $Y$.
The Euler characteristic of the fibers is $2$ at $0$ and $1$ elsewhere, so it is not locally constant.

## Explanations

### L1 human

Given a family of varieties, each with a sheaf on it, one wants to know how the cohomology of the fibers changes from one fiber to the next.
These theorems say that the dimensions can only jump up on special fibers, never down, and that their alternating sum stays constant in a flat family.
When the dimension does not jump, the cohomology groups of the fibers fit together into a vector bundle on the base.

### L2 human

The base change theorems are used to construct vector bundles on parameter spaces, such as the Hodge bundle $f_* \omega_{X/Y}$ on a moduli space of curves.
Semicontinuity says that a property like $H^1(X_y, \mathcal{F}_y) = 0$ is open in families, which is the starting point of deformation arguments.
Flat base change lets one compute higher direct images after a flat change of base, for example after passing to a completion or to an étale neighbourhood.
