---
tag: A9J2KK4CEJ
kind: definition
name: Quasiconformal mapping
msc: [30C62, 30C65]
defines: SB8KG46NHP
uses: [0QT00PB5G2, WMXDVF36ZT, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Quasiconformal_mapping
---

## Definition

Let $U$ and $V$ be [[open sets|02BH3MCBQB]] in $\C$ and let $K \ge 1$.
Write $f_z = \frac{1}{2}(f_x - i f_y)$ and $f_{\bar z} = \frac{1}{2}(f_x + i f_y)$ for the [[Wirtinger derivatives|WMXDVF36ZT]] of a function $f$, where $f_x$ and $f_y$ are its partial derivatives.
A map $f \colon U \to V$ is *$K$-quasiconformal* if:

1. $f$ is an orientation-preserving [[homeomorphism|0QT00PB5G2]] of $U$ onto $V$.
2. $f$ has locally square-integrable weak first partial derivatives on $U$, that is, $f$ lies in the Sobolev space $W^{1,2}_{\mathrm{loc}}(U)$.
3. $\abs{f_{\bar z}} \le k \abs{f_z}$ almost everywhere on $U$, where $k = (K - 1)/(K + 1)$.

A map is *quasiconformal* if it is $K$-quasiconformal for some $K \ge 1$.

## Remarks

Example: for $0 \le k < 1$, the real-linear map $f(z) = z + k \bar z$ has $f_z = 1$ and $f_{\bar z} = k$.
Its Jacobian determinant is $\abs{f_z}^2 - \abs{f_{\bar z}}^2 = 1 - k^2 > 0$, so it is an orientation-preserving homeomorphism of $\C$, and it is $K$-quasiconformal with $K = (1 + k)/(1 - k)$.
It maps the unit circle onto an ellipse with axis ratio $(1 + k)/(1 - k)$.
Non-example: complex conjugation $f(z) = \bar z$ is a homeomorphism, but $f_z = 0$ and $f_{\bar z} = 1$, so clause 3 fails for every $K$; it reverses orientation.
The quotient $\mu_f = f_{\bar z} / f_z$ is the complex dilatation of $f$, and $K_f = (1 + \norm{\mu_f}_\infty)/(1 - \norm{\mu_f}_\infty)$ is its maximal dilatation.
A map is $1$-quasiconformal if and only if it is conformal.
An equivalent geometric definition uses the moduli of quadrilaterals or annuli: $f$ is $K$-quasiconformal when it distorts each [[conformal modulus|2FQAKBVBX5]] by a factor of at most $K$.
