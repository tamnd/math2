---
tag: M135QJH5NQ
kind: example
name: The identity matrix of size two is not cyclic
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
not_instance_of:
  - target: 42MMQBTP0M
    note: for every v the cyclic subspace Z(v; I_2) is the span of v, of dimension at most 1, so no vector is cyclic
  - target: 0ZCWPNZTQ3
    note: I_2 has minimal polynomial x - 1 and characteristic polynomial (x - 1)^2, while every companion matrix has equal minimal and characteristic polynomials, so I_2 is not similar to a companion matrix
illustrates: [RK1QVMYW7H]
uses: [42MMQBTP0M, 06DW9BAWB1, 03NDVCSHSB, 039HF58KQ5, XYR7GPH20K, 027KDW2K72]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_subspace
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Companion_matrix
    locator: Similarity to companion matrix
---

## Example

Let $F$ be a field and let $I_2$ be the [[identity matrix|06DW9BAWB1]] of size $2$ over $F$.
We show that $I_2$ has no cyclic vector, and that it is not similar to any companion matrix.

1. For every $v \in F^2$ we have $I_2 v = v$, and so $I_2^k v = v$ for every $k \ge 0$.
2. So the cyclic subspace is $Z(v; I_2) = \operatorname{span}\{ v \}$, of dimension $0$ or $1$.
3. Since $\dim F^2 = 2$, no $v$ has $Z(v; I_2) = F^2$, so $I_2$ is not [[cyclic|42MMQBTP0M]].
4. The [[minimal polynomial|03NDVCSHSB]] of $I_2$ is $x - 1$, because $I_2 - I_2 = 0$ and the only monic polynomial of degree $0$ is $1$, which does not kill $I_2$.
5. The [[characteristic polynomial|039HF58KQ5]] of $I_2$ is $\det(x I_2 - I_2) = (x - 1)^2$.
6. By the [[theorem on companion matrices|XYR7GPH20K]], every companion matrix has equal minimal and characteristic polynomials.
7. [[Similar|027KDW2K72]] matrices have the same minimal polynomial and the same characteristic polynomial. By steps 4 to 6, $I_2$ is not similar to any [[companion matrix|0ZCWPNZTQ3]].

## Remarks

The same argument works for every scalar matrix $c I_n$ with $n \ge 2$, including the zero matrix.
Each vector spans its own line and nothing more, and the minimal polynomial $x - c$ is shorter than the characteristic polynomial $(x - c)^n$.
For $n = 1$ the matrix $(c)$ is cyclic, since it is the companion matrix $C(x - c)$.

The repeated eigenvalue is not the reason for the failure.
The [[Jordan block|07PH4RX0X5]] $J_2(1) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has the same characteristic polynomial $(x - 1)^2$, and it is cyclic with cyclic vector $e_2$.

## Explanations

### L1 human

The identity map moves nothing.
If you start with a vector and apply the identity, you get the same vector back.
So you never leave the line of the vector, and one vector cannot reach the whole plane.

### L2 human

Compare $I_2$ with $J_2(1)$, which has the same characteristic polynomial $(x - 1)^2$.
For $J_2(1)$, start at $e_2$:
$$J_2(1) e_2 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.$$
The vectors $e_2$ and $(1, 1)$ form a basis, so $J_2(1)$ is cyclic, and its minimal polynomial is $(x - 1)^2$ because $J_2(1) - I \ne 0$.
For $I_2$ the minimal polynomial is only $x - 1$, and no vector is cyclic.
So the characteristic polynomial alone does not decide whether a matrix is cyclic, and the minimal polynomial is what you must compare with it.
