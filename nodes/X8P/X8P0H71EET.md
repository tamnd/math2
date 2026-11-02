---
tag: X8P0H71EET
kind: definition
name: Frölicher–Nijenhuis bracket
msc: [58A10, 53C15, 17B70]
defines: D46QECMC10
uses: [F45VQ47GPV, 0E3G0GRPZ6, 0ZHSTAG8ZY, 0GRAATMGP1, 3J89REV9WQ, 68FGQEBD6J, PJWK0PKN6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Fr%C3%B6licher%E2%80%93Nijenhuis_bracket
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]].
Let $\Omega(M) = \bigoplus_k \Omega^k(M)$ be the graded algebra of [[differential forms|0E3G0GRPZ6]] with the [[wedge product|0GRAATMGP1]].
Let $\Omega^k(M, TM)$ be the space of $k$-forms with values in $TM$, that is, smooth sections of $\Lambda^k T^*M \otimes TM$.
A graded [[derivation|3J89REV9WQ]] of degree $j$ of $\Omega(M)$ is a linear map $D$ with $D(\Omega^k) \subseteq \Omega^{k+j}$ and $D(\alpha \wedge \beta) = D\alpha \wedge \beta + (-1)^{jk} \alpha \wedge D\beta$ for $\alpha \in \Omega^k(M)$.
The graded commutator of derivations $D_1, D_2$ of degrees $j_1, j_2$ is $[D_1, D_2] = D_1 D_2 - (-1)^{j_1 j_2} D_2 D_1$.

For $K \in \Omega^k(M, TM)$, let $\iota_K$ be the derivation of degree $k - 1$ given on decomposable $K = \alpha \otimes X$ by $\iota_K \omega = \alpha \wedge \iota_X \omega$.
Let $\mathcal{L}_K = [\iota_K, d] = \iota_K d - (-1)^{k-1} d\, \iota_K$, a derivation of degree $k$, where $d$ is the [[exterior derivative|0ZHSTAG8ZY]].

For $K \in \Omega^k(M, TM)$ and $L \in \Omega^l(M, TM)$, the *Frölicher–Nijenhuis bracket* $[K, L] \in \Omega^{k+l}(M, TM)$ is the unique element with
$$\mathcal{L}_{[K, L]} = [\mathcal{L}_K, \mathcal{L}_L].$$

## Remarks

The bracket exists and is unique because every graded derivation of $\Omega(M)$ that commutes with $d$ in the graded sense is $\mathcal{L}_K$ for exactly one vector-valued form $K$.
It is graded antisymmetric, $[K, L] = -(-1)^{kl} [L, K]$, and satisfies the graded Jacobi identity.

For $\alpha \in \Omega^k(M)$, $\beta \in \Omega^l(M)$ and vector fields $X, Y$, an explicit formula is
$$[\alpha \otimes X, \beta \otimes Y] = \alpha \wedge \beta \otimes [X, Y] + \alpha \wedge \mathcal{L}_X \beta \otimes Y - \mathcal{L}_Y \alpha \wedge \beta \otimes X + (-1)^k \big( d\alpha \wedge \iota_X \beta \otimes Y + \iota_Y \alpha \wedge d\beta \otimes X \big).$$

Example: for $k = l = 0$, take $\alpha = \beta = 1$.
The formula gives $[X, Y]$, the [[Lie bracket of vector fields|68FGQEBD6J]], and $\mathcal{L}_X$ is the usual [[Lie derivative|PJWK0PKN6Q]].
Another example: the identity $\mathrm{Id} \in \Omega^1(M, TM)$ has $\iota_{\mathrm{Id}} \omega = j \omega$ for $\omega \in \Omega^j(M)$.
Hence $\mathcal{L}_{\mathrm{Id}} \omega = (j + 1) d\omega - j\, d\omega = d\omega$, so $\mathcal{L}_{\mathrm{Id}} = d$ and $[\mathrm{Id}, L] = 0$ for every $L$.

Non-example: the naive rule $[\alpha \otimes X, \beta \otimes Y] = \alpha \wedge \beta \otimes [X, Y]$ does not define a bracket on $\Omega(M, TM)$.
For a function $f$, the elements $f\alpha \otimes X$ and $\alpha \otimes fX$ are equal, but the rule gives different results for them, since $[fX, Y] \ne f[X, Y]$ in general.
