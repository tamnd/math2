---
tag: RDPX2NEM47
kind: definition
name: Lanczos sigma factor
msc: [42A24, 42A10, 65T40]
defines: 31G7KHSYEC
uses: [G12KXDHPPS, 5NN2YZZR3V]
sources:
  - url: https://en.wikipedia.org/wiki/Sigma_approximation
---

## Definition

Let $m \ge 1$ be an integer.
Let $k$ be an integer with $\abs{k} < m$.
The *Lanczos sigma factor* of $k$ is $\sigma_{m,0} = 1$ for $k = 0$, and for $k \ne 0$ it is
$$\sigma_{m,k} = \frac{\sin(\pi k / m)}{\pi k / m}.$$
For a $2\pi$-periodic integrable function $f$ with [[Fourier coefficients|5NN2YZZR3V]] $\hat f(k)$, the *sigma approximation* of order $m$ of $f$ is
$$\Sigma_m f(x) = \sum_{\abs{k} < m} \sigma_{m,k} \, \hat f(k) e^{ikx}.$$

## Remarks

Let $S_{m-1} f(x) = \sum_{\abs{k} \le m-1} \hat f(k) e^{ikx}$ be the partial sum of the [[Fourier series|G12KXDHPPS]].
Since $\frac{m}{2\pi} \int_{x - \pi/m}^{x + \pi/m} e^{ikt} \, dt = \frac{\sin(\pi k/m)}{\pi k/m} e^{ikx}$ for $k \ne 0$,
$$\Sigma_m f(x) = \frac{m}{2\pi} \int_{x - \pi/m}^{x + \pi/m} S_{m-1} f(t) \, dt.$$
So the sigma approximation is the moving average of the partial sum over a window of length $2\pi/m$.
In the notation $\operatorname{sinc} u = \frac{\sin \pi u}{\pi u}$, the factors are $\sigma_{m,k} = \operatorname{sinc}(k/m)$.

Example: for $m = 2$ and $f(x) = \cos x$, the factor is $\sigma_{2, \pm 1} = \frac{\sin(\pi/2)}{\pi/2} = \frac{2}{\pi}$, so $\Sigma_2 f(x) = \frac{2}{\pi} \cos x$.
This agrees with the window average $\frac{1}{\pi} \int_{x - \pi/2}^{x + \pi/2} \cos t \, dt = \frac{2}{\pi} \cos x$.

Non-example: the [[Fejér weights|MA8X1G11DH]] $1 - \abs{k}/m$ also fade out high frequencies, but they are not the sigma factors; for $m = 2$ and $k = 1$ they give $1/2$, not $2/\pi$.
