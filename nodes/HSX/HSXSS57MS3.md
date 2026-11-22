---
tag: HSXSS57MS3
kind: example
name: The solution set of an inhomogeneous equation is not a kernel
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
not_instance_of:
  - target: 0S23E6YE83
    note: the solution set of x + y = 1 in R² does not contain (0, 0), so it is not a subspace and not a kernel
uses: [02YFME3RGW, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Linear_subspace
    locator: Definition
---

## Example

The solutions of $T(v) = w$ with $w \ne 0$ form a shifted copy of the kernel that misses the origin, so they are not a kernel themselves.
Let $T \colon \R^2 \to \R$ be $T(x, y) = x + y$, and let $S = \{(x, y) : T(x, y) = 1\}$.

1. Since $T(0, 0) = 0 \ne 1$, the zero vector is not in $S$, and a [[subspace|0EPTJA5QV4]] must contain $0$.
2. The vectors $(1, 0)$ and $(0, 1)$ are in $S$, but their sum $(1, 1)$ has $T(1, 1) = 2 \ne 1$, so $S$ is not closed under addition.
3. The vector $2\,(1, 0) = (2, 0)$ has $T(2, 0) = 2 \ne 1$, so $S$ is not closed under scalar multiples.
4. The [[kernel|02YFME3RGW]] of every linear map is a subspace, so $S$ is not the kernel of any linear map on $\R^2$.

## Remarks

The set $S$ is the line $x + y = 1$, which is parallel to the kernel $\ker T = \{(t, -t) : t \in \R\}$.
In fact $S = (1, 0) + \ker T$, because $T\bigl((1, 0) + (t, -t)\bigr) = 1 + 0 = 1$ for every $t$.
Every nonempty solution set of $T(v) = w$ is a translate of $\ker T$ in this way.
So $S$ is an affine subspace, and it is one coset of $\ker T$, an element of the [[quotient space|0BR3FY5Q8M]] $\R^2 / \ker T$.

If we change the right side from $1$ to $0$, the set becomes $\ker T$ itself, and all three tests pass.
If we change it to any other $c \ne 0$, the set is the parallel line $x + y = c$, which again fails all three tests.

## Explanations

### L1 human

The points with $x + y = 0$ form a line through the origin, and this line is the kernel of $T$.
The points with $x + y = 1$ form a parallel line that misses the origin.
A line that misses the origin is not a subspace, so it is not a kernel.

### L2 human

The solution set of a homogeneous system is a subspace, and the solution set of an inhomogeneous system is not.
The two are linked: one solution plus the kernel gives all solutions.
Here $(1, 0)$ is one solution, and adding the kernel vectors $(t, -t)$ gives every point of $S$.
Watch out: do not call the solution set of $Ax = b$ with $b \ne 0$ "the kernel".
