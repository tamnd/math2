---
tag: 068BZBXE0C
kind: statement
role: theorem
name: Existence of square roots of nonnegative reals
msc: [26A09]
uses: [0AXWET80YW]
sources:
  - url: https://en.wikipedia.org/wiki/Square_root
    locator: Properties and uses
---

## Statement

Let $x$ be a real number with $x \ge 0$.
Then there is exactly one real number $y$ with $y \ge 0$ and $y^2 = x$.

## Remarks

Existence uses the [[completeness axiom|0AXWET80YW]]: take $y = \sup \{t \ge 0 : t^2 \le x\}$ and show that $y^2 < x$ and $y^2 > x$ are both impossible.
Uniqueness: if $y, z \ge 0$ and $y^2 = z^2$, then $(y - z)(y + z) = 0$, thus $y = z$.
In $\mathbb{Q}$ the existence fails: $2$ has no rational square root, by the [[irrationality of the square root of 2|0DZGSDHD92]].

## Explanations

### L1 human

Every nonnegative real number is the area of exactly one square, and the side of that square is the square root.
This needs the real numbers: among the fractions, no square has area exactly $2$.
