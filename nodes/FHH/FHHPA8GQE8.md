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

We split $x$ into its part along the family and a remainder orthogonal to the family, and then we apply the Pythagorean theorem.
Let $V$ be an inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ linear in the first slot and [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.
Let $e_1, \dots, e_k$ be an [[orthonormal family|09VYHEF2VT]], and let $x \in V$.

1. For $u, w \in V$ and $a \in \mathbb{K}$, conjugate symmetry and linearity in the first slot give $\ip{u}{a w} = \overline{a}\ip{u}{w}$, and $\ip{u}{\cdot}$ is additive.
2. Set $c_i = \ip{x}{e_i}$, $s = \sum_{i=1}^{k} c_i e_i$ and $r = x - s$, so that $x = s + r$.
3. For each $j$, linearity in the first slot and $\ip{e_i}{e_j} = \delta_{ij}$ give $\ip{s}{e_j} = \sum_i c_i \ip{e_i}{e_j} = c_j$.
4. Hence $\ip{r}{e_j} = \ip{x}{e_j} - \ip{s}{e_j} = c_j - c_j = 0$ for each $j$.
5. By step 1, $\ip{r}{s} = \sum_{j} \overline{c_j}\ip{r}{e_j} = 0$, so $r$ and $s$ are [[orthogonal|0TS7VZJBWD]].
6. The [[Pythagorean theorem|0BVTDM872V]] gives $\norm{x}^2 = \norm{s + r}^2 = \norm{s}^2 + \norm{r}^2$.
7. By linearity in the first slot and step 1, $\norm{s}^2 = \ip{s}{s} = \sum_{i}\sum_{j} c_i \overline{c_j}\ip{e_i}{e_j}$.
8. Orthonormality leaves only the terms with $i = j$, so $\norm{s}^2 = \sum_{i} c_i \overline{c_i} = \sum_{i=1}^{k} \abs{c_i}^2$.
9. Part 2: steps 6 and 8 give $\norm{x}^2 - \sum_i \abs{c_i}^2 = \norm{r}^2 = \norm{x - s}^2$.
10. Part 1: the right side of step 9 is $\ip{r}{r} \geq 0$, so $\sum_{i=1}^{k} \abs{\ip{x}{e_i}}^2 \leq \norm{x}^2$.
11. Part 3, first direction: if equality holds, step 9 gives $\norm{r} = 0$, so $r = 0$ by positive definiteness.
12. Then $x = s = \sum_i c_i e_i$, so $x$ lies in the [[span|0HR573CHNM]] of $e_1, \dots, e_k$.
13. Part 3, second direction: suppose $x = \sum_j a_j e_j$; the computation of step 3 gives $c_i = \ip{x}{e_i} = a_i$ for each $i$.
14. Hence $s = \sum_i a_i e_i = x$ and $r = 0$, and step 9 gives equality.

This proves all three parts of [[Bessel's inequality|0RBT5PB74K]].

## Idea

The vector $s = \sum_i \ip{x}{e_i} e_i$ is the shadow of $x$ on the span of the family, and the remainder $x - s$ is orthogonal to every $e_i$.
Pythagoras then writes $\norm{x}^2$ as $\norm{s}^2$ plus the nonnegative number $\norm{x - s}^2$.
Orthonormality turns $\norm{s}^2$ into the plain sum of the squared coefficients, because every mixed term $\ip{e_i}{e_j}$ with $i \neq j$ vanishes.
The remainder is zero exactly when $x$ equals its shadow, and that is the equality case.

## Variants

One can skip the Pythagorean theorem and expand $0 \leq \norm{x - s}^2$ directly.
Both $\ip{x}{s}$ and $\ip{s}{x}$ equal $\sum_i \abs{c_i}^2$, so the expansion is $\norm{x}^2 - 2\sum_i \abs{c_i}^2 + \sum_i \abs{c_i}^2$, which gives part 2 at once.

For $k = 1$ and $e_1 = y / \norm{y}$ with $y \neq 0$, the inequality reads $\abs{\ip{x}{y}}^2 \leq \norm{x}^2 \norm{y}^2$.
So the argument above, for a single vector, is the [[proof of the Cauchy-Schwarz inequality by projection|6NB1CYDTNK]].
