---
tag: QNMSHKBBSG
kind: definition
name: Fox H-function transforms
msc: [44A20, 33C60]
defines: S60PA0RXRY
uses: [YCK709QB06, EAZMKENA4N]
sources:
  - url: https://en.wikipedia.org/wiki/Fox_H-function
---

## Definition

Fix integers $0 \le m \le q$ and $0 \le n \le p$, complex numbers $a_1, \dots, a_p$, $b_1, \dots, b_q$, and positive reals $A_1, \dots, A_p$, $B_1, \dots, B_q$.
Let $H(z)$ be the [[Fox H-function|EAZMKENA4N]] $H^{m,n}_{p,q}$ with the parameter pairs $(a_j, A_j)$ and $(b_j, B_j)$.
Let $f \colon (0, \infty) \to \C$ be such that the integral below converges for $y$ in a set $Y \subseteq (0, \infty)$.
The *H-transform* of $f$ with these parameters is the function
$$g(y) = \int_0^\infty H(xy)\, f(x)\, dx, \qquad y \in Y.$$

## Remarks

The [[Mellin transform|N5PVGRJE1T]] of the kernel is
$$\mathcal{M} H(s) = \frac{\prod_{j=1}^{m} \Gamma(b_j + B_j s) \prod_{j=1}^{n} \Gamma(1 - a_j - A_j s)}{\prod_{j=m+1}^{q} \Gamma(1 - b_j - B_j s) \prod_{j=n+1}^{p} \Gamma(a_j + A_j s)},$$
and formally $\mathcal{M} g(s) = \mathcal{M} H(s)\, \mathcal{M} f(1 - s)$.

Example: with all $A_j = B_j = 1$, the kernel is a Meijer G-function and the H-transform is a [[Meijer G-function transform|C0BCHX106R]].
In particular $m = q = 1$, $n = p = 0$, $b_1 = 0$, $B_1 = 1$ gives the kernel $e^{-z}$, whose Mellin transform is $\Gamma(s)$, and the H-transform is the [[Laplace transform|0V49JEZW06]].

Example with a scale different from $1$: $m = q = 1$, $n = p = 0$, $b_1 = 0$, $B_1 = 1/2$ gives the kernel with Mellin transform $\Gamma(s/2)$, which is $2 e^{-z^2}$.
The check is $\int_0^\infty 2 e^{-z^2} z^{s-1}\, dz = \Gamma(s/2)$, by the substitution $u = z^2$.

Non-example: if some $A_j$ or $B_j$ is $0$ or negative, the parameters are outside the definition of the H-function.
