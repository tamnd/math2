---
tag: SE2KEW5QFH
kind: definition
name: Euclidean quantum gravity
msc: [83C45, 81S40]
defines: MGPT8N01FW
uses: [7CBT4SM83Y, 1NYTFT5NPE, G686S8SEK0, JPE3A1SN7V, SAAB5S5A0D]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_quantum_gravity
---

## Definition

Let $M$ be a four-manifold with boundary $\partial M$, and let $h$ be a Riemannian metric on $\partial M$.
For a [[Riemannian metric|7CBT4SM83Y]] $g$ on $M$ inducing $h$ on $\partial M$, the Euclidean gravitational action is
$$I[g] = -\frac{1}{16 \pi G} \int_M (R - 2\Lambda) \sqrt{g} \, d^4x - \frac{1}{8 \pi G} \int_{\partial M} K \sqrt{h} \, d^3x.$$
Here $R$ is the scalar curvature of $g$, $\Lambda$ is the cosmological constant and $K$ is the trace of the extrinsic curvature of $\partial M$.
The boundary term is the [[Gibbons–Hawking–York term|SAAB5S5A0D]].
*Euclidean quantum gravity* defines amplitudes and partition functions by the formal [[path integral|1NYTFT5NPE]]
$$Z[h] = \int \mathcal{D}[g] \; e^{-I[g]/\hbar}$$
in units $c = 1$.
The integral runs over Riemannian metrics $g$ on $M$ that induce $h$ on $\partial M$, up to diffeomorphism.
It may also run over the topology of $M$.

## Remarks

The action $I$ is $-i$ times the Lorentzian [[Einstein–Hilbert action|JPE3A1SN7V]] with boundary term after the [[Wick rotation|G686S8SEK0]] $t = -i\tau$.
Example: the Euclidean Schwarzschild metric $\left(1 - \frac{2GM}{r}\right) d\tau^2 + \left(1 - \frac{2GM}{r}\right)^{-1} dr^2 + r^2 d\Omega^2$ is smooth at $r = 2GM$ only if $\tau$ has period $\beta = 8 \pi G M$ (with $\hbar = c = k_B = 1$).
Taking this saddle point, $Z \approx e^{-I}$ with $I = 4\pi G M^2$, gives the Hawking temperature $1/\beta$ and the Bekenstein–Hawking entropy $4 \pi G M^2$, a quarter of the horizon area in Planck units.
Non-example: a Lorentzian metric is not in the domain of the integral, since its weight $e^{iS/\hbar}$ is oscillatory and not of the form $e^{-I/\hbar}$.
The action is unbounded below under conformal rescalings $g \mapsto \Omega^2 g$ (the conformal factor problem), so the integral does not converge as written.
