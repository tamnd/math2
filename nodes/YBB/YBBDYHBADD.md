---
tag: YBBDYHBADD
kind: statement
role: theorem
name: Böttcher's equation
msc: [37F10, 39B32, 30D05]
uses: [0NAHXR1FRH, R6QVS6P21N, HNXXAPQKG3, 1G0B73WPX8]
about: [R6QVS6P21N]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%B6ttcher%27s_equation
---

## Statement

Let $U \subseteq \C$ be an open set containing $0$, and let $f \colon U \to \C$ be [[holomorphic|0NAHXR1FRH]].
Assume $f(z) = a_n z^n + a_{n+1} z^{n+1} + \cdots$ near $0$, with $n \ge 2$ and $a_n \ne 0$.
Then there is a holomorphic map $\varphi$ on a neighbourhood $V$ of $0$ with $\varphi(0) = 0$ and $\varphi'(0) \ne 0$ that solves *Böttcher's equation*
$$\varphi(f(z)) = \varphi(z)^n \quad \text{for all } z \in V \text{ with } f(z) \in V.$$
Such a $\varphi$ is unique up to multiplication by an $(n-1)$-st root of unity.

## Remarks

So near a superattracting [[fixed point|R6QVS6P21N]] of local degree $n$, the map $f$ is [[conjugate|HNXXAPQKG3]] to $w \mapsto w^n$.
The idea of the proof: after a linear change of variable one may take $a_n = 1$.
Then one sets $\varphi(z) = \lim_{k \to \infty} \big(f^k(z)\big)^{1/n^k}$, choosing the branches of the roots that are tangent to the identity.
The limit exists because $f^k(z)$ tends to $0$ very fast, and the correction factors form a convergent infinite product.
Example: $f(z) = z^2 / (1 - 2z + 2z^2)$ satisfies the equation with $n = 2$ and $\varphi(z) = z/(1 - z)$.
Indeed $\varphi(f(z)) = f(z)/(1 - f(z)) = z^2 / (1 - 2z + z^2) = \varphi(z)^2$.
For a monic [[polynomial|1G0B73WPX8]] $P$ of degree $d \ge 2$, the same result at the superattracting point $\infty$ gives a map $\varphi$ near $\infty$ with $\varphi(z) \sim z$ and $\varphi(P(z)) = \varphi(z)^d$.
This is the Böttcher coordinate used to define external rays.

## Explanations

### L1 human

The simplest map with a very strongly attracting fixed point is $w \mapsto w^n$, which squares or cubes distances to $0$ at each step.
The theorem says that every holomorphic map with such a fixed point looks exactly like $w \mapsto w^n$ near it, after a change of coordinates.

### L2 human

The equation was studied by Lucjan Böttcher in the early twentieth century.
It is the superattracting counterpart of Koenigs linearization, which handles multipliers $\lambda$ with $0 < \abs{\lambda} < 1$.
For polynomials the Böttcher coordinate at infinity is the main tool for describing the basin of infinity.
When the filled Julia set is connected, it extends to a conformal map from the basin of infinity onto the outside of the closed unit disc.
