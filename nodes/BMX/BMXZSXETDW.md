---
tag: BMXZSXETDW
kind: statement
role: theorem
name: Hankel inversion theorem
msc: [44A20, 33C10]
uses: [2P9YWDGKC4, CZCMRDWDYW]
about: [2P9YWDGKC4]
sources:
  - url: https://en.wikipedia.org/wiki/Hankel_transform
---

## Statement

Let $\nu \ge -\frac12$, and let $J_\nu$ be the [[Bessel function of the first kind|CZCMRDWDYW]] of order $\nu$.
Let $f \colon (0, \infty) \to \C$ satisfy $\int_0^\infty \abs{f(r)}\, r^{1/2}\, dr < \infty$, and let $F_\nu(k) = \int_0^\infty f(r) J_\nu(kr)\, r\, dr$ be its [[Hankel transform|2P9YWDGKC4]] of order $\nu$.
Let $r > 0$, and assume that $f$ is of bounded variation on a neighbourhood of $r$.
Then
$$\lim_{K \to \infty} \int_0^K F_\nu(k)\, J_\nu(kr)\, k\, dk = \frac{f(r^+) + f(r^-)}{2}.$$
In particular, the limit is $f(r)$ at every point $r$ where $f$ is continuous.

## Remarks

The proof follows the pattern of the Fourier inversion theorem for Fourier integrals.
After exchanging the integrals, the inner integral $\int_0^K J_\nu(kr) J_\nu(kt)\, k\, dk$ is computed in closed form from Bessel's equation, and it acts as an approximate identity concentrated at $t = r$ as $K \to \infty$.
A Riemann–Lebesgue argument disposes of the parts away from $r$, and the bounded variation near $r$ controls the part near $r$, exactly as in Dirichlet's theorem for Fourier series.
There is also an $L^2$ version: the Hankel transform of order $\nu$ extends to a unitary operator of $L^2((0, \infty), r\, dr)$ that is its own inverse.

Example: for $\nu = 0$ and $f(r) = e^{-r^2/2}$ one has $F_0(k) = e^{-k^2/2}$, and transforming again gives back $e^{-r^2/2}$.
For the indicator function of $[0, 1]$ and $\nu = 0$, $F_0(k) = J_1(k)/k$, and at $r = 1$ the inversion integral converges to the mean value $\frac12$ of the jump.

## Explanations

### L1 human

The Hankel transform breaks a radial function into circular waves.
This theorem says that adding the waves back together recovers the function.
At a jump, the reconstruction lands exactly halfway between the two values, as for Fourier series.

### L2 human

The theorem is the radial form of the Fourier inversion theorem, and for $\nu = \frac{n}{2} - 1$ it can be derived from it for radial functions on $\R^n$.
It justifies the solution of boundary value problems in cylindrical coordinates: transform in $r$, solve an ordinary differential equation in the remaining variable, and transform back.
The hypotheses parallel those of Dirichlet's pointwise convergence theorem for Fourier series.
