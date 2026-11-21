---
tag: VDC3D0JADY
kind: example
name: An array from a nonlinear system gives a false solution
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
not_instance_of:
  - target: 0T6MWGZSXA
    note: the system contains x squared, so it has no augmented matrix, and row reducing an array of its numbers gives a false answer
uses: [0YCDZ7N8VD, 0Q3ZT8J05R]
sources:
  - url: https://en.wikipedia.org/wiki/Augmented_matrix
    locator: lead section
---

## Example

Row reduction gives an answer even when it should not be used, and the answer can be false.
Consider over $\mathbb{R}$ the system
$$x^2 + y = 3, \qquad x - y = 1.$$

1. The term $x^2$ is not a constant times $x$, so the first equation is not a [[linear equation|0Q3ZT8J05R]].
2. Suppose a student treats $x^2$ as if it were $x$ and writes the array $\left[\begin{array}{cc|c} 1 & 1 & 3 \\ 1 & -1 & 1 \end{array}\right]$.
3. Reducing it, $R_2 \leftarrow R_2 - R_1$ gives the row $(0, -2 \mid -2)$. So $y = 1$, and then $x = 3 - 1 = 2$.
4. Check $(2, 1)$ in the true system: the first equation gives $4 + 1 = 5 \ne 3$. So $(2, 1)$ is not a solution.
5. Find the true solutions by substitution. The second equation gives $y = x - 1$, and then the first becomes $x^2 + x - 4 = 0$. So $x = \tfrac{-1 \pm \sqrt{17}}{2}$ and $y = x - 1$.
6. The array of step 2 is therefore not an [[augmented matrix|0YCDZ7N8VD]] of this system. The system has no augmented matrix at all, because it is not linear.

## Remarks

Only linear systems have augmented matrices.
The true system has exactly two solutions, one for each root of $x^2 + x - 4$.
No linear system over $\mathbb{R}$ has exactly two solutions, since its solution set is empty, a single point, or infinite.
So no table of numbers could describe this system and be solved by row reduction.

## Explanations

### L1 human

The table method works only when every unknown appears plainly, multiplied by a number.
A square of an unknown breaks it.
The method still produces numbers, so the mistake shows only when you put them back into the equations.

### L2 human

1. Check that each equation is linear before you build the table.
2. If one is not, use substitution or other methods for nonlinear equations.

Watch out: always check a solution in the original equations, not only in the table.
