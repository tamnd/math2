---
tag: S9Z6PKTXAS
kind: definition
name: Residuated lattice
msc: ["06F05", "03G10"]
defines: E337A6WVH3
uses: [WH4SFAACAS, 0R47MAD57S, BND6A96S3D]
sources:
  - url: https://en.wikipedia.org/wiki/Residuated_lattice
---

## Definition

A *residuated lattice* is a structure $(L, \wedge, \vee, \cdot, e, \backslash, /)$ such that:

1. $(L, \wedge, \vee)$ is a [[lattice|WH4SFAACAS]], with order $\le$;
2. $(L, \cdot, e)$ is a [[monoid|0R47MAD57S]];
3. $\backslash$ and $/$ are binary operations on $L$ such that for all $x, y, z \in L$,
$$x \cdot y \le z \iff y \le x \backslash z \iff x \le z / y.$$

The operations $\backslash$ and $/$ are the *left residual* and the *right residual*.

## Remarks

Clause 3 says that $x \backslash z$ is the largest $y$ with $x \cdot y \le z$, and $z / y$ is the largest $x$ with $x \cdot y \le z$.
Example: a [[Heyting algebra|BND6A96S3D]] $H$ with $x \cdot y = x \wedge y$, $e = 1$ and $x \backslash z = z / x = x \to z$ is a residuated lattice.
Clause 3 is then the defining rule $x \wedge y \le z \iff y \le x \to z$ of the Heyting implication.
Example: the group $\Z$ with $\min$, $\max$, $x \cdot y = x + y$, $e = 0$ and $x \backslash z = z / x = z - x$ is a residuated lattice, since $x + y \le z \iff y \le z - x$.
Non-example: $\N$ with $\min$, $\max$, ordinary multiplication and $e = 1$ satisfies clauses 1 and 2, but has no left residual.
For $x = 0$ and $z = 0$, every $y \in \N$ satisfies $0 \cdot y \le 0$, and $\N$ has no largest element.
Many authors also require $L$ to be bounded, or the monoid to be commutative, in which case $x \backslash z = z / x$ is written $x \to z$.
Multiplication in a residuated lattice is monotone and distributes over all existing joins.
