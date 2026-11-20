---
tag: JVH9RZ7QAB
kind: example
name: The trace inner product on 2 by 2 complex matrices
msc: ["15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
instance_of: [0NB0AWGJBW, 0QVNCJXRY3, 0MFJJV97RJ]
uses: [0VGSYBWHV2, 0XC1RDBY7A, 0DXKE10PHF, 0RE6X3BGPN]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Complex matrices
  - url: https://en.wikipedia.org/wiki/Frobenius_inner_product
    locator: Complex-valued matrices
---

## Example

Let $V = M_2(\mathbb{C})$ be the [[space of complex $2 \times 2$ matrices|0RE6X3BGPN]].
For $A, B \in V$ put
$$\ip{A}{B} = \tr(B^* A),$$
where $B^*$ is the [[conjugate transpose|0DXKE10PHF]] of $B$ and $\tr$ is the [[trace|0XC1RDBY7A]].
We check the three axioms of an [[inner product|0VGSYBWHV2]], and then we compute one example.

1. A formula by entries. The entry $(k, k)$ of $B^* A$ is $\sum_j \overline{b_{jk}} a_{jk}$, because row $k$ of $B^*$ is the conjugate of column $k$ of $B$. So $\ip{A}{B} = \sum_{j, k} a_{jk} \overline{b_{jk}}$.
2. Linearity in the first argument. Matrix multiplication and the trace are linear, so $\tr(B^*(aA + cC)) = a\tr(B^* A) + c\tr(B^* C)$.
3. Conjugate symmetry. By step 1, $\ip{B}{A} = \sum_{j, k} b_{jk}\overline{a_{jk}}$, and this is the conjugate of $\sum_{j, k} a_{jk}\overline{b_{jk}} = \ip{A}{B}$.
4. Positive definiteness. By step 1, $\ip{A}{A} = \sum_{j, k} |a_{jk}|^2$. This is a sum of nonnegative reals, and it is $0$ only when every entry of $A$ is $0$.
5. A computation. Let
$$A = \begin{pmatrix} 1 & i \\ 0 & 2 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 1 & i \end{pmatrix}, \qquad B^* = \begin{pmatrix} 1 & 1 \\ 0 & -i \end{pmatrix}.$$
6. The product is $B^* A = \begin{pmatrix} 1 & 2 + i \\ 0 & -2i \end{pmatrix}$, so $\ip{A}{B} = 1 - 2i$.
7. The entry formula of step 1 gives the same value: $1 \cdot 1 + i \cdot 0 + 0 \cdot 1 + 2 \cdot (-i) = 1 - 2i$.
8. In the other order, $A^* B = \begin{pmatrix} 1 & 0 \\ 2 - i & 2i \end{pmatrix}$, so $\ip{B}{A} = 1 + 2i = \overline{1 - 2i}$, as step 3 predicts.
9. The scalar $i$ in the first argument comes out unchanged: $\ip{iA}{B} = i(1 - 2i) = 2 + i$. In the second argument it comes out conjugated: $\ip{A}{iB} = -i(1 - 2i) = -2 - i$.
10. The [[induced norms|0MFJJV97RJ]] are $\norm{A}^2 = 1 + 1 + 0 + 4 = 6$ and $\norm{B}^2 = 1 + 0 + 1 + 1 = 3$.
11. The [[Cauchy-Schwarz inequality|0RFWW56Y22]] holds: $|\ip{A}{B}| = \sqrt{5}$ and $\norm{A} \, \norm{B} = \sqrt{18}$.

So $(M_2(\mathbb{C}), \ip{\cdot}{\cdot})$ is an [[inner product space|0QVNCJXRY3]].

## Remarks

The example shows that matrices can carry the same geometry as column vectors.
Step 1 shows that the trace inner product is the standard inner product of $\mathbb{C}^4$ on the four entries.
So the same proof works for $m \times n$ matrices.
The induced norm is the [[Frobenius norm|JT8Q204E4R]].
For real matrices the conjugate does nothing, and we get $\tr(B^{\mathsf{T}} A)$, as in the [[example of the Frobenius inner product|Z88VRHAS1X]].
By the [[cyclic property of the trace|0Y4NF1DRKD]], $\tr(B^* A) = \tr(A B^*)$, so books that write $\tr(AB^*)$ define the same inner product.
If we drop the star and use $\tr(BA)$, positivity fails: for $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ we get $A^2 = 0$, so $\tr(AA) = 0$ with $A \neq 0$.

## Explanations

### L1 human

A $2 \times 2$ matrix has four numbers, so we can treat it as a list of four numbers.
The trace inner product multiplies matching entries, with the second one conjugated, and adds the four results.
For the matrix with entries $1, 1, 1, 1$ paired with itself, we get $1 + 1 + 1 + 1 = 4$.
So the length of this matrix is $\sqrt{4} = 2$.
The formula $\tr(B^* A)$ is a short way to write this sum.

### L2 human

Worked example: the angle between two real matrices.

1. Take $A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. All entries are real, so $B^* = B^{\mathsf{T}}$.
2. By the entry formula, $\ip{A}{B} = 1 \cdot 1 + 0 \cdot 1 + 0 \cdot 0 + 1 \cdot 1 = 2$.
3. The norms are $\norm{A} = \sqrt{2}$ and $\norm{B} = \sqrt{3}$.
4. The cosine of the angle is $2 / \sqrt{6}$, which is less than $1$, as the Cauchy-Schwarz inequality requires.

The typical use is in numerical linear algebra, where the Frobenius norm measures the size of an error matrix.
A trap: $\tr(B^* A)$ and $\tr(A^* B)$ are conjugates of each other, not equal numbers, as steps 6 and 8 show.
