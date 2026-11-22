---
tag: 7TTA01BTBJ
kind: proof
name: Proof of the Eckart-Young-Mirsky theorem by a dimension count and a weighted sum
msc: [15A18, 15A60]
topics: [SS4EVPKT3A]
audience: ug2
proves: JJT6GC055J
methods: [0NTF6DMVAP]
uses: [000NPTMX6J, 0ZTEH055YF, K33BQX70N0, 0W4FSW1TVB, 06HTJNCMPA, 0BVTDM872V, 09DZ8CD1AK, 0Q8HZTJC7G]
sources:
  - url: https://en.wikipedia.org/wiki/Low-rank_approximation
    locator: Proof of Eckart–Young–Mirsky theorem (for spectral norm)
  - url: https://en.wikipedia.org/wiki/Low-rank_approximation
    locator: Proof of Eckart–Young–Mirsky theorem (for Frobenius norm)
---

## Proof

We compute the errors of $A_k$ in the singular bases, bound the operator norm error of any $B$ by finding a vector in its null space, and bound the Frobenius error by projecting $A$ onto the column space of $B$.

By the full form of the [[singular value decomposition|000NPTMX6J]], we extend $u_1, \dots, u_r$ to an orthonormal basis $u_1, \dots, u_m$ of $\C^m$, and $v_1, \dots, v_r$ to an orthonormal basis $v_1, \dots, v_n$ of $\C^n$.
Since $v_i^* v_j = 0$ for $i \ne j$ and $v_j^* v_j = 1$, we get $A v_j = \sigma_j u_j$ for $j \le r$ and $A v_j = 0$ for $j > r$.

*The rank of $A_k$.*

1. In the same way, $A_k v_j = \sigma_j u_j$ for $j \le k$ and $A_k v_j = 0$ for $j > k$. So the column space of $A_k$ is spanned by the independent vectors $u_1, \dots, u_k$, and $\operatorname{rank} A_k = k$.

*A lemma on the Frobenius norm.*

2. Let $M$ be an $m \times n$ matrix, and let $\rho_i = M^* e_i \in \C^n$, so that row $i$ of $M$ is $\rho_i^*$. By the [[definition of the Frobenius norm|K33BQX70N0]], $\norm{M}_F^2 = \sum_i \norm{\rho_i}^2$.
3. Entry $i$ of $M v_j$ is $\rho_i^* v_j$, so $\sum_j \norm{M v_j}^2 = \sum_i \sum_j \abs{\rho_i^* v_j}^2$.
4. By [[coordinates in an orthonormal basis|09DZ8CD1AK]] and the [[Pythagorean theorem|0BVTDM872V]], $\sum_j \abs{v_j^* \rho_i}^2 = \norm{\rho_i}^2$. With steps 2 and 3 this gives $\norm{M}_F^2 = \sum_j \norm{M v_j}^2$ for every orthonormal basis $v_1, \dots, v_n$ of $\C^n$.
5. The entries of $M^*$ have the same absolute values as the entries of $M$, so $\norm{M^*}_F = \norm{M}_F$.

*Part 1, the operator norm.*

6. Let $x = \sum_j c_j v_j$. By the formulas for $A v_j$ and $A_k v_j$,
$$(A - A_k) x = \sum_{j = k+1}^r \sigma_j c_j u_j.$$
7. The $u_j$ are orthonormal, so the Pythagorean theorem and $\sigma_j \le \sigma_{k+1}$ for $j > k$ give
$$\norm{(A - A_k) x}^2 = \sum_{j = k+1}^r \sigma_j^2 \abs{c_j}^2 \le \sigma_{k+1}^2 \sum_j \abs{c_j}^2 = \sigma_{k+1}^2 \norm{x}^2.$$
8. For the unit vector $x = v_{k+1}$, step 6 gives $\norm{(A - A_k) x} = \sigma_{k+1}$. With step 7 and the [[definition of the operator norm|0ZTEH055YF]], $\norm{A - A_k}_2 = \sigma_{k+1}$.
9. Now let $B$ have rank at most $k$. By the [[rank-nullity theorem|0W4FSW1TVB]], the null space $N$ of $B$ has dimension at least $n - k$.
10. Let $W$ be the span of $v_1, \dots, v_{k+1}$, of dimension $k + 1$. Since $N + W \subseteq \C^n$, the [[dimension formula for sums of subspaces|06HTJNCMPA]] gives
$$\dim(N \cap W) = \dim N + \dim W - \dim(N + W) \ge (n - k) + (k + 1) - n = 1.$$
11. So $N \cap W$ contains a unit vector $x = \sum_{j \le k+1} c_j v_j$, with $B x = 0$ and $\sum_{j \le k+1} \abs{c_j}^2 = 1$.
12. Then $(A - B) x = A x = \sum_{j \le k+1} \sigma_j c_j u_j$, and since $\sigma_j \ge \sigma_{k+1}$ for $j \le k + 1$,
$$\norm{A x}^2 = \sum_{j \le k+1} \sigma_j^2 \abs{c_j}^2 \ge \sigma_{k+1}^2.$$
13. By the definition of the operator norm, $\norm{A - B}_2 \ge \norm{(A - B) x} \ge \sigma_{k+1}$. This proves part 1.

*Part 2, the Frobenius norm.*

14. Step 4 with $M = A - A_k$, together with step 6, gives $\norm{A - A_k}_F^2 = \sum_j \norm{(A - A_k) v_j}^2 = \sum_{j = k+1}^r \sigma_j^2$. In the same way, $\norm{A}_F^2 = \sum_{j \le r} \sigma_j^2$.
15. Let $B$ have rank $q \le k$, let $w_1, \dots, w_q$ be an orthonormal basis of the column space of $B$, and let $P = \sum_{l \le q} w_l w_l^*$. For $y \in \C^m$, the vector $P y = \sum_l (w_l^* y) w_l$ lies in the column space and $w_l^* (y - P y) = 0$ for every $l$, so $P$ is the [[orthogonal projection|0Q8HZTJC7G]] onto the column space of $B$.
16. Let $a_j$ and $b_j$ be column $j$ of $A$ and of $B$. The vector $P a_j - b_j$ lies in the column space of $B$, and $a_j - P a_j$ is orthogonal to it, so the Pythagorean theorem gives
$$\norm{a_j - b_j}^2 = \norm{a_j - P a_j}^2 + \norm{P a_j - b_j}^2 \ge \norm{a_j - P a_j}^2.$$
17. The same theorem gives $\norm{a_j}^2 = \norm{a_j - P a_j}^2 + \norm{P a_j}^2$. The squared Frobenius norm is the sum of the squared lengths of the columns, so summing step 16 over $j$ gives $\norm{A - B}_F^2 \ge \norm{A}_F^2 - \norm{P A}_F^2$.
18. Extend $w_1, \dots, w_q$ to an orthonormal basis $w_1, \dots, w_m$ of $\C^m$. Then $P w_l = w_l$ for $l \le q$ and $P w_l = 0$ for $l > q$.
19. Since $P^* = P$, step 5 and then step 4 with $M = A^* P$ give $\norm{P A}_F^2 = \norm{A^* P}_F^2 = \sum_{l \le q} \norm{A^* w_l}^2$.
20. Since $A^* = \sum_{i \le r} \sigma_i v_i u_i^*$ and the $v_i$ are orthonormal, $\norm{A^* w_l}^2 = \sum_{i \le r} \sigma_i^2 \abs{u_i^* w_l}^2$.
21. So $\norm{P A}_F^2 = \sum_{i \le r} \sigma_i^2 c_i$, with weights $c_i = \sum_{l \le q} \abs{w_l^* u_i}^2$.
22. Since $P u_i = \sum_{l \le q} (w_l^* u_i) w_l$ with orthonormal $w_l$, the Pythagorean theorem gives $c_i = \norm{P u_i}^2$. Since $u_i - P u_i$ is orthogonal to $P u_i$, also $\norm{P u_i}^2 \le \norm{u_i}^2 = 1$, so $0 \le c_i \le 1$.
23. Coordinates in the orthonormal basis $u_1, \dots, u_m$ give $\sum_{i \le m} \abs{u_i^* w_l}^2 = \norm{w_l}^2 = 1$, so $\sum_{i \le r} c_i \le \sum_{l \le q} 1 = q \le k$.
24. We split the difference that we must bound:
$$\sum_{i \le r} \sigma_i^2 c_i - \sum_{i \le k} \sigma_i^2 = \sum_{i \le k} \sigma_i^2 (c_i - 1) + \sum_{k < i \le r} \sigma_i^2 c_i.$$
25. Let $k \ge 1$. In the first sum $c_i - 1 \le 0$ and $\sigma_i^2 \ge \sigma_k^2$, and in the second sum $c_i \ge 0$ and $\sigma_i^2 \le \sigma_k^2$. So the right side of step 24 is at most $\sigma_k^2 \left(\sum_{i \le r} c_i - k\right)$, which is at most $0$ by step 23. For $k = 0$ we have $q = 0$, so every $c_i = 0$ and the right side is $0$.
26. Steps 17, 21 and 25 give $\norm{A - B}_F^2 \ge \sum_{i \le r} \sigma_i^2 - \sum_{i \le k} \sigma_i^2 = \sum_{i = k+1}^r \sigma_i^2$, and with step 14 this proves part 2.

## Idea

In the singular bases, $A$ is a diagonal matrix with decreasing entries, and $A_k$ keeps the first $k$ of them.
For the operator norm, a matrix $B$ of rank $k$ kills a subspace of dimension $n - k$, and that subspace must meet the span of $v_1, \dots, v_{k+1}$, where $A$ stretches every vector by at least $\sigma_{k+1}$.
On such a vector, $A - B$ acts like $A$, so the error is at least $\sigma_{k+1}$.
For the Frobenius norm, the best matrix with a given column space is the projection $P A$.
Then the question becomes a sharing problem: give each $\sigma_i^2$ a weight between $0$ and $1$, with total at most $k$, and make the weighted sum as large as possible.
The best choice puts weight $1$ on the $k$ largest values, which is what $A_k$ does.

## Variants

A second proof of the Frobenius case starts from part 1.
Part 1 gives Weyl's inequality for singular values, $\sigma_{i+j-1}(A) \le \sigma_i(A - B) + \sigma_j(B)$.
For $\operatorname{rank} B \le k$ and $j = k + 1$ we have $\sigma_{k+1}(B) = 0$, so $\sigma_i(A - B) \ge \sigma_{k+i}(A)$ for each $i$.
Summing the squares gives $\norm{A - B}_F^2 \ge \sum_{i \ge 1} \sigma_{k+i}(A)^2$, which is part 2.
Inequalities of this kind belong to matrix analysis.

For real matrices the same proof works with real orthonormal bases and transposes in place of conjugate transposes.
