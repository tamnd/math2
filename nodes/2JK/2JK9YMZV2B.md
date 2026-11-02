---
tag: 2JK9YMZV2B
kind: statement
role: theorem
name: Weyl's law
msc: [35P20, 58J50]
uses: [0E0B6RA8K0, EETVA6QYX4, 0BQAA2BK3Q]
about: [0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Weyl_law
same_as:
  wikidata: Q7990330
  wikipedia: Weyl law
---

## Statement

Let $d \ge 1$ and let $\Omega \subseteq \R^d$ be a nonempty bounded open set with Lebesgue measure $\abs{\Omega}$.
Let $0 < \lambda_1 \le \lambda_2 \le \cdots$ be the [[eigenvalues|0BQAA2BK3Q]] of $-\Delta$ on $\Omega$ with the [[Dirichlet boundary condition|EETVA6QYX4]], repeated according to multiplicity, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
For $\lambda > 0$ let $N(\lambda)$ be the number of indices $k$ with $\lambda_k \le \lambda$.
Let $\omega_d$ be the volume of the unit ball in $\R^d$.
Then
$$\lim_{\lambda \to \infty} \frac{N(\lambda)}{\lambda^{d/2}} = \frac{\omega_d \abs{\Omega}}{(2\pi)^d}.$$

## Remarks

For a cube the eigenvalues are explicit, and counting them amounts to counting lattice points in a ball of radius $\sqrt{\lambda}$, which gives the formula.
For a general set one fills $\Omega$ from inside and covers it from outside by small cubes.
Then one compares eigenvalues with Dirichlet and Neumann conditions on the cubes; this is Dirichlet–Neumann bracketing.
Example: for $\Omega = (0, L) \subseteq \R$, the eigenvalues are $(k\pi / L)^2$ for $k \ge 1$, so $N(\lambda) = \floor{L \sqrt{\lambda} / \pi}$.
This agrees with the formula, since $\omega_1 = 2$ and $\frac{2L}{2\pi} = \frac{L}{\pi}$.
Equivalently, $\lambda_k \sim \frac{(2\pi)^2}{(\omega_d \abs{\Omega})^{2/d}} \, k^{2/d}$ as $k \to \infty$.
Hermann Weyl proved the law in 1911.

## Explanations

### L1 human

Up to a constant factor, the eigenvalues of the Laplacian on a region are the squares of the pitches of a drum of that shape.
Weyl's law says that, for high pitches, the number of notes below a given pitch depends only on the dimension and the size of the drum, not on its shape.

### L2 human

Weyl's law shows that the volume of a domain can be read off from its spectrum.
So it gives a first positive answer to the question whether one can hear the shape of a drum.
The same leading term holds for the Neumann condition when the boundary is regular enough, and an analogous law holds on compact Riemannian manifolds.
