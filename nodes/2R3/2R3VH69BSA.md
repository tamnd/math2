---
tag: 2R3VH69BSA
kind: definition
name: Clausen function
msc: ["33B30", "33E20"]
defines: AVS6G54711
uses: [04DXAFN2ES, G12KXDHPPS]
sources:
  - url: https://en.wikipedia.org/wiki/Clausen_function
---

## Definition

The *Clausen function* is the function $\operatorname{Cl}_2 \colon \R \to \R$ given by
$$\operatorname{Cl}_2(\theta) = -\int_0^{\theta} \log \abs{2 \sin \tfrac{t}{2}} \, dt,$$
where $\log$ is the [[natural logarithm|04DXAFN2ES]].
The integral converges for every real $\theta$, because the logarithmic singularities of the integrand at the points of $2\pi\Z$ are integrable.

## Remarks

Equivalently, $\operatorname{Cl}_2$ is the sum of the uniformly convergent [[Fourier series|G12KXDHPPS]]
$$\operatorname{Cl}_2(\theta) = \sum_{k=1}^{\infty} \frac{\sin k\theta}{k^2},$$
and $\operatorname{Cl}_2(\theta) = \operatorname{Im} \operatorname{Li}_2(e^{i\theta})$, where $\operatorname{Li}_2$ is the [[dilogarithm|G0X0NWSDB7]].
The function is odd and $2\pi$-periodic, and it vanishes at every multiple of $\pi$.

Example: at $\theta = \pi/2$, $\sin(k\pi/2)$ is $0$ for even $k$ and $(-1)^{m}$ for $k = 2m + 1$, so $\operatorname{Cl}_2(\pi/2) = \sum_{m \ge 0} (-1)^m / (2m+1)^2 = G$, Catalan's constant.
Its maximum on $\R$ is $\operatorname{Cl}_2(\pi/3) \approx 1.01494$.

Non-example: the series $\sum_{k \ge 1} \cos(k\theta)/k^2$ is not the Clausen function; it is the real part of $\operatorname{Li}_2(e^{i\theta})$, which equals $\frac{\pi^2}{6} - \frac{\pi\theta}{2} + \frac{\theta^2}{4}$ for $0 \le \theta \le 2\pi$.

Higher Clausen functions $\operatorname{Cl}_n$ are defined from $\operatorname{Li}_n(e^{i\theta})$ in a similar way.
