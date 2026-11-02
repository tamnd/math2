---
tag: ZE4QPBC1AF
kind: definition
name: Hartley transform
msc: [44A15, 42A38, 94A12]
defines: WEHYECYAVJ
uses: [DPVM34ADZV, X7GTF3D98F]
sources:
  - url: https://en.wikipedia.org/wiki/Hartley_transform
---

## Definition

Let $f \colon \R \to \C$ be Lebesgue [[integrable|X7GTF3D98F]].
Let $\operatorname{cas}(x) = \cos x + \sin x$.
The *Hartley transform* of $f$ is the function $\mathcal{H} f \colon \R \to \C$ given by
$$(\mathcal{H} f)(\omega) = \frac{1}{\sqrt{2\pi}} \int_\R f(t)\, \operatorname{cas}(\omega t)\, dt.$$

## Remarks

Let $F(\omega) = \frac{1}{\sqrt{2\pi}} \int_\R f(t) e^{-i\omega t}\, dt$ be the unitary [[Fourier transform|DPVM34ADZV]] with angular frequency.
For real $f$, $\operatorname{Re} F(\omega) = \frac{1}{\sqrt{2\pi}} \int f(t) \cos(\omega t)\, dt$ and $\operatorname{Im} F(\omega) = -\frac{1}{\sqrt{2\pi}} \int f(t) \sin(\omega t)\, dt$, so $\mathcal{H} f = \operatorname{Re} F - \operatorname{Im} F$.
In general $\mathcal{H} f(\omega) = \frac{1 + i}{2} F(\omega) + \frac{1 - i}{2} F(-\omega)$.
From this formula and the Fourier inversion theorem, $\mathcal{H}(\mathcal{H} f) = f$ when $f$ and $\mathcal{H} f$ are integrable and $f$ is continuous.
Also $\mathcal{H}$ extends to a unitary operator on $L^2(\R)$ with $\mathcal{H}^2 = \id$.

Example: $f(t) = e^{-t^2/2}$.
Since $f$ is even, $\int f(t) \sin(\omega t)\, dt = 0$, and $\frac{1}{\sqrt{2\pi}} \int e^{-t^2/2} \cos(\omega t)\, dt = e^{-\omega^2/2}$.
So $\mathcal{H} f(\omega) = e^{-\omega^2/2}$.

Non-example: $f(t) = 1$ is not integrable on $\R$, and $\int_\R \operatorname{cas}(\omega t)\, dt$ does not converge for any $\omega$.
