---
tag: PNTCSE6DWA
kind: definition
name: Fredholm equation of the second kind
msc: [45B05, 45A05]
defines: DEYYNVCV9J
uses: [GSMBXT7FPK, 526TCVMSHP]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_integral_equation
---

## Definition

Let $a < b$ be real numbers.
Let $K \colon [a, b] \times [a, b] \to \C$ be a [[kernel|GSMBXT7FPK]], for example continuous or square-integrable.
Let $f \colon [a, b] \to \C$ be a given function, and let $\lambda \in \C$ be a parameter.
Let $\varphi$ denote an unknown function on $[a, b]$.
The *Fredholm equation of the second kind* with kernel $K$, parameter $\lambda$ and right-hand side $f$ is
$$\varphi(x) - \lambda \int_a^b K(x, y) \, \varphi(y) \, dy = f(x), \qquad x \in [a, b].$$
It is *homogeneous* when $f = 0$.

## Remarks

Example: on $[0, 1]$, take $K(x, y) = xy$, $\lambda = 1$ and $f(x) = x$.
Then $\varphi(x) = 3x/2$ is a solution, since $\int_0^1 x y \cdot \tfrac{3y}{2} \, dy = \tfrac{3x}{2} \cdot \tfrac{1}{3} = \tfrac{x}{2}$ and $\tfrac{3x}{2} - \tfrac{x}{2} = x$.

Non-example: $\int_a^b K(x, y) \varphi(y) \, dy = f(x)$ is not of the second kind, because $\varphi$ does not appear outside the integral; it is a [[Fredholm equation of the first kind|2RMWAVR1HV]].

Some books write the equation as $\varphi - \lambda T_K \varphi = f$, where $(T_K \varphi)(x) = \int_a^b K(x, y) \varphi(y) \, dy$.
Others put $\lambda$ on the other side, as $\lambda \varphi - T_K \varphi = f$; for $\lambda \ne 0$ the two forms are equivalent after dividing by $\lambda$.
