---
tag: 2K13M9FBAN
kind: definition
name: Holomorphic function of several variables
msc: [32A10]
defines: 507C34W0ZT
uses: [BH57D2FBNR, 06EH97V2A7, 0NRYHJPQG2, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Definition

Let $D$ be an [[open set|02BH3MCBQB]] in $\C^n$ and let $f \colon D \to \C$.
The function $f$ is *complex differentiable* at $a \in D$ if there is a $\C$-[[linear map|0NRYHJPQG2]] $L \colon \C^n \to \C$ such that
$$\lim_{h \to 0} \frac{\abs{f(a + h) - f(a) - L(h)}}{\abs{h}} = 0.$$
The function $f$ is *holomorphic* on $D$ if it is complex differentiable at every point of $D$.

## Remarks

The map $L$ is the [[Fréchet derivative|06EH97V2A7]] of $f$ at $a$, and it has the form $L(h) = \sum_{j=1}^n \frac{\partial f}{\partial z_j}(a) \, h_j$.
Example: $f(z_1, z_2) = z_1 z_2$ is holomorphic on $\C^2$, since $f(a + h) - f(a) = a_2 h_1 + a_1 h_2 + h_1 h_2$ and $\abs{h_1 h_2} \le \abs{h}^2$.
Non-example: $g(z_1, z_2) = \bar z_1$ is real differentiable with derivative $h \mapsto \bar h_1$, but this map is not $\C$-linear, since it sends $i h$ to $-i \bar h_1$.
Equivalent forms: $f$ is holomorphic on $D$ if and only if $f$ is continuous and holomorphic in each variable separately.
It is also equivalent that $f$ is, near each point $a$, the sum of a convergent [[power series in several variables|R3QTCPTJK7]] centred at $a$.
By [[Hartogs's theorem on separate holomorphicity|ECJG25SAJR]], the continuity condition in the first equivalent form may even be dropped.
The set of holomorphic functions on $D$ is written $\mathcal{O}(D)$.
