---
tag: ZGH48BG36Z
kind: definition
name: Faber polynomials
msc: ["30E10", "30C10", "41A10"]
defines: PVTA9RQKWM
uses: [00R0X1WGPX, 0CDMXGPSES, 0VHNKP1N3K, 02WHMEG5ZR, 0X3XD2ATB0, DBQXRTC0VN]
sources:
  - url: https://en.wikipedia.org/wiki/Faber_polynomials
---

## Definition

Let $K \subseteq \C$ be a [[compact set|00R0X1WGPX]] with more than one point such that $\widehat{\C} \setminus K$ is simply connected, where $\widehat{\C} = \C \cup \set{\infty}$ is the [[Riemann sphere|0CDMXGPSES]].
Let $\Phi$ be the [[conformal map|0VHNKP1N3K]] of $\widehat{\C} \setminus K$ onto $\set{w : \abs{w} > 1} \cup \set{\infty}$ with $\Phi(\infty) = \infty$ and
$$\Phi(z) = \frac{z}{c} + d_0 + \frac{d_1}{z} + \frac{d_2}{z^2} + \cdots \quad \text{near } \infty,$$
with $c > 0$.
For $n \ge 0$, the *$n$-th Faber polynomial* $F_n$ of $K$ is the polynomial part of the [[Laurent series|0X3XD2ATB0]] of $\Phi(z)^n$ at $\infty$.
That is, $F_n$ is the unique polynomial such that $\Phi(z)^n - F_n(z) \to 0$ as $z \to \infty$.

## Remarks

The map $\Phi$ exists and is unique by the [[Riemann mapping theorem|02WHMEG5ZR]], since $\widehat{\C} \setminus K$ is simply connected and has more than one boundary point.
The constant $c$ is the [[logarithmic capacity|DBQXRTC0VN]] of $K$.
The polynomial $F_n$ has degree $n$ and leading coefficient $c^{-n}$.
Example: for the disc $\abs{z - a} \le r$, $\Phi(z) = (z - a)/r$ and $F_n(z) = ((z - a)/r)^n$.
Example: for $K = [-1, 1]$, $\Phi(z) = z + \sqrt{z^2 - 1}$, and $\Phi^n + \Phi^{-n} = 2 T_n$ with $T_n$ the Chebyshev polynomial; since $\Phi^{-n} \to 0$ at $\infty$, $F_n = 2 T_n$ for $n \ge 1$.
Non-example: the union of two disjoint closed discs does not qualify, because its complement in $\widehat{\C}$ is not simply connected, so there is no map $\Phi$.
With $\Psi = \Phi^{-1}$, the Faber polynomials have the generating function $\Psi'(w)/(\Psi(w) - z) = \sum_{n \ge 0} F_n(z) w^{-n-1}$ for $\abs{w}$ large.
