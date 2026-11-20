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

Let $T \colon \R^3 \to \R^3$ be $T(x) = Ax$ with
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 1 & 3 & 4 \end{pmatrix}.$$
Let $c_1 = (1, 0, 1)$, $c_2 = (2, 1, 3)$ and $c_3 = (3, 1, 4)$ be the columns of $A$.

1. The third row of $A$ is the sum of the first two rows. So $Ax = 0$ is equivalent to the two equations $x_1 + 2x_2 + 3x_3 = 0$ and $x_2 + x_3 = 0$.
2. The second equation gives $x_2 = -x_3$. The first then gives $x_1 = -2x_2 - 3x_3 = 2x_3 - 3x_3 = -x_3$.
3. So the [[kernel|02YFME3RGW]] is $\ker T = \{t\,(-1, -1, 1) : t \in \R\}$, a line through the origin.
4. Check: $A(-1, -1, 1) = (-1 - 2 + 3,\ -1 + 1,\ -1 - 3 + 4) = (0, 0, 0)$.
5. So the [[nullity|00K4FK4NBH]] of $T$ is $1$.
6. The [[image|0JB228DCWB]] is spanned by the columns. Since $c_3 = c_1 + c_2$, the image is spanned by $c_1$ and $c_2$.
7. The vectors $c_1$ and $c_2$ are not multiples of each other, so they are linearly independent. So the image is a plane and the [[rank|0JGB7A6GTS]] of $T$ is $2$.
8. Each column $(a, b, c)$ satisfies $c = a + b$: $1 = 1 + 0$, $3 = 2 + 1$ and $4 = 3 + 1$. So $\operatorname{im} T = \{(a, b, c) : c = a + b\}$.
9. For example, $(1, 1, 1)$ is not in the image, since $1 \ne 1 + 1$. So the system $Ax = (1, 1, 1)$ has no solution.

The rank and the nullity add up to $2 + 1 = 3 = \dim \R^3$, as the [[rank–nullity theorem|0W4FSW1TVB]] says.

## Remarks

- The relation $c_3 = c_1 + c_2$ gives the kernel vector $(1, 1, -1)$, which is $-1$ times the vector in step 3.
- Each relation among the columns gives a kernel vector, and each kernel vector gives a relation among the columns.
- The map is neither injective nor surjective. In finite dimension these two fail together for a map $V \to V$, by the [[theorem on endomorphisms|0912EEEVCT]].

## Explanations

### L1 human

The matrix squeezes all of space onto a plane, so one direction is lost.
The lost direction is the kernel, the line through $(-1, -1, 1)$.
The plane is the image, and the points off it cannot be reached.

### L2 human

The computation uses one row reduction for two answers.
The kernel comes from the solutions of $Ax = 0$, and the image comes from the independent columns.
The equation $c = a + b$ of the image is also a test for which systems $Ax = b$ can be solved.
The trap is to take the pivot columns of the reduced matrix as a basis of the image; one must take the matching columns of $A$ itself.
