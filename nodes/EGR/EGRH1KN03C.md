---
tag: EGRH1KN03C
kind: definition
name: Harmonic measure
msc: [31A15, 30C85]
defines: CFD7BPM51W
uses: [0W5NJQ8MKY, 8D56GQ4AG8, 0BVHZXWKCD, TCYSWCTYYM, 0JJ9J1XZ8G, 097KNJFJ7V]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_measure
---

## Definition

Let $\Omega \subset \C$ be a bounded [[domain|097KNJFJ7V]] with [[boundary|0JJ9J1XZ8G]] $\partial\Omega$.
Assume that the [[Dirichlet problem|8D56GQ4AG8]] on $\Omega$ is solvable for continuous data.
That is, for every continuous $\varphi \colon \partial\Omega \to \R$ there is a continuous $u_\varphi \colon \overline{\Omega} \to \R$ that is [[harmonic|0W5NJQ8MKY]] on $\Omega$ and equals $\varphi$ on $\partial\Omega$.
By the maximum principle, $u_\varphi$ is unique.
Let $z \in \Omega$.
The *harmonic measure* of $\Omega$ at $z$ is the unique Borel probability measure $\omega_z = \omega(z, \cdot, \Omega)$ on $\partial\Omega$ such that
$$u_\varphi(z) = \int_{\partial\Omega} \varphi \, d\omega_z \qquad \text{for every continuous } \varphi \colon \partial\Omega \to \R.$$
For a [[Borel set|0BVHZXWKCD]] $E \subseteq \partial\Omega$, the number $\omega(z, E, \Omega) = \omega_z(E)$ is the harmonic measure of $E$ at $z$.

## Remarks

The measure exists by the Riesz representation theorem.
Indeed, by the maximum principle, $\varphi \mapsto u_\varphi(z)$ is a positive linear functional on the continuous functions on $\partial\Omega$, and it sends $1$ to $1$.
For fixed $E$, the function $z \mapsto \omega(z, E, \Omega)$ is harmonic on $\Omega$ with values in $[0, 1]$.
Example: for the unit disc $\mathbb{D}$, the [[Poisson kernel|TCYSWCTYYM]] gives $d\omega_z(e^{i\theta}) = \frac{1 - \abs{z}^2}{2\pi \abs{e^{i\theta} - z}^2} \, d\theta$.
At $z = 0$ this is $d\theta / 2\pi$, so the harmonic measure of an arc is its length divided by $2\pi$.
Non-example: the punctured disc $\mathbb{D} \setminus \set{0}$ does not satisfy the hypothesis.
The data $1$ at $0$ and $0$ on the unit circle have no harmonic solution that is continuous up to the boundary.
With the more general Perron solution, the point $0$ gets harmonic measure $0$.
If $f \colon \Omega \to \Omega'$ is a conformal map that extends to a homeomorphism of the closures, then $\omega(f(z), f(E), \Omega') = \omega(z, E, \Omega)$.
Probabilistically, $\omega(z, E, \Omega)$ is the probability that a Brownian motion started at $z$ first leaves $\Omega$ through $E$.
