---
tag: BNWSH2QCSG
kind: proof
name: Proof of the normal form of nilpotent endomorphisms by Jordan chains
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
proves: Z2RTKWZZAZ
methods: [0ASJVEFA9J, 0NTF6DMVAP]
uses: [063D5Z2C70, 0W4FSW1TVB, B9CHNGJV5K, 0M0SNKZ482, 096AHMB3P4, 027KDW2K72]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_normal_form
    locator: A proof
  - url: https://en.wikipedia.org/wiki/Jordan_normal_form
    locator: Uniqueness
---

## Proof

We build a basis of chains by induction on $n = \dim V$, lifting the chains of the image $\operatorname{im} N$ by one step, and then we count blocks with the ranks of the powers.
A *chain basis* for $N$ is a basis made of the vectors $N^j u_i$ with $0 \le j < k_i$, where $N^{k_i} u_i = 0$.

1. If $n = 0$, the empty family is a chain basis. Let $n \ge 1$, and assume that every nilpotent map on a space of smaller dimension has a chain basis.
2. Let $m$ be the least integer with $N^m = 0$, which exists because $N$ is [[nilpotent|063D5Z2C70]]. Since $V \ne 0$ we have $m \ge 1$, and a vector $v$ with $N^{m-1} v \ne 0$ gives a nonzero vector $N^{m-1} v$ in $\ker N$.
3. Let $W = \operatorname{im} N$. Then $N(W) \subseteq W$, the restriction $N|_W$ is nilpotent, and $\dim W < n$ by step 2 and the [[rank-nullity theorem|0W4FSW1TVB]].
4. By the induction hypothesis, $W$ has a chain basis for $N|_W$: vectors $w_1, \dots, w_t$ and lengths $\ell_1, \dots, \ell_t \ge 1$ with $N^{\ell_i} w_i = 0$, such that the $N^j w_i$ with $0 \le j < \ell_i$ form a basis of $W$.
5. Each $w_i$ lies in $W = \operatorname{im} N$, so we can choose $u_i \in V$ with $N u_i = w_i$. Then $N^{\ell_i + 1} u_i = N^{\ell_i} w_i = 0$.
6. The vectors $N^{\ell_i} u_i = N^{\ell_i - 1} w_i$, for $i = 1, \dots, t$, lie in $\ker N$, since $N^{\ell_i} w_i = 0$. They are independent, since they belong to the basis of $W$ in step 4.
7. Extend them to a basis of $\ker N$ by vectors $z_1, \dots, z_q$. Then $\dim \ker N = t + q$.
8. Let $\mathcal{S}$ be the family of the vectors $N^j u_i$ with $1 \le i \le t$ and $0 \le j \le \ell_i$, together with $z_1, \dots, z_q$. It has $\sum_i (\ell_i + 1) + q = \dim W + t + q$ members, and this is $\dim \operatorname{im} N + \dim \ker N = n$ by rank-nullity.
9. To show that $\mathcal{S}$ is independent, let $\sum_{i, j} a_{ij} N^j u_i + \sum_p c_p z_p = 0$ and apply $N$. The $z_p$ and the $N^{\ell_i} u_i$ go to $0$, and $N^{j+1} u_i = N^j w_i$, so $\sum_i \sum_{j < \ell_i} a_{ij} N^j w_i = 0$.
10. These $N^j w_i$ are the basis of $W$ from step 4, so $a_{ij} = 0$ for all $j < \ell_i$.
11. What remains is $\sum_i a_{i \ell_i} N^{\ell_i} u_i + \sum_p c_p z_p = 0$. This is a relation in the basis of $\ker N$ from step 7, so these coefficients are $0$ as well.
12. By steps 8 to 11, $\mathcal{S}$ is a basis of $V$ with $n$ members. It is a chain basis: the chain of $u_i$ has length $\ell_i + 1$, and the chain of $z_p$ has length $1$, since $N z_p = 0$. This completes the induction, and we sort the chains so that $k_1 \ge \dots \ge k_s$.
13. In one chain $N^{k-1} u, \dots, N u, u$, call the vectors $f_1, \dots, f_k$. Then $N f_1 = N^k u = 0$ and $N f_p = f_{p-1}$ for $p \ge 2$, which is the action of $J_k(0)$ on the standard basis by [[part 1 of the lemma on Jordan blocks|B9CHNGJV5K]].
14. Each chain spans an $N$-invariant subspace, and $V$ is the direct sum of these subspaces, so the matrix of $N$ is the [[block diagonal matrix|0M0SNKZ482]] $J_{k_1}(0) \oplus \dots \oplus J_{k_s}(0)$. This proves part 1.
15. The basis has $\sum_i k_i$ vectors and $\dim V = n$, so $\sum_i k_i = n$. This proves part 2.
16. By part 5 of the lemma on Jordan blocks, $\dim \ker J_k(0)^j = \min(j, k)$. The kernel of a power of a block diagonal matrix is the direct sum of the kernels of the powers of the blocks, so $\dim \ker N^j = \sum_i \min(j, k_i)$.
17. Hence $\dim \ker N^j - \dim \ker N^{j-1} = \sum_i \bigl(\min(j, k_i) - \min(j - 1, k_i)\bigr)$. Each term is $1$ when $k_i \ge j$ and $0$ otherwise, so the difference is the number $b_j$ of $i$ with $k_i \ge j$.
18. By rank-nullity, $\dim \ker N^j = n - r_j$, so $b_j = r_{j-1} - r_j$. The number of $i$ with $k_i = j$ is $b_j - b_{j+1} = r_{j-1} - 2 r_j + r_{j+1}$. This proves part 3.
19. The ranks $r_j$ depend only on $N$, not on a basis, and by step 18 they fix the number of blocks of each size, so they fix the partition.
20. [[Similar|027KDW2K72]] nilpotent matrices have the same ranks of all powers, since $(P^{-1} N P)^j = P^{-1} N^j P$. Conversely, two nilpotent matrices with the same partition are similar to the same block diagonal matrix by part 1, so they are similar to each other. This proves part 4.
21. Column $j$ of the [[Young diagram|096AHMB3P4]] of $(k_1, \dots, k_s)$ has one box for each row of length at least $j$, so it has $b_j = r_{j-1} - r_j$ boxes by step 18. This proves part 5.

## Idea

The image of $N$ is a smaller space, so it has a chain basis by induction.
Each chain of the image is pulled back one step, so that it starts one level higher, and new chains of length one fill up the rest of the kernel.
For uniqueness, the ranks of the powers count how many chains reach each level, and those counts fix the partition.

## Variants

The module proof views $V$ as an $F[x]$-module that a power of $x$ kills, and it applies the structure theorem for finitely generated modules over a principal ideal domain, which gives $V \cong \bigoplus_i F[x]/(x^{k_i})$.
Another elementary proof works from the top down.
It chooses a complement of $\ker N^{m-1}$ in $V$, pushes it down with $N$, and at each level $\ker N^j$ adds a complement of $\ker N^{j-1} + N(\ker N^{j+1})$.
