---
tag: 0NAKHQ9XYY
kind: statement
role: theorem
name: Apollonius's theorem
msc: [51M04]
uses: [0XW8HX8VEV, 0S706JBZBG, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Apollonius%27s_theorem
    locator: Statement and relation to other theorem
same_as:
  wikidata: Q877489
  wikipedia: Apollonius's theorem
inventory: [F3CYM68Y0C]
---

## Statement

Let $A$, $B$ and $C$ be points of the Euclidean space $\mathbb{R}^n$, and let $D$ be the [[midpoint|0S706JBZBG]] of $B$ and $C$. Let $|XY|$ denote the [[distance|0NPPGHQNXQ]] between the points $X$ and $Y$.
Then
$$|AB|^2 + |AC|^2 = 2 \left( |AD|^2 + |BD|^2 \right).$$

## Remarks

For a triangle $ABC$ with the side lengths $a = |BC|$, $b = |CA|$, $c = |AB|$, the [[median|0XW8HX8VEV]] from $A$ thus has the length $m_a = \frac{1}{2} \sqrt{2 b^2 + 2 c^2 - a^2}$.
In vector form, with $u = B - A$ and $v = C - A$, the statement is the parallelogram law $\|u + v\|^2 + \|u - v\|^2 = 2\|u\|^2 + 2\|v\|^2$.
For an isosceles triangle with $|AB| = |AC|$, the median $AD$ is perpendicular to $BC$, and the theorem reduces to the [[Pythagorean theorem|0VP3A1290K]].

## History

The theorem is Proposition 122 of Book VII of the Collection of Pappus of Alexandria. It was possibly in the lost work Plane Loci of Apollonius of Perga.

## Explanations

### L1 human

The theorem relates the two sides from $A$ to the median from $A$. If you know the three sides of a triangle, it gives the length of each median. For the right triangle with legs $3$, $4$ and hypotenuse $5$, the median to the hypotenuse has length $\frac{1}{2}\sqrt{18 + 32 - 25} = \frac{5}{2}$.
