---
tag: B0ABS5W1FV
kind: example
name: Jordan form of a 4 × 4 matrix with one eigenvalue
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
instance_of: [7M1W0ZA49Q]
illustrates: [085HQ5G5TE, Z2RTKWZZAZ]
uses: [7M1W0ZA49Q, 0PBFS92AJP, 0EWQEYRVA8, 0W4FSW1TVB, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_normal_form
    locator: "Example: Obtaining the normal form"
---

## Example

We run the [[method for computing the Jordan form|7M1W0ZA49Q]] on a $4 \times 4$ matrix over $\mathbb{Q}$ with a single eigenvalue:
$$A = \begin{pmatrix} 2 & 0 & 0 & 1 \\ 0 & 2 & 0 & 1 \\ -1 & 1 & 2 & 0 \\ 1 & -1 & 0 & 2 \end{pmatrix}, \qquad N = A - 2I = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 \\ -1 & 1 & 0 & 0 \\ 1 & -1 & 0 & 0 \end{pmatrix}.$$

1. Multiply row by column to get the square:
$$N^2 = \begin{pmatrix} 1 & -1 & 0 & 0 \\ 1 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
The nonzero columns of $N^2$ are multiples of $(1, 1, 0, 0)$, and $N (1, 1, 0, 0) = (0, 0, -1 + 1, 1 - 1) = 0$, so $N^3 = N \cdot N^2 = 0$.
2. Since $N$ is nilpotent, $\chi_A = (x - 2)^4$, and $2$ is the only eigenvalue, with multiplicity $4$.
3. The rows of $N$ are $(0, 0, 0, 1)$ twice and $\pm (-1, 1, 0, 0)$, so the [[rank|0EWQEYRVA8]] of $N$ is $2$. The rank of $N^2$ is $1$, and the rank of $N^3$ is $0$.
4. By the [[rank-nullity theorem|0W4FSW1TVB]], the kernel dimensions are $d_1, d_2, d_3 = 2, 3, 4$.
5. The jumps are $2, 1, 1$. So there are $2$ blocks, one of them has size at least $2$ and at least $3$, and the sizes are $3$ and $1$: $J = J_3(2) \oplus J_1(2)$.
6. The kernels are $\ker N = \operatorname{span}\{(1, 1, 0, 0), (0, 0, 1, 0)\}$ and $\ker N^2 = \operatorname{span}\{(1, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)\}$.
7. For the chain of length $3$, choose $u = e_1$, which is not in $\ker N^2$ because its first two entries differ. Then $N u = (0, 0, -1, 1)$, and $N^2 u = (1, 1, 0, 0)$ is an eigenvector.
8. For the chain of length $1$, choose an eigenvector that is independent of $N^2 u$, namely $e_3 = (0, 0, 1, 0)$.
9. Put the chains in order, each from the eigenvector up to the top vector:
$$P = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 1 \\ 0 & 1 & 0 & 0 \end{pmatrix}, \qquad J = \begin{pmatrix} 2 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix}.$$
10. Check. The product is
$$AP = \begin{pmatrix} 2 & 1 & 2 & 0 \\ 2 & 1 & 0 & 0 \\ 0 & -2 & -1 & 2 \\ 0 & 2 & 1 & 0 \end{pmatrix},$$
and the columns of $PJ$ are $2 p_1$, $p_1 + 2 p_2$, $p_2 + 2 p_3$ and $2 p_4$, which are the same four columns.
11. The [[determinant|0C3CFHDN6R]] of $P$ is $-1 \ne 0$, so $P$ is invertible and $A = P J P^{-1}$.

## Remarks

The top vector is not unique.
The choice $u = e_2$ also works, with $N u = (0, 0, 1, -1)$ and $N^2 u = (-1, -1, 0, 0)$.
The choice $u = e_4$ fails, since $N^2 e_4 = 0$, so $e_4$ has height $2$ and its chain is too short.
For the chain of length one, the vector $(1, 1, 0, 0)$ is a wrong choice, because it is already the bottom of the first chain and $P$ would have two equal columns.

What changes when the ranks change?
If $N^2$ were $0$ with $\operatorname{rank} N = 2$, the jumps would be $2, 2$, and the form would be $J_2(2) \oplus J_2(2)$.
If $\operatorname{rank} N$ were $3$, there would be one block, $J_4(2)$, as for the [[block J₄(0)|7SYF048QE6]].

## Explanations

### L1 human

This matrix has only the eigenvalue $2$, so every Jordan block has $2$ on its diagonal.
The spaces of vectors that $A - 2I$ and its powers send to zero have dimensions $2$, $3$ and $4$.
The growth $2, 1, 1$ means two chains, of which only one goes on to the second and third steps.
So the form has one long block of size $3$ and one block of size $1$.

### L2 human

The jumps $2, 1, 1$ are the column lengths of the Young diagram of the partition $(3, 1)$, as the [[normal form of nilpotent endomorphisms|Z2RTKWZZAZ]] predicts.
The top of the long chain must come from outside $\ker N^2$, and $e_1$ is the simplest such vector, since $\ker N^2$ is cut out by the equation $x_1 = x_2$.
Once $u$ is fixed, the chain is forced: $N u$ and $N^2 u$ are computed, not chosen.
The trap is to choose the short chain first, as any eigenvector: the eigenvector $(1, 1, 0, 0)$ is the bottom of the long chain, so it cannot be used again.
