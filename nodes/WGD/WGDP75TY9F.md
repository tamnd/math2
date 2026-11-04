---
tag: WGDP75TY9F
kind: proof
name: Proof that a set is compact iff it is complete and totally bounded
msc: ["54E45"]
proves: 054Q5PW5GX
uses: [0P6PMJB4MA, 0WE5BBHGM6, 08EWT7J0SC, 0T2WYDTRP2, 0MCK8K2D7Z, 06JYPJ4WHH, 0DC3MPR7C9, 0B2305GNAZ, 0A6YRNZB2R, 0692CGQF00, 01M6CW9VM6, 0A3GWZ86AY]
sources:
  - url: https://www.math.ucla.edu/~tao/resource/general/121.1.00s/compact.pdf
    locator: Theorem 3.5 and Theorem 6.1
---

## Proof

We prove the two directions separately. Throughout, the metric on $K$ is the [[subspace metric|0T2WYDTRP2]], so distances in $K$ are distances in $X$. We test compactness of $K$ with [[open covers by open subsets of X|0P6PMJB4MA]].

First, let $K$ be compact. We show that $K$ is totally bounded.

1. Fix a real $\varepsilon > 0$. The [[open balls|0DC3MPR7C9]] $B(y, \varepsilon / 3)$, for $y \in K$, are [[open|0B2305GNAZ]] in $X$ and cover $K$. So finitely many of them cover $K$.
2. For $z, w \in B(y, \varepsilon / 3)$, the [[triangle inequality|01M6CW9VM6]] gives $d(z, w) < 2 \varepsilon / 3$. So each ball has [[diameter|0692CGQF00]] at most $2 \varepsilon / 3 < \varepsilon$.
3. Thus $K$ is covered by finitely many sets of diameter less than $\varepsilon$, for each $\varepsilon > 0$. So $K$ is [[totally bounded|0WE5BBHGM6]].

Next, let $K$ be compact. We show that $K$ is complete.

4. Let $(x_n)$ be a [[Cauchy sequence|0MCK8K2D7Z]] of points of $K$. Suppose, for a contradiction, that it [[converges|06JYPJ4WHH]] to no point of $K$. Then $K$ is nonempty, since it contains $x_1$.
5. Let $y \in K$. Since $(x_n)$ does not converge to $y$, there is $\varepsilon_y > 0$ such that for each $N$ some $n \ge N$ has $d(x_n, y) \ge 2 \varepsilon_y$.
6. Since $(x_n)$ is Cauchy, there is $N_y$ with $d(x_m, x_n) < \varepsilon_y$ for all $m, n \ge N_y$.
7. By step 5, choose $m \ge N_y$ with $d(x_m, y) \ge 2 \varepsilon_y$. For each $n \ge N_y$, the triangle inequality gives $d(x_n, y) \ge d(x_m, y) - d(x_m, x_n) > \varepsilon_y$.
8. So the ball $B(y, \varepsilon_y)$ contains no $x_n$ with $n \ge N_y$.
9. The balls $B(y, \varepsilon_y)$, for $y \in K$, are open and cover $K$. By compactness, finitely many cover $K$, say those with centres $y_1, \ldots, y_p$.
10. Let $N = \max(N_{y_1}, \ldots, N_{y_p})$. The point $x_N$ lies in $K$, so $x_N \in B(y_j, \varepsilon_{y_j})$ for some $j$. Since $N \ge N_{y_j}$, this contradicts step 8.
11. Hence each Cauchy sequence in $K$ converges to a point of $K$, and $K$ is [[complete|08EWT7J0SC]].

Conversely, let $K$ be complete and totally bounded. We argue by contradiction.

12. Let $(U_i)_{i \in I}$ be open subsets of $X$ with $K \subseteq \bigcup_{i \in I} U_i$. Call a set $C \subseteq K$ bad when no finite subfamily of $(U_i)$ covers $C$. Suppose that $K$ is bad.
13. A bad set is nonempty, because the empty subfamily covers $\varnothing$.
14. Claim: if $C \subseteq K$ is bad and $\eta > 0$, then some bad $C' \subseteq C$ has $\operatorname{diam}(C') < \eta$. Indeed, total boundedness gives sets $A_1, \ldots, A_n$ of diameter less than $\eta$ that cover $K$.
15. Then $C = (C \cap A_1) \cup \cdots \cup (C \cap A_n)$. If no $C \cap A_k$ were bad, joining finitely many finite subfamilies would cover $C$. So some $C' = C \cap A_k$ is bad, and $\operatorname{diam}(C') \le \operatorname{diam}(A_k) < \eta$.
16. Let $C_0 = K$. For $n \ge 1$, apply step 14 to $C_{n-1}$ with $\eta = 1/n$. We get bad sets $K \supseteq C_1 \supseteq C_2 \supseteq \cdots$ with $\operatorname{diam}(C_n) < 1/n$.
17. By step 13, choose $x_n \in C_n$ for each $n \ge 1$. For $m \ge n$, both $x_m$ and $x_n$ lie in $C_n$, so $d(x_m, x_n) < 1/n$.
18. Let $\varepsilon > 0$. Since [[the reals are Archimedean|0A3GWZ86AY]], there is $N$ with $N \varepsilon > 1$. Then $d(x_m, x_n) < 1/N < \varepsilon$ for $m, n \ge N$. So $(x_n)$ is Cauchy.
19. Since $K$ is complete, $x_n \to x$ for some $x \in K$. Choose $i$ with $x \in U_i$.
20. The set $U_i$ is open in the [[metric topology|0A6YRNZB2R]]. So there is $r > 0$ with $B(x, r) \subseteq U_i$.
21. Choose $n$ with $1/n < r/2$ and $d(x_n, x) < r/2$. This is possible by the Archimedean property and $x_n \to x$.
22. Let $z \in C_n$. Then $d(z, x) \le d(z, x_n) + d(x_n, x) < 1/n + r/2 < r$. So $C_n \subseteq B(x, r) \subseteq U_i$.
23. Thus the single set $U_i$ covers $C_n$, and $C_n$ is not bad. This contradicts step 16.
24. So some finite subfamily of $(U_i)$ covers $K$. By [[compactness via open covers|0P6PMJB4MA]], $K$ is compact.

## Idea

Compactness gives finite covers by small balls, which is total boundedness. A Cauchy sequence with no limit stays away from each point, so the balls witnessing this would need infinitely many members. For the converse, a cover with no finite subcover has a "bad" piece at every scale. The bad pieces shrink to a point, and the open set around that point swallows a whole bad piece.
