---
tag: Q6T1TTJJZG
kind: definition
name: Vanishing moments of a wavelet
msc: [42C40, 65T60]
defines: 7QERXM0C52
uses: [4PZ35C0GV3, 01XAHPADBA, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Daubechies_wavelet
---

## Definition

Let $\psi \colon \R \to \C$ be a [[wavelet|4PZ35C0GV3]] and let $p \ge 1$ be an integer.
Suppose that $x \mapsto x^k \psi(x)$ is [[Lebesgue integrable|DWJF7ABPR1]] on $\R$ for $k = 0, \dots, p - 1$.
The wavelet $\psi$ has *$p$ vanishing moments* if its [[moments|01XAHPADBA]] of order less than $p$ vanish:
$$\int_\R x^k \, \psi(x) \, dx = 0 \qquad \text{for } k = 0, 1, \dots, p - 1.$$

## Remarks

Equivalently, $\int_\R P(x) \psi(x) \, dx = 0$ for every polynomial $P$ of degree less than $p$.
In terms of the Fourier transform, under the same integrability, this says that $\hat\psi$ has a zero of order at least $p$ at $\xi = 0$.
The *number* of vanishing moments of $\psi$ is the largest such $p$.

Example: the [[Haar wavelet|JW5PA9XA7F]] $\psi = 1_{[0, 1/2)} - 1_{[1/2, 1)}$ has $\int \psi = \tfrac12 - \tfrac12 = 0$, so it has $1$ vanishing moment.

Non-example: the Haar wavelet does not have $2$ vanishing moments, since $\int_\R x \psi(x) \, dx = \tfrac18 - \tfrac38 = -\tfrac14 \ne 0$.
