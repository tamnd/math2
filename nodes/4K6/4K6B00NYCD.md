---
tag: 4K6B00NYCD
kind: definition
name: Beltrami equation
msc: [30C62]
defines: 9J7GFJ1GPF
uses: [WMXDVF36ZT, 02BH3MCBQB, 0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Beltrami_equation
---

## Definition

Let $U$ be an [[open set|02BH3MCBQB]] in $\C$.
Let $\mu \colon U \to \C$ be a measurable function with $\norm{\mu}_\infty \le k$ for some constant $k < 1$.
The *Beltrami equation* with *Beltrami coefficient* $\mu$ is
$$f_{\bar z} = \mu f_z,$$
where $f_z$ and $f_{\bar z}$ are the [[Wirtinger derivatives|WMXDVF36ZT]] of $f$.
A *solution* is a function $f \in W^{1,2}_{\mathrm{loc}}(U)$, that is, with locally square-integrable weak first partial derivatives, that satisfies the equation almost everywhere on $U$.

## Remarks

Example: for $\mu = 0$ the equation is $f_{\bar z} = 0$, which is the Cauchy–Riemann system, and its solutions are the [[holomorphic functions|0NAHXR1FRH]] on $U$.
Example: for a constant $c$ with $\abs{c} < 1$, the function $f(z) = z + c \bar z$ has $f_z = 1$ and $f_{\bar z} = c$, so it solves the equation with $\mu = c$.
Non-example: the coefficient $\mu = 1$ fails the condition $\norm{\mu}_\infty < 1$.
Then the equation reads $f_{\bar z} - f_z = i f_y = 0$, and every function of $x$ alone solves it, so the equation is degenerate and its solutions are never homeomorphisms.
A homeomorphic solution is a [[quasiconformal mapping|SB8KG46NHP]] whose complex dilatation is $\mu$.
