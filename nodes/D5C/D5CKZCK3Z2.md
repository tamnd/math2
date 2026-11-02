---
tag: D5CKZCK3Z2
kind: definition
name: Uniform algebra
msc: [46J10, 46J05]
defines: ZP55RF3A0C
uses: [0TVJZYB6SH, 0S1FJ8VEX9, 0X3WGX95FE, 08VZ57PT26]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_algebra
---

## Definition

Let $X$ be a [[compact|0TVJZYB6SH]] [[Hausdorff space|0S1FJ8VEX9]], and let $C(X)$ be the algebra of [[continuous|0X3WGX95FE]] functions $X \to \C$ with the sup norm $\norm{f}_\infty = \max_{x \in X} \abs{f(x)}$.
A *uniform algebra* on $X$ is a subalgebra $A \subseteq C(X)$ such that:

1. $A$ is closed in $C(X)$ for the sup norm, that is, under [[uniform convergence|08VZ57PT26]];
2. $A$ contains the constant functions;
3. $A$ separates the points of $X$: for $x \ne y$ in $X$ there is $f \in A$ with $f(x) \ne f(y)$.

## Remarks

A uniform algebra is a commutative unital Banach algebra with $\norm{f^2} = \norm{f}^2$ for all $f$.
Conversely, a commutative unital complex Banach algebra with $\norm{a^2} = \norm{a}^2$ for all $a$ is isometrically isomorphic, through the Gelfand transform, to a uniform algebra on its character space.

Example: the disc algebra $A(\mathbb{D})$ on the closed unit disc $X = \overline{\mathbb{D}}$, the continuous functions on $X$ that are holomorphic in the open disc.
It is a subalgebra; it is closed because [[uniform limits of holomorphic functions are holomorphic|0431RN0R1N]]; it contains the constants; and $f(z) = z$ separates points.

Non-example: on $X = [0, 1]$, let $A = \set{f \in C([0,1]) : f(0) = f(1)}$.
It is a closed subalgebra containing the constants, but no $f \in A$ distinguishes $0$ from $1$, so clause 3 fails.

By the [[Stone–Weierstrass theorem|1P8D3MK79H]], a uniform algebra on $X$ that is closed under complex conjugation equals $C(X)$.
