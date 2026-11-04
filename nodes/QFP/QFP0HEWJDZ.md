---
tag: QFP0HEWJDZ
kind: proof
name: Proof of the epsilon-delta form of the limit of a function
msc: [26A03]
proves: 0GBZDAFPX8
uses: [0TXTSEMHR5, 0TK8Y3J5RW]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_function
    locator: (ε, δ)-definition of limit
---

## Proof

We compare open intervals with symmetric intervals $(c - r, c + r)$.

1. Let $D \subseteq \R$, let $f \colon D \to \R$, let $a$ be a limit point of $D$, and let $L \in \R$.
2. Claim: if $V = (p, q)$ is an [[open interval|0TK8Y3J5RW]] containing a point $c$, then $r = \min(c - p, q - c)$ is positive and $(c - r, c + r) \subseteq V$.
3. Proof of the claim: $p < c < q$ gives $r > 0$. If $\abs{y - c} < r$, then $y > c - r \ge p$ and $y < c + r \le q$, so $y \in V$.
4. Assume first that $\lim_{x \to a} f(x) = L$ in the sense of the [[definition|0TXTSEMHR5]]. Let $\varepsilon > 0$.
5. The set $V = (L - \varepsilon, L + \varepsilon)$ is an open interval containing $L$. The definition gives an open interval $U$ containing $a$ with $f(x) \in V$ for all $x \in U \cap D$ with $x \ne a$.
6. By the claim, there is $\delta > 0$ with $(a - \delta, a + \delta) \subseteq U$.
7. Let $x \in D$ with $0 < \abs{x - a} < \delta$. Then $x \in U \cap D$ and $x \ne a$. So $f(x) \in V$, that is, $\abs{f(x) - L} < \varepsilon$.
8. So the epsilon-delta condition holds.
9. Conversely, assume the epsilon-delta condition. Let $V$ be an open interval containing $L$.
10. By the claim, there is $\varepsilon > 0$ with $(L - \varepsilon, L + \varepsilon) \subseteq V$. The condition gives $\delta > 0$ for this $\varepsilon$.
11. Let $U = (a - \delta, a + \delta)$. This is an open interval containing $a$.
12. Let $x \in U \cap D$ with $x \ne a$. Then $0 < \abs{x - a} < \delta$, so $\abs{f(x) - L} < \varepsilon$. Hence $f(x) \in (L - \varepsilon, L + \varepsilon) \subseteq V$.
13. So $\lim_{x \to a} f(x) = L$ in the sense of the definition. This proves the equivalence.

## Idea

The definition speaks of arbitrary open intervals, the condition of symmetric ones of radius $\varepsilon$ or $\delta$. Every symmetric interval is an open interval, and every open interval around a point contains a symmetric one. So the two conditions say the same thing.
