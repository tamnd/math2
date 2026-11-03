---
tag: ARM5EN11YN
kind: definition
name: Hamiltonian perturbation theory
msc: [70H09, 70H08]
defines: JYS0H01WK2
uses: [M3T81YNSKC, G026JG1YX5, D4TRNRC45C, AAECHE30BD]
sources:
  - url: https://en.wikipedia.org/wiki/Perturbation_theory
---

## Definition

Let $D \subseteq \R^n$ be open, let $\mathbb{T}^n = \R^n / 2\pi \Z^n$, and let
$$H_\varepsilon(I, \theta) = H_0(I) + \varepsilon H_1(I, \theta)$$
be a smooth Hamiltonian on $D \times \mathbb{T}^n$ in [[action-angle coordinates|M3T81YNSKC]], with a real parameter $\varepsilon$.
Let $\omega(I) = \nabla H_0(I)$ be the unperturbed frequencies, and let $\langle H_1 \rangle(I) = (2\pi)^{-n} \int_{\mathbb{T}^n} H_1(I, \theta) \, d\theta$ be the average over the angles.
*First-order Hamiltonian perturbation theory* seeks a [[canonical transformation|G026JG1YX5]] $(I, \theta) \mapsto (J, \varphi)$ of a special form.
Its type 2 [[generating function|D4TRNRC45C]] is
$$F(J, \theta) = J \cdot \theta + \varepsilon S(J, \theta),$$
so that $I = J + \varepsilon \, \partial S / \partial \theta$ and $\varphi = \theta + \varepsilon \, \partial S / \partial J$.
The function $S$ solves the *homological equation*
$$\omega(J) \cdot \frac{\partial S}{\partial \theta}(J, \theta) + H_1(J, \theta) = \langle H_1 \rangle(J).$$
In the new variables the Hamiltonian is $H_0(J) + \varepsilon \langle H_1 \rangle(J) + O(\varepsilon^2)$, which does not depend on the angles up to order $\varepsilon^2$.
Higher orders repeat the step with the remainder.

## Remarks

The new Hamiltonian follows from a Taylor expansion: $H_0(J + \varepsilon \partial_\theta S) + \varepsilon H_1 = H_0(J) + \varepsilon (\omega \cdot \partial_\theta S + H_1) + O(\varepsilon^2)$.
With the [[Fourier series|AAECHE30BD]] $H_1 = \sum_{k \in \Z^n} h_k(J) e^{i k \cdot \theta}$, the solution is
$$S(J, \theta) = \sum_{k \ne 0} \frac{i \, h_k(J)}{k \cdot \omega(J)} e^{i k \cdot \theta},$$
which requires $k \cdot \omega(J) \ne 0$ for every $k$ with $h_k \ne 0$; the numbers $k \cdot \omega$ are the small divisors.

Example: $n = 1$, $H_\varepsilon = I + \varepsilon I \cos \theta$, so $\omega = 1$ and $\langle H_1 \rangle = 0$.
The homological equation $\partial_\theta S = -J \cos \theta$ has the solution $S = -J \sin \theta$, and the new Hamiltonian is $J + O(\varepsilon^2)$.

Non-example: for $n = 2$, $H_0 = I_1 - I_2$ and $H_1 = \cos(\theta_1 + \theta_2)$, the frequency is $\omega = (1, -1)$ and $k = (1, 1)$ gives $k \cdot \omega = 0$.
The homological equation then has no solution, since the left side has no $e^{i(\theta_1 + \theta_2)}$ term while $H_1 - \langle H_1 \rangle$ does; this is a resonance.
