---
tag: AYN9675FTS
kind: definition
name: Harish-Chandra c-function
msc: ["43A90", "22E46", "22E30"]
defines: 4X2N0BN3M0
uses: [XJS07AJ50Y, T2EB8R9HEV, 4YDR9Q36DS, VY0HXD3GC4, A6MQCW28KZ]
sources:
  - url: https://en.wikipedia.org/wiki/Harish-Chandra%27s_c-function
---

## Definition

Let $G$ be a connected noncompact [[semisimple Lie group|XJS07AJ50Y]] with finite centre, and $K$ a [[maximal compact subgroup|T2EB8R9HEV]].
Let $G = K A N$ be an [[Iwasawa decomposition|4YDR9Q36DS]], with $\mathfrak a$ the Lie algebra of $A$.
For $g \in G$ let $H(g) \in \mathfrak a$ be defined by $g \in K \exp(H(g)) N$.
Let $\mathfrak a^*_+$ be the positive Weyl chamber in $\mathfrak a^*$ for the restricted roots that occur in $N$.
Let $\rho$ be half the sum of these roots, counted with multiplicity.
Let $\theta$ be the Cartan involution fixing $K$, and $\bar N = \theta(N)$, with the [[Haar measure|VY0HXD3GC4]] $d\bar n$ normalized by $\int_{\bar N} e^{-2\rho(H(\bar n))} \, d\bar n = 1$.
The *Harish-Chandra c-function* is
$$c(\lambda) = \int_{\bar N} e^{-(i \lambda + \rho)(H(\bar n))} \, d\bar n$$
for $\lambda \in \mathfrak a^*_\C$ with $\operatorname{Re}(i \lambda) \in \mathfrak a^*_+$, where the integral converges absolutely, and its meromorphic continuation to $\mathfrak a^*_\C$ elsewhere.

## Remarks

The normalization gives $c(-i \rho) = 1$.
For $\operatorname{Re}(i \lambda) \in \mathfrak a^*_+$ and $H$ in the positive chamber of $\mathfrak a$, the spherical function $\varphi_\lambda$ of [[Harish-Chandra's formula|A6MQCW28KZ]] satisfies
$$\lim_{t \to \infty} e^{(-i \lambda + \rho)(t H)} \varphi_\lambda(\exp t H) = c(\lambda).$$
For real $\lambda$ one has $\overline{c(\lambda)} = c(-\lambda)$, so $\abs{c(\lambda)}^2 = c(\lambda) c(-\lambda)$.

Example: for $G = \mathrm{SL}(2, \R)$ and $\lambda = s \rho$ with $s \in \C$,
$$c(s \rho) = \frac{\Gamma(i s / 2)}{\sqrt{\pi} \, \Gamma\big((1 + i s)/2\big)},$$
which equals $1$ at $s = -i$, as it should.

Non-example: the integral defining $c(\lambda)$ diverges for real $\lambda$, since then $\abs{e^{-(i \lambda + \rho)(H(\bar n))}} = e^{-\rho(H(\bar n))}$, which is not integrable on $\bar N$; for real $\lambda$ the value $c(\lambda)$ is defined by continuation.
