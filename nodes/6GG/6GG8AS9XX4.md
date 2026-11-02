---
tag: 6GG8AS9XX4
kind: definition
name: Legendre integral transform
msc: [44A15, 42C10, 33C45]
defines: 51PH7Z03TJ
uses: [QFYGJVA996, SASP14MA1Z, RK2G9HN63E]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_transform_(integral_transform)
---

## Definition

Let $f \colon [-1, 1] \to \C$ be Lebesgue integrable, and let $P_n$ denote the [[Legendre polynomial|QFYGJVA996]] of degree $n$.
The *Legendre transform* of $f$ is the sequence $(\tilde f(n))_{n \ge 0}$ given by
$$\tilde f(n) = \int_{-1}^{1} P_n(x)\, f(x)\, dx, \qquad n = 0, 1, 2, \dots$$

## Remarks

The integrals converge because $\abs{P_n(x)} \le 1$ on $[-1, 1]$.
Let $f \in L^2([-1, 1])$, the [[$L^2$ space|SASP14MA1Z]].
Then the inverse transform is the [[Fourier–Legendre series|RK2G9HN63E]]
$$f(x) = \sum_{n=0}^{\infty} \frac{2n + 1}{2}\, \tilde f(n)\, P_n(x),$$
with convergence in $L^2([-1, 1])$; this follows from $\int_{-1}^{1} P_m P_n\, dx = \frac{2}{2n+1} \delta_{mn}$ and the completeness of the Legendre polynomials.
If $f$ is twice continuously differentiable on $[-1, 1]$, integration by parts gives $\int_{-1}^{1} P_n(x)\, \frac{d}{dx}\big[(1 - x^2) f'(x)\big]\, dx = -n(n+1)\, \tilde f(n)$, the rule that makes the transform useful for Legendre's equation.

Example: $f(x) = x^2$.
Since $x^2 = \frac{1}{3} P_0(x) + \frac{2}{3} P_2(x)$, orthogonality gives $\tilde f(0) = \frac{1}{3} \cdot 2 = \frac{2}{3}$, $\tilde f(2) = \frac{2}{3} \cdot \frac{2}{5} = \frac{4}{15}$, and $\tilde f(n) = 0$ otherwise.
Directly, $\tilde f(0) = \int_{-1}^{1} x^2\, dx = \frac{2}{3}$.

Non-example: $f(x) = \frac{1}{1 - x}$ is not integrable on $[-1, 1]$, and $\tilde f(0) = \int_{-1}^{1} \frac{dx}{1 - x}$ diverges.
