---
tag: K4C77FGSW6
kind: definition
name: Schröder's equation
msc: [39B12, 30D05, 39B32]
defines: VTJV7JVJEA
uses: [0EPAT51DXQ, R6QVS6P21N, SRAN4EKWS0]
sources:
  - url: https://en.wikipedia.org/wiki/Schr%C3%B6der%27s_equation
---

## Definition

Let $X$ be a set, let $f \colon X \to X$ be a [[function|0EPAT51DXQ]], and let $\lambda \in \C$.
*Schröder's equation* for $f$ and $\lambda$ is the [[functional equation|SRAN4EKWS0]]
$$\Psi(f(x)) = \lambda \, \Psi(x) \quad \text{for all } x \in X,$$
in which the unknown is a function $\Psi \colon X \to \C$.
In the main case, $X$ is a neighbourhood of a [[fixed point|R6QVS6P21N]] $0$ of a holomorphic map $f$, and $\lambda = f'(0)$.
Then one asks for a holomorphic $\Psi$ with $\Psi(0) = 0$ and $\Psi'(0) = 1$.

## Remarks

Example: $f(x) = x^2 + 2x$ on $X = (-1, \infty)$, with $\lambda = 2$.
The fixed point is $0$, and $f'(0) = 2$.
The function $\Psi(x) = \log(1 + x)$ is a solution with $\Psi(0) = 0$ and $\Psi'(0) = 1$, since $\Psi(f(x)) = \log\big((1+x)^2\big) = 2 \log(1 + x)$.

Non-example: for the same $f$, the function $\Psi(x) = x$ is not a solution, since $f(x) = x^2 + 2x \ne 2x$ for $x \ne 0$.

If $\Psi$ is invertible, the equation says $f = \Psi^{-1} \circ (\lambda \Psi)$, so $f^n = \Psi^{-1} \circ (\lambda^n \Psi)$ for every $n \ge 0$.
The function $\Psi$ is called a Schröder function of $f$.
If $\Psi$ is a solution, so is $c \Psi$ for every constant $c$; the condition $\Psi'(0) = 1$ fixes this freedom.
