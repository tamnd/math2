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
We first write the formula by entries, then check the three axioms of an [[inner product|0VGSYBWHV2]], and then compute one example.

1. Row $k$ of $B^*$ is the conjugate of column $k$ of $B$, so the diagonal entry $(k, k)$ of $B^* A$ is $\sum_j \overline{b_{jk}}\, a_{jk}$.
Adding over $k$ gives
$$\ip{A}{B} = \sum_{j, k} a_{jk} \overline{b_{jk}}.$$
2. Linearity in the first slot holds, because matrix multiplication and the trace are linear: $\tr(B^*(aA + cC)) = a\tr(B^* A) + c\tr(B^* C)$.
3. Conjugate symmetry holds, because by step 1 the number $\ip{B}{A} = \sum_{j, k} b_{jk}\overline{a_{jk}}$ is the conjugate of $\sum_{j, k} a_{jk}\overline{b_{jk}}$.
4. Positive definiteness holds, because by step 1 we have $\ip{A}{A} = \sum_{j, k} \abs{a_{jk}}^2$, which is $0$ only when every entry of $A$ is $0$.
5. For the computation take
$$A = \begin{pmatrix} 1 & i \\ 0 & 2 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 1 & i \end{pmatrix}, \qquad B^* = \begin{pmatrix} 1 & 1 \\ 0 & -i \end{pmatrix}.$$
6. Multiply and take the trace:
$$B^* A = \begin{pmatrix} 1 & 2 + i \\ 0 & -2i \end{pmatrix}, \qquad \ip{A}{B} = 1 - 2i.$$
7. Check with the entry formula of step 1:
$$1 \cdot \overline{1} + i \cdot \overline{0} + 0 \cdot \overline{1} + 2 \cdot \overline{i} = 1 - 2i.$$
8. In the other order, $A^* B = \begin{pmatrix} 1 & 0 \\ 2 - i & 2i \end{pmatrix}$, so $\ip{B}{A} = 1 + 2i$, the conjugate of $1 - 2i$ as step 3 predicts.
9. A scalar in the first slot comes out unchanged, $\ip{iA}{B} = i(1 - 2i) = 2 + i$.
A scalar in the second slot comes out conjugated, $\ip{A}{iB} = -i(1 - 2i) = -2 - i$.
10. The [[induced norms|0MFJJV97RJ]] are given by $\norm{A}^2 = 1 + 1 + 0 + 4 = 6$ and $\norm{B}^2 = 1 + 0 + 1 + 1 = 3$.
11. The [[Cauchy-Schwarz inequality|0RFWW56Y22]] holds, since $\abs{\ip{A}{B}} = \sqrt{5}$ and $\norm{A} \, \norm{B} = \sqrt{18}$.

So $(M_2(\mathbb{C}), \ip{\cdot}{\cdot})$ is an [[inner product space|0QVNCJXRY3]].

## Remarks

Step 1 is the heart of the example: the trace inner product is the standard inner product of $\mathbb{C}^4$, applied to the four entries.
So the same argument works for $m \times n$ matrices, and the induced norm is the [[Frobenius norm|JT8Q204E4R]], the square root of the sum of the squared moduli of the entries.
For real matrices the conjugate does nothing, and the formula becomes $\tr(B^{\mathsf{T}} A)$, as in the [[example of the Frobenius inner product|Z88VRHAS1X]].

Books also write $\tr(A B^*)$, and that is the same inner product, by the [[cyclic property of the trace|0Y4NF1DRKD]].
The star cannot be dropped.
With $\tr(BA)$ in place of $\tr(B^* A)$, take $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$: then $A^2 = 0$, so $\tr(AA) = 0$ although $A \neq 0$.

## Explanations

### L1 human

A $2 \times 2$ matrix has four numbers, so we can treat it as a list of four numbers.
The trace inner product multiplies matching entries, with the entry of the second matrix conjugated, and adds the four results.
For the matrix with all four entries equal to $1$, paired with itself, we get $1 + 1 + 1 + 1 = 4$.
So the length of this matrix is $\sqrt{4} = 2$.
The formula $\tr(B^* A)$ is a short way to write this sum.

### L2 human

Here is a typical question: what is the angle between $A = I_2$ and $B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$?
Both matrices are real, so $B^* = B^{\mathsf{T}}$, and the entry formula gives
$$\ip{A}{B} = 1 \cdot 1 + 0 \cdot 1 + 0 \cdot 0 + 1 \cdot 1 = 2.$$
The norms are $\norm{A} = \sqrt{2}$ and $\norm{B} = \sqrt{3}$, so
$$\cos\theta = \frac{2}{\sqrt{2}\sqrt{3}} = \frac{2}{\sqrt{6}} \approx 0.816,$$
and $\theta$ is about $35.3$ degrees.
In numerical linear algebra the same norm measures how far an approximate matrix is from the exact one.
Watch out: $\tr(B^* A)$ and $\tr(A^* B)$ are conjugates of each other, not equal numbers, as steps 6 and 8 show.
