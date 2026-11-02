---
tag: RDFYHS2Q55
kind: example
name: Laplace transform of a power function
msc: [44A10, 33B15]
illustrates: [0V49JEZW06]
uses: [05XT5AVJBK, 0V3FZMVB4K, 0WFCGVMRRC]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Example

Let $\alpha > -1$ be real and $f(t) = t^\alpha$ for $t > 0$.
Its [[Laplace transform|05XT5AVJBK]] is
$$\mathcal{L}\{t^\alpha\}(s) = \frac{\Gamma(\alpha + 1)}{s^{\alpha + 1}} \quad (\operatorname{Re} s > 0),$$
where $\Gamma$ is the [[gamma function|0V3FZMVB4K]] and $s^{\alpha + 1}$ is the principal power.
For $\alpha = n \in \N$ this is $\mathcal{L}\{t^n\}(s) = n!/s^{n + 1}$, with $n!$ the [[factorial|0WFCGVMRRC]].
Check for real $s > 0$: the substitution $u = st$ gives
$$\int_0^\infty t^\alpha e^{-st}\, dt = \frac{1}{s^{\alpha + 1}} \int_0^\infty u^\alpha e^{-u}\, du = \frac{\Gamma(\alpha + 1)}{s^{\alpha + 1}}.$$
The integral converges at $0$ because $\alpha > -1$, and at $\infty$ because of the factor $e^{-st}$.
Both sides are holomorphic in $s$ on $\operatorname{Re} s > 0$ and agree for real $s > 0$, so they agree on the whole half-plane.
For example, $\mathcal{L}\{t^{-1/2}\}(s) = \sqrt{\pi / s}$, since $\Gamma(1/2) = \sqrt{\pi}$.

## Explanations

### L1 human

Powers of $t$ become negative powers of $s$: $1 \mapsto 1/s$, $t \mapsto 1/s^2$, $t^2 \mapsto 2/s^3$, and so on.
The factorials come from integrating by parts once for each power of $t$.
For powers that are not whole numbers the factorial is replaced by the gamma function.
