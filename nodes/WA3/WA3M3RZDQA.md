---
tag: WA3M3RZDQA
kind: definition
name: de Rham cohomology
msc: [58A12, 57R19]
defines: GX74C07T0G
uses: [F45VQ47GPV, 0E3G0GRPZ6, 0ZHSTAG8ZY]
sources:
  - url: https://en.wikipedia.org/wiki/De_Rham_cohomology
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]], and for $k \ge 0$ let $\Omega^k(M)$ be the real vector space of smooth [[differential forms|0E3G0GRPZ6]] of degree $k$ on $M$.
Let $d \colon \Omega^k(M) \to \Omega^{k+1}(M)$ be the [[exterior derivative|0ZHSTAG8ZY]]; it satisfies $d \circ d = 0$.
A form $\omega$ is *closed* if $d\omega = 0$, and *exact* if $\omega = d\eta$ for some $\eta \in \Omega^{k-1}(M)$; for $k = 0$ only the zero form counts as exact.
The $k$-th *de Rham cohomology group* of $M$ is the quotient vector space
$$H^k_{\mathrm{dR}}(M) = \frac{\ker\big(d \colon \Omega^k(M) \to \Omega^{k+1}(M)\big)}{\im\big(d \colon \Omega^{k-1}(M) \to \Omega^k(M)\big)}.$$

## Remarks

Since $d \circ d = 0$, every exact form is closed, so the quotient makes sense.
$H^0_{\mathrm{dR}}(M)$ is the space of locally constant functions, so when $M$ has finitely many connected components its dimension is their number.
Example: on $\R^n$ every closed $k$-form with $k \ge 1$ is exact, by the Poincaré lemma, so $H^k_{\mathrm{dR}}(\R^n) = 0$ for $k \ge 1$ and $H^0_{\mathrm{dR}}(\R^n) = \R$.
Non-example of exactness: on $M = \R^2 \setminus \set{0}$ the form $\omega = (x \, dy - y \, dx)/(x^2 + y^2)$ is closed but not exact.
Its integral over the unit circle is $2\pi$, while the integral of an exact form $df$ over a closed loop is $0$; so $H^1_{\mathrm{dR}}(\R^2 \setminus \set{0}) \neq 0$, and in fact it is $\R$.
A smooth map $f \colon M \to N$ induces linear maps $f^* \colon H^k_{\mathrm{dR}}(N) \to H^k_{\mathrm{dR}}(M)$ by pullback of forms, and the wedge product of forms makes $\bigoplus_k H^k_{\mathrm{dR}}(M)$ a graded ring.
