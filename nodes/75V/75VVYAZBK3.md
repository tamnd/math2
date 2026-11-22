---
tag: 75VVYAZBK3
kind: proof
name: Proof of Grassmann's formula by extending a basis of the intersection
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 06HTJNCMPA
methods: [01XM7JEKHY, 0NTF6DMVAP]
uses: [0RMKABS2S5, 0V33SPH7RR, 05G2G0P224, 0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6, 0EPTJA5QV4, 0QW084460E, 0M4SXE5WW3, 0WK0Y8RH1M]
sources:
  - book: isbn:9783031410253
    locator: Section 2C
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Facts
---

## Proof

We extend one basis of $U \cap W$ in two directions, to a basis of $U$ and to a basis of $W$, and we show that the pieces together form a basis of $U + W$.

1. By the theorem on the [[intersection of subspaces|0V33SPH7RR]], $U \cap W$ is a [[linear subspace|0EPTJA5QV4]] of $U$. By the theorem on the [[dimension of a subspace|0QW084460E]], it is finite-dimensional. Let $k = \dim(U \cap W)$, and let $z_1, \dots, z_k$ be a [[basis|0VTQTPQGAV]] of $U \cap W$.
2. The list $z_1, \dots, z_k$ is [[linearly independent|0EVHJFTG9Z]] in $U$, so by the [[extension theorem|0M4SXE5WW3]] it extends to a basis of $U$. By the [[dimension theorem|0WK0Y8RH1M]] this basis has $\dim U$ vectors, so we can write it as $z_1, \dots, z_k, u_1, \dots, u_r$ with $r = \dim U - k$.
3. In the same way, $W$ has a basis $z_1, \dots, z_k, w_1, \dots, w_s$ with $s = \dim W - k$.
4. Let $\mathcal{B}$ be the list $z_1, \dots, z_k, u_1, \dots, u_r, w_1, \dots, w_s$. Each of its vectors lies in $U$ or in $W$, and so in the [[sum|0RMKABS2S5]] $U + W$, since $u = u + 0$ and $w = 0 + w$.
5. To see that $\mathcal{B}$ [[spans|0BJKVF90Z6]] $U + W$, take $u + w$ with $u \in U$ and $w \in W$. By step 2, $u$ is a combination of the $z_i$ and the $u_j$, and by step 3, $w$ is a combination of the $z_i$ and the $w_l$, so $u + w$ is a combination of $\mathcal{B}$.
6. For independence, suppose that $\sum_i a_i z_i + \sum_j b_j u_j + \sum_l c_l w_l = 0$, and put $y = \sum_l c_l w_l$.
7. Then $y \in W$, and also $y = -\sum_i a_i z_i - \sum_j b_j u_j \in U$. So $y \in U \cap W$, and by step 1, $y = \sum_i d_i z_i$ for some scalars $d_i$.
8. This gives $\sum_i d_i z_i - \sum_l c_l w_l = 0$. The list of step 3 is independent, so every $c_l = 0$ (and every $d_i = 0$), and therefore $y = 0$.
9. Now $\sum_i a_i z_i + \sum_j b_j u_j = 0$. The list of step 2 is independent, so every $a_i = 0$ and every $b_j = 0$.
10. By steps 5 to 9, $\mathcal{B}$ is a basis of $U + W$, so $U + W$ is finite-dimensional with $\dim(U + W) = k + r + s$. An independent list has no repeated vector, since $x - x = 0$ would be a nontrivial relation, so $\mathcal{B}$ really has $k + r + s$ distinct vectors.
11. By steps 1 to 3 and 10,
$$\dim(U + W) + \dim(U \cap W) = (k + r + s) + k = (k + r) + (k + s) = \dim U + \dim W.$$

## Idea

The vectors of $U \cap W$ are counted twice in $\dim U + \dim W$.
Starting from a basis of $U \cap W$ and extending it inside $U$ and inside $W$ makes this double count visible: the $z_i$ appear in both bases, the $u_j$ and $w_l$ in only one.
The combined list spans $U + W$ for an easy reason, and it is independent because a relation would push a combination of the $w_l$ into $U \cap W$, where only the $z_i$ live.
So the sum has a basis of $k + r + s$ vectors, and the count is done.

## Variants

The [[rank-nullity theorem|0W4FSW1TVB]] gives a shorter proof.
The map $U \times W \to U + W$, $(u, w) \mapsto u - w$, is linear and onto, and its kernel $\{(z, z) : z \in U \cap W\}$ has dimension $\dim(U \cap W)$, so $\dim U + \dim W = \dim(U + W) + \dim(U \cap W)$.
A proof by quotient spaces counts both sides of $(U + W)/W \cong U/(U \cap W)$.
