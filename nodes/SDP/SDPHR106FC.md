---
tag: SDPHR106FC
kind: definition
name: Chevalley–Eilenberg complex
msc: [17B56, 17B55]
defines: 362T9VND0H
uses: [5JJYBJ6A8K, TZAZ163QGK, 0MDMZ965VE, WQ82C0M3QB]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra_cohomology
---

## Definition

Let $\mathfrak{g}$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$, and let $M$ be a $\mathfrak{g}$-module, that is, a [[representation|TZAZ163QGK]] of $\mathfrak{g}$, with action $(x, m) \mapsto x \cdot m$.
For $n \ge 0$, let $C^n(\mathfrak{g}, M)$ be the vector space of alternating $k$-multilinear maps $\omega \colon \mathfrak{g}^n \to M$, equivalently $C^n(\mathfrak{g}, M) = \Hom_k(\Lambda^n \mathfrak{g}, M)$, where $\Lambda^n \mathfrak{g}$ is the $n$-th [[exterior power|0MDMZ965VE]].
The differential $d \colon C^n(\mathfrak{g}, M) \to C^{n+1}(\mathfrak{g}, M)$ is
$$
\begin{aligned}
(d\omega)(x_1, \ldots, x_{n+1}) ={}& \sum_{i=1}^{n+1} (-1)^{i+1}\, x_i \cdot \omega(x_1, \ldots, \widehat{x_i}, \ldots, x_{n+1}) \\
&+ \sum_{1 \le i < j \le n+1} (-1)^{i+j}\, \omega([x_i, x_j], x_1, \ldots, \widehat{x_i}, \ldots, \widehat{x_j}, \ldots, x_{n+1}),
\end{aligned}
$$
where a hat marks an omitted argument.
Then $d \circ d = 0$.
The *Chevalley–Eilenberg complex* of $\mathfrak{g}$ with coefficients in $M$ is the [[cochain complex|WQ82C0M3QB]] $(C^\bullet(\mathfrak{g}, M), d)$.

## Remarks

Example: in low degrees the formula reads $(dm)(x) = x \cdot m$ for $m \in C^0 = M$, and $(d\omega)(x, y) = x \cdot \omega(y) - y \cdot \omega(x) - \omega([x, y])$ for $\omega \in C^1$.
Check of $d \circ d = 0$ in degree $0$: $(d\,dm)(x, y) = x \cdot (y \cdot m) - y \cdot (x \cdot m) - [x, y] \cdot m = 0$, because $M$ is a module.

Non-example: dropping the second sum, the one with the bracket, does not give a complex.
Take $\mathfrak{g} = \mathfrak{sl}_2$ acting on $M = \mathfrak{g}$ by the adjoint action, with standard basis $e, f, h$ and $[e, f] = h$, $[h, e] = 2e$.
Then $d$ in degree $0$ followed by the shortened map in degree $1$ sends $m = e$ to the $2$-cochain $(x, y) \mapsto [x, [y, e]] - [y, [x, e]] = [[x, y], e]$, whose value at $(e, f)$ is $[h, e] = 2e \neq 0$.

The cohomology of this complex is the Lie algebra cohomology $H^n(\mathfrak{g}, M)$.
When $\mathfrak{g}$ is free as a module over a commutative ring, the same formulas define the complex over that ring.
