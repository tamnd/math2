---
tag: 4D1E2YYJNZ
kind: example
name: Bilateral Laplace transform of a probability law
msc: [44A10, "60E10"]
instance_of: [6J2AGD0BYY]
uses: [059TJN0NZ1, 0WQVXP7PDB, 05AQE0QR0D, 0E99F51GVB]
sources:
  - url: https://en.wikipedia.org/wiki/Two-sided_Laplace_transform
---

## Example

Let $\mu$ be a [[probability measure|059TJN0NZ1]] on $\R$, for example the law of a real random variable $X$.
Its [[two-sided Laplace transform|6J2AGD0BYY]] is
$$\mathcal{B}\mu(s) = \int_{\R} e^{-sx} \, d\mu(x) = E\left[e^{-sX}\right],$$
for the complex $s$ at which the integral converges absolutely.
Since $\abs{e^{-sx}} = e^{-x \operatorname{Re} s}$, convergence depends only on $\operatorname{Re} s$, and it always holds on the line $\operatorname{Re} s = 0$, where the integrand has modulus $1$.
For real $t$, the [[moment-generating function|0WQVXP7PDB]] is $M_X(t) = \mathcal{B}\mu(-t)$.

Take $\mu$ the standard [[normal distribution|05AQE0QR0D]], with density $(2\pi)^{-1/2} e^{-x^2/2}$.
Completing the square gives $-sx - x^2/2 = -(x + s)^2/2 + s^2/2$.
So
$$\mathcal{B}\mu(s) = e^{s^2/2} \cdot \frac{1}{\sqrt{2\pi}} \int_{\R} e^{-(x+s)^2/2} \, dx = e^{s^2/2}$$
for every $s \in \C$, where the last integral equals $\sqrt{2\pi}$ by a shift of the line of integration.
Here the strip of convergence is the whole plane.

Take $\mu$ the [[exponential distribution|0E99F51GVB]] with rate $\lambda > 0$, with density $\lambda e^{-\lambda x}$ on $[0, \infty)$.
Then $\int_0^\infty e^{-sx} \lambda e^{-\lambda x} \, dx = \lambda / (\lambda + s)$ when $\operatorname{Re} s > -\lambda$, and the integral diverges when $\operatorname{Re} s \le -\lambda$.
Here the strip of convergence is the half-plane $\operatorname{Re} s > -\lambda$.

## Explanations

### L1 human

A probability law can be turned into a function of a complex variable by averaging the exponential $e^{-sX}$.
This is the moment-generating function read with the opposite sign and allowed to take complex arguments.
For the bell curve the answer is the very simple function $e^{s^2/2}$.
For the exponential law the answer $\lambda / (\lambda + s)$ only makes sense to the right of the line $\operatorname{Re} s = -\lambda$.
The reason is that the tail of this law decays only like $e^{-\lambda x}$.
