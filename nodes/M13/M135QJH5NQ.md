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

1. For every $v \in F^2$, $I_2 v = v$. So $I_2^k v = v$ for all $k \ge 0$.
2. So $Z(v; I_2) = \operatorname{span}\set{v}$, of dimension $0$ or $1$.
3. Since $\dim F^2 = 2$, no $v$ satisfies $Z(v; I_2) = F^2$. So $I_2$ is not [[cyclic|42MMQBTP0M]].
4. The [[minimal polynomial|03NDVCSHSB]] of $I_2$ is $x - 1$, since $I_2 - I_2 = 0$ and no constant monic polynomial kills $I_2$.
5. The [[characteristic polynomial|039HF58KQ5]] of $I_2$ is $\det(x I_2 - I_2) = (x - 1)^2$.
6. By the [[theorem on companion matrices|XYR7GPH20K]], a companion matrix has equal minimal and characteristic polynomials.
7. Similar matrices have the same minimal and characteristic polynomials. By steps 4 to 6, $I_2$ is not [[similar|027KDW2K72]] to any [[companion matrix|0ZCWPNZTQ3]].

## Remarks

The same argument works for every scalar matrix $c I_n$ with $n \ge 2$, and for the zero matrix.
For $n = 1$ the matrix $(c)$ is cyclic: it is the companion matrix $C(x - c)$.
The matrix $J_2(1) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has the same characteristic polynomial as $I_2$, but it is cyclic with cyclic vector $e_2$.

## Explanations

### L1 human

The identity map moves nothing.
If you start with a vector and apply the identity, you get the same vector again.
So you never leave the line of the vector, and one vector cannot reach the whole plane.

### L2 human

1. Compare $I_2$ with $J_2(1)$. Both have characteristic polynomial $(x - 1)^2$.
2. $J_2(1) e_2 = (1, 1)$, and $e_2, (1, 1)$ is a basis. So $J_2(1)$ is cyclic.
3. $I_2$ is not cyclic by the steps above.

So the characteristic polynomial alone does not decide whether a matrix is cyclic.
The trap is to think that a matrix with a repeated eigenvalue is never cyclic: $J_2(1)$ is a counterexample.
