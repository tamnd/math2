---
tag: 0YY8VX28JR
kind: concept
name: Moore-Penrose inverse
aliases: [pseudoinverse]
msc: [15A09]
topics: [SS4EVPKT3A]
audience: ug2
specializes: [FPHNJ5AAYF]
uses: [0PSRCMCM5X, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Singular value decomposition (SVD)
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Linear least-squares
  - book: isbn:9781733146678
    locator: Chapter 7
same_as:
  wikidata: Q43219517
  wikipedia: Moore–Penrose inverse
inventory: [Z0BK2ZVY1Y]
---

## Summary

The Moore-Penrose inverse, or pseudoinverse, gives every matrix an inverse of a kind, even a rectangular or singular one.
It undoes the matrix where the matrix can be undone, it sends the rest to zero, and it turns every linear system into one best answer.
For an $m \times n$ complex matrix $A$, the pseudoinverse is the $n \times m$ matrix $X = A^+$ that satisfies the four Penrose conditions
$$A X A = A, \qquad X A X = X, \qquad (A X)^* = A X, \qquad (X A)^* = X A,$$
where $^*$ is the [[conjugate transpose|0EX045E2BP]].
The [[formal definition|0PSRCMCM5X]] states them.
Every matrix has exactly one pseudoinverse, and for a [[singular value decomposition|000NPTMX6J]] $A = U \Sigma V^*$ it is $A^+ = V \Sigma^+ U^*$, by [[the theorem on the pseudoinverse from the SVD|Q9YN0F60ZW]].
For each $b \in \C^m$, the vector $A^+ b$ is the least-squares solution of $Ax = b$ with the smallest norm.

## Motivation

Only a square matrix with nonzero determinant has an inverse.
A system $Ax = b$ with a rectangular or singular $A$ can have no solution, or it can have infinitely many.
In both cases we still want one sensible answer that depends linearly on $b$.

The [[least-squares|0BYTQ4X1HC]] idea gives the first half of the answer: choose $x$ so that $\norm{Ax - b}$ is as small as possible.
When many vectors $x$ reach that minimum, choose the one of smallest norm.
This rule defines a linear map $b \mapsto x$, and its matrix is $A^+$.
The four Penrose conditions describe the same matrix by equations, with no minimization at all, so we can check a candidate by multiplying matrices.

Numerical software computes $A^+$ to solve least-squares problems with dependent columns, in statistics for regression with collinear variables, and in control and signal processing.
Its error analysis leads to the singular values again, and the [[Eckart-Young-Mirsky theorem|JJT6GC055J]] uses the same singular value picture for approximation.

## Notation

We write $A^+$.
Some books write $A^\dagger$, and numerical software calls the function `pinv`.
In the SVD formula, $\Sigma^+$ is the $n \times m$ matrix with diagonal entries $1/\sigma_i$ for the nonzero singular values $\sigma_i$ and zeros elsewhere, so it has the shape of $\Sigma^{\mathsf{T}}$.
The words "pseudoinverse" and "generalized inverse" sometimes mean a wider class: a [[generalized inverse|FPHNJ5AAYF]] only needs $A G A = A$.
Read the definition in each book before you use its formulas.

## Remarks

### A first computation

Start with a diagonal matrix, where everything is visible.
Let $A = \operatorname{diag}(2, 0)$.
It doubles the first coordinate and kills the second, so the best we can do is halve the first coordinate and kill the second:
$$A^+ = \begin{pmatrix} \tfrac12 & 0 \\ 0 & 0 \end{pmatrix}.$$
Check: $A A^+ = A^+ A = \operatorname{diag}(1, 0)$, which is symmetric, and $A A^+ A = \operatorname{diag}(2, 0) = A$ and $A^+ A A^+ = \operatorname{diag}(\tfrac12, 0) = A^+$.
So all four conditions hold.
The rule for every diagonal matrix is the same: invert the nonzero entries and keep the zeros.

A row vector works the same way.
For $A = \begin{pmatrix} 1 & 1 \end{pmatrix}$, the candidate $X = \tfrac12 \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ gives
$$A X = (1), \qquad X A = \frac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}.$$
Both products are symmetric, $A X A = A$ and $X A X = X$, so $A^+ = X$.
Here $A^+ b = (\tfrac{b}{2}, \tfrac{b}{2})$ is the shortest solution of $x_1 + x_2 = b$.

### Two worked matrices

When the columns of $A$ are independent, $A^* A$ is invertible and $A^+ = (A^* A)^{-1} A^*$.
For $A$ with rows $(1, 1)$, $(1, 0)$ and $(0, 1)$, [[the example with independent columns|SYDSCH64X8]] finds
$$A^+ = \frac13 \begin{pmatrix} 1 & 2 & -1 \\ 1 & -1 & 2 \end{pmatrix},$$
and it gets the same matrix from the SVD.
Check: the first row of $A^+$ times the first column $(1, 1, 0)$ of $A$ is $\tfrac13(1 + 2) = 1$, and times the second column $(1, 0, 1)$ it is $\tfrac13(1 - 1) = 0$.

When the columns are dependent, that formula breaks, but the SVD still works.
The matrix with columns $(1, 2, 3)$ and $(2, 4, 6)$ is $u v^{\mathsf{T}}$ with $u = (1, 2, 3)$ and $v = (1, 2)$.
[[The rank-one example|PHVR0HP7M5]] shows that
$$A^+ = \frac{v u^{\mathsf{T}}}{\norm{u}^2 \norm{v}^2} = \frac{1}{70} \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix},$$
and it checks all four conditions with the numbers $u^{\mathsf{T}} u = 14$ and $v^{\mathsf{T}} v = 5$.

### What the four conditions say

Each condition has a job.
Conditions 3 and 4 say that $A A^+$ and $A^+ A$ are Hermitian, and with conditions 1 and 2 they are also idempotent, so both are orthogonal projections.
In fact $A A^+$ is the [[orthogonal projection|0Q8HZTJC7G]] onto the column space of $A$, and $A^+ A$ is the orthogonal projection onto the column space of $A^*$, which is the row space of $A$ when $A$ is real.
Condition 1 says that $A^+$ undoes $A$ well enough that applying $A$ again gives back $A$.
Condition 2 says that $A^+$ is no larger than it must be, and together with the others it makes $A^+$ zero on the orthogonal complement of the column space of $A$.

So the pseudoinverse is the inverse of the bijection from the row space onto the column space, extended by zero.
This picture gives the first rules at once.
We have $(A^+)^+ = A$ and $(A^*)^+ = (A^+)^*$, because the four conditions are symmetric under these swaps, and $(cA)^+ = c^{-1} A^+$ for every scalar $c \ne 0$.
The rank of $A^+$ equals the rank of $A$, and if $A$ is square and invertible, then $A^+ = A^{-1}$.

### What it is not

The identity matrix is not the pseudoinverse of $\operatorname{diag}(1, 0)$, although it satisfies three of the four conditions.
[[The diagonal non-example|2GME1M2784]] shows that $X = I_2$ fails only $X A X = X$, because $X A X = A \ne I_2$.
So $I_2$ is a generalized inverse of $\operatorname{diag}(1, 0)$, but not its Moore-Penrose inverse, which is $\operatorname{diag}(1, 0)$ itself.

The rule $(AB)^{-1} = B^{-1} A^{-1}$ does not carry over.
Take $A = \begin{pmatrix} 1 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
Then $AB = (1)$, so $(AB)^+ = 1$.
But $B^+ = \begin{pmatrix} 1 & 0 \end{pmatrix}$ and $A^+ = \tfrac12 \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, so
$$B^+ A^+ = \begin{pmatrix} 1 & 0 \end{pmatrix} \cdot \frac12 \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac12 \ne 1.$$

### Watch out

The formula $(A^* A)^{-1} A^*$ needs independent columns.
For the rank-one matrix above, $A^{\mathsf{T}} A = \begin{pmatrix} 14 & 28 \\ 28 & 56 \end{pmatrix}$ has determinant $14 \cdot 56 - 28^2 = 0$, so the formula has no meaning, while $A^+$ exists.

The product $A A^+$ is the identity only when the rows of $A$ are independent.
For $A$ with rows $(1, 1)$, $(1, 0)$, $(0, 1)$, the product $A A^+$ is a $3 \times 3$ matrix of rank $2$, so it cannot be $I_3$.

To form $\Sigma^+$, invert only the nonzero singular values and transpose the shape.
For $\Sigma = \begin{pmatrix} 4 & 0 \\ 0 & 0 \\ 0 & 0 \end{pmatrix}$, the right answer is $\Sigma^+ = \begin{pmatrix} \tfrac14 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$, and $1/0$ never appears.

### Other generalized inverses

The four conditions select one matrix from a larger family.
A matrix with only $A G A = A$ is a [[generalized inverse|FPHNJ5AAYF]], and one with conditions 1 and 2 is a reflexive generalized inverse; neither is unique in general.
For square matrices, the [[Drazin inverse|ZR6XXP36X8]] is another standard choice, and it is built so that it commutes with $A$.
Matrix theory names these classes by the conditions that they satisfy.

### History

E. H. Moore described the inverse in 1920, and Arne Bjerhammar in 1951.
Roger Penrose gave the four conditions in 1955 and proved that they determine one matrix.
Earlier, in 1903, Fredholm had used a pseudoinverse of integral operators.

### Try it

First, find the pseudoinverse of the column $A = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$.
The columns are independent, so $A^+ = (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} = \tfrac{1}{25} \begin{pmatrix} 3 & 4 \end{pmatrix}$, and $A^+ A = 1$.

Second, find the pseudoinverse of $\operatorname{diag}(5, 0, -2)$.
Invert the nonzero entries and keep the zero: the answer is $\operatorname{diag}(\tfrac15, 0, -\tfrac12)$.

Third, what is the pseudoinverse of the $2 \times 3$ zero matrix?
It is the $3 \times 2$ zero matrix, since then all four products in the conditions are zero.

## Explanations

### L1 human

Many matrices have no inverse, because they squash some directions flat.
The pseudoinverse is the best replacement.
It takes the right side $b$ of a system $Ax = b$ and returns the best $x$.
Best means two things: $Ax$ comes as close to $b$ as possible, and among such $x$ it is the shortest.
For example, $x_1 + x_2 = 4$ has many solutions, and the pseudoinverse picks $(2, 2)$, the one nearest the origin.
For a matrix that has an inverse, the pseudoinverse is the usual inverse.

### L2 human

Here is a typical use: the best solution of $A x = b$ for $A = \operatorname{diag}(2, 0)$ and $b = (6, 1)$.
The system asks for $2 x_1 = 6$ and $0 \cdot x_2 = 1$, and the second equation has no solution.
Apply the pseudoinverse from the first computation:
$$A^+ b = \begin{pmatrix} \tfrac12 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 6 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \end{pmatrix}.$$
Every $x = (3, t)$ gives $A x = (6, 0)$, with the smallest possible error $\norm{Ax - b} = 1$.
Among these, $t = 0$ gives the shortest $x$, and that is the answer $A^+ b$.
The same two steps, fit the part you can and set the free part to zero, are what $V \Sigma^+ U^*$ does in the singular bases of any matrix.
Watch out: $A^+$ is not continuous where the rank jumps, since $\operatorname{diag}(1, \varepsilon)^+ = \operatorname{diag}(1, 1/\varepsilon)$ for $\varepsilon \ne 0$ but $\operatorname{diag}(1, 0)^+ = \operatorname{diag}(1, 0)$.

### L3 human

The pseudoinverse depends on the inner products on $\C^n$ and $\C^m$, because "orthogonal projection" and "smallest norm" do.
Other inner products give weighted pseudoinverses, with the same theory.
The uniqueness proof uses only the four equations and the rule $(XY)^* = Y^* X^*$, so the same conditions define a Moore-Penrose inverse in any ring with an involution, where it may or may not exist.
For bounded operators between Hilbert spaces, a bounded pseudoinverse exists exactly when the range is closed, and this belongs to functional analysis.
In floating point, software computes $A^+$ from the SVD and treats singular values below a threshold as zero, which links the pseudoinverse to the [[condition number|AB3S6MHJ8X]] and to the truncated SVD of the [[Eckart-Young-Mirsky theorem|JJT6GC055J]].
