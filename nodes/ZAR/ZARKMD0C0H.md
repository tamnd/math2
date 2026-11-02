---
tag: ZARKMD0C0H
kind: definition
name: Allen–Cahn equation
msc: [35K58, 35K57]
defines: 7S813PEV69
uses: [TAAHWE917M, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Allen%E2%80%93Cahn_equation
---

## Definition

Let $\Omega \subseteq \R^n$ be open and let $\varepsilon > 0$.
Let $W(u) = \frac{1}{4}(1 - u^2)^2$, so that $W'(u) = u^3 - u$.
The *Allen–Cahn equation* is the [[reaction–diffusion equation|TAAHWE917M]] for $u \colon \Omega \times (0, T) \to \R$:
$$u_t = \Delta u - \frac{1}{\varepsilon^2} W'(u) = \Delta u - \frac{1}{\varepsilon^2}(u^3 - u),$$
where $\Delta$ is the [[Laplacian|0E0B6RA8K0]] in $x$.

## Remarks

Example: with $n = 1$, the function $u(x) = \tanh\!\big(x/(\sqrt{2}\,\varepsilon)\big)$ is a stationary solution.
Indeed, with $s = x/(\sqrt{2}\,\varepsilon)$ one finds $u'' = -\varepsilon^{-2}\operatorname{sech}^2(s)\tanh(s) = \varepsilon^{-2}(u^3 - u)$.
Non-example: the Cahn–Hilliard equation $u_t = \Delta(u^3 - u - \varepsilon^2 \Delta u)$ is of fourth order, so it is not of this form.
The equation is the $L^2$ gradient flow of the energy
$$E(u) = \int_\Omega \Big( \frac{1}{2}\abs{\nabla u}^2 + \frac{1}{\varepsilon^2} W(u) \Big)\, dx,$$
so $E$ does not increase along smooth solutions with Neumann boundary conditions.
Some authors scale the equation as $u_t = \varepsilon^2 \Delta u - W'(u)$ instead.
