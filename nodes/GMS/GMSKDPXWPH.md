---
tag: GMSKDPXWPH
kind: definition
name: Szegő kernel
msc: [32A25, 32A35]
defines: Y1XE9SQB5A
uses: [507C34W0ZT, PNNNFJVF6W, 4CK2GSRAGD, 065HE5V98E]
sources:
  - url: https://en.wikipedia.org/wiki/Szeg%C5%91_kernel
---

## Definition

Let $\Omega \subset \C^n$ be a bounded domain with $C^2$ boundary $\partial\Omega$, and let $\sigma$ be the [[surface measure|065HE5V98E]] on $\partial\Omega$.
Let $H^2(\partial\Omega)$ be the closure in $L^2(\partial\Omega, \sigma)$ of the restrictions to $\partial\Omega$ of the functions [[holomorphic|507C34W0ZT]] on a neighbourhood of $\overline{\Omega}$.
Each $f \in H^2(\partial\Omega)$ is the boundary value of a unique holomorphic function on $\Omega$, also written $f$.
For each $z \in \Omega$, the map $f \mapsto f(z)$ is a bounded linear functional on the Hilbert space $H^2(\partial\Omega)$.
The *Szegő kernel* of $\Omega$ is the function $S \colon \Omega \times \partial\Omega \to \C$ such that, for each $z \in \Omega$, the function $\zeta \mapsto \overline{S(z, \zeta)}$ lies in $H^2(\partial\Omega)$ and
$$f(z) = \int_{\partial\Omega} S(z, \zeta) \, f(\zeta) \, d\sigma(\zeta) \quad \text{for all } f \in H^2(\partial\Omega).$$

## Remarks

By the Riesz representation theorem the function $\overline{S(z, \cdot)}$ exists and is unique.
So $S$ is the reproducing kernel of the [[Hardy space|PNNNFJVF6W]] $H^2(\partial\Omega)$, in the sense of [[reproducing kernel Hilbert spaces|4CK2GSRAGD]].
The kernel extends to $\Omega \times \Omega$, holomorphic in the first variable and antiholomorphic in the second, with $S(z, w) = \overline{S(w, z)}$.

Example: for the unit disc $\mathbb{D} \subset \C$ with arc length, $S(z, \zeta) = \dfrac{1}{2\pi(1 - z\bar\zeta)}$.
Check: for $\abs{\zeta} = 1$ one has $\bar\zeta = 1/\zeta$, so $\dfrac{1}{1 - z\bar\zeta} = \dfrac{\zeta}{\zeta - z}$, and $d\sigma = \abs{d\zeta} = \dfrac{d\zeta}{i\zeta}$.
The formula becomes $f(z) = \dfrac{1}{2\pi i}\displaystyle\oint_{\abs{\zeta} = 1} \dfrac{f(\zeta)}{\zeta - z}\, d\zeta$, which is Cauchy's integral formula.
For the unit ball of $\C^n$ the kernel is $S(z, \zeta) = \dfrac{(n-1)!}{2\pi^n} (1 - \ip{z}{\zeta})^{-n}$, where $\ip{z}{\zeta} = \sum_j z_j \bar\zeta_j$; at $z = 0$ it is $1$ divided by the area $2\pi^n/(n-1)!$ of the sphere.

Non-example: on the unit disc, the Poisson kernel $P(z, \zeta) = \dfrac{1 - \abs{z}^2}{2\pi\abs{\zeta - z}^2}$ also satisfies $f(z) = \int_{\partial\mathbb{D}} P(z, \zeta) f(\zeta) \, d\sigma(\zeta)$ for all $f \in H^2(\partial\mathbb{D})$.
It is not the Szegő kernel, because for $z \ne 0$ the function $\zeta \mapsto P(z, \zeta)$ has nonzero Fourier coefficients of negative index, so it does not lie in $H^2(\partial\mathbb{D})$.

The [[Bergman kernel|8RWDHW0CXC]] is defined in the same way, with $L^2(\Omega)$ in place of $L^2(\partial\Omega, \sigma)$.
