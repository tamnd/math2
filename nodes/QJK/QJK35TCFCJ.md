---
tag: QJK35TCFCJ
kind: definition
name: Muckenhoupt weights
msc: [42B25, 42B35]
defines: T86RSJ8M86
uses: [X7GTF3D98F, 2Z2QVWZ262, VX1A56P5KQ, RARTMA0ZEC]
sources:
  - url: https://en.wikipedia.org/wiki/Muckenhoupt_weights
---

## Definition

Let $n \ge 1$.
A *weight* on $\R^n$ is a locally [[integrable|X7GTF3D98F]] function $w \colon \R^n \to [0, \infty)$ with $w > 0$ [[almost everywhere|RARTMA0ZEC]].
For a cube $Q \subseteq \R^n$ with sides parallel to the axes, let $\abs{Q}$ be its [[Lebesgue measure|2Z2QVWZ262]].

1. For $1 < p < \infty$, the weight $w$ is in the *Muckenhoupt class* $A_p$ if
$$[w]_{A_p} = \sup_Q \left( \frac{1}{\abs{Q}} \int_Q w \, dx \right) \left( \frac{1}{\abs{Q}} \int_Q w^{-1/(p - 1)} \, dx \right)^{p - 1} < \infty,$$
where the supremum is over all such cubes $Q$.
2. The weight $w$ is in $A_1$ if there is a constant $C$ with $Mw(x) \le C w(x)$ for almost every $x$, where $M$ is the [[Hardy–Littlewood maximal function|VX1A56P5KQ]].

A weight in some class $A_p$ is called a *Muckenhoupt weight*.

## Remarks

By Hölder's inequality $[w]_{A_p} \ge 1$, and $A_1 \subseteq A_p \subseteq A_q$ for $1 < p < q$.
The union $A_\infty = \bigcup_{p \ge 1} A_p$ has several equivalent descriptions, for example through a reverse Hölder inequality.
For $p = 2$ the condition reads $\sup_Q \left( \frac{1}{\abs{Q}}\int_Q w \right) \left( \frac{1}{\abs{Q}}\int_Q w^{-1} \right) < \infty$.

Example: $n = 1$, $p = 2$, $w(x) = \abs{x}^a$ with $-1 < a < 1$.
On $Q = [0, L]$ the two averages are $L^a/(1 + a)$ and $L^{-a}/(1 - a)$, whose product is $1/(1 - a^2)$ for every $L$.
Intervals symmetric about $0$ give the same averages.
On intervals far from $0$ compared with their length, $w$ is almost constant, so the product is close to $1$.
The remaining intervals lie in a symmetric interval of comparable length, and this case analysis shows $w \in A_2$.
More generally $\abs{x}^a \in A_p(\R^n)$ exactly when $-n < a < n(p - 1)$.

Non-example: $n = 1$, $p = 2$, $w(x) = \abs{x}$.
It is a weight, but on $Q = [0, 1]$ the average of $w^{-1} = 1/x$ is infinite, so $w \notin A_2$.
