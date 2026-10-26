---
tag: 01AAYNSBN6
kind: statement
role: proposition
name: Distance from a point to a line
msc: [51N20]
uses: [0NPPGHQNXQ, 0MP9BCF6DP, 0WQJJCCTC8]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    locator: Line defined by an equation
same_as:
  wikidata: Q2485106
  wikipedia: Distance from a point to a line
---

## Statement

Let $a$, $b$ and $c$ be real numbers with $(a, b) \neq (0, 0)$, and let $L = \{(x, y) \in \mathbb{R}^2 : a x + b y + c = 0\}$ be a [[line|0MP9BCF6DP]] in the plane.
Let $P = (x_0, y_0)$ be a point of $\mathbb{R}^2$. The distance from $P$ to $L$ is the smallest [[Euclidean distance|0NPPGHQNXQ]] $d(P, Q)$ for $Q \in L$. Then
$$\operatorname{dist}(P, L) = \frac{|a x_0 + b y_0 + c|}{\sqrt{a^2 + b^2}}.$$

## Remarks

The smallest distance is reached at exactly one point $Q$ of $L$, the foot of the perpendicular from $P$. It is $Q = P - \frac{a x_0 + b y_0 + c}{a^2 + b^2} (a, b)$.
In $\mathbb{R}^n$, let $L$ be the line through the point $A$ with the direction vector $v$. The distance from $P$ to $L$ is the length of the part of $P - A$ that is perpendicular to $v$: the length of $(P - A) - \frac{(P - A) \cdot v}{v \cdot v} v$.
In $\mathbb{R}^3$ this distance is also $\|(P - A) \times v\| / \|v\|$.

## Explanations

### L1 human

The shortest way from a point to a line is the path that meets the line at a right angle. The formula measures this path. For the line $y = 0$, thus $a = 0$, $b = 1$, $c = 0$, it gives $|y_0|$: the height of the point above or below the horizontal axis.
