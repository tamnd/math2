---
tag: ~faf4cfba
kind: example
name: Ranks of the powers of the nilpotent Jordan block J₄(0)
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
instance_of: [07PH4RX0X5]
illustrates: [~d1324a3e]
uses: [0PBFS92AJP, 0W4FSW1TVB, 07BSPZPSMF]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_matrix
    locator: Definition
---

## Example

Let $N = J_4(0)$, so $N e_1 = 0$, $N e_2 = e_1$, $N e_3 = e_2$ and $N e_4 = e_3$.

1. $N = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ has the independent nonzero columns $e_1, e_2, e_3$, so its rank is $3$.
2. $N^2$ sends $e_3 \mapsto e_1$, $e_4 \mapsto e_2$ and $e_1, e_2 \mapsto 0$. Its rank is $2$.
3. $N^3$ sends $e_4 \mapsto e_1$ and the other basis vectors to $0$. Its rank is $1$.
4. $N^4 = 0$, so $N$ is [[nilpotent|07BSPZPSMF]] of index $4$.
5. By the [[rank-nullity theorem|0W4FSW1TVB]], $\dim \ker N^j = 1, 2, 3, 4$ for $j = 1, 2, 3, 4$.
6. The kernels grow by one dimension at each step: $\ker N^j = \operatorname{span}(e_1, \dots, e_j)$.

## Remarks

The growth $\dim \ker N^j - \dim \ker N^{j-1} = 1$ for $j = 1, \dots, 4$ says that there is exactly one Jordan block, of size $4$.
Compare $J_2(0) \oplus J_2(0)$, also nilpotent of size $4$: its kernels have dimensions $2, 4$, and the growth $2, 2$ says that there are two blocks of size $2$.
The vector $e_4$ is a cyclic vector, and $e_4 \mapsto e_3 \mapsto e_2 \mapsto e_1 \mapsto 0$ is a Jordan chain.

## Explanations

### L1 human

Each power of this matrix pushes the basis vectors one more step toward zero.
So each power loses one unit of rank, until the fourth power is zero.

### L2 human

Rank and kernel dimension always add up to $4$ here.
The ranks $3, 2, 1, 0$ give kernel dimensions $1, 2, 3, 4$.
This rank pattern is the fingerprint of a single block $J_4(0)$, and it is what the Jordan form algorithm reads.
