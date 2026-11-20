---
tag: E2MNC3W2DM
kind: statement
role: theorem
name: Cartesian decomposition of a complex square matrix
msc: ["15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [0P17NGQQMQ]
uses: [0EKZCX4K3P, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Skew-Hermitian_matrix
    locator: lead section
---

## Statement

Let $A$ be a complex $n \times n$ matrix.
Then there are unique [[Hermitian|0EKZCX4K3P]] matrices $H$ and $K$ with $A = H + iK$.
They are
$$H = \tfrac12 \left(A + A^*\right), \qquad K = \tfrac{1}{2i} \left(A - A^*\right).$$
Equivalently, $A$ is in one way only the sum of the Hermitian matrix $H$ and the skew-Hermitian matrix $iK$.

## Remarks

### Why each hypothesis is needed

- The matrix must be square, because a Hermitian matrix is square.
- The scalars must be complex. Over $\mathbb{R}$, the analogue is the [[symmetric plus skew-symmetric decomposition|K284W6D15Z]].

### Consequences

- $A$ is Hermitian if and only if $K = 0$, and skew-Hermitian if and only if $H = 0$.
- $A$ is [[normal|0MR0BYF0K2]], that is $A^* A = A A^*$, if and only if $HK = KH$.
- For each $x \in \mathbb{C}^n$, $x^* A x = x^* H x + i\, x^* K x$ with $x^* H x$ and $x^* K x$ real. So these are the real and imaginary parts of $x^* A x$.

### Generalizations

- The same formulas hold in every complex $*$-algebra, such as the bounded operators on a Hilbert space.

## Explanations

### L1 human

Each complex number is $a + ib$ with $a$ and $b$ real.
Each complex square matrix is $H + iK$ with $H$ and $K$ Hermitian.
Hermitian matrices play the part of the real numbers.

### L2 human

The formulas copy $\operatorname{Re} z = (z + \overline{z})/2$ and $\operatorname{Im} z = (z - \overline{z})/(2i)$.
The conjugate transpose $A^*$ plays the part of $\overline{z}$.
