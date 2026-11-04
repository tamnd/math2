---
tag: ARGNNXKHMN
kind: proof
name: Proof that compactness and sequential compactness agree in metric spaces
msc: ["54E45"]
proves: 0K8SGQSV7G
uses: [063W5JMY85, 00R0X1WGPX, 0CARW59WD2, 0P6PMJB4MA, 0A26X79RTB, 0DC3MPR7C9, 0B2305GNAZ, 06JYPJ4WHH, 0R8J3ZQMJS, 01M6CW9VM6]
sources:
  - url: https://proofwiki.org/wiki/Sequentially_Compact_Metric_Space_is_Compact
    locator: Proof 2
  - url: https://en.wikipedia.org/wiki/Sequentially_compact_space
    locator: Examples and properties
---

## Proof

We prove each implication. The second one goes through a finite net of balls and a Lebesgue number, both proved here for sequentially compact sets.

1. Let $(X, d)$ be a [[metric space|063W5JMY85]] and let $K \subseteq X$. Write $B(x, r)$ for the [[open ball|0DC3MPR7C9]]. [[Open balls are open|0B2305GNAZ]].
2. Assume $K$ is [[compact|00R0X1WGPX]]. Let $(x_n)$ be a sequence in $K$. Suppose, for a contradiction, that no [[subsequence|0R8J3ZQMJS]] [[converges|06JYPJ4WHH]] to a point of $K$.
3. Claim: each $y \in K$ has a radius $r_y > 0$ such that the set $I_y = \set{n : x_n \in B(y, r_y)}$ is finite.
4. Proof of the claim: otherwise, for each $r > 0$ there are infinitely many $n$ with $x_n \in B(y, r)$. Then choose $n_1$ with $x_{n_1} \in B(y, 1)$.
5. Given $n_k$, choose $n_{k+1} > n_k$ with $x_{n_{k+1}} \in B(y, 1/(k+1))$. This is possible, since infinitely many indices qualify.
6. Then $d(x_{n_k}, y) < 1/k$ for all $k$, so $x_{n_k} \to y \in K$. This contradicts step 2 and proves the claim.
7. The open balls $B(y, r_y)$ with $y \in K$ cover $K$. By [[compactness via open covers|0P6PMJB4MA]], there are $y_1, \ldots, y_m \in K$ with $K \subseteq B(y_1, r_{y_1}) \cup \cdots \cup B(y_m, r_{y_m})$.
8. Each $x_n$ lies in $K$, so in one of these balls. Hence every index $n$ lies in the finite set $I_{y_1} \cup \cdots \cup I_{y_m}$.
9. But there are infinitely many indices $n$. This contradiction shows that $K$ is [[sequentially compact|0CARW59WD2]].
10. Now assume $K$ is sequentially compact. If $K = \emptyset$, then $K$ is compact, since the empty subfamily covers it. So assume $K \ne \emptyset$.
11. Claim A: for each $\varepsilon > 0$ there are finitely many points $a_1, \ldots, a_p \in K$ with $K \subseteq B(a_1, \varepsilon) \cup \cdots \cup B(a_p, \varepsilon)$.
12. Proof of Claim A: suppose it fails for some $\varepsilon$. Pick $a_1 \in K$. Given $a_1, \ldots, a_p$, their balls do not cover $K$, so pick $a_{p+1} \in K$ outside all of them.
13. Then $d(a_p, a_q) \ge \varepsilon$ for all $p \ne q$. By sequential compactness, some subsequence $(a_{p_k})$ converges to a point $a \in K$.
14. For large $k$, $d(a_{p_k}, a) < \varepsilon / 2$. For two such distinct indices $k < l$, the [[triangle inequality|01M6CW9VM6]] gives $d(a_{p_k}, a_{p_l}) < \varepsilon$. This contradicts step 13.
15. Claim B: let $(U_i)_{i \in I}$ be open sets of $X$ that cover $K$. Then there is $\delta > 0$ such that for each $x \in K$, the ball $B(x, \delta)$ lies in some $U_i$.
16. Proof of Claim B: suppose not. Then for each $n \ge 1$ there is $x_n \in K$ such that $B(x_n, 1/n)$ lies in no $U_i$.
17. By sequential compactness, a subsequence $(x_{n_k})$ converges to some $a \in K$. Then $a \in U_j$ for some $j$.
18. By the description of [[open sets of a metric space|0A26X79RTB]], there is $r > 0$ with $B(a, r) \subseteq U_j$.
19. Choose $k$ with $d(x_{n_k}, a) < r / 2$ and $1/n_k < r / 2$. This is possible, since $n_k \ge k$ for the strictly increasing indices $n_k \ge 1$.
20. Let $z \in B(x_{n_k}, 1/n_k)$. Then $d(z, a) \le d(z, x_{n_k}) + d(x_{n_k}, a) < r / 2 + r / 2 = r$. So $B(x_{n_k}, 1/n_k) \subseteq B(a, r) \subseteq U_j$.
21. This contradicts the choice of $x_{n_k}$ in step 16, and proves Claim B.
22. Now let $(U_i)_{i \in I}$ be open sets of $X$ that cover $K$. Take $\delta$ from Claim B, and apply Claim A with $\varepsilon = \delta$ to get $a_1, \ldots, a_p \in K$.
23. For each $j$, Claim B gives an index $i_j$ with $B(a_j, \delta) \subseteq U_{i_j}$.
24. Then $K \subseteq B(a_1, \delta) \cup \cdots \cup B(a_p, \delta) \subseteq U_{i_1} \cup \cdots \cup U_{i_p}$.
25. So each cover of $K$ by open sets of $X$ has a finite subcover. By compactness via open covers, $K$ is compact.

## Idea

Suppose a sequence in a compact set had no convergent subsequence. Then each point has a ball that holds only finitely many terms, and finitely many such balls cover $K$, which is absurd.
Conversely, sequential compactness gives two uniform facts: $K$ is covered by finitely many $\varepsilon$-balls, and one radius $\delta$ fits each small ball into a set of the cover. Together they give a finite subcover.
