---
tag: TP6CV9DS8T
kind: proof
name: Proof of the Baire category theorem by nested closed balls
msc: ["54E52"]
proves: 0A7KGAYHGV
uses: [063W5JMY85, 08EWT7J0SC, 0D5KR33H7X, 0CNQXVBHCX, 0G5AV9Q4RR, 0C38S0KMJK, 0HAZEFH137, 0A26X79RTB, 0DC3MPR7C9, 0B2305GNAZ, 05DSV40EB9, 0YS40B38JD, 09GQ3ZTQJ9, 0MCK8K2D7Z, 06JYPJ4WHH, 01M6CW9VM6]
sources:
  - url: https://en.wikipedia.org/wiki/Baire_category_theorem
    locator: Proof
---

## Proof

We argue by contradiction. We build a nested sequence of closed balls with radii tending to $0$, and use completeness to get a point in all of them.

1. Let $(X, d)$ be a [[complete metric space|08EWT7J0SC]]. Let $F_1, F_2, \ldots$ be [[closed|0G5AV9Q4RR]] subsets of $X$ with $\operatorname{int} F_n = \emptyset$ for each $n$. Here $\operatorname{int}$ is the [[interior|0C38S0KMJK]].
2. Let $U_n = X \setminus F_n$. Each $U_n$ is open, since $F_n$ is closed.
3. Claim: each nonempty open set $V$ meets each $U_n$. Otherwise $V \subseteq F_n$. The [[interior is the largest open subset|0HAZEFH137]], so $V \subseteq \operatorname{int} F_n = \emptyset$, a contradiction.
4. Let $W = \operatorname{int} \bigcup_n F_n$. By the same statement, $W$ is open and $W \subseteq \bigcup_n F_n$. Assume, for a contradiction, that $W \ne \emptyset$.
5. By step 3, the set $W \cap U_1$ is nonempty. It is open, since a [[topology|0CNQXVBHCX]] is closed under finite intersections. Pick $x_1$ in it.
6. By the description of [[open sets of a metric space|0A26X79RTB]], there is $s > 0$ with $B(x_1, s) \subseteq W \cap U_1$. Here $B$ is the [[open ball|0DC3MPR7C9]]. Let $r_1 = \min(s / 2, 1/2)$.
7. Let $\bar{B}(x, r)$ be the [[closed ball|05DSV40EB9]]. Since $r_1 < s$, we get $\bar{B}(x_1, r_1) \subseteq B(x_1, s) \subseteq W \cap U_1$.
8. Suppose $x_n$ and $r_n > 0$ are chosen. The set $B(x_n, r_n) \cap U_{n+1}$ is open, since [[open balls are open|0B2305GNAZ]]. It is nonempty by step 3.
9. As in steps 6 and 7, choose $x_{n+1}$ and $r_{n+1}$ with $0 < r_{n+1} \le 1/(n+1)$ and $\bar{B}(x_{n+1}, r_{n+1}) \subseteq B(x_n, r_n) \cap U_{n+1}$.
10. Write $\bar{B}_n = \bar{B}(x_n, r_n)$. By steps 7 and 9, $\bar{B}_{n+1} \subseteq \bar{B}_n$, $\bar{B}_n \subseteq U_n$, $\bar{B}_1 \subseteq W$ and $r_n \le 1/n$ for all $n$.
11. By step 10, $\bar{B}_m \subseteq \bar{B}_n$ for $m \ge n$. So $x_m \in \bar{B}_n$ for all $m \ge n$.
12. For $m, p \ge n$, the [[triangle inequality|01M6CW9VM6]] gives $d(x_m, x_p) \le d(x_m, x_n) + d(x_n, x_p) \le 2 r_n \le 2/n$.
13. Given $\varepsilon > 0$, choose $n > 2/\varepsilon$. Step 12 then shows that $(x_m)$ is a [[Cauchy sequence|0MCK8K2D7Z]].
14. Since $X$ is complete, $(x_m)$ [[converges|06JYPJ4WHH]] to some $x \in X$.
15. Fix $n$. The tail $(x_m)_{m \ge n}$ also converges to $x$, and all its terms lie in $\bar{B}_n$ by step 11.
16. [[Closed balls are closed|0YS40B38JD]], and [[closed sets contain their limits|09GQ3ZTQJ9]]. So $x \in \bar{B}_n$ for every $n$.
17. By steps 10 and 16, $x \in W$ and $x \in U_n$ for every $n$. So $x \in W$ but $x \notin \bigcup_n F_n$.
18. This contradicts $W \subseteq \bigcup_n F_n$ from step 4. So $\operatorname{int} \bigcup_n F_n = \emptyset$.
19. This holds for every countable family of closed sets with empty interior. So $X$ is a [[Baire space|0D5KR33H7X]].

## Idea

A nonempty open set inside $\bigcup_n F_n$ would leave room to shrink a ball away from $F_1$, then from $F_2$, and so on.
The centres of these nested balls form a Cauchy sequence, and completeness gives a limit. That limit lies in the open set but in no $F_n$.
