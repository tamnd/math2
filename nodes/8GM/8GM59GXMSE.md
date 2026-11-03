---
tag: 8GM59GXMSE
kind: definition
name: Coherence
msc: [78A10, 60G10]
defines: VQCMBT9YSK
uses: [DT0QXJE705, KX1EXRW47E, 0RFWW56Y22, 3ZXN26PW4G]
sources:
  - url: https://en.wikipedia.org/wiki/Coherence_(physics)
---

## Definition

Let $U(\mathbf r, t)$ be a complex scalar wave field, given as a random process in time at each point $\mathbf r$.
Assume that for any two points the processes are jointly wide-sense [[stationary|DT0QXJE705]] with finite second moments.
The *mutual coherence function* of the points $\mathbf r_1, \mathbf r_2$ is
$$\Gamma_{12}(\tau) = E\bigl[U(\mathbf r_1, t + \tau) \, \overline{U(\mathbf r_2, t)}\bigr], \qquad \tau \in \R,$$
which does not depend on $t$.
Let $I_j = \Gamma_{jj}(0)$ be the mean intensity at $\mathbf r_j$, and assume $I_1, I_2 > 0$.
The *complex degree of coherence* is $\gamma_{12}(\tau) = \Gamma_{12}(\tau) / \sqrt{I_1 I_2}$.
The field is *coherent* at $(\mathbf r_1, \mathbf r_2, \tau)$ if $\abs{\gamma_{12}(\tau)} = 1$, *incoherent* if $\gamma_{12}(\tau) = 0$, and *partially coherent* otherwise.

## Remarks

The [[Cauchy–Schwarz inequality|0RFWW56Y22]] gives $\abs{\gamma_{12}(\tau)} \le 1$.
*Temporal coherence* is described by $\gamma_{11}(\tau)$ at one point, and *spatial coherence* by $\gamma_{12}(0)$.
Put two equal pinholes at $\mathbf r_1$ and $\mathbf r_2$, as in Young's experiment, and look where the path delay between them is $\tau$.
There the [[interference|KX1EXRW47E]] fringes have visibility $V = \frac{2\sqrt{I_1 I_2}}{I_1 + I_2} \abs{\gamma_{12}(\tau)}$.
By the [[Wiener–Khinchin theorem|3ZXN26PW4G]], $\Gamma_{11}$ is the Fourier transform of the power spectrum of the light, so a narrow spectrum gives a long coherence time.

Example: a monochromatic plane wave $U = a \, e^{i(\mathbf k \cdot \mathbf r - \omega t + \Phi)}$, with $a > 0$ and a phase $\Phi$ uniform on $[0, 2\pi)$, has
$$\Gamma_{12}(\tau) = a^2 e^{i \mathbf k \cdot (\mathbf r_1 - \mathbf r_2)} e^{-i\omega\tau}.$$
So $\abs{\gamma_{12}(\tau)} = 1$ for all points and delays: the wave is fully coherent.

Non-example: if $U(\mathbf r_1, \cdot)$ and $U(\mathbf r_2, \cdot)$ are independent with mean zero, then $\Gamma_{12} = 0$ and the two points are incoherent.
Light from two separate lamps behaves this way, and it gives no stable fringes.
