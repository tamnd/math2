---
tag: Q9YN0F60ZW
kind: statement
role: theorem
name: The pseudoinverse from the SVD and minimum-norm least squares
msc: [15A09, 15A18, 65F20]
topics: [SS4EVPKT3A]
audience: ug2
about: [0YY8VX28JR]
uses: [0PSRCMCM5X, 000NPTMX6J, 0AR68JTMDT, 0BYTQ4X1HC, 0Q8HZTJC7G, 03AJKXH1AV]
proofs: [2X5WK5XRMH]
sources:
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Existence and uniqueness
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Singular value decomposition (SVD)
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Projectors
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Linear least-squares
  - book: isbn:9781733146678
    locator: Chapter 7
---

## Statement

Every matrix has exactly one pseudoinverse, the SVD computes it, and it gives the shortest least-squares solution of every linear system.

Let $A$ be an $m \times n$ complex matrix of rank $r$, and let $A = U \Sigma V^*$ be a [[singular value decomposition|000NPTMX6J]], with $U$ and $V$ [[unitary|0AR68JTMDT]], columns $u_1, \dots, u_m$ and $v_1, \dots, v_n$, and nonzero singular values $\sigma_1, \dots, \sigma_r$.
Let $\Sigma^+$ be the $n \times m$ matrix with $(\Sigma^+)_{ii} = 1/\sigma_i$ for $i \le r$ and all other entries $0$.

1. Existence. The matrix $X = V \Sigma^+ U^*$ satisfies the four Penrose conditions of the [[Moore-Penrose inverse|0PSRCMCM5X]].
2. Uniqueness. At most one $n \times m$ matrix satisfies the four conditions. So $A^+ = V \Sigma^+ U^*$, and this matrix does not depend on the choice of SVD.
3. Projections. $A A^+ = \sum_{i=1}^r u_i u_i^*$ is the [[orthogonal projection|0Q8HZTJC7G]] onto the [[column space|03AJKXH1AV]] of $A$, and $A^+ A = \sum_{i=1}^r v_i v_i^*$ is the orthogonal projection onto the column space of $A^*$.
4. Least squares. Let $b \in \C^m$. The vector $x^+ = A^+ b$ minimizes $\norm{Ax - b}$ over $x \in \C^n$, and among all minimizers it is the only one of smallest norm.
5. Reality. If $A$ is real, then $A^+$ is real.

## Remarks

### Why each hypothesis is needed

There is no hypothesis on $A$ at all, and that is the point of the theorem.
Rectangular, singular and zero matrices all have exactly one pseudoinverse.
The SVD is only a tool for the construction, and part 2 says that the result is the same for every SVD that we might choose.

All four conditions are needed for uniqueness in part 2.
For $A = \operatorname{diag}(1, 0)$, [[the diagonal non-example|2GME1M2784]] shows that $I_2$ satisfies conditions 1, 3 and 4, and $I_2 \ne A^+ = A$.

The norms in part 4 are the standard Euclidean norms.
With a weighted norm such as $\norm{x}_W^2 = x^* W x$ for a positive definite $W$, the shortest solution changes, and a weighted pseudoinverse describes it.
For example, $x_1 + x_2 = 3$ has shortest standard solution $(\tfrac32, \tfrac32)$, but for $\norm{x}_W^2 = x_1^2 + 2 x_2^2$ the shortest solution is $(2, 1)$, since $x_1 = 2 x_2$ at the minimum.

### What it gives you

The theorem turns the four abstract conditions into a recipe: find an SVD, invert the nonzero singular values, and swap the roles of $U$ and $V$.
In the reduced form $A = U_r \Sigma_r V_r^*$, this reads $A^+ = V_r \Sigma_r^{-1} U_r^*$.

Two closed formulas follow.
If the columns of $A$ are independent, then $r = n$ and $A^+ = (A^* A)^{-1} A^*$, as [[the example with independent columns|SYDSCH64X8]] checks.
If the rows are independent, then $r = m$ and $A^+ = A^* (A A^*)^{-1}$, so $A^+ b$ is the [[minimum-norm solution|QM2Y84VDX8]] of $Ax = b$.
For real $A$, part 4 contains the [[least-squares solution from a reduced SVD|SBP2PCHH9M]].

The real use is the case of dependent columns, where the normal equations have a whole affine space of solutions.
[[The rank-one example|PHVR0HP7M5]] has $A = u v^{\mathsf{T}}$ with $u = (1, 2, 3)$ and $v = (1, 2)$.
For $b = (1, 1, 1)$ every $x$ with $x_1 + 2 x_2 = \tfrac37$ is a least-squares solution, and $A^+ b = (\tfrac{3}{35}, \tfrac{6}{35})$ is the shortest of them.
Check: $\tfrac{3}{35} + 2 \cdot \tfrac{6}{35} = \tfrac{15}{35} = \tfrac37$.

### The converse

The least-squares property in part 4 determines $A^+$ on its own.
Suppose an $n \times m$ matrix $X$ has $X b = x^+$ for every $b \in \C^m$.
Then $X e_j = A^+ e_j$ for each standard basis vector $e_j$, so the columns of $X$ and $A^+$ agree and $X = A^+$.
So part 4 can serve as a second definition of the pseudoinverse, and many applied books start there.

### Generalizations

For a bounded operator between Hilbert spaces, the four conditions have a bounded solution exactly when the range of the operator is closed.
This belongs to functional analysis.
Weighted inner products on $\C^m$ and $\C^n$ give weighted pseudoinverses, and the proof is the same after a change of coordinates.

## History

Moore described the inverse in 1920, and Arne Bjerhammar described it again in 1951.
Roger Penrose characterized it by the four conditions in 1955, which is why they carry his name.

## Explanations

### L1 human

Every matrix has exactly one pseudoinverse.
To find it, write the matrix as rotate, stretch, rotate with the SVD.
Undo the two rotations, and undo each stretch by a nonzero factor $\sigma$ by stretching by $1/\sigma$.
A stretch by zero cannot be undone, so it stays zero.
The result gives the best solution of $Ax = b$: as close to $b$ as possible, and then as short as possible.

### L2 human

Here is why the recipe solves least squares.
In the coordinates $y = V^* x$ and $c = U^* b$, the unitary matrices keep all lengths, so
$$\norm{Ax - b}^2 = \norm{\Sigma y - c}^2 = \sum_{i=1}^r \abs{\sigma_i y_i - c_i}^2 + \sum_{i=r+1}^m \abs{c_i}^2.$$
The first sum is zero exactly when $y_i = c_i / \sigma_i$ for $i \le r$, and the second sum does not depend on $x$.
The coordinates $y_{r+1}, \dots, y_n$ do not change $Ax$, and setting them to zero makes $\norm{x} = \norm{y}$ as small as possible.
That choice is $y = \Sigma^+ c$, so $x = V \Sigma^+ U^* b = A^+ b$.
Watch out: inverting every diagonal entry of $\Sigma$ is wrong when $r < \min(m, n)$, because some entries are $0$.

### L3 human

Part 3 says that $A$ restricts to a bijection from the column space of $A^*$ onto the column space of $A$, and that $A^+$ is its inverse, extended by zero on the orthogonal complement of the column space of $A$.
The uniqueness proof in part 2 uses only the four equations and the rule $(XY)^* = Y^* X^*$, so it works in every ring with an involution.
The map $A \mapsto A^+$ is continuous on the set of matrices of a fixed rank, but it jumps where the rank changes, which is why numerical software sets small singular values to zero before it inverts.
