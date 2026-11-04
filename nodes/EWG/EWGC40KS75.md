---
tag: EWGC40KS75
kind: proof
name: Proof of the expectation of a product of independent random variables by simple functions
msc: [60A05]
proves: 05AW1G0WE1
uses: [0DCT0QZVQ1, 0E9502NT92, 0DKRR22AEQ, 0YVRNEDSVG, 0TK8Y3J5RW, 0BVHZXWKCD, 7WMBX7M4P6, 0VSB0XF4G7, GEA8H3228S, G2S6H789RG, 0734RSVF2V, 0P7PTC8DDE]
sources:
  - url: https://proofwiki.org/wiki/Expectation_of_Product_of_Independent_Random_Variables_is_Product_of_Expectations
---

## Proof

We prove the formula for nonnegative parts by approximation with simple functions and monotone convergence, then combine the parts.

1. Let $X$ and $Y$ be [[independent|0E9502NT92]] integrable real [[random variables|0DKRR22AEQ]] on a probability space $(\Omega, \mathcal{F}, P)$.
2. For a real number $u$ put $u^+ = \max(u, 0)$ and $u^- = \max(-u, 0)$. Then $u = u^+ - u^-$ and $\abs{u} = u^+ + u^-$.
3. For $n \ge 1$ and $u \ge 0$ let $\varphi_n(u) = \min\left(n, 2^{-n} \floor{2^n u}\right)$, where $\floor{\cdot}$ is the [[floor function|0YVRNEDSVG]].
4. The function $\varphi_n$ takes only the finitely many values $k 2^{-n}$ with $0 \le k \le n 2^n$. It is nondecreasing, and $0 \le \varphi_n(u) \le u$.
5. We have $\varphi_n(u) \le \varphi_{n+1}(u)$. Indeed $2 \floor{2^n u}$ is an integer at most $2^{n+1} u$, so it is at most $\floor{2^{n+1} u}$.
6. Dividing by $2^{n+1}$ gives $2^{-n} \floor{2^n u} \le 2^{-n-1} \floor{2^{n+1} u}$. Since also $n \le n + 1$, the minimum in step 3 does not decrease.
7. We have $\varphi_n(u) \to u$. For $n \ge u$ we get $\varphi_n(u) = 2^{-n} \floor{2^n u}$, and this lies in $(u - 2^{-n}, u]$.
8. Let $g$ be one of the maps $x \mapsto x^+$ and $x \mapsto x^-$ from $\R$ to $[0, \infty)$. Each is monotone, so $\varphi_n \circ g$ is monotone on $\R$.
9. Hence for each $c$ the set $\set{x \in \R : \varphi_n(g(x)) = c}$ is an [[interval|0TK8Y3J5RW]] or empty. If $x < z < y$ and the values at $x$ and $y$ equal $c$, monotonicity forces the value $c$ at $z$.
10. Every interval is a [[Borel set|0BVHZXWKCD]]. It is open or closed, or it is an open interval together with one closed endpoint.
11. Let $g$ and $h$ be maps as in step 8, let $U = g(X)$ and $V = h(Y)$, and assume $E[U] < \infty$ and $E[V] < \infty$. We show $E[UV] = E[U] \, E[V]$ in steps 12 to 17.
12. Let $U_n = \varphi_n(U)$, with distinct values $c_1, \dots, c_r$. By steps 9 and 10, $A_i = \set{U_n = c_i} = \set{X \in J_i}$ with Borel sets $J_i$. The $A_i$ are disjoint events covering $\Omega$.
13. In the same way, $V_n = \varphi_n(V)$ has distinct values $d_1, \dots, d_s$, taken on the disjoint events $B_j = \set{Y \in K_j}$ with Borel sets $K_j$.
14. So $U_n V_n = \sum_{i, j} c_i d_j \mathbf{1}_{A_i \cap B_j}$ is a nonnegative [[simple function|7WMBX7M4P6]], written with pairwise disjoint sets $A_i \cap B_j$ and [[indicator functions|0VSB0XF4G7]].
15. By the [[integral of a non-negative function|GEA8H3228S]] for simple functions, $E[U_n V_n] = \sum_{i, j} c_i d_j \, P(A_i \cap B_j)$. By independence, $P(A_i \cap B_j) = P(X \in J_i) \, P(Y \in K_j) = P(A_i) \, P(B_j)$.
16. So $E[U_n V_n] = \left(\sum_i c_i P(A_i)\right) \left(\sum_j d_j P(B_j)\right) = E[U_n] \, E[V_n]$, again by the formula for simple functions.
17. By steps 5 and 7, $U_n$ increases to $U$ and $V_n$ increases to $V$. Products of nondecreasing nonnegative sequences are nondecreasing, so $U_n V_n$ increases to $UV$.
18. By the [[monotone convergence theorem|G2S6H789RG]], $UV$ is measurable, and $E[U_n] \to E[U]$, $E[V_n] \to E[V]$ and $E[U_n V_n] \to E[UV]$.
19. The limits $E[U]$ and $E[V]$ are finite. By the [[limit of a product of sequences|0734RSVF2V]] and step 16, $E[UV] = E[U] \, E[V]$. This proves the claim of step 11.
20. Now $X^+ \le \abs{X}$, so every simple $s$ with $0 \le s \le X^+$ also satisfies $s \le \abs{X}$. By the supremum definition, $E[X^+] \le E[\abs{X}] < \infty$.
21. In the same way $E[X^-]$, $E[Y^+]$ and $E[Y^-]$ are finite, because $X$ and $Y$ are integrable.
22. For signs $\sigma, \tau \in \set{+, -}$ let $W_{\sigma\tau} = X^\sigma Y^\tau$. By steps 11 to 21, each $W_{\sigma\tau}$ is a nonnegative random variable with $E[W_{\sigma\tau}] = E[X^\sigma] \, E[Y^\tau] < \infty$. So each is integrable.
23. Expanding $(X^+ - X^-)(Y^+ - Y^-)$ gives $XY = W_{++} - W_{+-} - W_{-+} + W_{--}$ at every point of $\Omega$.
24. By [[linearity of expectation|0P7PTC8DDE]], applied three times, $XY$ is integrable and $E[XY] = E[W_{++}] - E[W_{+-}] - E[W_{-+}] + E[W_{--}]$.
25. By step 22, the right side is $E[X^+] E[Y^+] - E[X^+] E[Y^-] - E[X^-] E[Y^+] + E[X^-] E[Y^-]$.
26. This factors as $\left(E[X^+] - E[X^-]\right)\left(E[Y^+] - E[Y^-]\right)$. By the definition of [[expected value|0DCT0QZVQ1]], it equals $E[X] \, E[Y]$.

## Idea

For simple random variables built from events of the form $\set{X \in J}$ and $\set{Y \in K}$, independence turns the expectation of the product into a double sum that factors. Every nonnegative random variable is an increasing limit of such simple ones, and monotone convergence carries the identity to the limit. Splitting $X$ and $Y$ into positive and negative parts handles the general integrable case.
