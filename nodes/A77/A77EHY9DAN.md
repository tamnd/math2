---
tag: A77EHY9DAN
kind: definition
name: Signature operator
msc: [58J20, 58A14, 57R20]
defines: 4NCYA7GME1
uses: [7CBT4SM83Y, 0E3G0GRPZ6, 0ZHSTAG8ZY, 1Y4WX4XQWJ, PWG3GKZG80, MT9P2X85V8, WK8GKRKAVD, TEG1ZX1AGJ]
sources:
  - url: https://en.wikipedia.org/wiki/Signature_operator
---

## Definition

Let $(M, g)$ be a closed oriented [[Riemannian manifold|7CBT4SM83Y]] of dimension $4k$.
Let $\Omega^*(M) = \bigoplus_p \Omega^p(M)$ be the space of smooth complex-valued [[differential forms|0E3G0GRPZ6]], with [[exterior derivative|0ZHSTAG8ZY]] $d$, [[Hodge star|1Y4WX4XQWJ]] $\star$ and codifferential $\delta$, the formal adjoint of $d$.
Define $\tau \colon \Omega^*(M) \to \Omega^*(M)$ by
$$\tau \omega = i^{p(p-1) + 2k} \star \omega \quad \text{for } \omega \in \Omega^p(M).$$
Then $\tau^2 = \id$ and $\tau (d + \delta) = -(d + \delta) \tau$.
Let $\Omega^\pm(M)$ be the $\pm 1$ eigenspaces of $\tau$.
The *signature operator* of $M$ is the restriction
$$D^+ = d + \delta \colon \Omega^+(M) \to \Omega^-(M).$$

## Remarks

The operator $d + \delta$ is elliptic with square the [[Hodge Laplacian|PWG3GKZG80]], so $D^+$ is an [[elliptic operator|MT9P2X85V8]] of order $1$.
Its index equals the signature $\sigma(M)$ of the [[intersection form|WK8GKRKAVD]] on $H^{2k}(M; \R)$.
Indeed, the harmonic forms of degrees $p \ne 2k$ contribute equally to the kernel and the cokernel and cancel.
On harmonic $2k$-forms $\tau = \star$, whose $\pm 1$ eigenspaces are the self-dual and anti-self-dual forms.
The Atiyah–Singer index theorem applied to $D^+$ gives the [[Hirzebruch signature theorem|TEG1ZX1AGJ]].

Example: on $2k$-forms, $\tau = i^{2k(2k-1) + 2k} \star = i^{4k^2} \star = \star$.
For $M = \C P^2$ ($k = 1$), the harmonic $2$-forms are the multiples of the Kähler form $\omega_{FS}$, which is self-dual, so $\sigma(\C P^2) = 1$ and the index of $D^+$ is $1$.

Non-example: the operator $d + \delta \colon \Omega^{\mathrm{even}}(M) \to \Omega^{\mathrm{odd}}(M)$ uses the splitting by degree instead of the splitting by $\tau$.
It is the de Rham or Euler operator, and its index is the Euler characteristic, not the signature; for $\C P^2$ it is $3$.

## Explanations

### L1 human

The signature operator is $d + d^*$ on forms, split by a twisted Hodge star, and its index is the signature of the manifold.
