---
tag: 56PQG6K7YT
kind: proof
name: Proof of the epsilon-delta form of continuity
msc: [26A15]
proves: 0W8YHHGCJG
uses: [0EEE2CZB2A, 0TK8Y3J5RW]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Weierstrass and Jordan definitions (epsilon–delta) of continuous functions
---

## Proof

We compare open intervals with symmetric intervals $(c - r, c + r)$.

1. Let $D \subseteq \R$, let $f \colon D \to \R$, and let $a \in D$.
2. Claim: if $V = (p, q)$ is an [[open interval|0TK8Y3J5RW]] containing a point $c$, then $r = \min(c - p, q - c)$ is positive and $(c - r, c + r) \subseteq V$.
3. Proof of the claim: $p < c < q$ gives $r > 0$. If $\abs{y - c} < r$, then $y > c - r \ge p$ and $y < c + r \le q$, so $y \in V$.
4. Assume first that $f$ is [[continuous at|0EEE2CZB2A]] $a$. Let $\varepsilon > 0$.
5. The set $V = (f(a) - \varepsilon, f(a) + \varepsilon)$ is an open interval containing $f(a)$. The definition gives an open interval $U$ containing $a$ with $f(x) \in V$ for all $x \in U \cap D$.
6. By the claim, there is $\delta > 0$ with $(a - \delta, a + \delta) \subseteq U$.
7. Let $x \in D$ with $\abs{x - a} < \delta$. Then $x \in U \cap D$, so $f(x) \in V$, that is, $\abs{f(x) - f(a)} < \varepsilon$.
8. So the epsilon-delta condition holds.
9. Conversely, assume the epsilon-delta condition. Let $V$ be an open interval containing $f(a)$.
10. By the claim, there is $\varepsilon > 0$ with $(f(a) - \varepsilon, f(a) + \varepsilon) \subseteq V$. The condition gives $\delta > 0$ for this $\varepsilon$.
11. Let $U = (a - \delta, a + \delta)$, an open interval containing $a$.
12. Let $x \in U \cap D$. Then $\abs{x - a} < \delta$, so $\abs{f(x) - f(a)} < \varepsilon$. Hence $f(x) \in V$.
13. So $f$ is continuous at $a$ in the sense of the definition. This proves the equivalence.

## Idea

The definition speaks of arbitrary open intervals, the condition of symmetric ones of radius $\varepsilon$ or $\delta$. Every symmetric interval is an open interval, and every open interval around a point contains a symmetric one. So the two conditions are the same.
