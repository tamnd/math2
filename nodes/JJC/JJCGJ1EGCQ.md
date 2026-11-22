---
tag: JJCGJ1EGCQ
kind: concept
name: Codimension of a subspace
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug2
uses: [00YC1D652K, 0BR3FY5Q8M, 03GSZ8RTZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Codimension
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Properties
---

## Summary

The codimension of a subspace counts the directions that the subspace misses, or, in other words, the independent linear equations that you need to cut it out.
A plane through the origin in $\R^3$ misses one direction, and a line misses two.
Let $U$ be a [[subspace|00YC1D652K]] of a vector space $V$ over a field $F$.
The *codimension* of $U$ in $V$ is the [[dimension|03GSZ8RTZJ]] of the [[quotient space|0BR3FY5Q8M]]:
$$\operatorname{codim}_V U = \dim (V / U).$$
When $V$ is finite-dimensional, the [[dimension of a quotient space|0SXDQ6TN00]] gives the equivalent form $\operatorname{codim}_V U = \dim V - \dim U$.
The quotient form also works when $V$ and $U$ are both infinite-dimensional, where the difference has no meaning.

## Motivation

A plane through $0$ in $\R^3$ is the solution set of one linear equation, such as $x + y + z = 0$.
A line through $0$ needs two equations, such as $x = y$ and $y = z$.
In both cases the number of equations is $3 - \dim U$, the number of directions that $U$ leaves out.
Many questions are about this number rather than about $\dim U$: how many conditions a solution must meet, or how much freedom is lost.

In an infinite-dimensional space the subtraction breaks down.
In the polynomial space $\R[x]$, the subspace $\{p : p(0) = 0\}$ is cut out by one equation, yet both it and $\R[x]$ have infinite dimension.
The quotient sees the right number: the map $p \mapsto p(0)$ is linear and onto $\R$, with kernel this subspace, so the quotient is a line and the codimension is $1$.
Codimension returns in duality, where a subspace of codimension $k$ is the common kernel of $k$ independent [[linear forms|07YQ1C78G0]], and in analysis, where the index of a [[Fredholm operator|Q5B5YGY7D6]] is built from it.

## Notation

We write $\operatorname{codim}_V U$, or $\operatorname{codim} U$ when the ambient space $V$ is clear.
A subspace of codimension $1$ is a *hyperplane*.
In Mathlib the codimension of a finite-codimensional subspace is written as `Module.finrank K (V ⧸ U)`, the finite rank of the quotient.
Watch the subscript: the codimension depends on $V$ as well as on $U$.

## Remarks

### Three computations

First take the plane $U = \{(x, y, z) : x + y + z = 0\}$ in $\R^3$.
The map $\varphi(x, y, z) = x + y + z$ is linear and onto $\R$, since $\varphi(t, 0, 0) = t$, and its kernel is $U$.
By the [[first isomorphism theorem|0MTBGVZ4XJ]], $\R^3 / U \cong \R$, so $\operatorname{codim} U = 1$.
Check: $\dim \R^3 - \dim U = 3 - 2 = 1$.

Next take the multiples of $x^2$ in $\R[x]$, the subspace $x^2 \R[x]$.
Each polynomial $a_0 + a_1 x + a_2 x^2 + \dots$ differs from $a_0 + a_1 x$ by a multiple of $x^2$, so the cosets of $1$ and $x$ span the quotient.
They are independent, because $a + bx$ is a multiple of $x^2$ only when $a = b = 0$.
So the codimension is $2$, as [[polynomials modulo x²|PHA4SATHWE]] works out in detail.

Last, take the kernels $U$ and $W$ of the forms $x_1 + x_2 + x_3 + x_4$ and $x_1 - x_2$ on $\R^4$.
Each is a hyperplane, and [[two hyperplanes in R⁴|7Y08BD14Y6]] shows that $U \cap W$ has codimension $2$.

### Hyperplanes and equations

A subspace $H$ is a hyperplane exactly when $H = \ker \varphi$ for a nonzero linear form $\varphi \colon V \to F$.
If $\varphi \ne 0$, then $\varphi$ is onto $F$, so $V / \ker \varphi \cong F$ is a line.
Conversely, if $V / H$ is a line, then an isomorphism $V / H \cong F$ composed with the [[quotient map|0J0SK5FF4M]] is a nonzero form with kernel $H$.
In the same way, $U$ has finite codimension $k$ exactly when $U$ is the common kernel of $k$ independent linear forms.
For example, the functions $f$ in $C[0, 1]$ with $\int_0^1 f = 0$ form a hyperplane, since integration is a nonzero linear form.

### The rules you can use

Codimension $0$ means $U = V$, because $V / U = 0$ exactly when every coset is $U$.
Every [[complement|0M83V17KHX]] $W$ of $U$ has $\dim W = \operatorname{codim}_V U$, because $W \cong V / U$.
Codimension adds along a chain $U \subseteq X \subseteq V$:
$$\operatorname{codim}_V U = \operatorname{codim}_V X + \operatorname{codim}_X U.$$
The reason is the [[third isomorphism theorem|07RB3EMBWW]], which gives $(V / U) / (X / U) \cong V / X$.
For two subspaces, the [[codimension of an intersection|G7DHT62D9F]] is at most the sum, $\operatorname{codim}(U \cap W) \le \operatorname{codim} U + \operatorname{codim} W$, with equality exactly when $U + W = V$ (when both codimensions are finite).
In finite dimension, $\operatorname{codim}_V U$ also equals the dimension of the [[annihilator|0ASHNYF7AG]] $U^0$ in the dual space.

### What it is not

The even polynomials in $\R[x]$ form a subspace of infinite codimension, not of finite codimension.
The cosets of $x, x^3, x^5, \dots$ are independent in the quotient, because a finite combination of odd powers is even only when it is zero.
An affine plane such as $x + y + z = 1$ is cut out by one equation, but it does not contain $0$.
It is not a subspace, so it has no codimension in the sense of linear algebra.

### Watch out

Three mistakes come up often.
The first is to define the codimension as $\dim V - \dim U$ in infinite dimension: in $\R[x]$ both the even polynomials and $\{p : p(0) = 0\}$ give $\infty - \infty$, yet their codimensions are $\infty$ and $1$.
The second is to treat codimension as a property of $U$ alone: a line has codimension $1$ in a plane and codimension $2$ in $\R^3$.
The third is to count equations without checking independence: $x = 0$ and $2x = 0$ in $\R^3$ cut out a plane, of codimension $1$, not $2$.

### History

Counting the conditions that define a geometric object is much older than the word codimension.
The definition through the quotient space is the one that extends to infinite dimension, and it is the form that functional analysis uses for the Fredholm index.

### Try it

First, find the codimension of $U = \{(x_1, x_2, x_3, x_4, x_5) : x_1 = x_2 = x_3\}$ in $\R^5$.
The answer is $2$, because the two equations $x_1 - x_2 = 0$ and $x_2 - x_3 = 0$ are independent and $\dim U = 3$.

Second, find the codimension of $\{p \in \R[x] : p(0) = p(1) = p(2) = 0\}$.
The answer is $3$: the map $p \mapsto (p(0), p(1), p(2))$ is onto $\R^3$ by interpolation with polynomials of degree at most $2$, and its kernel is the subspace.

## Explanations

### L1 human

Think of the codimension as the number of directions a flat piece of space leaves out.
Space has three directions.
A flat sheet through the origin uses two of them and misses one, so its codimension is $1$.
A line through the origin uses one direction and misses two, so its codimension is $2$.
Each missing direction matches one equation that you must write down to describe the piece.

### L2 human

Here is a typical problem: find the codimension of $U = \{x \in \R^4 : x_1 + x_2 = 0,\ x_3 = 2 x_4\}$.
The two equations have coefficient rows $(1, 1, 0, 0)$ and $(0, 0, 1, -2)$, and these rows are not proportional, so the equations are independent.
To see the quotient directly, use the map
$$\psi(x) = (x_1 + x_2,\ x_3 - 2 x_4).$$
It is onto $\R^2$, since $\psi(a, 0, b, 0) = (a, b)$, and its kernel is $U$.
So $\R^4 / U \cong \R^2$ by the first isomorphism theorem, and $\operatorname{codim} U = 2$.
Check: a basis of $U$ is $(1, -1, 0, 0), (0, 0, 2, 1)$, so $\dim U = 2 = 4 - 2$.
The method works the same way in infinite dimension: find a map onto $F^k$ whose kernel is $U$.

### L3 human

The codimension of $U$ is the dimension of the cokernel of the inclusion $U \to V$, so it is the dual notion to the dimension of a kernel.
For a linear map $T$ with finite-dimensional kernel and image of finite codimension, the Fredholm index $\dim \ker T - \operatorname{codim} \operatorname{im} T$ is the basic invariant of [[Fredholm theory|242TFD41KZ]].
In algebraic geometry, the codimension of a subvariety plays the same role, and Krull's principal ideal theorem says that one equation lowers the dimension by at most one.
In the [[exact sequence|946YAZNYKX]] $0 \to U \to V \to V / U \to 0$, the codimension is the dimension of the third term.
