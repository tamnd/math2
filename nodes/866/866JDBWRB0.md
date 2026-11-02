---
tag: 866JDBWRB0
kind: definition
name: Single layer potential
msc: [31B10, 31A10]
defines: 9T6ZEV4125
uses: [02BH3MCBQB, 05D5EGMFYV, 065HE5V98E, BSJ8X2XRN9, 0DEB0JMN0W, JHKSF3XFY2, DCMFQ01QGS]
sources:
  - url: https://en.wikipedia.org/wiki/Newtonian_potential
---

## Definition

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded [[open set|02BH3MCBQB]] whose [[boundary|05D5EGMFYV]] $\partial\Omega$ is a $C^1$ hypersurface, with surface measure $\sigma$.
Let $\Phi$ be the [[fundamental solution of the Laplacian|BSJ8X2XRN9]],
$$\Phi(x) = -\frac{1}{2\pi} \log\abs{x} \ (n = 2), \qquad \Phi(x) = \frac{1}{(n-2)\,\omega_n}\, \abs{x}^{2-n} \ (n \ge 3),$$
where $\omega_n$ is the area of the unit sphere in $\R^n$, so that $-\Delta \Phi = \delta_0$.
Let $\varphi \colon \partial\Omega \to \R$ be continuous.
The *single layer potential* with density $\varphi$ is the function
$$S\varphi(x) = \int_{\partial\Omega} \Phi(x - y)\, \varphi(y)\, d\sigma(y), \qquad x \in \R^n.$$

## Remarks

The integral is a [[surface integral|065HE5V98E]].
For $x \notin \partial\Omega$ the integrand is smooth in $x$, and $S\varphi$ is [[harmonic|0DEB0JMN0W]] on $\R^n \setminus \partial\Omega$.
For $x \in \partial\Omega$ the singularity of $\Phi(x - y)$ is integrable on the $(n-1)$-dimensional surface, so $S\varphi(x)$ is still defined.
It is the [[potential of the measure|JHKSF3XFY2]] $\varphi\,\sigma$ carried by $\partial\Omega$.

Example: let $\Omega$ be the unit ball in $\R^3$ and $\varphi \equiv 1$.
Then $\Phi(x) = 1/(4\pi\abs{x})$ and the mean of $1/\abs{x - y}$ over the unit sphere in $y$ is $1/\max(\abs{x}, 1)$.
Since the sphere has area $4\pi$, $S\varphi(x) = 1$ for $\abs{x} \le 1$ and $S\varphi(x) = 1/\abs{x}$ for $\abs{x} \ge 1$.
It is continuous across the sphere, while its radial derivative jumps from $0$ to $-1$.

Non-example: the integral $\int_\Omega \Phi(x - y) f(y)\, dy$ over the open set itself is a volume potential, the [[Newtonian potential|DCMFQ01QGS]] of $f$, and not a single layer potential.
It is a potential of a charge spread through a solid, not over a surface.
