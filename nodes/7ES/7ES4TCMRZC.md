---
tag: 7ES4TCMRZC
kind: definition
name: Oscillatory integral
msc: [42B20, 41A60]
defines: D5HZKE8E1A
uses: [0V33BNKZ9S, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Oscillatory_integral
---

## Definition

Let $n \ge 1$.
Let $\phi \colon \R^n \to \R$ be a [[smooth function|0V33BNKZ9S]], the *phase*.
Let $\psi \colon \R^n \to \C$ be a smooth function with compact support, the *amplitude*.
The *oscillatory integral* with phase $\phi$ and amplitude $\psi$ is the function of the real parameter $\lambda$ given by
$$I(\lambda) = \int_{\R^n} e^{i\lambda\phi(x)} \psi(x) \, dx.$$
A point $x$ with $\nabla\phi(x) = 0$ is a *critical point*, or stationary point, of the phase.

## Remarks

Example: $n = 1$, $\phi(x) = x$ and $\psi$ smooth with compact support.
Then $I(\lambda) = \int e^{i\lambda x}\psi(x) \, dx$ is the Fourier transform of $\psi$ at $-\lambda/(2\pi)$, and repeated integration by parts gives $\abs{I(\lambda)} \le C_N \abs{\lambda}^{-N}$ for every $N$.
More generally, if $\nabla\phi \ne 0$ on the support of $\psi$, then $I(\lambda)$ decays faster than any power of $\lambda$.

Non-example: $\phi(x) = x$ and $\psi \equiv 1$ on $\R$.
The amplitude does not have compact support, and $\int_\R e^{i\lambda x} \, dx$ does not converge as a [[Lebesgue integral|DWJF7ABPR1]].
Such integrals are still given a meaning as distributions, which is the setting of the more general oscillatory integrals of Hörmander.

If $x_0$ is the only critical point in the support of $\psi$ and the Hessian of $\phi$ at $x_0$ is invertible, the method of stationary phase gives $I(\lambda) = O(\lambda^{-n/2})$ as $\lambda \to \infty$.
