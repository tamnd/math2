---
tag: AQAKY2RTJZ
kind: proof
name: Proof of Eisenstein's criterion
msc: ["12E05"]
proves: 02BPKD7TMD
uses: [00X2A9G9W3, 0QFV5Y1Z5X, 0SP14DZN0G, 000JFQGDXG, 0QKVE1GD9A, 055HT85T3S, 05K3J8J8T2, 051VYKA1EX, 0SN0MAEKYX, 0T233AZ1GE, 019NFGFPR5]
methods: [0J0XBKG64S]
sources:
  - url: https://www.jmilne.org/math/CourseNotes/FT.pdf
    locator: Proposition 1.16
  - url: https://en.wikipedia.org/wiki/Eisenstein%27s_criterion
    locator: Basic proof
---

## Proof

1. Let $f = a_n x^n + \dots + a_0 \in \Z[x]$ and the [[prime|0SN0MAEKYX]] $p$ satisfy the three hypotheses. Since $p \nmid a_n$, we have $a_n \ne 0$, so $\deg f = n \ge 1$.
2. The ring $\Z$ is a [[Euclidean domain|000JFQGDXG]], hence a [[principal ideal domain|0QKVE1GD9A]], hence a [[unique factorisation domain|055HT85T3S]]. Its [[field of fractions|05K3J8J8T2]] is $\Q$.
3. Let $c > 0$ be the greatest common divisor of $a_0, \dots, a_n$, and let $f_0 = f / c \in \Z[x]$. Write $f_0 = \sum_i a'_i x^i$ with $a'_i = a_i / c$.
4. The polynomial $f_0$ is [[primitive|0SP14DZN0G]]. Indeed, if an integer $r$ with $\abs{r} \ge 2$ divides every $a'_i$, then $c \abs{r}$ divides every $a_i$, which contradicts the choice of $c$.
5. Since $c \mid a_n$ and $p \nmid a_n$, we have $p \nmid c$. For $i < n$, $p \mid a_i = c \, a'_i$, so $p \mid a'_i$ by [[Euclid's lemma|051VYKA1EX]].
6. Also $p \nmid a'_n$, since $a'_n$ divides $a_n$. And $p^2 \nmid a'_0$, since otherwise $p^2$ would divide $c \, a'_0 = a_0$. So $f_0$ satisfies the three hypotheses.
7. In $\Q[x]$, $f = c f_0$ and $c$ is a [[unit|019NFGFPR5]]. So $f$ is [[irreducible|00X2A9G9W3]] in $\Q[x]$ if and only if $f_0$ is.
8. By [[Gauss's lemma|0QFV5Y1Z5X]] and Step 4, it is enough to show that $f_0$ is irreducible in $\Z[x]$. We argue by contradiction.
9. The units of $\Z[x]$ are $\pm 1$. Indeed, if $u v = 1$, then $\deg u = \deg v = 0$ by the [[degree of a product|0T233AZ1GE]], and $u, v \in \Z$ with $u v = 1$.
10. Since $\deg f_0 = n \ge 1$, the polynomial $f_0$ is nonzero and not a unit. Suppose that $f_0 = g h$ with $g, h \in \Z[x]$ not units.
11. If $g$ were a constant $r$, then $r$ would divide every coefficient of $f_0$. By Step 4, $r = \pm 1$, a unit. So $\deg g \ge 1$, and in the same way $\deg h \ge 1$.
12. Write $g = b_s x^s + \dots + b_0$ and $h = c_t x^t + \dots + c_0$ with $b_s c_t \ne 0$. Then $s, t \ge 1$ and $s + t = n$, so $s < n$. Set $b_j = 0$ for $j > s$ and $c_j = 0$ for $j > t$.
13. We have $a'_0 = b_0 c_0$. Since $p \mid a'_0$, Euclid's lemma gives $p \mid b_0$ or $p \mid c_0$. Both cannot hold, because $p^2 \nmid a'_0$. Say $p \mid b_0$ and $p \nmid c_0$.
14. We show by induction on $i$ that $p \mid b_i$ for $0 \le i \le s$. The case $i = 0$ is Step 13.
15. Let $1 \le i \le s$ and assume $p \mid b_j$ for all $j < i$. Comparing coefficients of $x^i$ gives $a'_i = b_i c_0 + \sum_{j=0}^{i-1} b_j c_{i-j}$.
16. Since $i \le s < n$, we have $p \mid a'_i$ by Step 5. Each term $b_j c_{i-j}$ with $j < i$ is divisible by $p$. So $p \mid b_i c_0$.
17. Since $p \nmid c_0$, Euclid's lemma gives $p \mid b_i$. This completes the induction.
18. In particular $p \mid b_s$. The leading coefficient of $f_0$ is $a'_n = b_s c_t$, so $p \mid a'_n$. This contradicts Step 6.
19. So $f_0$ is irreducible in $\Z[x]$. By Steps 7 and 8, $f$ is irreducible in $\Q[x]$.

## Idea

After Gauss's lemma, a factorisation over $\Q$ becomes one over $\Z$. The prime $p$ divides exactly one of the two constant terms. Comparing coefficients one degree at a time pushes $p$ through all coefficients of that factor, up to its leading coefficient. Then $p$ would divide the leading coefficient of $f$, which is excluded.
