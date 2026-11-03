---
tag: T39WGAQD0K
kind: definition
name: Young's modulus
msc: [74B05]
defines: T8ENJX1905
uses: [80737NDZ4V, 8QS6QMJF5Z, KG2XWEMJ30]
sources:
  - url: https://en.wikipedia.org/wiki/Young%27s_modulus
---

## Definition

Let a homogeneous isotropic linear elastic material have [[Lamé parameters|80737NDZ4V]] $\lambda$ and $\mu$, with $\mu > 0$ and $3\lambda + 2\mu > 0$, so that $\lambda + \mu > 0$ as well.
Consider the state of uniaxial stress $\sigma = s \, e_1 \otimes e_1$ with $s \ne 0$, where $\sigma$ is the [[Cauchy stress tensor|KG2XWEMJ30]].
Let $\varepsilon$ be the [[strain|8QS6QMJF5Z]] that produces this stress.
The *Young's modulus* of the material is
$$E = \frac{\sigma_{11}}{\varepsilon_{11}} = \frac{\mu (3\lambda + 2\mu)}{\lambda + \mu}.$$

## Remarks

The ratio does not depend on $s$, because the law is linear.
Example: inverting $\sigma = \lambda (\tr \varepsilon) I + 2\mu \varepsilon$ for $\sigma = s \, e_1 \otimes e_1$ gives $\tr \varepsilon = s/(3\lambda + 2\mu)$ and $\varepsilon_{11} = \frac{s(\lambda + \mu)}{\mu(3\lambda + 2\mu)}$, which is the formula above.
With the steel values $\lambda \approx 120$ GPa and $\mu \approx 80$ GPa it gives $E \approx 80 \cdot 520 / 200 = 208$ GPa.

Non-example: in uniaxial strain the sides are held fixed, so that only $\varepsilon_{11} \ne 0$.
Then $\sigma_{11} / \varepsilon_{11} = \lambda + 2\mu$, the P-wave modulus, which is larger than $E$ when $\lambda > 0$.
The definition requires the sides to be free of stress.

For a bar of length $L$ and cross-section $A$ pulled by a force $F$, the elongation is $\Delta L = F L / (E A)$.
For anisotropic materials Young's modulus depends on the direction of the pull.
