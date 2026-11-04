---
tag: RCXYRDJ7PK
kind: proof
name: Proof of the lifting-the-exponent lemma for odd primes
msc: [11A51]
proves: 0JYF6PTKEW
uses: [04VCPS30ZE, 0850JJMJYZ, 051VYKA1EX, 0EHWPWGHB2, 0TPW25CBN6, 0J5VGJYYC3, 072D5G4SK6, 00FWBN7F0Y]
sources:
  - url: https://en.wikipedia.org/wiki/Lifting-the-exponent_lemma
    locator: Proof
---

## Proof

1. Let $p$ be an odd prime, $x, y$ integers with $p \nmid x$, $p \nmid y$, $p \mid x - y$, and $n \ge 1$. Here $\nu_p$ is the [[p-adic valuation|04VCPS30ZE]].
2. If $x = y$, then $x^n - y^n = 0$. Both sides equal $\infty$, since $\nu_p(0) = \infty$. Assume from now on that $x \ne y$.
3. For integers $X, Y$ and $N \ge 1$, put $S_N(X, Y) = \sum_{j=0}^{N-1} X^{N-1-j} Y^j$. Expanding the product, the terms cancel in pairs, and $X^N - Y^N = (X - Y) \, S_N(X, Y)$.
4. Claim A: if $p \nmid X$ and $p \mid X - Y$ and $p \nmid N$, then $p \nmid S_N(X, Y)$. Indeed $Y \equiv X \pmod p$, so each term is congruent to $X^{N-1}$, by [[powers|0J5VGJYYC3]] and [[products|072D5G4SK6]] of congruences.
5. So $S_N(X, Y) \equiv N X^{N-1} \pmod p$. By [[Euclid's lemma|051VYKA1EX]], $p \nmid N X^{N-1}$. This proves claim A.
6. Claim B: if $p \nmid X$ and $p \mid X - Y$, then $\nu_p(S_p(X, Y)) = 1$. Write $Y = X + t$ with $p \mid t$.
7. Let $1 \le j \le p - 1$. By the [[binomial theorem|0EHWPWGHB2]], $Y^j = X^j + j X^{j-1} t + t^2 w_j$ for an integer $w_j$. Since $p^2 \mid t^2$, we get $X^{p-1-j} Y^j \equiv X^{p-1} + j X^{p-2} t \pmod{p^2}$.
8. This also holds for $j = 0$, where both sides equal $X^{p-1}$. Summing over $j$ with the [[sum rule for congruences|00FWBN7F0Y]], $S_p(X, Y) \equiv p X^{p-1} + X^{p-2} t \sum_{j=0}^{p-1} j \pmod{p^2}$.
9. Here $\sum_{j=0}^{p-1} j = p \cdot \frac{p-1}{2}$, and $\frac{p-1}{2}$ is an integer because $p$ is odd. Since $p \mid t$, the second term is divisible by $p^2$.
10. So $S_p(X, Y) \equiv p X^{p-1} \pmod{p^2}$. Thus $p \mid S_p(X, Y)$. As $p \nmid X^{p-1}$, also $p^2 \nmid S_p(X, Y)$. This proves claim B.
11. Let $X, Y$ satisfy $p \nmid X$, $p \nmid Y$, $p \mid X - Y$ and $X \ne Y$. By claim B, $S_p(X, Y) \ne 0$, so $X^p \ne Y^p$. By step 3 and the [[valuation of a product|0850JJMJYZ]], $\nu_p(X^p - Y^p) = \nu_p(X - Y) + 1$.
12. For the same $X, Y$ and $p \nmid N$, claim A gives $\nu_p(S_N(X, Y)) = 0$. So $\nu_p(X^N - Y^N) = \nu_p(X - Y)$.
13. For $i \ge 0$, let $x_i = x^{p^i}$ and $y_i = y^{p^i}$. By Euclid's lemma $p \nmid x_i$ and $p \nmid y_i$. By step 3, $x_i - y_i$ is a multiple of $x - y$, so $p \mid x_i - y_i$.
14. Claim: $x_i \ne y_i$ and $\nu_p(x_i - y_i) = \nu_p(x - y) + i$. We argue by induction on $i$. The case $i = 0$ is step 2.
15. If the claim holds for $i$, then step 11 applies to $X = x_i$, $Y = y_i$. Since $x_{i+1} = x_i^p$ and $y_{i+1} = y_i^p$, it gives $x_{i+1} \ne y_{i+1}$ and $\nu_p(x_{i+1} - y_{i+1}) = \nu_p(x - y) + i + 1$.
16. Write $n = p^a b$ with $a = \nu_p(n)$ and $p \nmid b$. Then $x^n - y^n = x_a^b - y_a^b$.
17. By step 12 with $X = x_a$, $Y = y_a$, $N = b$, and then step 14, $\nu_p(x^n - y^n) = \nu_p(x_a - y_a) = \nu_p(x - y) + \nu_p(n)$.

## Idea

Factor $x^n - y^n = (x - y)(x^{n-1} + \dots + y^{n-1})$. When $x \equiv y \pmod p$, the second factor is about $n x^{n-1}$ modulo $p$. So it adds no factor of $p$ when $p \nmid n$, and for $n = p$ it adds exactly one; oddness of $p$ kills the next correction term. Each factor $p$ of $n$ therefore adds one to the valuation.
