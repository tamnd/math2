---
tag: PW8XX59WNH
kind: definition
name: Laplace transform of distributions
msc: [46F12, 44A10]
defines: 6Z3XJVYT2Q
uses: [AES2T5JPFP, CG9JEATW3Q, 0V49JEZW06, 0KPHENZ5S7, 09C4JP7Y0M]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Definition

Let $T$ be a distribution on $\R$ with support in $[0, \infty)$.
Let $\sigma_0 \in \R$ be such that $e^{-\sigma_0 t} T$ is a [[tempered distribution|AES2T5JPFP]].
Fix a smooth function $\chi \colon \R \to [0, 1]$ with $\chi = 1$ on $[-1/2, \infty)$ and $\chi = 0$ on $(-\infty, -1]$.
The *Laplace transform* of $T$ is the function defined for $\operatorname{Re} s > \sigma_0$ by
$$(\mathcal{L} T)(s) = \left\langle e^{-\sigma_0 t} T, \ \chi(t) \, e^{-(s - \sigma_0) t} \right\rangle.$$

## Remarks

For $\operatorname{Re} s > \sigma_0$, the function $\chi(t) e^{-(s - \sigma_0) t}$ lies in the [[Schwartz space|CG9JEATW3Q]], so the pairing makes sense.
The value does not depend on the choice of $\chi$ or of $\sigma_0$, because $T$ is supported in $[0, \infty)$; formally it is $\langle T, e^{-st} \rangle$.
$\mathcal{L} T$ is holomorphic on $\operatorname{Re} s > \sigma_0$.
For a locally integrable function $f$ of exponential order vanishing on $(-\infty, 0)$, it agrees with the ordinary [[Laplace transform|0V49JEZW06]] $\int_0^\infty e^{-st} f(t) \, dt$.
For all such $T$, $\mathcal{L}(T') = s \, \mathcal{L} T$, and the transform of a convolution is the product of the transforms.

Example: the [[Dirac delta|0KPHENZ5S7]] $\delta$ has support $\set{0}$ and is tempered, so $\sigma_0 = 0$ works, and $\mathcal{L}\delta(s) = \chi(0) e^{0} = 1$.
Likewise $\mathcal{L}\delta'(s) = -\frac{d}{dt}\left(\chi(t) e^{-st}\right)\big|_{t=0} = s$.
With the [[Heaviside step function|09C4JP7Y0M]] $H$, $\mathcal{L} H = 1/s$ and $H' = \delta$, consistent with $\mathcal{L}(H') = s \cdot \frac{1}{s} = 1$.

Non-example: $T = H(t) e^{t^2}$ is a distribution supported in $[0, \infty)$, but the positive function $e^{-\sigma_0 t} e^{t^2}$ grows faster than any polynomial. Hence $e^{-\sigma_0 t} T$ is tempered for no $\sigma_0$, and $T$ has no Laplace transform.
