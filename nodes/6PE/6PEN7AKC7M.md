---
tag: 6PEN7AKC7M
kind: object
name: Kakeya set
msc: [28A75, 28A78]
instance_of: [0R6EWFKRCF]
sources:
  - url: https://en.wikipedia.org/wiki/Kakeya_set
same_as:
  wikidata: Q3054869
  wikipedia: Kakeya set
---

## Description

Let $n \ge 2$.
A *Kakeya set*, or *Besicovitch set*, is a [[compact set|0R6EWFKRCF]] $K \subseteq \R^n$ that contains a line segment of length $1$ in every direction.
That is, for each unit vector $e \in \R^n$ there is a point $a \in \R^n$ with $\set{a + t e : 0 \le t \le 1} \subseteq K$.
The closed ball of radius $1/2$ about the origin is a Kakeya set.
For a unit vector $e$, the segment from $-e/2$ to $e/2$ lies in the ball.
Besicovitch showed that there are Kakeya sets in $\R^2$ with [[Lebesgue measure|2Z2QVWZ262]] zero.
If $K \subseteq \R^2$ is such a set, then $K \times [0,1]^{n-2}$ is a Kakeya set in $\R^n$ of measure zero.
Indeed, let $e = (e_1, e_2, e')$ be a unit vector.
Take a segment of $K$ in the direction of $(e_1, e_2)$ with length $\abs{(e_1, e_2)}$.
The last $n - 2$ coordinates then move by $te'$ for $0 \le t \le 1$, starting from a suitable corner of the cube.

## Remarks

Although a Kakeya set may have measure zero, Davies proved in 1971 that every Kakeya set in $\R^2$ has [[Hausdorff dimension|SSNFTHZ6YJ]] $2$.
The Kakeya conjecture asks whether every Kakeya set in $\R^n$ has Hausdorff dimension $n$.
In 2025 Hong Wang and Joshua Zahl posted a proof for $n = 3$.
Some authors do not require a Kakeya set to be compact.

## Explanations

### L1 human

A Kakeya set is a set in which a needle of length one can be found pointing in every direction.
A disc of diameter one works, since a diameter can point in any direction.
The surprise is that such a set can be so thin that it has area zero.
Its needles overlap in a very clever way, so that very little room is used.
