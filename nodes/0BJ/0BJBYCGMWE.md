---
tag: 0BJBYCGMWE
kind: statement
role: theorem
name: Injectivity and the kernel
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
about: [0S23E6YE83, 0NRYHJPQG2]
uses: [02YFME3RGW, 0RJF668P1T, 0PVG1CRAJN, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Properties
  - book: isbn:9780134860244
    locator: Section 2.1
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Statement

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].

1. $T$ is [[injective|0PVG1CRAJN]] if and only if its [[kernel|02YFME3RGW]] is $\ker T = \{0\}$.
2. If $T$ is injective and $v_1, \dots, v_k \in V$ are [[linearly independent|0EVHJFTG9Z]], then $T(v_1), \dots, T(v_k)$ are linearly independent.
3. Conversely, if $T$ sends some basis of $V$ to a linearly independent family, then $T$ is injective.

## Remarks

### Why each hypothesis is needed

- Part 1 needs linearity. The map $x \mapsto x^2$ on $\R$ has $\{x : x^2 = 0\} = \{0\}$, but it is not injective, since $1$ and $-1$ have the same image.
- Part 2 needs injectivity. The projection $(x, y) \mapsto (x, 0)$ sends the independent vectors $(1, 0)$ and $(1, 1)$ to the dependent vectors $(1, 0)$ and $(1, 0)$.
- Part 3 needs a basis, or at least a spanning set. The projection above sends the single vector $(1, 0)$ to an independent family, but it is not injective.

### Consequences

- The map $x \mapsto Ax$ is injective if and only if $Ax = 0$ has only the solution $x = 0$, that is, the columns of $A$ are independent.
- If $T \colon V \to W$ is injective and $V$ is finite-dimensional, then $\dim V \le \dim W$, by part 2 applied to a basis.
- So there is no injective linear map $\R^3 \to \R^2$.
- An injective linear map sends a basis of $V$ to a basis of $\im T$.

### Converse

Part 3 is the converse of part 2 for a basis.
Part 1 is an equivalence, so it is its own converse.

### Generalizations

- A homomorphism of groups, rings or modules is injective if and only if its kernel is trivial, with the same proof.
- For maps of sets, there is no kernel, and injectivity must be checked on all pairs of points.

## History

For linear systems, part 1 says this: if $Ax = 0$ has only the trivial solution, then $Ax = b$ has at most one solution for each $b$.
This form is older than the abstract notion of a linear map, which Peano defined in 1888.

## Explanations

### L1 human

To test if a linear map is one to one, it is enough to look at the vectors sent to zero.
If two vectors have the same image, then their difference is sent to zero.
So if only $0$ goes to $0$, no two vectors share an image.
A one-to-one linear map keeps independent vectors independent.

### L2 human

Let $T(x, y) = (x + y,\ x - y,\ 2x)$ from $\R^2$ to $\R^3$.

1. $T(x, y) = 0$ gives $x + y = 0$ and $x - y = 0$, so $x = y = 0$.
2. So $\ker T = \{0\}$, and $T$ is injective by part 1.
3. $T(e_1) = (1, 1, 2)$ and $T(e_2) = (1, -1, 0)$ are independent, as part 2 predicts.

The test of part 1 replaces "check all pairs $u, v$" by "solve one homogeneous system".
The trap is to use the test for a non-linear map, where it fails.
