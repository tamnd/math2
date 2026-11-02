---
tag: YCQFP0KN48
kind: definition
name: Homology with coefficients
msc: [55N10, 55U20]
defines: XT7VWNTKGB
uses: [M0Q5CFJ7ZH, 082GHNPJ53, DDQRERAQCV, 1DDYB6VVSR]
sources:
  - url: https://en.wikipedia.org/wiki/Homology_(mathematics)
---

## Definition

Let $X$ be a topological space and let $G$ be an [[abelian group|082GHNPJ53]].
The group $C_n(X; G)$ of singular $n$-chains with coefficients in $G$ is the set of finite formal sums $\sum_i g_i \sigma_i$.
Here $g_i \in G$ and $\sigma_i \colon \Delta^n \to X$ are singular $n$-simplices; equivalently, $C_n(X; G) = C_n(X) \otimes_{\Z} G$.
The boundary map is $\partial\left(\sum_i g_i \sigma_i\right) = \sum_i \sum_{k=0}^{n} (-1)^k g_i \, \sigma_i|_{[v_0, \ldots, \hat v_k, \ldots, v_n]}$, where the hat means that the vertex is omitted.
This gives a chain complex, and the *homology of $X$ with coefficients in $G$*, written $H_n(X; G)$, is its homology in degree $n$.
For a subspace $A \subseteq X$, the relative groups $H_n(X, A; G)$ come from $C_n(X; G) / C_n(A; G)$ in the same way.

## Remarks

For $G = \Z$ this is ordinary [[singular homology|M0Q5CFJ7ZH]].
If $R$ is a commutative ring, then $H_n(X; R)$ is an $R$-module; for a field it is a vector space.
The universal coefficient theorem gives a split exact sequence $0 \to H_n(X) \otimes G \to H_n(X; G) \to \operatorname{Tor}(H_{n-1}(X), G) \to 0$, with [[Tor|DDQRERAQCV]] the Tor functor.

Example: for the [[real projective plane|1DDYB6VVSR]], $H_1(\R P^2) = \Z/2$ and $H_2(\R P^2) = 0$.
The universal coefficient theorem gives $H_2(\R P^2; \Z/2) \cong 0 \oplus \operatorname{Tor}(\Z/2, \Z/2) \cong \Z/2$.

Non-example: the construction needs $G$ to be abelian, since the boundary formula adds coefficients in an arbitrary order.
The proof that $\partial \circ \partial = 0$ rearranges the double sum and cancels terms in pairs, which uses that addition in $G$ is commutative.
