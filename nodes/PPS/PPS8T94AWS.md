---
tag: PPS8T94AWS
kind: definition
name: Calderón–Zygmund kernel
msc: [42B20]
defines: 78N6AXP9VV
uses: [HTMCEARGDD]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral_operators_of_convolution_type
  - url: https://en.wikipedia.org/wiki/Singular_integral
---

## Definition

Let $n \ge 1$ and let $\Delta = \set{(x, x) : x \in \R^n}$ be the diagonal of $\R^n \times \R^n$.
A *Calderón–Zygmund kernel*, or standard kernel, is a function $K \colon (\R^n \times \R^n) \setminus \Delta \to \C$ for which there are constants $A > 0$ and $0 < \delta \le 1$ such that:

1. $\abs{K(x, y)} \le A \abs{x - y}^{-n}$ for all $x \ne y$;
2. $\abs{K(x, y) - K(x', y)} \le A \dfrac{\abs{x - x'}^\delta}{\abs{x - y}^{n + \delta}}$ whenever $\abs{x - x'} \le \frac{1}{2}\abs{x - y}$;
3. $\abs{K(x, y) - K(x, y')} \le A \dfrac{\abs{y - y'}^\delta}{\abs{x - y}^{n + \delta}}$ whenever $\abs{y - y'} \le \frac{1}{2}\abs{x - y}$.

## Remarks

Example: $n = 1$ and $K(x, y) = \frac{1}{\pi(x - y)}$, the kernel of the Hilbert transform.
Clause 1 holds with $A = 1/\pi$.
For clause 2, if $\abs{x - x'} \le \frac{1}{2}\abs{x - y}$ then $\abs{x' - y} \ge \frac{1}{2}\abs{x - y}$, and
$$\abs{K(x, y) - K(x', y)} = \frac{\abs{x - x'}}{\pi \abs{x - y}\abs{x' - y}} \le \frac{2}{\pi}\frac{\abs{x - x'}}{\abs{x - y}^2},$$
so clause 2 holds with $\delta = 1$; clause 3 is the same by symmetry.

Non-example: $K(x, y) = \abs{x - y}^{-n - 1/2}$ fails clause 1, because it is too large near the diagonal.

A convolution kernel $K(x, y) = k(x - y)$ is a Calderón–Zygmund kernel when $\abs{k(x)} \le A\abs{x}^{-n}$ and $\abs{\nabla k(x)} \le A\abs{x}^{-n-1}$ for $x \ne 0$, by the mean value theorem.
A weaker smoothness condition often used for convolution kernels is the Hörmander condition $\int_{\abs{x} > 2\abs{y}} \abs{k(x - y) - k(x)} \, dx \le A$ for all $y \ne 0$.
The size and smoothness conditions alone do not give an $L^2$ bound; one also needs cancellation, as for the [[singular integral operators|HTMCEARGDD]] with mean-zero angular part.
