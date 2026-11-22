---
tag: TBP8ZNSCGQ
kind: example
name: The plane as the direct sum of two lines
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0XYYT5KNTX]
illustrates: [20A0K3KBZD]
uses: [041JTZCK9Q, 0EPTJA5QV4, 0V33SPH7RR]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Internal direct sum
  - book: isbn:9783031410253
    locator: Section 1C
---

## Example

Let $U = \R(1, 0)$ and $W = \R(1, 2)$ in $\R^2$.
We check that $\R^2 = U \oplus W$, and we find the two parts of a vector.

1. $U$ and $W$ are [[subspaces|0EPTJA5QV4]], since each is the span of one vector.
2. Intersection.
   If $a(1, 0) = b(1, 2)$, then the second coordinates give $0 = 2b$, so $b = 0$, and then the first coordinates give $a = 0$.
   So $U \cap W = \{0\}$, and the sum $U + W$ is [[direct|041JTZCK9Q]] by the [[criteria for two subspaces|20A0K3KBZD]].
3. Sum.
   For $(x, y) \in \R^2$, we solve $(x, y) = a(1, 0) + b(1, 2) = (a + b, 2b)$.
   The second coordinate gives $b = y/2$, and the first gives $a = x - y/2$.
   So every vector of $\R^2$ lies in $U + W$, and $\R^2 = U \oplus W$.
4. A vector.
   For $(3, 4)$ we get $b = 2$ and $a = 1$, so
$$(3, 4) = (1, 0) + (2, 4), \qquad (1, 0) \in U, \quad (2, 4) \in W.$$
   Check: $(1, 0) + (2, 4) = (3, 4)$, and $(2, 4) = 2 \cdot (1, 2)$.

## Remarks

### No right angle needed

The two lines are not perpendicular, and no inner product enters the argument.
Any two different lines through $0$ in $\R^2$ give a direct sum in the same way: they meet only in $0$, and $1 + 1 = 2$, so the [[dimension criterion|P4JG9DJ2HH]] applies.

### Changing the second line

If we replace $(1, 2)$ by $(1, c)$, the same steps give $b = y/c$ and $a = x - y/c$, as long as $c \ne 0$.
For $c = 0$ the second line is the first line again, the equation $0 = cb$ no longer forces $b = 0$, and the sum is the single line $U$.

### The projection hidden in the formula

The map $(x, y) \mapsto (x - y/2, 0)$, which keeps the part in $U$, is the [[projection|033DA1WE8Y]] onto $U$ along $W$.
It sends $(3, 4)$ to $(1, 0)$, and it sends every vector of $W$, such as $(1, 2)$, to $0$.

## Explanations

### L1 human

The horizontal line and the slanted line through $(1, 2)$ cross only at the origin.
Each point of the plane can be reached by a step along the first line followed by a step along the second, and in only one way.
To reach $(3, 4)$, step $1$ to the right, then go twice along $(1, 2)$.

### L2 human

Step 3 is a $2 \times 2$ linear system in the unknowns $a$ and $b$, with the matrix
$$\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}.$$
Its columns are the two spanning vectors $(1, 0)$ and $(1, 2)$.
The determinant is $1 \cdot 2 - 1 \cdot 0 = 2 \ne 0$, so the system has exactly one solution for each right side $(x, y)$.
Existence of the solution is $U + W = \R^2$, and uniqueness is the directness of the sum.
So for two lines in the plane, the direct sum test is the same as asking that the two spanning vectors form an invertible matrix.
