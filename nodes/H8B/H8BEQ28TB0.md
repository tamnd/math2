---
tag: H8BEQ28TB0
kind: statement
role: theorem
name: The Hoffman–Singleton theorem
sources:
  - wikipedia: en:1399856@r1363981900
    locator: Strongly regular graph, section Algebraic properties of strongly regular graphs > The Hoffman–Singleton theorem
    note: adopted
    mention: wikipedia://en/1399856#S4HA
    sections: [Statement]
inventory: [GW0GFKCB7H]
---

## Statement

As noted above, the multiplicities of the eigenvalues are given by

$$M_{\pm} = \frac{1}{2}\left[(v - 1) \pm \frac{2k + (v - 1)(\lambda - \mu)}{\sqrt{(\lambda - \mu)^2 + 4(k - \mu)}}\right]$$

which must be integers.

In 1960, Alan Hoffman and Robert Singleton examined those expressions when applied on Moore graphs, which are strongly regular graphs that have *λ* = 0 and *μ* = 1. Such graphs are free of triangles (otherwise *λ* would exceed zero) and quadrilaterals (otherwise *μ* would exceed 1), hence they have a girth (smallest cycle length) of 5. Substituting the values of *λ* and *μ* in the equation $(v - k - 1)\mu = k(k - \lambda - 1)$, it can be seen that $v = k^2 + 1$, and the eigenvalue multiplicities reduce to

$$M_{\pm} = \frac{1}{2}\left[k^2 \pm \frac{2k - k^2}{\sqrt{4k - 3}}\right]$$

For the multiplicities to be integers, the quantity $\frac{2k - k^2}{\sqrt{4k - 3}}$ must be rational, therefore either the numerator $2k - k^2$ is zero or the denominator $\sqrt{4k - 3}$ is an integer.

If the numerator $2k - k^2$ is zero, the possibilities are:

- *k* = 0 and *v* = 1 yields a trivial graph with one vertex and no edges, and
- *k* = 2 and *v* = 5 yields the 5-vertex [[cycle graph|0QQ0F12962]] $C_5$, usually drawn as a regular pentagon.

If the denominator $\sqrt{4k - 3}$ is an integer *t*, then $4k - 3$ is a perfect square $t^2$, so $k = \frac{t^2 + 3}{4}$. Substituting:

$$\begin{aligned} M_{\pm} &= \frac{1}{2} \left[\left(\frac{t^2 + 3}{4}\right)^2 \pm \frac{\frac{t^2 + 3}{2} - \left(\frac{t^2 + 3}{4}\right)^2}{t}\right], \end{aligned}$$

so

$$\begin{aligned} 32 M_{\pm} &= (t^2 + 3)^2 \pm \frac{8(t^2 + 3) - (t^2 + 3)^2}{t} \\ &= t^4 + 6t^2 + 9 \pm \frac{- t^4 + 2t^2 + 15}{t} \\ &= t^4 + 6t^2 + 9 \pm \left(-t^3 + 2t + \frac{15}{t}\right). \end{aligned}$$

Since both sides are integers, $\frac{15}{t}$ must be an integer, therefore *t* is a factor of 15, namely $t \in \{\pm 1, \pm 3, \pm 5, \pm 15\}$, therefore $k \in \{1, 3, 7, 57\}$. In turn:

- *k* = 1 and *v* = 2 yields a trivial graph of two vertices joined by an edge,
- *k* = 3 and *v* = 10 yields the [[Petersen graph|0NR95CTFCZ]],
- *k* = 7 and *v* = 50 yields the Hoffman–Singleton graph, discovered by Hoffman and Singleton in the course of this analysis, and
- *k* = 57 and *v* = 3250 famously predicts a graph that has neither been discovered since 1960, nor has its existence been disproven.

The Hoffman-Singleton theorem states that there are no girth-5 Moore graphs except the ones listed above.
