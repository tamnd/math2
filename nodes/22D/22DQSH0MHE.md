---
tag: 22DQSH0MHE
kind: definition
name: Lie algebra cohomology
msc: [17B56, 17B55]
defines: 69NARSMQCM
uses: [5JJYBJ6A8K, TZAZ163QGK, WQ82C0M3QB]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra_cohomology
---

## Definition

Let $\mathfrak{g}$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $F$, and let $M$ be a $\mathfrak{g}$-[[module|TZAZ163QGK]].
For $n \ge 0$, let $C^n(\mathfrak{g}, M)$ be the space of alternating $n$-linear maps $\mathfrak{g}^n \to M$, with $C^0(\mathfrak{g}, M) = M$.
Define $d \colon C^n(\mathfrak{g}, M) \to C^{n+1}(\mathfrak{g}, M)$ by
$$
\begin{aligned}
(d\omega)(x_0, \dots, x_n) &= \sum_{i=0}^{n} (-1)^i x_i \cdot \omega(x_0, \dots, \widehat{x_i}, \dots, x_n) \\
&\quad + \sum_{0 \le i < j \le n} (-1)^{i+j} \omega([x_i, x_j], x_0, \dots, \widehat{x_i}, \dots, \widehat{x_j}, \dots, x_n),
\end{aligned}
$$
where a hat marks an omitted argument.
Then $d \circ d = 0$, so $(C^\bullet(\mathfrak{g}, M), d)$ is a cochain [[complex|WQ82C0M3QB]].
The *Lie algebra cohomology* of $\mathfrak{g}$ with coefficients in $M$ is
$$H^n(\mathfrak{g}, M) = \ker\big(d \colon C^n \to C^{n+1}\big) / \operatorname{im}\big(d \colon C^{n-1} \to C^n\big),$$
with $C^{-1} = 0$.

## Remarks

The complex is the [[Chevalley–Eilenberg complex|362T9VND0H]].
In low degrees, $H^0(\mathfrak{g}, M) = \set{m \in M : x \cdot m = 0 \text{ for all } x}$, the invariants.
$H^1(\mathfrak{g}, M)$ is the space of linear maps $D \colon \mathfrak{g} \to M$ with $D[x, y] = x \cdot D(y) - y \cdot D(x)$, modulo the maps $x \mapsto x \cdot m$.
Example: let $\mathfrak{g} = F x$ be one-dimensional; then $C^n = 0$ for $n \ge 2$ and $d m = (x \mapsto x \cdot m)$ on $C^0$.
So $H^0(\mathfrak{g}, M) = \ker(x)$ and $H^1(\mathfrak{g}, M) \cong M / xM$; for trivial $M = F$ both are $F$.
Non-example: dropping the bracket terms from $d$ gives a map that does not square to zero.
For $m \in M$, the result would be $(x_0, x_1) \mapsto x_0 x_1 m - x_1 x_0 m = [x_0, x_1] \cdot m$, which is nonzero for $\mathfrak{sl}_2(F)$ acting on $F^2$; the bracket term $-\omega([x_0, x_1])$ cancels it.
Equivalently, $H^n(\mathfrak{g}, M) \cong \operatorname{Ext}^n_{U(\mathfrak{g})}(F, M)$, where $U(\mathfrak{g})$ is the [[universal enveloping algebra|SCZ8PRVY00]].
