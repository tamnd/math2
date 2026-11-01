---
tag: TSX2MAA95V
kind: definition
name: Elimination theory
msc: [13P15, 13P10]
defines: 9PA8CVSWPD
uses: [04C5ZBG1WT, 0SDC934R52, 096Z9MP2ME, 0B68KNPGCG, C83KPT47R0, 0PF6TM8TWT]
sources:
  - url: https://en.wikipedia.org/wiki/Elimination_theory
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]], let $S = k[x_1, \ldots, x_n]$ be the [[polynomial ring|0SDC934R52]], and let $I$ be an [[ideal|096Z9MP2ME]] of $S$.
For $0 \le l < n$, the *$l$-th elimination ideal* of $I$ is
$$I_l = I \cap k[x_{l+1}, \ldots, x_n].$$
Elimination theory is the study of the elimination ideals of ideals and of their zero sets.

## Remarks

$I_l$ is an ideal of $k[x_{l+1}, \ldots, x_n]$; it consists of the consequences of the equations of $I$ in which $x_1, \ldots, x_l$ do not occur.
Elimination theorem: if $G$ is a [[Gröbner basis|C83KPT47R0]] of $I$ for the [[lexicographic order|0B68KNPGCG]] with $x_1 > \cdots > x_n$, then $G \cap k[x_{l+1}, \ldots, x_n]$ is a Gröbner basis of $I_l$.
Closure theorem: let $k$ be [[algebraically closed|0PF6TM8TWT]], and project the zero set of $I$ to the last $n - l$ coordinates.
Then the zero set of $I_l$ in $k^{n-l}$ is the Zariski closure of this projection.

Example: in $k[t, x, y]$ with the lexicographic order $t > x > y$, let $I = (x - t, \; y - t^2)$.
Since $y - t^2 = (y - x^2) - (t - x)(t + x)$, one gets $I = (t - x, \; x^2 - y)$.
These two generators have coprime leading terms $t$ and $x^2$, so they form a Gröbner basis, and the first elimination ideal is $I_1 = (x^2 - y)$: eliminating $t$ gives the parabola $y = x^2$.

Non-example: $x - t$ lies in $I$ but not in $I_1$, because it involves the eliminated variable $t$.
