---
tag: VH4FD4ZHEQ
kind: definition
name: Period map
msc: [32G20, 14D07]
defines: YGNXQVTWP3
uses: [VKQSM3BCE4, X60JG9AEQJ, HABCJ4Y0SR, ZSM083M97C, CYPA882RB9, NHRWCQQKTH]
sources:
  - url: https://en.wikipedia.org/wiki/Period_mapping
---

## Definition

Let $\varpi \colon \mathcal{X} \to B$ be a complex analytic family of compact complex manifolds, as in a [[deformation|VKQSM3BCE4]].
Assume that $B$ is simply connected and that every fibre $X_t$ is a [[Kähler manifold|X60JG9AEQJ]].
Fix $k \ge 0$, a base point $0 \in B$, and put $H = H^k(X_0, \C)$.
By Ehresmann's theorem the family is smoothly locally trivial, and since $B$ is simply connected this gives canonical isomorphisms $H^k(X_t, \C) \cong H$ for all $t$.
By the [[Hodge decomposition|HABCJ4Y0SR]], $H^k(X_t, \C)$ has the Hodge filtration $F^p H^k(X_t) = \bigoplus_{r \ge p} H^{r, k-r}(X_t)$, whose dimensions $f^p$ do not depend on $t$.
The *period map* of the family is
$$\mathcal{P} \colon B \to \mathcal{F}, \qquad t \mapsto \left(F^k H^k(X_t) \subseteq F^{k-1} H^k(X_t) \subseteq \cdots \subseteq F^1 H^k(X_t)\right).$$
Here each $F^p H^k(X_t)$ is viewed as a subspace of $H$, and $\mathcal{F}$ is the [[flag variety|NHRWCQQKTH]] of flags in $H$ with dimensions $f^k \le \cdots \le f^1$.
Its components $\mathcal{P}^p \colon t \mapsto F^p H^k(X_t)$ map to the [[Grassmannian|CYPA882RB9]] of $f^p$-dimensional subspaces of $H$.

## Remarks

For a base that is not simply connected, one defines the period map on the universal cover.
Alternatively, it is a map to the quotient of a period domain by the monodromy group.
When the fibres are projective with a fixed polarization, the period map on primitive cohomology takes values in a period domain of polarized [[Hodge structures|ZSM083M97C]].

Example: the family $\C/(\Z + \tau\Z)$ over the upper half-plane, with $k = 1$.
Identify $H = H^1(X_\tau, \C)$ with $\C^2$ by integrating over the loops $[0, 1]$ and $[0, \tau]$.
Then $F^1 = H^{1,0}$ is spanned by the class of $dz$, with periods $(1, \tau)$, so $\mathcal{P}(\tau) = [1 : \tau] \in \mathbb{P}^1$, which is injective.

Example: a trivial family $X \times B \to B$ has a constant period map.
