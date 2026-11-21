---
tag: S9Z6PKTXAS
kind: definition
name: Residuated lattice
msc: ["06F05", "03G10"]
defines: E337A6WVH3
topics: [QYA4H5Y7VR]
audience: research
uses: [WH4SFAACAS, 0R47MAD57S, BND6A96S3D]
sources:
  - url: https://en.wikipedia.org/wiki/Residuated_lattice
    locator: Definition; Examples
  - book: isbn:9780444521415
---

## Definition

A *residuated lattice* is a structure $(L, \wedge, \vee, \cdot, e, \backslash, /)$ such that:

1. $(L, \wedge, \vee)$ is a [[lattice|WH4SFAACAS]], with order $\le$;
2. $(L, \cdot, e)$ is a [[monoid|0R47MAD57S]];
3. $\backslash$ and $/$ are binary operations on $L$ such that for all $x, y, z \in L$,
$$x \cdot y \le z \iff y \le x \backslash z \iff x \le z / y.$$

The operations $\backslash$ and $/$ are the two *residuals* of the multiplication.

## Notation

Texts differ on which residual is "left" and which "right".
When $\cdot$ is commutative, $x \backslash z = z / x$, and one writes $x \to z$.
The unit $e$ is also written $1$ or $1'$.

## Remarks

Clause 3 says that $x \backslash z$ is the largest $y$ with $x \cdot y \le z$, and $z / y$ is the largest $x$ with $x \cdot y \le z$.
Example: a [[Heyting algebra|BND6A96S3D]] $H$ with $x \cdot y = x \wedge y$, $e = 1$ and $x \backslash z = z / x = x \to z$ is a residuated lattice.
Clause 3 is then the defining rule $x \wedge y \le z \iff y \le x \to z$ of the Heyting implication.
Example: the group $\Z$ with $\min$, $\max$, $x \cdot y = x + y$, $e = 0$ and $x \backslash z = z / x = z - x$ is a residuated lattice, since $x + y \le z \iff y \le z - x$.
Non-example: $\N$ with $\min$, $\max$, ordinary multiplication and $e = 1$ satisfies clauses 1 and 2, but has no left residual.
For $x = 0$ and $z = 0$, every $y \in \N$ satisfies $0 \cdot y \le 0$, and $\N$ has no largest element.
Many authors also require $L$ to be bounded, or the monoid to be commutative, in which case $x \backslash z = z / x$ is written $x \to z$.
Multiplication in a residuated lattice is monotone and distributes over all existing joins.

## Explanations

### L1 human

A residuated lattice has an order, a way to combine two elements, and two ways to divide.
Dividing $z$ by $x$ gives the largest element that, combined with $x$, stays below $z$.

### L2 human

1. In $(\Z, \min, \max, +, 0)$, take $x = 3$ and $z = 5$.
2. The largest $y$ with $3 + y \le 5$ is $2 = 5 - 3$, so $x \backslash z = 2$.
3. In a Heyting algebra, the largest $y$ with $x \land y \le z$ is $x \to z$.

The typical use: the residuals model implications in [[substructural logics|E337A6WVH3]].
The trap: when $\cdot$ is not commutative, $x \backslash z$ and $z / x$ can differ.
