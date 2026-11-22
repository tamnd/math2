---
tag: 3DT0AG8DFS
kind: proof
name: Proof of the dimension statement for orthogonal complements of a bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
proves: M2JH84VEY9
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [05Q4JD6XEH, 3ND2FNJ38Y, 00889YD15K, 0W4FSW1TVB, 0M4SXE5WW3, 0R8X9XA83A, 20A0K3KBZD, 06HTJNCMPA, 0WGAXEK99E, M0G958M917]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: General bilinear forms
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Proof

We write $W^\perp$ as the kernel of a linear map from $V$ to $W^*$, apply rank-nullity, and then decide when that map is surjective and when $W$ meets $W^\perp$.
Let $k = \dim W$.
Define $\rho \colon V \to W^*$ by letting $\rho(v)$ be the linear form $w \mapsto B(w, v)$ on $W$.

Part 1.

1. Each $\rho(v)$ is a linear form on $W$, because $B$ is linear in the first slot.
2. The map $\rho$ is linear, because $B$ is linear in the second slot, so $\rho(av + bv') = a\rho(v) + b\rho(v')$.
3. The kernel of $\rho$ is the set of $v$ with $B(w, v) = 0$ for all $w \in W$, which is $W^\perp$ by the [[definition|05Q4JD6XEH]].
4. The [[rank-nullity theorem|0W4FSW1TVB]] gives $n = \dim W^\perp + \dim \operatorname{im} \rho$.
5. The image lies in $W^*$, and $\dim W^* = k$ by the [[dimension of the dual space|00889YD15K]]. So $\dim \operatorname{im} \rho \le k$.
6. Steps 4 and 5 give $\dim W^\perp \ge n - k$, which is part 1.

Part 2.
Let $B$ be nondegenerate.

7. By the [[criteria for nondegeneracy|3ND2FNJ38Y]], the map $R_B \colon V \to V^*$, $v \mapsto B(\cdot, v)$, is an isomorphism.
8. Let $\psi \in W^*$. [[Extend a basis|0M4SXE5WW3]] $(w_1, \dots, w_k)$ of $W$ to a basis $(w_1, \dots, w_n)$ of $V$.
9. Since [[a linear map is fixed by its values on a basis|0R8X9XA83A]], there is $\varphi \in V^*$ with $\varphi(w_i) = \psi(w_i)$ for $i \le k$ and $\varphi(w_i) = 0$ for $i > k$. Then $\varphi$ restricted to $W$ is $\psi$.
10. By step 7, $\varphi = R_B(v)$ for some $v \in V$. Then $\rho(v)$ is the restriction of $R_B(v) = \varphi$ to $W$, which is $\psi$.
11. So $\rho$ is surjective, and $\dim \operatorname{im} \rho = k$. Step 4 now gives $\dim W^\perp = n - k$, which is part 2.

Part 3.
Let $B_W$ be the restriction of $B$ to $W \times W$.

12. The intersection $W \cap W^\perp$ is the set of $w \in W$ with $B(w', w) = 0$ for all $w' \in W$, which is the right radical of $B_W$.
13. By the criteria for nondegeneracy, applied to $B_W$ on the finite-dimensional space $W$, this right radical is $\{0\}$ exactly when $B_W$ is nondegenerate.
14. Let $B_W$ be nondegenerate. By step 13, $W \cap W^\perp = \{0\}$, so the sum $W + W^\perp$ is direct by the [[criteria for a direct sum|20A0K3KBZD]].
15. By the [[dimension formula for sums|06HTJNCMPA]] and part 1, $\dim(W + W^\perp) = k + \dim W^\perp - 0 \ge k + (n - k) = n$.
16. A [[subspace of full dimension is the whole space|0WGAXEK99E]], so $W + W^\perp = V$, and $V = W \oplus W^\perp$.
17. Conversely, let $V = W \oplus W^\perp$. Then $W \cap W^\perp = \{0\}$, and step 13 shows that $B_W$ is nondegenerate.

Part 4.
Let $B$ be nondegenerate and [[reflexive|M0G958M917]].

18. Let $w \in W$ and $v \in W^\perp$. Then $B(w, v) = 0$, and reflexivity gives $B(v, w) = 0$.
19. This holds for every $v \in W^\perp$, so $w \in (W^\perp)^\perp$. Hence $W \subseteq (W^\perp)^\perp$.
20. Part 2 applied to $W^\perp$ and then to $W$ gives $\dim (W^\perp)^\perp = n - \dim W^\perp = n - (n - k) = k$.
21. So $W$ is a subspace of $(W^\perp)^\perp$ of the same finite dimension, and by the reason of step 16, $W = (W^\perp)^\perp$.

This proves all four parts.

## Idea

The complement $W^\perp$ is the kernel of a linear map from $V$ to $W^*$, and $W^*$ has dimension $\dim W$, so rank-nullity gives the inequality at once.
For a nondegenerate form the map is onto: every linear form on $W$ extends to $V$, and every linear form on $V$ comes from a vector.
The direct sum question then reduces to whether $W$ meets $W^\perp$, and that intersection is exactly the radical of the form restricted to $W$.
Part 4 is the usual trick of one inclusion plus equal dimensions.

## Variants

Part 2 also has a proof with matrices.
Write a basis of $W$ as the columns of an $n \times k$ matrix $C$ of rank $k$, and let $A$ be the matrix of $B$.
Then $v$ lies in $W^\perp$ exactly when $C^{\mathsf{T}} A y = 0$ for its coordinate column $y$, so $W^\perp$ is the null space of the $k \times n$ matrix $C^{\mathsf{T}} A$.
When $A$ is invertible, $C^{\mathsf{T}} A$ has the rank $k$ of $C^{\mathsf{T}}$, and rank-nullity gives $\dim W^\perp = n - k$.
