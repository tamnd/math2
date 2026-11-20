---
tag: FHHPA8GQE8
kind: proof
name: Proof of Bessel's inequality
msc: ["46C05", "15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: 0RBT5PB74K
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [0VGSYBWHV2, 0KG4D8AP6G, 09VYHEF2VT, 0BVTDM872V, 0TS7VZJBWD, 0HR573CHNM]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel's_inequality
    locator: Proof
---

## Proof

Let $V$ be an inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.
Let $e_1, \dots, e_k$ be an [[orthonormal family|09VYHEF2VT]], and let $x \in V$.

1. For $u, w \in V$ and $a \in \mathbb{K}$, conjugate symmetry and linearity give $\ip{u}{a w} = \overline{a}\ip{u}{w}$. Also $\ip{u}{\cdot}$ is additive.
2. Set $c_i = \ip{x}{e_i}$, $s = \sum_{i=1}^{k} c_i e_i$ and $r = x - s$. Then $x = s + r$.
3. For each $j$, linearity in the first argument and orthonormality give $\ip{s}{e_j} = \sum_i c_i \ip{e_i}{e_j} = c_j$.
4. So $\ip{r}{e_j} = \ip{x}{e_j} - \ip{s}{e_j} = c_j - c_j = 0$ for each $j$.
5. By step 1, $\ip{r}{s} = \sum_{j} \overline{c_j}\ip{r}{e_j} = 0$. So $r$ and $s$ are [[orthogonal|0TS7VZJBWD]].
6. The [[Pythagorean theorem|0BVTDM872V]] gives $\norm{x}^2 = \norm{r + s}^2 = \norm{r}^2 + \norm{s}^2$.
7. By step 1 and linearity, $\norm{s}^2 = \ip{s}{s} = \sum_{i}\sum_{j} c_i \overline{c_j}\ip{e_i}{e_j}$.
8. By orthonormality, only the terms with $i = j$ remain. So $\norm{s}^2 = \sum_{i} c_i \overline{c_i} = \sum_{i=1}^{k} |c_i|^2$.
9. Part 2. Steps 6 and 8 give $\norm{x}^2 - \sum_i |c_i|^2 = \norm{r}^2 = \norm{x - s}^2$.
10. Part 1. Since $\norm{r}^2 = \ip{r}{r} \geq 0$, step 9 gives $\sum_{i=1}^{k} |\ip{x}{e_i}|^2 \leq \norm{x}^2$.
11. Part 3, first direction. Suppose equality holds. By step 9, $\norm{r} = 0$, so $r = 0$ by positive definiteness.
12. Then $x = s = \sum_i c_i e_i$, so $x$ lies in the [[span|0HR573CHNM]] of $e_1, \dots, e_k$.
13. Part 3, second direction. Suppose $x = \sum_j a_j e_j$. As in step 3, $\ip{x}{e_i} = a_i$ for each $i$, so $c_i = a_i$.
14. Hence $s = \sum_i a_i e_i = x$ and $r = 0$. Step 9 gives equality.

## Idea

The vector $s = \sum_i \ip{x}{e_i} e_i$ is the part of $x$ along the directions $e_i$, and $x - s$ is orthogonal to all of them.
By Pythagoras, $\norm{x}^2$ is $\norm{s}^2$ plus the nonnegative remainder $\norm{x - s}^2$.
Orthonormality makes $\norm{s}^2$ the sum of the squared coefficients, and the remainder vanishes exactly when $x = s$.

## Variants

- One can expand $0 \leq \norm{x - s}^2$ directly: it equals $\norm{x}^2 - 2\sum_i |c_i|^2 + \sum_i |c_i|^2$, which gives part 2 without Pythagoras.
- For $k = 1$ and $e_1 = y/\norm{y}$, the inequality is $|\ip{x}{y}|^2 \leq \norm{x}^2\norm{y}^2$. This is the [[proof of Cauchy-Schwarz by projection|6NB1CYDTNK]].
