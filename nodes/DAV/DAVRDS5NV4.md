---
tag: DAVRDS5NV4
kind: example
name: The powers of the diagonal matrix diag(2, −1, 3)
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [044JNC7ZAA]
uses: [0Q9PGXD9E4, 076JGP6R3T, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: Matrix operations
---

## Example

Let
$$D = \operatorname{diag}(2, -1, 3) = \begin{pmatrix} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 3 \end{pmatrix},$$
a [[diagonal matrix|0Q9PGXD9E4]] over $\mathbb{R}$.
We compute its powers, its inverse and a polynomial in it.

1. By the [[product rule|076JGP6R3T]], $(D^2)_{ij} = \sum_k d_{ik} d_{kj}$. A term is nonzero only when $i = k$ and $k = j$, so $D^2$ is diagonal with entries $d_{ii}^2$:
$$D^2 = \operatorname{diag}(4, 1, 9).$$
2. By [[induction|0ASJVEFA9J]] on $k \ge 1$, $D^k = \operatorname{diag}(2^k, (-1)^k, 3^k)$. The case $k = 1$ is the definition of $D$. If the formula holds for $k$, then step 1, applied to the product of two diagonal matrices, gives
$$D^{k+1} = D^k D = \operatorname{diag}(2^k \cdot 2, (-1)^k \cdot (-1), 3^k \cdot 3) = \operatorname{diag}(2^{k+1}, (-1)^{k+1}, 3^{k+1}).$$
3. For example, $D^5 = \operatorname{diag}(32, -1, 243)$.
4. Every diagonal entry is nonzero, so $D$ is invertible with $D^{-1} = \operatorname{diag}(\tfrac{1}{2}, -1, \tfrac{1}{3})$. Check: the product is $\operatorname{diag}(2 \cdot \tfrac{1}{2}, (-1)(-1), 3 \cdot \tfrac{1}{3}) = I$.
5. Take $p(x) = x^2 - x - 6 = (x - 3)(x + 2)$. Then $p(D) = D^2 - D - 6I$, and each diagonal entry is $p$ of the entry of $D$:
$$p(D) = \operatorname{diag}(p(2), p(-1), p(3)) = \operatorname{diag}(4 - 2 - 6, \; 1 + 1 - 6, \; 9 - 3 - 6) = \operatorname{diag}(-4, -4, 0).$$

## Remarks

Step 5 is an instance of a general rule: for every polynomial $p$, $p(\operatorname{diag}(d_1, \dots, d_n)) = \operatorname{diag}(p(d_1), \dots, p(d_n))$.
So $p(D) = 0$ exactly when $p(2) = p(-1) = p(3) = 0$.
Over $\mathbb{R}$ this means that $(x - 2)(x + 1)(x - 3)$ divides $p$, and this cubic is the minimal polynomial of $D$.

The sign pattern of the middle entry, $(-1)^k$, never settles, while the third entry grows fastest.
For large $k$ the power $D^k$ is dominated by the entry $3^k$, which is the start of the power method for the largest eigenvalue.

## Explanations

### L1 human

To raise a diagonal matrix to a power, raise each diagonal number to that power.
The zeros off the diagonal stay zero.
So the fifth power of $\operatorname{diag}(2, -1, 3)$ has $2^5 = 32$, $(-1)^5 = -1$ and $3^5 = 243$ on its diagonal.

### L2 human

The map $x \mapsto Dx$ stretches the three axes by $2$, $-1$ and $3$, and doing it $k$ times stretches them by the $k$-th powers.
For a general matrix, a [[diagonalization|07SQCNV233]] $A = PDP^{-1}$ gives $A^k = PD^kP^{-1}$, so the same computation does the hard part.
Watch out: the rule "raise each entry to the power" is true only for diagonal matrices; for $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ the square has entry $2$ at $(1, 2)$, not $1$.
