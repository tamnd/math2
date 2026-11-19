---
tag: 01AAYNSBN6
kind: statement
role: proposition
name: Distance from a point to a line
msc: ["51N20"]
topics: [VKVAJ94SKZ]
audience: school
about: [~1297517b]
uses: [0NPPGHQNXQ, 0MP9BCF6DP, 0WQJJCCTC8]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    locator: Line defined by an equation
same_as:
  wikidata: Q2485106
  wikipedia: Distance from a point to a line
---

## Statement

Let $a$, $b$ and $c$ be real numbers with $(a, b) \neq (0, 0)$.
Let $L = \{(x, y) \in \mathbb{R}^2 : a x + b y + c = 0\}$ be a [[line|0MP9BCF6DP]] in the plane, and let $P = (x_0, y_0) \in \mathbb{R}^2$.
The distance from $P$ to $L$ is the least [[Euclidean distance|0NPPGHQNXQ]] $d(P, Q)$ for $Q \in L$.
This least value exists, and
$$\operatorname{dist}(P, L) = \frac{|a x_0 + b y_0 + c|}{\sqrt{a^2 + b^2}}.$$

## Remarks

### Why each hypothesis is needed

The condition $(a, b) \neq (0, 0)$ makes $L$ a line with the [[normal vector|0WQJJCCTC8]] $(a, b)$.
Without it, the denominator is $0$, and $L$ is empty or all of $\mathbb{R}^2$.

### Consequences

- The least distance is reached at exactly one point, the foot $Q = P - \dfrac{a x_0 + b y_0 + c}{a^2 + b^2} (a, b)$.
- The parallel lines $a x + b y + c_1 = 0$ and $a x + b y + c_2 = 0$ have the distance $\dfrac{|c_1 - c_2|}{\sqrt{a^2 + b^2}}$.

### Converse

The distance is $0$ if and only if $P \in L$.

### Generalizations

In $\mathbb{R}^n$, let $L$ be the line through $A$ with the direction $v$.
The distance from $P$ to $L$ is the length of $(P - A) - \dfrac{(P - A) \cdot v}{v \cdot v} v$.
In $\mathbb{R}^3$ it is also $\|(P - A) \times v\| / \|v\|$, by the [[distance theorem for lines in space|~c9d9dc6b]].
The [[distance to a plane|0K1E2S6Z69]] is the same formula one dimension higher.

## Explanations

### L1 human

The shortest way from a point to a line meets the line at a right angle.
The formula measures this shortest way.
For the line $y = 0$, with $a = 0$, $b = 1$, $c = 0$, it gives $|y_0|$, the height of the point above or below the horizontal axis.

### L2 human

Worked example: the point $(3, 4)$ and the line $3x - 4y + 2 = 0$.

1. The numerator is $|9 - 16 + 2| = 5$.
2. The denominator is $\sqrt{9 + 16} = 5$.
3. The distance is $1$.
4. The foot is $(3, 4) - \tfrac{-5}{25}(3, -4) = (3.6, 3.2)$, and $3 \cdot 3.6 - 4 \cdot 3.2 + 2 = 0$.

A trap: the formula needs the equation in the form $ax + by + c = 0$; for $y = mx + k$ write $mx - y + k = 0$ first.
