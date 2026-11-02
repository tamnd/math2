---
tag: A7MZ6GG7W0
kind: definition
name: Persistent homology
msc: [55N31, 62R40]
defines: S8SNBHVPSP
uses: [V8GZ0W1ZZ5, C6J40QF82R, 04C5ZBG1WT, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Persistent_homology
---

## Definition

Let $\F$ be a [[field|04C5ZBG1WT]] and let $K$ be a finite [[simplicial complex|V8GZ0W1ZZ5]] with a filtration by subcomplexes
$$K_0 \subseteq K_1 \subseteq \cdots \subseteq K_m = K.$$
For $i \le j$ and $p \ge 0$, the inclusion $K_i \subseteq K_j$ induces a linear map $f_p^{i,j} \colon H_p(K_i; \F) \to H_p(K_j; \F)$ of [[simplicial homology|C6J40QF82R]] groups, which are [[vector spaces|000AYPA9AJ]] over $\F$.
The *$p$-th persistent homology group* from $i$ to $j$ is the image
$$H_p^{i,j} = \im f_p^{i,j} \subseteq H_p(K_j; \F),$$
and its dimension $\beta_p^{i,j}$ is the *persistent Betti number*.
The family of all $H_p(K_i; \F)$ with all maps $f_p^{i,j}$ is the *$p$-th persistence module* of the filtration.

## Remarks

A class is *born* at $i$ if it lies in $H_p(K_i; \F)$ but not in the image of $f_p^{i-1,i}$.
It *dies* at $j$ if it merges with an older class or becomes $0$ when passing from $K_{j-1}$ to $K_j$.
The persistence module splits, uniquely up to order, as a direct sum of interval modules.
The list of their intervals $[b, d)$ is the *barcode*.
The same data, as points $(b, d)$ in the plane, form the *persistence diagram*.

Example: let $K_0$ consist of two vertices $a, b$ and let $K_1$ add the edge $ab$.
Then $H_0(K_0; \F) \cong \F^2$, $H_0(K_1; \F) \cong \F$, and $f_0^{0,1}$ is onto, so $\beta_0^{0,1} = 1$.
The barcode in degree $0$ is $\set{[0, \infty), [0, 1)}$: one component lives forever and one dies when the edge joins them.

Non-example: a family of complexes $K_0, K_1$ where $K_1$ does not contain $K_0$ is not a filtration, and no maps $f_p^{0,1}$ are induced.
Zigzag persistence treats such cases with maps in both directions.

For a finite set of points in a metric space, the standard filtrations are the Vietoris–Rips and Čech complexes at increasing scale.
