---
tag: 6GY4GAMY9Z
kind: definition
name: Riemann's differential equation
msc: ["33C05", "34M03"]
defines: RS8Z48E784
uses: [0NT64JV96A, H96HXG6CA0]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%27s_differential_equation
---

## Definition

Let $a, b, c \in \C$ be distinct, and let $\alpha, \alpha', \beta, \beta', \gamma, \gamma' \in \C$ satisfy
$$\alpha + \alpha' + \beta + \beta' + \gamma + \gamma' = 1.$$
*Riemann's differential equation* with these data is the [[ordinary differential equation|0NT64JV96A]]
$$\begin{aligned} w'' &+ \left[\frac{1 - \alpha - \alpha'}{z - a} + \frac{1 - \beta - \beta'}{z - b} + \frac{1 - \gamma - \gamma'}{z - c}\right] w' \\ &+ \left[\frac{\alpha\alpha'(a - b)(a - c)}{z - a} + \frac{\beta\beta'(b - c)(b - a)}{z - b} + \frac{\gamma\gamma'(c - a)(c - b)}{z - c}\right] \frac{w}{(z - a)(z - b)(z - c)} = 0. \end{aligned}$$

## Remarks

Its singular points are $a$, $b$, $c$, all [[regular singular points|H96HXG6CA0]], and $\infty$ is an ordinary point.
The exponents are $\alpha, \alpha'$ at $a$, $\beta, \beta'$ at $b$ and $\gamma, \gamma'$ at $c$.

Check at $z = a$: multiplying by $(z - a)^2$ and letting $z \to a$, the indicial equation is $r(r - 1) + (1 - \alpha - \alpha') r + \alpha\alpha' = (r - \alpha)(r - \alpha') = 0$, so the exponents at $a$ are $\alpha$ and $\alpha'$.

Example: take the singular points $0$, $\infty$, $1$, using the limiting form in which the factors with $b$ are dropped as $b \to \infty$.
With exponents $0, 1 - C$ at $0$, $A, B$ at $\infty$ and $0, C - A - B$ at $1$, the equation becomes the [[hypergeometric differential equation|W8VE25R5A7]] with parameters $A, B, C$.

Non-example: exponents with sum different from $1$ are not allowed, because the equation then acquires a fourth singular point at $\infty$.
The condition on the sum is Fuchs's relation for three singular points.

The solutions are written with the [[Riemann P-symbol|WWW053WXP2]].
