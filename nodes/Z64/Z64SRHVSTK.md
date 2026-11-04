---
tag: Z64SRHVSTK
kind: proof
name: Proof of Liouville's theorem by Cauchy's estimates
msc: [30D20]
proves: 0EHKVRF4J6
uses: [0419794R0T, 0DG0Z72CQD, 0D1C9Y1EXA, 0JJRENWMP6, 0BYZTFM0DJ]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%27s_theorem_(complex_analysis)
    locator: Proof
---

## Proof

1. Let $f : \C \to \C$ be an [[entire function|0419794R0T]], and let $M$ be a real number with $\abs{f(z)} \le M$ for each $z \in \C$.
2. Fix $c \in \C$ and a real number $r > 0$. The closed disc $\set{z : \abs{z - c} \le r}$ lies in $\C$, where $f$ is [[holomorphic|0DG0Z72CQD]].
3. On the circle $\abs{z - c} = r$ we have $\abs{f(z)} \le M$. So [[Cauchy's estimates|0JJRENWMP6]] with $n = 1$ give $\abs{f'(c)} \le M / r$.
4. Step 3 holds for every $r > 0$. Letting $r \to \infty$ gives $\abs{f'(c)} \le 0$, so $f'(c) = 0$.
5. Since $c$ was arbitrary, $f'(c) = 0$ for each $c \in \C$.
6. View $f$ as a map $\R^2 \to \R^2$ by $x + iy \leftrightarrow (x, y)$. Fix $c \in \C$.
7. By the definition of [[complex differentiability|0D1C9Y1EXA]] with $f'(c) = 0$, we have $\abs{f(c + h) - f(c)} / \abs{h} \to 0$ as $h \to 0$.
8. Step 7 says that $f$ is differentiable at $c$ as a map of two real variables, with total derivative $Df(c) = 0$.
9. The set $\C = \R^2$ is open and connected. By step 8 and the theorem that a [[zero derivative on a connected open set implies constant|0BYZTFM0DJ]], $f$ is constant.

## Idea

Cauchy's estimates bound $f'(c)$ by the bound of $f$ on a circle divided by the radius. For an entire function the radius can be as large as we like, while the bound $M$ stays the same. So the derivative is zero everywhere, and $f$ is constant.
