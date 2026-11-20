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

Let $U$ be a [[subspace|00YC1D652K]] of a vector space $V$.
The *codimension* of $U$ in $V$ is the [[dimension|03GSZ8RTZJ]] of the [[quotient space|0BR3FY5Q8M]], $\operatorname{codim}_V U = \dim(V / U)$.
In finite dimension, $\operatorname{codim}_V U = \dim V - \dim U$.
The codimension counts the independent linear conditions needed to cut out $U$, and it stays meaningful when $V$ and $U$ are infinite-dimensional.

## Motivation

A plane in $\R^3$ is given by one linear equation, and a line by two.
The number of equations is $3 - \dim U$, the number of directions missing from $U$.
In an infinite-dimensional space, such as $\R[x]$, the subspace $\{p : p(0) = 0\}$ is also given by one equation.
Its dimension is infinite, but the number of missing directions is $1$.
The codimension measures this number directly through the quotient, without subtracting infinite dimensions.

## Notation

We write $\operatorname{codim}_V U$, or $\operatorname{codim} U$ when $V$ is clear.
A subspace of codimension $1$ is called a *hyperplane*.
In Mathlib, one writes the codimension as `Module.finrank K (V ⧸ U)`.

## Remarks

### Examples

- A plane through $0$ in $\R^3$ has codimension $1$, and a line through $0$ has codimension $2$.
- [[Hyperplanes in R⁴|7Y08BD14Y6]]: the kernel of a nonzero linear form on $\R^4$ has codimension $1$, and two different hyperplanes meet in a subspace of codimension $2$.
- In $\R[x]$, the subspace $x^2 \R[x]$ has codimension $2$, by [[polynomials modulo x²|PHA4SATHWE]].
- In $\R[x]$, the subspace $\{p : p(1) = 0\}$ is a hyperplane.
- In the space of continuous functions on $[0, 1]$, the functions with integral $0$ form a hyperplane.

### Non-examples

- In $\R[x]$, the subspace of even polynomials has infinite codimension, since the cosets of $x, x^3, x^5, \dots$ are independent in the quotient.
- An affine plane such as $x + y + z = 1$ in $\R^3$ is not a subspace, so it has no codimension in this sense, although it is cut out by one equation.

### Basic properties

- $\operatorname{codim}_V U = 0$ if and only if $U = V$.
- Every complement $W$ of $U$ has $\dim W = \operatorname{codim}_V U$, since $W \cong V / U$.
- The hyperplanes of $V$ are exactly the kernels of the nonzero [[linear forms|07YQ1C78G0]] on $V$. More generally, $U$ has codimension $k$ exactly when it is the intersection of the kernels of $k$ independent linear forms.
- The [[codimension of an intersection|G7DHT62D9F]]: $\operatorname{codim}(U \cap W) \le \operatorname{codim} U + \operatorname{codim} W$, with equality if and only if $U + W = V$.
- If $U \subseteq X \subseteq V$, then $\operatorname{codim}_V U = \operatorname{codim}_V X + \operatorname{codim}_X U$.
- In finite dimension, $\operatorname{codim}_V U = \dim U^0$, the dimension of the [[annihilator|0ASHNYF7AG]] of $U$ in the dual space.

### History

The word codimension became common in the mid twentieth century, in algebraic geometry and in functional analysis.
In algebraic geometry, the codimension of a subvariety counts the equations needed to define it locally.
In functional analysis, subspaces of finite codimension and Fredholm operators made the notion essential in infinite dimension.

### Common errors

- Defining the codimension as $\dim V - \dim U$ in infinite dimension. This difference has no meaning when both dimensions are infinite.
- Thinking that codimension is intrinsic to $U$. It depends on the ambient space: a line has codimension $1$ in a plane and codimension $2$ in $\R^3$.
- Thinking that $k$ equations always cut out a subspace of codimension $k$. The equations must be independent, as for $x = 0$ and $2x = 0$, which give codimension $1$.

## Explanations

### L1 human

The codimension of a subspace is the number of directions it misses.
A plane in space misses one direction, so its codimension is $1$.
A line in space misses two directions, so its codimension is $2$.

### L2 human

Let $U = \{(x_1, x_2, x_3, x_4) : x_1 + x_2 = 0,\ x_3 = 2x_4\}$ in $\R^4$.

1. The two equations are independent, since their coefficient rows $(1, 1, 0, 0)$ and $(0, 0, 1, -2)$ are not proportional.
2. So $U$ has dimension $4 - 2 = 2$ and codimension $2$.
3. The map $v \mapsto (x_1 + x_2, x_3 - 2x_4)$ is surjective onto $\R^2$ with kernel $U$, so $\R^4 / U \cong \R^2$ directly.

The trap is to count the equations without checking that they are independent.

### L3 human

The codimension is the dimension of the cokernel of the inclusion $U \to V$.
It is additive along chains of subspaces, which makes it the right measure of size for subspaces of infinite-dimensional spaces.
The Fredholm index $\dim \ker T - \operatorname{codim} \operatorname{im} T$ of an operator is built from it.
In algebraic geometry, Krull's principal ideal theorem says that one equation cuts the dimension by at most one, an analogue of the codimension of a hyperplane.
