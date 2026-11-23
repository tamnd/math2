---
tag: JYXQF7533K
kind: proof
name: Proof of the comparison of Cantor normal forms
msc: ["03E10", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
proves: DXKWBFWCE0
uses: [KAEDCQ8RM6, 6GD30FGYDZ]
methods: [0ASJVEFA9J, 0WCP0PVET6, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_arithmetic
    locator: Cantor normal form
---

## Proof

We bound a normal form above by the next power of $\omega$ after its leading exponent, and then compare two normal forms at their first difference.
We use these facts of [[ordinal arithmetic|KAEDCQ8RM6]], for ordinals $\alpha, \beta, \gamma, \delta$ and natural numbers $c, d$.

- (F1) Addition is associative.
- (F2) Addition is strictly increasing in its right argument: $\beta < \gamma$ implies $\alpha + \beta < \alpha + \gamma$.
- (F3) $\alpha + \beta \ge \alpha$, by (F2) with $0 \le \beta$.
- (F4) $\omega^\beta \cdot (c + 1) = \omega^\beta \cdot c + \omega^\beta$, by the definition of multiplication.
- (F5) Multiplication on the left by $\omega^\beta > 0$ is strictly increasing in its right argument, so $c < d$ gives $\omega^\beta c < \omega^\beta d$, and $c < \omega$ gives $\omega^\beta c < \omega^\beta \omega$.
- (F6) $\omega^\beta \cdot \omega = \omega^{\beta + 1}$, and $\beta + 1 \le \delta$ gives $\omega^{\beta + 1} \le \omega^\delta$.

First, three lemmas.

1. Lemma 1: if $\beta < \delta$ and $c$ is a natural number, then $\omega^\beta c < \omega^\delta$.
   By (F5) and (F6), $\omega^\beta c < \omega^\beta \omega = \omega^{\beta + 1} \le \omega^\delta$, since $\beta + 1 \le \delta$.
2. Lemma 2: if $\sigma$ is a normal form whose exponents are all less than $\delta$, then $\sigma < \omega^\delta$.
   We prove this by [[induction|0ASJVEFA9J]] on the number $k$ of terms of $\sigma$.
3. For $k = 0$, $\sigma = 0 < \omega^\delta$, since $\omega^\delta \ge 1$.
4. For $k \ge 1$, write $\sigma = \omega^{\beta_1} c_1 + t$, where $t$ is the normal form of the other $k - 1$ terms.
   The exponents of $t$ are less than $\beta_1$, so $t < \omega^{\beta_1}$ by the induction hypothesis.
5. By (F2) and (F4), $\sigma < \omega^{\beta_1} c_1 + \omega^{\beta_1} = \omega^{\beta_1}(c_1 + 1)$, and by Lemma 1 with $\beta_1 < \delta$ this is less than $\omega^\delta$.
6. Lemma 3: if $\sigma$ is a normal form with leading pair $(\beta_1, c_1)$, then $\sigma \ge \omega^{\beta_1} c_1 \ge \omega^{\beta_1} \ge 1$, by (F3) and (F5).

Now let $\alpha$ and $\alpha'$ have the term lists $(\beta_i, c_i)_{i \le k}$ and $(\beta'_i, c'_i)_{i \le m}$.

7. If the term lists are equal, then $\alpha$ and $\alpha'$ are the same sum, so $\alpha = \alpha'$.
8. If the lists differ, let $j$ be the least index with $j > k$, or $j > m$, or $(\beta_j, c_j) \ne (\beta'_j, c'_j)$.
   Let $\pi$ be the sum of the common terms with index less than $j$.
9. By (F1), $\alpha = \pi + \rho$ and $\alpha' = \pi + \rho'$, where $\rho$ and $\rho'$ are the normal forms of the terms with index at least $j$.
10. By (F2), $\rho < \rho'$ gives $\alpha < \alpha'$, and $\rho' < \rho$ gives $\alpha' < \alpha$, so it is enough to compare $\rho$ and $\rho'$.
11. Case A: $j > k$ and $j \le m$, which is condition 1 of the theorem.
    Then $\rho = 0$ and $\rho' \ge 1$ by Lemma 3, so $\alpha < \alpha'$.
12. Case B: $j \le \min(k, m)$ and $\beta_j < \beta'_j$.
    All exponents of $\rho$ are at most $\beta_j < \beta'_j$, so Lemma 2 gives $\rho < \omega^{\beta'_j}$, and Lemma 3 gives $\omega^{\beta'_j} \le \rho'$, so $\alpha < \alpha'$.
13. Case C: $j \le \min(k, m)$, $\beta_j = \beta'_j = \beta$ and $c_j < c'_j$.
    Write $\rho = \omega^\beta c_j + t$; the exponents of $t$ are less than $\beta$, so $t < \omega^\beta$ by Lemma 2.
14. By (F2), (F4) and (F5), $\rho < \omega^\beta c_j + \omega^\beta = \omega^\beta (c_j + 1) \le \omega^\beta c'_j$, and Lemma 3 gives $\omega^\beta c'_j \le \rho'$, so $\alpha < \alpha'$.
15. Cases B and C together are condition 2 of the theorem, so each of conditions 1 and 2 gives $\alpha < \alpha'$.
16. The remaining possibilities in step 8 are the cases A, B and C with $\alpha$ and $\alpha'$ exchanged, and steps 11 to 14 then give $\alpha' < \alpha$.
17. Suppose $\alpha < \alpha'$.
    The lists are not equal by step 7, and the exchanged cases do not hold, since they give $\alpha' < \alpha$.
    So case A, B or C holds, and condition 1 or 2 is true.
18. For the corollary, if the term lists differ, steps 15 and 16 give $\alpha < \alpha'$ or $\alpha' < \alpha$, so $\alpha \ne \alpha'$.

Steps 15 and 17 prove the equivalence, and step 18 proves the corollary. $\blacksquare$

## Idea

Split off the common leading terms, which do not affect the comparison because addition is strictly increasing on the right.
At the first difference, the whole rest of the smaller side is bounded by one power of $\omega$, by Lemma 2.
The larger side reaches that power with its first remaining term alone.
So the first difference decides the order, exactly as in a dictionary.

## Variants

We can also prove uniqueness of the normal form first, by division with remainder, and then derive the comparison rule.
The proof above goes the other way and gets uniqueness as a corollary.
The same proof works for normal forms to any base $\beta \ge 2$ in place of $\omega$, with coefficients $0 < c_i < \beta$.
Lemma 1 then uses $\beta^\gamma c < \beta^{\gamma + 1}$ for $c < \beta$.
