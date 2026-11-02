---
tag: J28WVG6KPT
kind: definition
name: Double layer potential
msc: [31B10, 31A10]
defines: EG8Z3FWV9A
uses: [02BH3MCBQB, 05D5EGMFYV, 065HE5V98E, BSJ8X2XRN9, 0DEB0JMN0W, 0JX86PSSA9, 9T6ZEV4125]
sources:
  - url: https://en.wikipedia.org/wiki/Double_layer_potential
---

## Definition

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded [[open set|02BH3MCBQB]] whose [[boundary|05D5EGMFYV]] $\partial\Omega$ is a $C^1$ hypersurface.
Let $\sigma$ be surface measure on $\partial\Omega$ and $\nu(y)$ the outward unit normal at $y \in \partial\Omega$.
Let $\Phi$ be the [[fundamental solution of the Laplacian|BSJ8X2XRN9]], normalised by $-\Delta\Phi = \delta_0$.
Let $\varphi \colon \partial\Omega \to \R$ be continuous.
The *double layer potential* with density $\varphi$ is the function
$$D\varphi(x) = \int_{\partial\Omega} \frac{\partial \Phi(x - y)}{\partial \nu(y)}\, \varphi(y)\, d\sigma(y), \qquad x \in \R^n \setminus \partial\Omega,$$
where $\dfrac{\partial \Phi(x - y)}{\partial \nu(y)} = \nu(y) \cdot \nabla_y \big[\Phi(x - y)\big]$ is the derivative in $y$ along the outward normal.

## Remarks

The integral is a [[surface integral|065HE5V98E]] with an integrand that is smooth in $x$ off $\partial\Omega$, and $D\varphi$ is [[harmonic|0DEB0JMN0W]] on $\R^n \setminus \partial\Omega$.
For $n = 3$, $\Phi(x) = 1/(4\pi\abs{x})$ and the kernel is $\dfrac{\nu(y) \cdot (x - y)}{4\pi \abs{x - y}^3}$.

Example (Gauss's integral): let $\varphi \equiv 1$.
By the [[divergence theorem|0JX86PSSA9]], $D1(x) = -1$ for $x \in \Omega$ and $D1(x) = 0$ for $x \notin \overline{\Omega}$.
For the unit ball in $\R^3$ and $x = 0$ this is a direct check: $\nu(y) = y$, so the kernel is $y \cdot (-y)/(4\pi) = -1/(4\pi)$, and the sphere has area $4\pi$.

Non-example: replacing the normal derivative of $\Phi$ by $\Phi$ itself gives the [[single layer potential|9T6ZEV4125]] instead.
For the unit ball in $\R^3$ with $\varphi \equiv 1$, that potential equals $1$ inside the ball, while the double layer potential equals $-1$ there.
