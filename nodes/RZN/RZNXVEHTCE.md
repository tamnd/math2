---
tag: RZNXVEHTCE
kind: example
name: Kernel, image, rank and nullity of a 3 × 3 matrix map
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
instance_of: [0S23E6YE83, 0WSFKKT6FF, 0ZZXSBTR4J, 0APCFW7639]
uses: [02YFME3RGW, 0JB228DCWB, 0JGB7A6GTS, 00K4FK4NBH, 0PDVQEP0ZC]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Illustration
  - book: isbn:9780321982384
    locator: Section 4.2
---

## Example

One row reduction of a $3 \times 3$ matrix gives the kernel, the image, the rank and the nullity of its map at once.
Let $T \colon \R^3 \to \R^3$ be $T(x) = Ax$ with
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 1 & 3 & 4 \end{pmatrix},$$
and let $c_1 = (1, 0, 1)$, $c_2 = (2, 1, 3)$ and $c_3 = (3, 1, 4)$ be the columns of $A$.

1. The third row of $A$ is the sum of the first two, so $Ax = 0$ is equivalent to the two equations $x_1 + 2x_2 + 3x_3 = 0$ and $x_2 + x_3 = 0$.
2. The second equation gives $x_2 = -x_3$, and the first then gives $x_1 = -2x_2 - 3x_3 = 2x_3 - 3x_3 = -x_3$.
3. So the [[kernel|02YFME3RGW]] is the line $\ker T = \{t\,(-1, -1, 1) : t \in \R\}$, and the [[nullity|00K4FK4NBH]] of $T$ is $1$.
4. The [[image|0JB228DCWB]] is spanned by the columns, and $c_3 = c_1 + c_2$, so it is spanned by $c_1$ and $c_2$ alone.
5. The vectors $c_1$ and $c_2$ are not multiples of each other, so they are independent, the image is a plane, and the [[rank|0JGB7A6GTS]] of $T$ is $2$.
6. Each column $(a, b, c)$ satisfies $c = a + b$, since $1 = 1 + 0$, $3 = 2 + 1$ and $4 = 3 + 1$, so $\operatorname{im} T = \{(a, b, c) : c = a + b\}$.

Check the kernel vector:
$$A \begin{pmatrix} -1 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 - 2 + 3 \\ -1 + 1 \\ -1 - 3 + 4 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}.$$
The rank and the nullity add up to $2 + 1 = 3 = \dim \R^3$, as the [[rank-nullity theorem|0W4FSW1TVB]] says.

## Remarks

The equation of the image is a test for solvability.
For example, $(1, 1, 1)$ is not in the image, since $1 \ne 1 + 1$, so the system $Ax = (1, 1, 1)$ has no solution.
On the other hand, $(1, 1, 2)$ satisfies $2 = 1 + 1$, and indeed $A(-1, 1, 0)^{\mathsf T} = (1, 1, 2)$.

The relation $c_3 = c_1 + c_2$ can be rewritten as $1 \cdot c_1 + 1 \cdot c_2 - 1 \cdot c_3 = 0$, and so $(1, 1, -1)$ is a kernel vector, which is $-1$ times the vector of step 3.
In general each relation among the columns gives a kernel vector, and each kernel vector gives a relation among the columns.

The map is neither injective nor surjective, and in finite dimension these two fail together for a map from a space to itself, by the [[theorem on endomorphisms|0912EEEVCT]].
If we change the entry $4$ to $5$, the third row is no longer the sum of the first two, the only solution of $Ax = 0$ is $0$, and the map becomes bijective.

## Explanations

### L1 human

The matrix squeezes all of space onto a plane, so one direction is lost.
The lost direction is the kernel, the line through $(-1, -1, 1)$.
The plane is the image, and the points off it cannot be reached.

### L2 human

The computation uses one row reduction for two answers.
The kernel comes from the solutions of $Ax = 0$, and the image comes from the independent columns.
The equation $c = a + b$ of the image tells which systems $Ax = b$ can be solved.
Watch out: a basis of the image consists of the pivot columns of $A$ itself, not of the reduced matrix, because row operations change the column space.
