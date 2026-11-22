---
tag: 60W7PZXBVB
kind: example
name: The binomial formula does not generalize to matrices
msc: ["00A35", "15A99"]
topics: [N4P3E53HM0, Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: 976RZZCT1H
    note: the passage from numbers to matrices drops the commutativity ab = ba, which the proof of the formula needs, so the generalized formula is false
  - target: 8G3X8MPG7E
    note: A = (1, 1; 0, 1) and B = (1, 0; 1, 1) give AB = (2, 1; 1, 1) but BA = (1, 1; 1, 2), so the pair does not commute
uses: [976RZZCT1H, 032Q9FB8MT, 099E72KTF8, 0EHWPWGHB2]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Non-commutativity
  - url: https://en.wikipedia.org/wiki/Binomial_theorem
    locator: lead section
---

## Example

For real numbers, $(a + b)^2 = a^2 + 2ab + b^2$, the case $n = 2$ of the [[binomial theorem|0EHWPWGHB2]].
We test the same formula on $2 \times 2$ matrices, with [[matrix multiplication|032Q9FB8MT]] as the product.
Let
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}.$$

1. Compute the two mixed products, row times column:
$$AB = \begin{pmatrix} 1 + 1 & 0 + 1 \\ 0 + 1 & 0 + 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad BA = \begin{pmatrix} 1 + 0 & 1 + 0 \\ 1 + 0 & 1 + 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}.$$
So $AB \ne BA$.
2. Add the matrices and square the sum:
$$A + B = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad (A + B)^2 = \begin{pmatrix} 4 + 1 & 2 + 2 \\ 2 + 2 & 1 + 4 \end{pmatrix} = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}.$$
3. Square each matrix:
$$A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \qquad B^2 = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}.$$
4. Evaluate the right side of the school formula:
$$A^2 + 2AB + B^2 = \begin{pmatrix} 1 + 4 + 1 & 2 + 2 + 0 \\ 0 + 2 + 2 & 1 + 2 + 1 \end{pmatrix} = \begin{pmatrix} 6 & 4 \\ 4 & 4 \end{pmatrix}.$$
5. The matrices of steps 2 and 4 differ in the entries $(1, 1)$ and $(2, 2)$. So $(A + B)^2 \ne A^2 + 2AB + B^2$ for this pair.
6. The distributive law alone gives the correct expansion, $(A + B)^2 = (A + B)(A + B) = A^2 + AB + BA + B^2$.
7. Check:
$$A^2 + AB + BA + B^2 = \begin{pmatrix} 1 + 2 + 1 + 1 & 2 + 1 + 1 + 0 \\ 0 + 1 + 1 + 2 & 1 + 1 + 2 + 1 \end{pmatrix} = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix},$$
which agrees with step 2.

## Remarks

The proof of the formula for numbers has exactly one step that uses [[commutativity|099E72KTF8]]: it replaces $ab + ba$ by $2ab$.
Matrices satisfy every other rule in that proof, but not $AB = BA$.
So the passage from numbers to matrices drops a hypothesis that the proof needs, and the formula fails.
This makes the example a non-example of a correct [[generalization|976RZZCT1H]].
Subtracting step 6 from the school formula shows the exact condition: the formula holds for $A$ and $B$ if and only if $BA = AB$.

The formula does hold for two matrices that commute.
For example, with $B = A$ we get $(2A)^2 = 4A^2 = A^2 + 2A^2 + A^2$.
In every ring, the binomial theorem $(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$ holds for elements with $ab = ba$, and the [[binomial theorem for commuting matrices|DS9TS6AFMW]] is the matrix case.
So the correct generalization is "to every ring, for commuting elements", and not "to every ring".

## Explanations

### L1 human

For ordinary numbers, $3 \cdot 5$ and $5 \cdot 3$ are the same.
The square formula $(a + b)^2 = a^2 + 2ab + b^2$ uses this fact, because it counts $ab$ and $ba$ as two copies of one thing.
For matrices the order of a product matters, and $AB$ and $BA$ can differ.
So for matrices you must write $AB + BA$ where numbers allow $2ab$.

### L2 human

The typical use of this example is a habit of checking.
Before you use a familiar algebraic rule in a new setting, list the laws that its proof needs, and check each law in the new setting.
Here the list is the distributive law, associativity and commutativity, and only the last one fails for matrices.
Watch out: the formula holds for many matrices, for example for any two diagonal matrices, so a test with diagonal matrices does not reveal the problem.
A pair with no zero entries in the products, like the pair above, is a safer test.
