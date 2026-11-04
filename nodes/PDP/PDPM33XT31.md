---
tag: PDPM33XT31
kind: proof
name: Proof of the decomposition of a permutation into disjoint cycles
msc: [20B30]
proves: 0YWDAZPRPQ
uses: [0RJMNEN3BJ, 0ZKPH2BD1T, 00DRK90Z6K, 01HT2CH8BH, 0CHQKZFK5S, 0PVG1CRAJN]
sources:
  - url: https://en.wikipedia.org/wiki/Permutation
    locator: Cycle notation
---

## Proof

We split $X$ into the orbits of the powers of $\sigma$. Each orbit with at least two points gives one cycle.

1. Let $X$ be a finite set and $\sigma \in \operatorname{Sym}(X)$, the [[symmetric group|0RJMNEN3BJ]]. Products are compositions, and $\sigma^m$ is defined for $m \in \mathbb{Z}$ with the [[laws of exponents|00DRK90Z6K]].
2. For distinct $a_0, \dots, a_{k-1} \in X$, the [[cycle|0ZKPH2BD1T]] $(a_0\ a_1\ \dots\ a_{k-1})$ sends $a_i$ to $a_{i+1}$ for $i < k-1$, sends $a_{k-1}$ to $a_0$, and fixes every other point.
3. For $x \in X$, let $O(x) = \{\sigma^m(x) : m \in \mathbb{Z}\}$. The relation "$y \in O(x)$" is reflexive ($m = 0$), symmetric ($x = \sigma^{-m}(y)$), and transitive ($\sigma^{m'}(\sigma^m(x)) = \sigma^{m+m'}(x)$).
4. So it is an equivalence relation, and the sets $O(x)$ are its classes. By [[equivalence classes form a partition|01HT2CH8BH]], the distinct sets $O(x)$ are pairwise disjoint and cover $X$.
5. Fix $x \in X$. Since $X$ is finite, $\sigma^i(x) = \sigma^j(x)$ for some $0 \le i < j$. Applying $\sigma^{-i}$ gives $\sigma^{j-i}(x) = x$. Let $k \ge 1$ be the least integer with $\sigma^k(x) = x$.
6. The points $\sigma^p(x)$ with $0 \le p < k$ are distinct. Indeed, $\sigma^i(x) = \sigma^j(x)$ with $0 \le i < j < k$ would give $\sigma^{j-i}(x) = x$ with $0 < j - i < k$.
7. Since $\sigma^k$ fixes $x$, so do its inverse $\sigma^{-k}$ and every power $\sigma^{qk}$ with $q \in \mathbb{Z}$.
8. Let $m \in \mathbb{Z}$. By the [[division algorithm|0CHQKZFK5S]], $m = qk + r$ with $0 \le r < k$. By step 7, $\sigma^m(x) = \sigma^r(\sigma^{qk}(x)) = \sigma^r(x)$.
9. By steps 6 and 8, $O(x) = \{x, \sigma(x), \dots, \sigma^{k-1}(x)\}$ has exactly $k$ elements. If $k = 1$, then $O(x) = \{x\}$ and $\sigma(x) = x$.
10. Let $k \ge 2$ and $c = (x\ \sigma(x)\ \dots\ \sigma^{k-1}(x))$. By steps 2 and 5, $c(z) = \sigma(z)$ for $z \in O(x)$. Also $c$ fixes each point outside $O(x)$ and moves each point of $O(x)$.
11. So $c$ is determined by the set $O = O(x)$: it equals $\sigma$ on $O$ and the identity outside $O$. Write $c_O$ for it.
12. Let $O_1, \dots, O_r$ be the distinct orbits with at least two points, and let $c_j = c_{O_j}$. By steps 4 and 10, the cycles $c_j$ have length at least $2$ and pairwise disjoint sets of moved points $O_j$.
13. Let $y \in X$ lie in a one-point orbit. By step 9, $\sigma(y) = y$. Each $c_j$ fixes $y$, since $y \notin O_j$. So $c_1 c_2 \cdots c_r(y) = y = \sigma(y)$.
14. Let $y \in O_j$. Then $\sigma(y) \in O_j$. For $i \ne j$, the cycle $c_i$ fixes each point of $O_j$, so it fixes $y$ and $\sigma(y)$.
15. In $c_1 \cdots c_r(y)$, the factors $c_i$ with $i > j$ act first and fix $y$. Then $c_j$ gives $\sigma(y)$, and the factors with $i < j$ fix it. So $c_1 \cdots c_r(y) = \sigma(y)$.
16. By steps 13 to 15, $\sigma = c_1 c_2 \cdots c_r$. When $r = 0$, this is the empty product, the identity. This proves existence.
17. For uniqueness, let $\sigma = d_1 \cdots d_s$ with cycles $d_l$ of length at least $2$ and pairwise disjoint sets of moved points $M_l$.
18. Let $z \in M_l$. If $d_l(d_l(z)) = d_l(z)$, then $d_l(z) = z$ because $d_l$ is [[injective|0PVG1CRAJN]]. This is false, so $d_l(z) \in M_l$.
19. For $i \ne l$, $d_i$ fixes each point of $M_l$. As in step 15, step 18 gives $\sigma(z) = d_l(z)$ for each $z \in M_l$.
20. Write $d_l = (b_0\ b_1\ \dots\ b_{t-1})$ with $t \ge 2$. By step 19, $\sigma^p(b_0) = b_p$ for $0 \le p < t$, and $\sigma^t(b_0) = b_0$.
21. Since the $b_p$ are distinct, the least $k \ge 1$ with $\sigma^k(b_0) = b_0$ is $t$. By steps 9 and 10, $O(b_0) = M_l$, and $c_{O(b_0)} = (b_0\ \sigma(b_0)\ \dots\ \sigma^{t-1}(b_0)) = d_l$.
22. So $M_l$ is one of the orbits $O_j$, and $d_l = c_j$. Distinct $l$ give distinct $j$, because the sets $M_l$ are nonempty and pairwise disjoint.
23. Conversely, let $y \in O_j$. By step 9, $\sigma(y) \ne y$, since $O_j$ has at least two points. If every $d_l$ fixed $y$, their product $\sigma$ would fix $y$.
24. So $y \in M_l$ for some $l$. By steps 4 and 21, $O_j = O(y) = M_l$, so $c_j = d_l$.
25. By steps 22 and 24, $l \mapsto j$ is a bijection with $d_l = c_j$. So the factors $d_1, \dots, d_s$ are $c_1, \dots, c_r$ in some order.

## Idea

Following $x, \sigma(x), \sigma^2(x), \dots$ must return to $x$, because $X$ is finite. The points visited form an orbit, and on it $\sigma$ acts as one cycle. The orbits do not overlap, so these cycles are disjoint and their product is $\sigma$. Any disjoint cycle decomposition must have the orbits as its supports, which gives uniqueness.
