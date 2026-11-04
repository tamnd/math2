---
tag: 4N8SCS4TTJ
kind: proof
name: Proof of Young's inequality for products
msc: [26D15]
proves: 07VHQ31EYJ
uses: [0TV07AQT62, 0P9BNBW2W3, 0RKW2X63YR, 0K2FNY6DYV, 0ZS54B9GJF, 0044CPHJBV]
sources:
  - url: https://en.wikipedia.org/wiki/Young%27s_inequality_for_products
    locator: Standard version for conjugate Hölder exponents
---

## Proof

We use the strict concavity of the logarithm.

1. Let $p, q > 1$ with $\frac{1}{p} + \frac{1}{q} = 1$, and let $a, b \ge 0$.
   For $c > 0$ and real $r$, the [[power|0TV07AQT62]] is $c^r = e^{r \ln c}$. For $c = 0$ and $r > 0$ we use the usual convention $0^r = 0$.
2. For $c > 0$ we have $c^r > 0$, because the [[exponential function is positive|0P9BNBW2W3]].
   Also $\ln(c^r) = r \ln c$, because [[$\ln$ is the inverse of $\exp$|0RKW2X63YR]].
3. First let $a = 0$ or $b = 0$. Then $a b = 0$, and both terms $\frac{a^p}{p}$ and $\frac{b^q}{q}$ are at least $0$. So the inequality holds.
4. In this case equality means $\frac{a^p}{p} + \frac{b^q}{q} = 0$. Both terms are nonnegative, so this means $a^p = 0$ and $b^q = 0$.
   One of $a^p$ and $b^q$ is already $0$. So equality holds exactly when the other one is $0$ too, that is, when $a^p = b^q$.
5. Now let $a, b > 0$. Put $x = a^p$, $y = b^q$ and $t = \frac{1}{p}$. Then $x, y > 0$ by step 2, $t \in (0, 1)$ since $p > 1$, and $1 - t = \frac{1}{q}$.
6. By the [[logarithm of a product|0K2FNY6DYV]] and step 2,
   $$\ln(a b) = \ln a + \ln b = \tfrac{1}{p} \ln x + \tfrac{1}{q} \ln y = t \ln x + (1 - t) \ln y.$$
7. Suppose $x \ne y$. The [[logarithm is strictly concave|0ZS54B9GJF]], so $\ln(t x + (1 - t) y) > t \ln x + (1 - t) \ln y = \ln(a b)$.
8. The [[logarithm|0044CPHJBV]] is strictly increasing by [[the inverse result|0RKW2X63YR]]. If $t x + (1 - t) y \le a b$, then $\ln(t x + (1 - t) y) \le \ln(a b)$, against step 7. So $a b < \frac{a^p}{p} + \frac{b^q}{q}$, with strict inequality.
9. Suppose $x = y$. Then $t x + (1 - t) y = x = a^p$. Also $\ln b = \frac{1}{q} \ln y = \frac{1}{q} \ln x = \frac{p}{q} \ln a$.
10. Hence $\ln(a b) = \big(1 + \frac{p}{q}\big) \ln a$. Since $1 + \frac{p}{q} = p \big( \frac{1}{p} + \frac{1}{q} \big) = p$, this is $p \ln a = \ln(a^p)$.
11. The logarithm is strictly increasing, so it is injective. So $a b = a^p = \frac{a^p}{p} + \frac{b^q}{q}$, and equality holds.
12. Steps 8 and 11 show that for $a, b > 0$ the inequality holds, with equality exactly when $a^p = b^q$. With steps 3 and 4, this proves the statement for all $a, b \ge 0$.

## Idea

Take logarithms. The logarithm of $a b$ is the weighted average of $\ln a^p$ and $\ln b^q$ with weights $1/p$ and $1/q$. Concavity of the logarithm says that this average is at most the logarithm of the weighted average of $a^p$ and $b^q$. Strict concavity gives the equality case.
