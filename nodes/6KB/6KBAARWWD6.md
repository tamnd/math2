---
tag: 6KBAARWWD6
kind: definition
name: Bargmann transform
msc: [44A15, 30H20, "46E22"]
defines: QPH28QH036
uses: [SASP14MA1Z, 0G4F0XB9X2, HM2HHE3J51, MM0EJ2GDE4, 52VS07H6GK]
sources:
  - url: https://en.wikipedia.org/wiki/Segal%E2%80%93Bargmann_space
---

## Definition

Let $\mathcal{F}^2$ be the space of [[entire functions|0G4F0XB9X2]] $F$ with
$$\norm{F}^2 = \frac{1}{\pi} \int_\C \abs{F(z)}^2 e^{-\abs{z}^2}\, dA(z) < \infty,$$
where $dA$ is Lebesgue measure on $\C = \R^2$.
It is a [[Hilbert space|HM2HHE3J51]], the Segal–Bargmann space.
The *Bargmann transform* of $f \in L^2(\R)$, the [[$L^2$ space|SASP14MA1Z]], is the function
$$Bf(z) = \pi^{-1/4} \int_\R \exp\Big( -\frac{z^2}{2} + \sqrt{2}\, z x - \frac{x^2}{2} \Big) f(x)\, dx, \qquad z \in \C.$$

## Remarks

For fixed $z$ the kernel is a Gaussian in $x$, so it lies in $L^2(\R)$, and the integral converges by the Cauchy–Schwarz inequality.
The function $Bf$ is entire, and $B$ is a [[unitary operator|MM0EJ2GDE4]] from $L^2(\R)$ onto $\mathcal{F}^2$.
The monomials $z^n / \sqrt{n!}$ form an orthonormal basis of $\mathcal{F}^2$, and $B$ maps the normalized [[Hermite function|52VS07H6GK]] $\psi_n$ to $z^n / \sqrt{n!}$.
Conventions differ: some authors use the weight $e^{-\pi \abs{z}^2}$ or $e^{-\abs{z}^2/\hbar}$ and rescale the kernel accordingly.

Example: $f = \psi_0 = \pi^{-1/4} e^{-x^2/2}$.
Then $Bf(z) = \pi^{-1/2} e^{-z^2/2} \int_\R e^{-x^2 + \sqrt{2} z x}\, dx = \pi^{-1/2} e^{-z^2/2} \cdot \sqrt{\pi}\, e^{z^2/2} = 1$.
The constant $1$ has norm $\frac{1}{\pi} \int_\C e^{-\abs{z}^2}\, dA = 1$, equal to $\norm{\psi_0}_{L^2} = 1$.

Non-example: the function $F(z) = e^{z^2}$ is entire but not in $\mathcal{F}^2$.
On the real axis $\abs{F(x)}^2 e^{-x^2} = e^{x^2}$, and the integral of $\abs{F}^2 e^{-\abs{z}^2}$ over a neighbourhood of the real axis diverges, so $F$ is not a Bargmann transform.
