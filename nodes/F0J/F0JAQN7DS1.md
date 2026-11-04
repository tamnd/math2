---
tag: F0JAQN7DS1
kind: proof
name: Proof that the logarithm grows slower than any power
msc: [26A12, 33B10]
proves: 00DGYY10FV
uses: [0044CPHJBV, 0RKW2X63YR, 0TV07AQT62, 012C7GFF20, 0E8HNVBCSP, 0P9BNBW2W3, 0KN2V7840E, 0Y12QYTJK3]
sources:
  - url: https://proofwiki.org/wiki/Order_of_Natural_Logarithm_Function
---

## Proof

1. Fix a real $a > 0$, and let $b = a/2 > 0$. For $x > 0$, [[real powers|0TV07AQT62]] are $x^c = e^{c \ln x}$, where $\ln$ is the [[natural logarithm|0044CPHJBV]].
2. Let $x \ge 1$, and let $t = \ln x$. Since [[$\ln$ is strictly increasing|0RKW2X63YR]] and $\ln 1 = 0$, we have $t \ge 0$.
3. By the inequality [[$1 + y \le e^y$|012C7GFF20]] with $y = b t$, we get $b t \le 1 + b t \le e^{b t} = x^b$. So $\ln x \le \frac{1}{b} x^b$.
4. By the [[exponential of a sum|0E8HNVBCSP]], $x^a = e^{2 b t} = e^{b t} e^{b t} = x^b \cdot x^b$. Also $x^b > 0$ by [[positivity of the exponential|0P9BNBW2W3]].
5. Dividing step 3 by $x^a$, and using $\ln x \ge 0$, gives $0 \le \frac{\ln x}{x^a} \le \frac{1}{b \, x^b}$ for every $x \ge 1$.
6. Let $\varepsilon > 0$. Let $K = \frac{1}{b \varepsilon} > 0$, and let $M = \max(1, e^{(\ln K)/b})$.
7. Let $x > M$. Then $\ln x > \ln(e^{(\ln K)/b}) = (\ln K)/b$, since $\ln$ is strictly increasing and $\ln(e^y) = y$.
8. So $b \ln x > \ln K$. Since [[$\exp$ is strictly increasing|0KN2V7840E]], $x^b = e^{b \ln x} > e^{\ln K} = K$.
9. By step 5, for $x > M$ we get $0 \le \frac{\ln x}{x^a} < \frac{1}{b K} = \varepsilon$.
10. By the [[definition of a limit at infinity|0Y12QYTJK3]], $\lim_{x \to \infty} \frac{\ln x}{x^a} = 0$. That is, $\ln x = o(x^a)$ as $x \to \infty$.

## Idea

The inequality $1 + y \le e^y$ gives $\ln x \le \frac{2}{a} x^{a/2}$, so the logarithm is at most a multiple of half the power. Dividing by $x^a$ leaves a multiple of $x^{-a/2}$, which tends to $0$. Using half the exponent leaves room to spare.
