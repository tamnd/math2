---
tag: 75VVYAZBK3
kind: proof
name: Proof of Grassmann's formula by extending a basis of the intersection
msc: [15A03]
proves: 06HTJNCMPA
uses: [0RMKABS2S5, 0V33SPH7RR, 05G2G0P224, 0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6, 0EPTJA5QV4, 0QW084460E, 0M4SXE5WW3, 0WK0Y8RH1M]
sources:
  - url: https://proofwiki.org/wiki/Grassmann%27s_Formula
---

## Proof

We extend a basis of $U \cap W$ to bases of $U$ and of $W$, and show that together they give a basis of $U + W$.

1. By [[intersection of subspaces|0V33SPH7RR]], $U \cap W$ is a [[linear subspace|0EPTJA5QV4]] of $U$. By [[the dimension of a subspace|0QW084460E]], it is finite-dimensional. Let $k = \dim(U \cap W)$ and let $z_1, \dots, z_k$ be a [[basis|0VTQTPQGAV]] of it.
2. The family $z_1, \dots, z_k$ is [[linearly independent|0EVHJFTG9Z]] in $U$. By [[the extension to a basis|0M4SXE5WW3]], it extends to a basis of $U$.
3. By the [[dimension theorem|0WK0Y8RH1M]], this basis has $\dim U$ vectors. Write it as $z_1, \dots, z_k, u_1, \dots, u_r$ with $r = \dim U - k$.
4. In the same way, $W$ has a basis $z_1, \dots, z_k, w_1, \dots, w_s$ with $s = \dim W - k$.
5. Let $\mathcal{B}$ be the family $z_1, \dots, z_k, u_1, \dots, u_r, w_1, \dots, w_s$. Each vector of $\mathcal{B}$ lies in $U$ or in $W$, so it lies in the [[sum|0RMKABS2S5]] $U + W$, as $u = u + 0$ or $w = 0 + w$.
6. The set $U + W$ is a linear subspace of $V$. It contains $0 = 0 + 0$. Also $(u + w) + (u' + w') = (u + u') + (w + w')$ and $a(u + w) = au + aw$, with $u, u' \in U$ and $w, w' \in W$.
7. Let $u + w \in U + W$ with $u \in U$ and $w \in W$. By step 3, $u$ is a combination of the $z_i$ and the $u_j$. By step 4, $w$ is a combination of the $z_i$ and the $w_l$.
8. So $u + w$ is a linear combination of $\mathcal{B}$. Hence $\mathcal{B}$ [[spans|0BJKVF90Z6]] $U + W$.
9. For independence, let $\sum_{i} a_i z_i + \sum_{j} b_j u_j + \sum_{l} c_l w_l = 0$ with coefficients in $F$. Let $y = \sum_{l} c_l w_l$.
10. Then $y \in W$. Also $y = -\sum_{i} a_i z_i - \sum_{j} b_j u_j \in U$. So $y \in U \cap W$.
11. By step 1, $y = \sum_{i} d_i z_i$ for some $d_i \in F$. So $\sum_{i} d_i z_i - \sum_{l} c_l w_l = 0$.
12. The family $z_1, \dots, z_k, w_1, \dots, w_s$ is linearly independent by step 4. So all $c_l = 0$, and $y = 0$.
13. Then $\sum_{i} a_i z_i + \sum_{j} b_j u_j = 0$. The family of step 3 is linearly independent, so all $a_i = 0$ and all $b_j = 0$.
14. By steps 8 to 13, $\mathcal{B}$ is a basis of $U + W$. So $U + W$ is finite-dimensional.
15. A linearly independent family has no repeated vectors, since $1 \cdot x - 1 \cdot x = 0$ is a nontrivial relation. So $\mathcal{B}$ has $k + r + s$ distinct vectors, and $\dim(U + W) = k + r + s$ by the definition of [[dimension|05G2G0P224]].
16. By steps 1, 3, 4 and 15, $\dim(U + W) + \dim(U \cap W) = (k + r + s) + k = (k + r) + (k + s) = \dim U + \dim W$.

## Idea

Vectors in both subspaces get counted twice in $\dim U + \dim W$. Starting from a basis of $U \cap W$ and extending it inside $U$ and inside $W$ makes this double count explicit. The combined family is a basis of $U + W$, because any relation among it forces a vector of $W$ into $U \cap W$, where it must vanish.
