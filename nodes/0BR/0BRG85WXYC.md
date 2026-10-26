---
tag: 0BRG85WXYC
kind: statement
role: theorem
name: Goursat's theorem
aliases: [goursat-lemma]
msc: ["30E20"]
uses: [0DG0Z72CQD, 00FWNP9TXY]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem
    locator: Discussion
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations
    locator: Goursat's theorem and its generalizations
---

## Statement

Let $U \subseteq \mathbb{C}$ be an open set and let $f : U \to \mathbb{C}$ be [[holomorphic|0DG0Z72CQD]] on $U$.
Let $Q = \{x + iy : a_1 \le x \le b_1, \ a_2 \le y \le b_2\}$ be a closed rectangle with $Q \subseteq U$, where $a_1 < b_1$ and $a_2 < b_2$ are real numbers.
Let $\partial Q$ be the boundary of $Q$, traveled once counterclockwise. Then the [[contour integral|00FWNP9TXY]] of $f$ along $\partial Q$ is
$$\oint_{\partial Q} f(z) \, dz = 0.$$

## Remarks

The theorem does not assume that $f'$ is continuous. This is the difference with the older proof by Green's theorem.
The same statement holds for each closed triangle $T \subseteq U$ and its boundary.
Proof idea: divide $Q$ into four equal rectangles and keep one where the integral is largest. Repeat, and use the complex derivative at the limit point.
Goursat's theorem is the first step to [[primitives on a disc|02AC7JR6G6]] and to [[Cauchy's integral theorem|01MPZXYVYF]].

## Explanations

### L1 human

If $f$ is holomorphic on a rectangle and its inside, then the integral of $f$ around the edge of the rectangle is zero.
The surprise is that this needs only the existence of the complex derivative, and nothing about its continuity.
