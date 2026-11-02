---
tag: 7KMD9JA3QZ
kind: definition
name: Bifurcation from a characteristic value
msc: [47J15, 45G10, 45C05]
defines: 4HQBRDQ3A9
uses: [06GZ956657, M2NEP1K5AE, DC7HMHVREP, D9TW46P19Y, 0FY42N02DV, P88X34MSVV]
sources:
  - url: https://en.wikipedia.org/wiki/Bifurcation_theory
---

## Definition

Let $X$ be a real [[Banach space|06GZ956657]], let $K \colon X \to X$ be a [[compact linear operator|M2NEP1K5AE]], and let $R \colon X \to X$ be a continuous map with $\norm{R(\varphi)} / \norm{\varphi} \to 0$ as $\varphi \to 0$.
Consider the equation
$$\varphi = \lambda\bigl(K \varphi + R(\varphi)\bigr), \quad \lambda \in \R,\ \varphi \in X,$$
which has the trivial solution $\varphi = 0$ for every $\lambda$.
A number $\lambda_0$ is a *bifurcation point* of the equation if every neighbourhood of $(\lambda_0, 0)$ in $\R \times X$ contains a solution $(\lambda, \varphi)$ with $\varphi \ne 0$.
One then says that nonzero solutions *bifurcate from* $\lambda_0$.

## Remarks

Every bifurcation point is a [[characteristic value|DC7HMHVREP]] of $K$: a number $\lambda_0$ with $\varphi = \lambda_0 K \varphi$ for some $\varphi \ne 0$.
Indeed, if $\lambda_0$ is not one, then $I - \lambda K$ is invertible with uniformly bounded inverse for $\lambda$ near $\lambda_0$, and $\norm{\varphi} \le C \abs{\lambda} \norm{R(\varphi)}$ forces $\varphi = 0$ for small $\varphi$.
Krasnosel'skii's theorem gives a converse: if $R$ is also compact, every characteristic value of $K$ of odd [[algebraic multiplicity|0FY42N02DV]] is a bifurcation point.

Example: $X = \R$, $K = 1$ and $R(\varphi) = -\varphi^3$.
The characteristic value is $\lambda_0 = 1$, and for $\lambda > 1$ the nonzero solutions are $\varphi = \pm\sqrt{1 - 1/\lambda}$, which tend to $0$ as $\lambda \to 1$; so $1$ is a bifurcation point, a [[pitchfork bifurcation|P88X34MSVV]].

Non-example: $X = \R^2$, $K = I$ and $R(x, y) = (-y^3, x^3)$.
The characteristic value $1$ has multiplicity $2$, which is even.
The equations are $(1 - \lambda) x + \lambda y^3 = 0$ and $(1 - \lambda) y - \lambda x^3 = 0$; multiplying the first by $y$, the second by $x$ and subtracting gives $\lambda(x^4 + y^4) = 0$.
So for $\lambda$ near $1$ the only solution is $x = y = 0$, and $1$ is not a bifurcation point.
