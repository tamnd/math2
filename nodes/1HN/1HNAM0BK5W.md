---
tag: 1HNAM0BK5W
kind: proof
name: Proof that the order of a permutation is the lcm of its cycle lengths
msc: [20B30]
proves: 0DH7HMXP9F
uses: [0RJMNEN3BJ, 0YWDAZPRPQ, 0ZKPH2BD1T, 0PVG1CRAJN, 0JPYSD5E0B, 09S5SN35DJ]
sources:
  - url: https://en.wikipedia.org/wiki/Permutation
    locator: Order of a permutation
---

## Proof

We compute $\sigma^m$ on the points of each cycle separately.

1. Let $\sigma \in S_n$, the [[symmetric group|0RJMNEN3BJ]], and let $\sigma = c_1 c_2 \cdots c_r$ be its [[decomposition into disjoint cycles|0YWDAZPRPQ]], where $c_i$ has length $k_i$ and set of moved points $M_i$.
2. Here $\operatorname{lcm}(k_1, \dots, k_r)$ is the least positive integer that each $k_i$ divides, as for the [[least common multiple|09S5SN35DJ]] of two integers. It exists, since $k_1 k_2 \cdots k_r$ is such an integer.
3. A [[cycle|0ZKPH2BD1T]] of length $1$ is the identity. Removing such a factor changes neither $\sigma$ nor the lcm. So we may assume $k_i \ge 2$, and then $|M_i| = k_i$.
4. Let $c = (a_0\ a_1\ \dots\ a_{k-1})$ be a cycle of length $k$. By induction on $m \ge 0$, $c^m(a_p) = a_q$, where $q$ is the remainder of $p + m$ on division by $k$. Also $c^m$ fixes every other point.
5. Let $m \ge 1$. If $k \mid m$, step 4 gives $c^m(a_p) = a_p$ for each $p$, so $c^m$ is the identity.
6. Conversely, if $c^m$ is the identity, then $c^m(a_0) = a_0$. By step 4 and since the $a_p$ are distinct, the remainder of $m$ on division by $k$ is $0$. So $k \mid m$.
7. Let $z \in M_i$. If $c_i(c_i(z)) = c_i(z)$, then $c_i(z) = z$ since $c_i$ is [[injective|0PVG1CRAJN]]. This is false, so $c_i(z) \in M_i$.
8. For $j \ne i$, the cycle $c_j$ fixes each point of $M_i$, since the sets of moved points are disjoint.
9. In $c_1 \cdots c_r(z)$ with $z \in M_i$, the factors after $c_i$ fix $z$, then $c_i$ gives $c_i(z) \in M_i$, and the factors before $c_i$ fix it. So $\sigma(z) = c_i(z)$.
10. A point outside all $M_i$ is fixed by each $c_j$, so it is fixed by $\sigma$.
11. By steps 7, 9 and 10 and induction on $m \ge 0$, $\sigma^m(z) = c_i^m(z)$ for $z \in M_i$. Also $\sigma^m$ fixes each point outside all $M_i$.
12. Let $m \ge 1$. By step 11, $\sigma^m$ is the identity exactly when $c_i^m(z) = z$ for each $i$ and each $z \in M_i$.
13. Since $c_i^m$ fixes the points outside $M_i$, this holds exactly when each $c_i^m$ is the identity. By steps 5 and 6, this holds exactly when $k_i \mid m$ for each $i$.
14. The [[order|0JPYSD5E0B]] of $\sigma$ is the least $m \ge 1$ with $\sigma^m$ the identity. By steps 2 and 13, it is $\operatorname{lcm}(k_1, \dots, k_r)$.
15. If $r = 0$ after step 3, then $\sigma$ is the identity, of order $1$, and the lcm of an empty list is $1$ by step 2.

## Idea

Each cycle of $\sigma$ moves its own points, and on those points $\sigma^m$ acts like the $m$-th power of that cycle. A cycle of length $k$ returns to the identity exactly at the multiples of $k$. So $\sigma^m$ is the identity exactly when $m$ is a common multiple of all the cycle lengths, and the least such $m$ is the lcm.
