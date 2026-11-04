---
tag: H8A67Z5ZDB
kind: proof
name: Proof of Hölder's inequality for sums
msc: [26D15]
proves: 0BKDAGMGX9
uses: [07VHQ31EYJ, 0TV07AQT62, 0P9BNBW2W3, 0RKW2X63YR, 0J7PHRBNNS, 0E8HNVBCSP, 0GMV7GP8W0]
sources:
  - url: https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality
    locator: Proof of Hölder's inequality
---

## Proof

We normalize both sides and apply Young's inequality to each term.

1. Let $S = \sum_{i=1}^{n} |a_i|^p$ and $T = \sum_{i=1}^{n} |b_i|^q$. Let $A = S^{1/p}$ and $B = T^{1/q}$, with the [[real power|0TV07AQT62]] $c^r = e^{r \ln c}$ for $c > 0$ and the convention $0^r = 0$ for $r > 0$.
2. For $c > 0$ we have $c^p > 0$, because the [[exponential function is positive|0P9BNBW2W3]].
3. Suppose $S = 0$. Each term $|a_i|^p$ is at least $0$, so each term is $0$. By step 2, each $a_i = 0$.
   Then the left side is $0$, and the right side is at least $0$. So the inequality holds. The case $T = 0$ is the same.
4. From now on let $S > 0$ and $T > 0$. Then $A = e^{\frac{1}{p} \ln S} > 0$, and $\ln A = \frac{1}{p} \ln S$ since [[$\ln$ is the inverse of $\exp$|0RKW2X63YR]].
   So $A^p = e^{p \ln A} = e^{\ln S} = S$. In the same way $B > 0$ and $B^q = T$.
5. Let $c \ge 0$. We claim $(c / A)^p = c^p / A^p$. For $c = 0$ both sides are $0$.
   For $c > 0$, the [[logarithm of a quotient|0J7PHRBNNS]] gives $(c/A)^p = e^{p \ln c - p \ln A}$. By the [[exponential of a sum|0E8HNVBCSP]], $e^{p \ln c - p \ln A} \, e^{p \ln A} = e^{p \ln c}$. So $(c/A)^p = c^p / A^p$.
6. In the same way, $(c / B)^q = c^q / B^q$ for each $c \ge 0$.
7. Put $x_i = |a_i| / A$ and $y_i = |b_i| / B$. These are nonnegative. By [[Young's inequality|07VHQ31EYJ]] and steps 4 to 6,
   $$x_i y_i \le \frac{x_i^p}{p} + \frac{y_i^q}{q} = \frac{|a_i|^p}{p S} + \frac{|b_i|^q}{q T}.$$
8. Add these inequalities over $i = 1, \dots, n$. The right sides add up to $\frac{S}{p S} + \frac{T}{q T} = \frac{1}{p} + \frac{1}{q} = 1$.
9. Since [[$|a_i b_i| = |a_i| |b_i|$|0GMV7GP8W0]], the left sides add up to $\frac{1}{A B} \sum_{i=1}^{n} |a_i b_i|$. So this sum is at most $1$.
10. Multiply by $A B > 0$. This gives $\sum_{i=1}^{n} |a_i b_i| \le A B = \big( \sum_{i=1}^{n} |a_i|^p \big)^{1/p} \big( \sum_{i=1}^{n} |b_i|^q \big)^{1/q}$.

## Idea

Both sides scale in the same way when all $a_i$ or all $b_i$ are multiplied by a positive number. So we may scale the two sums on the right to equal $1$. Then Young's inequality bounds each product $|a_i| |b_i|$, and the bounds add up to $\frac{1}{p} + \frac{1}{q} = 1$.
