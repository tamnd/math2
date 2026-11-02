---
tag: 3SS5K8MHPK
kind: definition
name: Radial basis function
msc: [41A30, 41A63, 65D12]
defines: ZBSXSTQM2J
uses: [0XPR1E85W0, 0NPPGHQNXQ, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Radial_basis_function
---

## Definition

Let $d \ge 1$ and let $\norm{\cdot}$ be the Euclidean norm on [[Euclidean space|0XPR1E85W0]] $\R^d$.
A *radial basis function* is a [[function|0EPAT51DXQ]] $\Phi \colon \R^d \to \R$ of the form
$$\Phi(x) = \varphi(\norm{x}),$$
for some function $\varphi \colon [0, \infty) \to \R$.
For a centre $c \in \R^d$, the translate $x \mapsto \varphi(\norm{x - c})$ depends only on the [[Euclidean distance|0NPPGHQNXQ]] from $x$ to $c$.

## Remarks

Common choices of $\varphi$, with a shape parameter $\varepsilon > 0$:

1. Gaussian: $\varphi(r) = e^{-(\varepsilon r)^2}$;
2. multiquadric: $\varphi(r) = \sqrt{1 + (\varepsilon r)^2}$;
3. inverse multiquadric: $\varphi(r) = 1 / \sqrt{1 + (\varepsilon r)^2}$;
4. polyharmonic splines: $\varphi(r) = r^k$ for odd $k$ and $\varphi(r) = r^k \log r$ for even $k$, with $\varphi(0) = 0$.

Example: $\Phi(x) = e^{-\norm{x}^2}$ on $\R^2$ is radial: $\Phi(x_1, x_2) = e^{-(x_1^2 + x_2^2)}$ only depends on $\norm{x}$.
For instance $\Phi(1, 0) = \Phi(0, 1) = e^{-1}$.

Non-example: $\Psi(x_1, x_2) = e^{-(x_1^2 + 2 x_2^2)}$ is not radial: $\norm{(1, 0)} = \norm{(0, 1)} = 1$, but $\Psi(1, 0) = e^{-1} \ne e^{-2} = \Psi(0, 1)$.
