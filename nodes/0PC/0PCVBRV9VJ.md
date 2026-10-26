---
tag: 0PCVBRV9VJ
kind: statement
role: theorem
name: Fermat's theorem on stationary points
aliases: [interior-extremum-theorem]
msc: [26A24]
uses: [00999TYPXB, 0NS8BP96QX, 0F1WR9C83K]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_extremum_theorem
    locator: Statement
same_as:
  wikidata: Q727102
  wikipedia: Interior extremum theorem
---

## Statement

Let $I$ be an open interval, let $f \colon I \to \mathbb{R}$, and let $a \in I$.
Assume that $f$ has a [[local maximum|00999TYPXB]] or a [[local minimum|0NS8BP96QX]] at $a$, and that $f$ is differentiable at $a$.
Then $f'(a) = 0$.

## Remarks

At a local maximum, the difference quotient $(f(a + h) - f(a))/h$ is $\le 0$ for small $h > 0$ and $\ge 0$ for small $h < 0$. So the limit is both $\le 0$ and $\ge 0$.
The point must be interior. On $[0, 1]$, the function $x$ has a maximum at $1$, where its derivative is $1$.
Mathlib states it as `IsLocalExtr.deriv_eq_zero`.

## Explanations

### L1 human

At the top of a smooth hill, the tangent line is horizontal.
If the slope were positive or negative, moving a little would give a higher value.
