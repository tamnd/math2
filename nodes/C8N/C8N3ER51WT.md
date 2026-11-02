---
tag: C8N3ER51WT
kind: definition
name: Borel–Moore homology
msc: [55N35, 55N30]
defines: T1N6E5Q8Z2
uses: [0FE2SB8WVJ, 0S1FJ8VEX9, M0Q5CFJ7ZH, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Borel–Moore_homology
---

## Definition

Let $X$ be a [[locally compact|0FE2SB8WVJ]] [[Hausdorff space|0S1FJ8VEX9]] and let $A$ be an [[abelian group|082GHNPJ53]].
A *locally finite singular $i$-chain* on $X$ is a formal sum $c = \sum_\sigma a_\sigma \sigma$, possibly infinite, over singular $i$-simplices $\sigma \colon \Delta^i \to X$ with $a_\sigma \in A$.
It is required that every point of $X$ has a neighbourhood that meets the image of only finitely many $\sigma$ with $a_\sigma \neq 0$.
These chains form a group $C^{\mathrm{lf}}_i(X; A)$, and the usual boundary formula of [[singular homology|M0Q5CFJ7ZH]] defines $\partial \colon C^{\mathrm{lf}}_i(X; A) \to C^{\mathrm{lf}}_{i-1}(X; A)$ with $\partial \circ \partial = 0$.
The *Borel–Moore homology* of $X$ is the homology of this [[chain complex|WQ82C0M3QB]]:
$$H^{\mathrm{BM}}_i(X; A) = H_i(C^{\mathrm{lf}}_\bullet(X; A)).$$

## Remarks

The boundary of a locally finite chain is locally finite, because each face of $\sigma$ has image inside the image of $\sigma$.
If $X$ is compact, a locally finite chain is a finite chain, so $H^{\mathrm{BM}}_i(X; A) = H_i(X; A)$.
Some authors define the theory with sheaves.
If $X = Y \setminus Z$ for a finite CW complex $Y$ and a subcomplex $Z$, then $H^{\mathrm{BM}}_i(X; A) \cong H_i(Y, Z; A)$.

Example: on $X = \R$, the chain $c = \sum_{k \in \Z} \sigma_k$, where $\sigma_k$ is the affine path from $k$ to $k+1$, is locally finite, and $\partial c = \sum_k (\set{k+1} - \set{k}) = 0$.
Its class generates $H^{\mathrm{BM}}_1(\R; \Z) \cong \Z$, while $H^{\mathrm{BM}}_0(\R; \Z) = 0$.

Non-example: the infinite sum $\sum_{k \ge 1} \tau_k$, where $\tau_k$ is the affine path from $0$ to $1/k$ in $\R$, is not locally finite: every neighbourhood of $0$ meets all the $\tau_k$.

For an oriented $n$-manifold $M$, Poincaré duality takes the form $H^{\mathrm{BM}}_i(M; \Z) \cong H^{n-i}(M; \Z)$.
