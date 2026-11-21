---
tag: 01AAYNSBN6
kind: statement
role: proposition
name: Distance from a point to a line
msc: ["51N20"]
topics: [VKVAJ94SKZ]
audience: school
about: [C6GAS92QHX]
uses: [0NPPGHQNXQ, 0MP9BCF6DP, 0WQJJCCTC8]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    locator: Line defined by an equation
same_as:
  wikidata: Q2485106
  wikipedia: Distance from a point to a line
---

## Statement

In the plane, the distance from a point to a line is what you get by putting the point into the equation of the line and dividing by the length of the normal.
Let $a$, $b$ and $c$ be real numbers with $(a, b) \neq (0, 0)$.
Let $L = \{(x, y) \in \mathbb{R}^2 : a x + b y + c = 0\}$ be a [[line|0MP9BCF6DP]] in the plane, and let $P = (x_0, y_0) \in \mathbb{R}^2$.
The distance from $P$ to $L$ is the least [[Euclidean distance|0NPPGHQNXQ]] $d(P, Q)$ for $Q \in L$.
This least value exists, and
$$\operatorname{dist}(P, L) = \frac{|a x_0 + b y_0 + c|}{\sqrt{a^2 + b^2}}.$$

## Remarks

### Why each hypothesis is needed

The condition $(a, b) \neq (0, 0)$ makes $L$ a line, with [[normal vector|0WQJJCCTC8]] $(a, b)$.
Without it the denominator is $0$, and the set $L$ is empty when $c \neq 0$ and all of $\mathbb{R}^2$ when $c = 0$, so there is no line to measure to.

### What it gives you

The least distance is reached at exactly one point, the foot of the perpendicular,
$$Q = P - \frac{a x_0 + b y_0 + c}{a^2 + b^2} \, (a, b).$$
For example, the point $(3, 4)$ and the line $3x - 4y + 2 = 0$ give the numerator $|9 - 16 + 2| = 5$ and the denominator $\sqrt{9 + 16} = 5$, so the distance is $1$.
The foot is $(3, 4) + \tfrac{1}{5}(3, -4) = (3.6, 3.2)$, and indeed $3 \cdot 3.6 - 4 \cdot 3.2 + 2 = 0$.

Two parallel lines $a x + b y + c_1 = 0$ and $a x + b y + c_2 = 0$ are at the distance $|c_1 - c_2| / \sqrt{a^2 + b^2}$.
Without the absolute value, the sign of $a x_0 + b y_0 + c$ tells on which side of $L$ the point lies.

### The converse

The distance is $0$ exactly when $P \in L$, since the numerator vanishes exactly then.

### Beyond the plane

In $\mathbb{R}^n$, let $L$ be the line through $A$ with direction $v$.
The distance from $P$ to $L$ is the length of the part of $P - A$ perpendicular to $v$,
$$\Bigl\| (P - A) - \frac{(P - A) \cdot v}{v \cdot v} \, v \Bigr\|.$$
In $\mathbb{R}^3$ this is also $\|(P - A) \times v\| / \|v\|$, by the [[distance theorem for lines in space|Q6YGYNSY5H]].
The [[distance to a plane|0K1E2S6Z69]] is the same formula one dimension higher.

## Explanations

### L1 human

The shortest way from a point to a line meets the line at a right angle.
The formula measures this shortest way.
For the line $y = 0$, with $a = 0$, $b = 1$ and $c = 0$, it gives $|y_0|$, the height of the point above or below the horizontal axis.

### L2 human

To use the formula, first bring the line into the form $ax + by + c = 0$.
Then substitute the point into the left side, take the absolute value, and divide by the length of $(a, b)$.
For the line $y = 2x + 1$, written as $2x - y + 1 = 0$, and the point $(0, 0)$, this gives $\tfrac{1}{\sqrt{5}}$.
Watch out: the form $y = mx + k$ must be rewritten as $mx - y + k = 0$ first, or the denominator comes out wrong.
