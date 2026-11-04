---
tag: FHHPA8GQE8
kind: proof
name: Proof of Bessel's inequality
msc: [46C05]
proves: 0RBT5PB74K
uses: [0VGSYBWHV2, 0KG4D8AP6G, 09VYHEF2VT, 0BVTDM872V, 0TS7VZJBWD]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel's_inequality
    locator: Proof
---

## Proof

We split $x$ into a combination of the $e_i$ and a part orthogonal to them, and apply the Pythagorean theorem.

1. Let $V$ be an inner product space over $\mathbb{K} = \R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$. Let $e_1, \dots, e_k$ be an [[orthonormal family|09VYHEF2VT]] and let $x \in V$.
2. For all $u, w \in V$ and $a \in \mathbb{K}$, conjugate symmetry and linearity in the first argument give $\ip{u}{a w} = \overline{a \ip{w}{u}} = \overline{a} \ip{u}{w}$. In the same way, $\ip{u}{\cdot}$ is additive.
3. Set $c_i = \ip{x}{e_i}$, $s = \sum_{i=1}^{k} c_i e_i$ and $r = x - s$. Then $x = s + r$.
4. For each $j$, linearity in the first argument and orthonormality give $\ip{s}{e_j} = \sum_i c_i \ip{e_i}{e_j} = c_j$.
5. So $\ip{r}{e_j} = \ip{x}{e_j} - \ip{s}{e_j} = c_j - c_j = 0$ for each $j$.
6. By step 2, $\ip{r}{s} = \sum_{j} \overline{c_j} \ip{r}{e_j} = 0$. So $r$ and $s$ are [[orthogonal|0TS7VZJBWD]].
7. By the [[Pythagorean theorem|0BVTDM872V]], $\norm{x}^2 = \norm{r + s}^2 = \norm{r}^2 + \norm{s}^2$.
8. By step 2 and linearity in the first argument, $\norm{s}^2 = \ip{s}{s} = \sum_{i} \sum_{j} c_i \overline{c_j} \ip{e_i}{e_j}$.
9. By orthonormality, only the terms with $i = j$ remain. So $\norm{s}^2 = \sum_{i} c_i \overline{c_i} = \sum_{i=1}^{k} \abs{c_i}^2$.
10. Since $\norm{r}^2 = \ip{r}{r} \ge 0$, steps 7 and 9 give $\sum_{i=1}^{k} \abs{\ip{x}{e_i}}^2 = \norm{s}^2 \le \norm{x}^2$.

## Idea

The vector $s = \sum_i \ip{x}{e_i} e_i$ is the part of $x$ along the directions $e_i$, and $x - s$ is orthogonal to all of them. By Pythagoras, $\norm{x}^2$ is $\norm{s}^2$ plus a nonnegative remainder. Orthonormality makes $\norm{s}^2$ the sum of the squared coefficients.
