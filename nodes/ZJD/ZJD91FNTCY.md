---
tag: ZJD91FNTCY
kind: definition
name: Weighted polynomial approximation
msc: [41A81, 41A10]
defines: 6XQYHACGT0
uses: [0X3WGX95FE, 1G0B73WPX8, YDN0T4MEX0]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Definition

Let $w \colon \R \to [0, \infty)$ be a continuous function, called the *weight*, such that $x^k w(x) \to 0$ as $\abs{x} \to \infty$ for every integer $k \ge 0$.
Let $C_w$ be the space of [[continuous functions|0X3WGX95FE]] $f \colon \R \to \R$ with $f(x) w(x) \to 0$ as $\abs{x} \to \infty$, with the seminorm $\norm{f}_w = \sup_{x \in \R} \abs{f(x)} w(x)$.
Let $\mathcal{P}_n$ be the set of real [[polynomial functions|1G0B73WPX8]] of degree at most $n$.
*Weighted polynomial approximation* is the approximation of $f \in C_w$ by elements of $\mathcal{P}_n$, measured by the weighted error
$$E_n(f)_w = \inf\set{\norm{f - p}_w : p \in \mathcal{P}_n} .$$

## Remarks

The decay condition on $w$ ensures that every polynomial lies in $C_w$, so $E_n(f)_w$ is finite.
$E_n(f)_w$ is the [[error of best approximation|YDN0T4MEX0]] of $f$ from $\mathcal{P}_n$ in the seminorm $\norm{\cdot}_w$.
Polynomials are dense in $C_w$ exactly when $E_n(f)_w \to 0$ for every $f \in C_w$; Bernstein's approximation problem asks for which weights this holds.
The same name is used for the weighted $L^p$ error $\inf_p \left( \int_\R \abs{f - p}^p w \, dx \right)^{1/p}$, and for weights on an interval.
Example: $w(x) = e^{-x^2}$ satisfies the decay condition, since $x^k e^{-x^2} \to 0$ for each $k$.
The function $f(x) = \abs{x}$ is continuous with $\abs{x} e^{-x^2} \to 0$, so $f \in C_w$, and $E_n(f)_w \le \norm{f}_w = \sup_x \abs{x} e^{-x^2} = e^{-1/2}/\sqrt{2}$ for every $n$, using $p = 0$.
In the weighted $L^2$ version with the same weight, the best constant approximation of $x^2$ is $c = \int x^2 e^{-x^2} dx \big/ \int e^{-x^2} dx = 1/2$.
Non-example: $w \equiv 1$ fails the decay condition, and then $\norm{p}_w = \infty$ for every nonconstant polynomial $p$.
