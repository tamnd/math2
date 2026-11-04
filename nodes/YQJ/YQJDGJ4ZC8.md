---
tag: YQJDGJ4ZC8
kind: proof
name: Proof of the product formula for the generating function of a sum of independent random variables
msc: ["60E05"]
proves: 0REMT01N36
uses: [0Z8PSSAVBA, 0XCE070V8B, 0VGMEBVW1M, 0WF4EJP91W]
sources:
  - url: https://en.wikipedia.org/wiki/Probability_generating_function
    locator: Functions of independent random variables
---

## Proof

We argue by induction on the number of terms, using the mass function of a sum and a Cauchy product of series.

1. Let $X_1, \dots, X_n$ be [[independent|0XCE070V8B]] random variables with values in $\N = \set{0, 1, 2, \dots}$. Let $p_i(k) = P(X_i = k)$ be the [[mass function|0WF4EJP91W]] of $X_i$.
2. For $1 \le m \le n$, let $S_m = X_1 + \dots + X_m$. Then $S_m$ takes values in $\N$, and $S_n = S$.
3. Fix a complex number $z$ with $\abs{z} \le 1$. For a variable $V$ with values in $\N$, the [[generating function|0Z8PSSAVBA]] is $G_V(z) = \sum_{k \ge 0} P(V = k) z^k$.
4. The events $\set{V = k}$ for $k \in \N$ are disjoint with union $\Omega$. By countable additivity of the [[probability measure|0VGMEBVW1M]], $\sum_k P(V = k) = 1$.
5. Hence $\sum_k \abs{P(V = k) z^k} \le 1$. So the series for $G_V(z)$ converges absolutely.
6. We prove $G_{S_m}(z) = \prod_{i=1}^m G_{X_i}(z)$ by induction on $m$. For $m = 1$, both sides are $G_{X_1}(z)$.
7. Let $2 \le m \le n$ and assume the claim for $m - 1$. Fix integers $l, r \ge 0$.
8. Let $T$ be the finite set of tuples $(k_1, \dots, k_{m-1}) \in \N^{m-1}$ with $k_1 + \dots + k_{m-1} = l$. For $k \in T$, let $E_k = \set{X_1 = k_1, \dots, X_{m-1} = k_{m-1}}$.
9. Since each $X_i$ takes values in $\N$, the event $\set{S_{m-1} = l}$ is the disjoint union of the events $E_k$ for $k \in T$.
10. The definition of independence with $J = \set{1, \dots, m}$ gives $P(E_k \cap \set{X_m = r}) = p_1(k_1) \cdots p_{m-1}(k_{m-1}) \, p_m(r)$.
11. The same definition with $J = \set{1, \dots, m-1}$ gives $P(E_k) = p_1(k_1) \cdots p_{m-1}(k_{m-1})$.
12. Summing steps 10 and 11 over $k \in T$ with finite additivity gives $P(S_{m-1} = l, X_m = r) = P(S_{m-1} = l) \, p_m(r)$.
13. For $j \in \N$, the event $\set{S_m = j}$ is the disjoint union over $l = 0, \dots, j$ of $\set{S_{m-1} = l, X_m = j - l}$.
14. By step 12 and finite additivity, $P(S_m = j) = \sum_{l=0}^{j} P(S_{m-1} = l) \, p_m(j - l)$.
15. Let $a_l = P(S_{m-1} = l) z^l$ and $b_r = p_m(r) z^r$. Let $\alpha = \sum_l a_l = G_{S_{m-1}}(z)$ and $\beta = \sum_r b_r = G_{X_m}(z)$.
16. Let $c_j = P(S_m = j) z^j$. Since $z^j = z^l z^{j-l}$, step 14 gives $c_j = \sum_{l=0}^{j} a_l b_{j-l}$.
17. Fix $N \ge 0$. Then $\sum_{j=0}^N c_j$ is the sum of $a_l b_r$ over pairs with $l + r \le N$. The product $\left(\sum_{l \le N} a_l\right)\left(\sum_{r \le N} b_r\right)$ is the sum over pairs with $l, r \le N$.
18. Their difference $D_N$ is the sum of $a_l b_r$ over pairs with $l, r \le N$ and $l + r > N$. Each such pair has $l > N/2$ or $r > N/2$.
19. By step 5, $\sum_l \abs{a_l} \le 1$ and $\sum_r \abs{b_r} \le 1$. So $\abs{D_N} \le \sum_{l > N/2} \abs{a_l} + \sum_{r > N/2} \abs{b_r}$.
20. The right side of step 19 is a sum of two tails of convergent series. So $D_N \to 0$ as $N \to \infty$.
21. The product of partial sums in step 17 tends to $\alpha \beta$. By step 20, $\sum_{j=0}^N c_j \to \alpha\beta$ as well.
22. So $G_{S_m}(z) = \sum_j c_j = G_{S_{m-1}}(z) \, G_{X_m}(z)$. By the induction hypothesis, this equals $\prod_{i=1}^m G_{X_i}(z)$.
23. For $m = n$, this gives $G_S(z) = G_{X_1}(z) \, G_{X_2}(z) \cdots G_{X_n}(z)$.

## Idea

The mass function of a sum of two independent variables is the convolution of their mass functions. Multiplying two power series also convolves their coefficients. So the generating function of the sum is the product of the generating functions.
