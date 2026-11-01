---
tag: 8NMH42GJRK
kind: definition
name: Riemann–Stieltjes integral
msc: [26A42]
defines: JT9AFHG0NA
uses: [069P20KYQT, 0HBY48G8G1, 0QM4TXT3DR]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Stieltjes_integral
---

## Definition

Let $a < b$ be real numbers and let $f, g \colon [a, b] \to \R$ be functions.
A tagged [[partition|069P20KYQT]] $(P, c)$ of $[a, b]$ consists of points $a = x_0 < x_1 < \cdots < x_n = b$ and tags $c_i \in [x_{i-1}, x_i]$.
Its mesh is $\max_i (x_i - x_{i-1})$, and its Riemann–Stieltjes sum is
$$S(P, c, f, g) = \sum_{i=1}^{n} f(c_i) \bigl(g(x_i) - g(x_{i-1})\bigr).$$
The function $f$ is *Riemann–Stieltjes integrable* with respect to $g$, with integral $A \in \R$, if the following holds.
For every $\varepsilon > 0$ there is $\delta > 0$ such that $\abs{S(P, c, f, g) - A} < \varepsilon$ for every tagged partition $(P, c)$ of mesh less than $\delta$.
One writes $A = \int_a^b f(x)\, dg(x)$.

## Remarks

Example: if $f$ is continuous and $g$ is continuously differentiable on $[a, b]$, then $\int_a^b f \, dg = \int_a^b f(x) g'(x)\, dx$.
By the mean value theorem, $g(x_i) - g(x_{i-1}) = g'(d_i)(x_i - x_{i-1})$ for some $d_i \in (x_{i-1}, x_i)$.
Uniform continuity of $g'$ lets one replace $d_i$ by $c_i$ with a small error, which leaves a [[Riemann sum|0HBY48G8G1]] of $f g'$.
With $g(x) = x$ the definition is that of the [[Riemann integral|0QM4TXT3DR]].

Non-example: on $[-1, 1]$ let $f = g$ be $0$ on $[-1, 0]$ and $1$ on $(0, 1]$.
If $0 = x_k$ is a partition point, the only nonzero term is $f(c_{k+1})$.
It is $0$ for the tag $c_{k+1} = 0$ and $1$ for any other tag.
So sums of every small mesh take both values $0$ and $1$, and $f$ is not integrable with respect to $g$.

If $f$ is continuous and $g$ has [[bounded variation|A8251BHCMP]], then $\int_a^b f \, dg$ exists.
Some authors use the limit over refinements of partitions instead of the mesh, which gives a slightly larger class of integrable pairs.
