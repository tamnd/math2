---
tag: PJN54XYB5T
kind: definition
name: Fractional Fourier transform
msc: [42A38, 44A15, 94A12]
defines: 28VV812XWQ
uses: [DPVM34ADZV, 52VS07H6GK, SASP14MA1Z, MM0EJ2GDE4]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_Fourier_transform
---

## Definition

Let $\psi_n(x) = (2^n n! \sqrt{\pi})^{-1/2} H_n(x) e^{-x^2/2}$, $n \ge 0$, be the normalized [[Hermite functions|52VS07H6GK]]; they form an orthonormal basis of $L^2(\R)$, the [[$L^2$ space|SASP14MA1Z]].
Let $\alpha \in \R$.
The *fractional Fourier transform* of angle $\alpha$ is the [[unitary operator|MM0EJ2GDE4]] $\mathcal{F}_\alpha$ on $L^2(\R)$ given by
$$\mathcal{F}_\alpha \Big( \sum_{n \ge 0} c_n \psi_n \Big) = \sum_{n \ge 0} e^{-i n \alpha}\, c_n \psi_n$$
for every square-summable sequence $(c_n)$.

## Remarks

Let $\mathcal{F} f(\xi) = \frac{1}{\sqrt{2\pi}} \int_\R f(x) e^{-i x \xi}\, dx$ be the unitary [[Fourier transform|DPVM34ADZV]].
Each $\psi_n$ satisfies $\mathcal{F} \psi_n = (-i)^n \psi_n$, so $\mathcal{F}_{\pi/2} = \mathcal{F}$.
Also $\mathcal{F}_0 = \id$, $\mathcal{F}_\pi f(x) = f(-x)$, $\mathcal{F}_\alpha \mathcal{F}_\beta = \mathcal{F}_{\alpha + \beta}$, and $\mathcal{F}_\alpha$ depends only on $\alpha$ modulo $2\pi$.
For $0 < \alpha < \pi$ it is an integral operator: for $f$ integrable and square-integrable,
$$\mathcal{F}_\alpha f(\xi) = \sqrt{\frac{1 - i \cot\alpha}{2\pi}} \int_\R \exp\Big( \frac{i}{2} \cot\alpha\, (x^2 + \xi^2) - \frac{i\, x \xi}{\sin\alpha} \Big) f(x)\, dx,$$
with the principal branch of the square root; at $\alpha = \pi/2$ this is the formula for $\mathcal{F}$.
Some authors use the order $a = 2\alpha/\pi$ instead of the angle, so that $\mathcal{F}$ has order $1$.

Example: $f = \psi_0 = \pi^{-1/4} e^{-x^2/2}$.
Its only coefficient is $c_0 = 1$, and $e^{-i \cdot 0 \cdot \alpha} = 1$, so $\mathcal{F}_\alpha \psi_0 = \psi_0$ for every $\alpha$.

Non-example: the transform $f \mapsto \int_\R f(x) e^{-i x \xi}\, dx$ without the factor $\frac{1}{\sqrt{2\pi}}$ is not $\mathcal{F}_{\pi/2}$.
It sends $\psi_n$ to $\sqrt{2\pi}\, (-i)^n \psi_n$, so it multiplies the coefficient $c_n$ by a number of modulus $\sqrt{2\pi} \ne 1$, and it is not unitary.
