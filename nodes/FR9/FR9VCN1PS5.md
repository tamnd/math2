---
tag: FR9VCN1PS5
kind: definition
name: Cartan matrix
msc: ["17B22", "17B20"]
defines: H59F1XBDZP
uses: [AVVV93CASN, CSBM217V1N, XV6Q01FVAS, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan_matrix
---

## Definition

Let $\Phi$ be a [[root system|AVVV93CASN]] in a Euclidean space $E$ with inner product $(\cdot, \cdot)$.
Let $\Delta = (\alpha_1, \dots, \alpha_l)$ be a base of [[simple roots|CSBM217V1N]] in a fixed order.
The *Cartan matrix* of $\Phi$ with respect to $\Delta$ is the $l \times l$ [[matrix|0VD9ZSWWJG]] $A = (a_{ij})$ with entries
$$a_{ij} = \langle \alpha_i, \alpha_j \rangle = \frac{2 (\alpha_i, \alpha_j)}{(\alpha_j, \alpha_j)} = (\alpha_i, \alpha_j^\vee),$$
where $\alpha_j^\vee$ is the [[coroot|XV6Q01FVAS]] of $\alpha_j$.

## Remarks

The diagonal entries are $a_{ii} = 2$, the other entries lie in $\set{0, -1, -2, -3}$, and $a_{ij} = 0$ if and only if $a_{ji} = 0$.
Example: for $B_2$ with $\alpha_1 = e_1 - e_2$ and $\alpha_2 = e_2$, one has $(\alpha_1, \alpha_1) = 2$, $(\alpha_2, \alpha_2) = 1$ and $(\alpha_1, \alpha_2) = -1$.
So $a_{12} = 2(-1)/1 = -2$ and $a_{21} = 2(-1)/2 = -1$, and $A = \begin{pmatrix} 2 & -2 \\ -1 & 2 \end{pmatrix}$.
Non-example: $\begin{pmatrix} 2 & -4 \\ -1 & 2 \end{pmatrix}$ is not the Cartan matrix of a root system, since $a_{12} a_{21} = 4$ would force $\alpha_1$ and $\alpha_2$ to be proportional, which two simple roots never are.
Some authors, for example in the theory of Kac–Moody algebras, use the transpose convention $a_{ij} = \langle \alpha_j, \alpha_i \rangle$.
A different reordering of $\Delta$ conjugates $A$ by a permutation matrix, and a different base gives the same matrix up to such a reordering.
This notion is not the [[Cartan matrix of an algebra|ZBQ4KRC98K]] in the representation theory of finite-dimensional algebras.

## Explanations

### L1 human

The Cartan matrix is the table of the numbers $\langle \alpha_i, \alpha_j \rangle$ for the simple roots.
It stores all the angles and length ratios between simple roots in whole numbers.
