---
tag: 4G6RX0APF1
kind: proof
name: Proof of the Lebesgue number lemma by a finite cover of balls
msc: ["54E45"]
proves: 040CFNJEAP
uses: [0QPHW703PV, 0NVPNC12JY, 0A6YRNZB2R, 0DC3MPR7C9, 0B2305GNAZ, 0692CGQF00, 01M6CW9VM6]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue%27s_number_lemma
    locator: Proof
---

## Proof

We cover $X$ by balls whose doubles lie in members of the cover, and take the smallest radius of a finite subcover.

1. If $X$ is empty, there is no nonempty $A \subseteq X$, and the [[diameter|0692CGQF00]] is only defined for nonempty sets. So $\delta = 1$ works. From now on let $X$ be nonempty.
2. Let $p \in X$. Since the $U_i$ cover $X$, choose $i(p) \in I$ with $p \in U_{i(p)}$.
3. The set $U_{i(p)}$ is open in the [[metric topology|0A6YRNZB2R]]. So there is $r_p > 0$ with $B(p, 2 r_p) \subseteq U_{i(p)}$.
4. The [[open balls|0DC3MPR7C9]] $B(p, r_p)$, for $p \in X$, are [[open|0B2305GNAZ]] and each contains its centre. So they form an [[open cover|0NVPNC12JY]] of $X$.
5. Since $X$ is [[compact|0QPHW703PV]], finitely many of these balls cover $X$. Call their centres $p_1, \ldots, p_n$, with $n \ge 1$, and write $r_k = r_{p_k}$.
6. Let $\delta = \min(r_1, \ldots, r_n)$. Then $\delta > 0$.
7. Let $A \subseteq X$ have $\operatorname{diam}(A) < \delta$. The diameter is only defined for nonempty sets, so pick $a \in A$.
8. By step 5, $a \in B(p_k, r_k)$ for some $k$, so $d(a, p_k) < r_k$.
9. Let $y \in A$. Then $d(y, a) \le \operatorname{diam}(A) < \delta \le r_k$.
10. By the [[triangle inequality|01M6CW9VM6]], $d(y, p_k) \le d(y, a) + d(a, p_k) < r_k + r_k = 2 r_k$.
11. So $A \subseteq B(p_k, 2 r_k)$. By step 3, $A \subseteq U_{i(p_k)}$. Thus $\delta$ is a Lebesgue number of the cover.

## Idea

Around each point choose a ball such that the ball of twice the radius fits inside one set of the cover. Compactness leaves finitely many such balls, so the smallest radius is positive. A set of smaller diameter sits in one small ball around a point of it, and hence in the double ball.
