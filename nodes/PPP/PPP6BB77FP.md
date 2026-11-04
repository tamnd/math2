---
tag: PPP6BB77FP
kind: proof
name: Proof that one-sided limits of a monotone function exist
msc: [26A48]
proves: 0KJXHN0TW0
uses: [0WFF6AZPBP, 0909PWZR62, 07EGCNHAVW, 0AXWET80YW, 0EDH403M21, 0BTMQ04556, 04KFTA34C5]
sources:
  - url: https://www.jirka.org/ra/html/sec_monotonefunc.html
    locator: Proposition 3.6.2
---

## Proof

Here $f$ is increasing in the sense of a [[monotone function|0WFF6AZPBP]]: $x \le y$ implies $f(x) \le f(y)$.

1. Let $S = \set{f(x) : a < x < c}$. It is nonempty, since $\frac{a + c}{2} \in (a, c)$.
2. For $a < x < c$ we have $f(x) \le f(c)$, since $f$ is increasing. So $f(c)$ is an upper bound of $S$.
3. By the [[completeness axiom|0AXWET80YW]], $S$ has a [[supremum|0BTMQ04556]] $L$. Since $f(c)$ is an upper bound, $L \le f(c)$.
4. The point $c$ is a [[limit point|07EGCNHAVW]] of $(a, b) \cap (-\infty, c) = (a, c)$. Indeed, for $\delta > 0$ the point $c - \frac{1}{2}\min(\delta, c - a)$ lies in $(a, c)$ and within $\delta$ of $c$.
5. Let $\varepsilon > 0$. The number $L - \varepsilon$ is not an upper bound of $S$. So there is $x_0 \in (a, c)$ with $f(x_0) > L - \varepsilon$.
6. Put $\delta = c - x_0 > 0$. Let $x \in (a, b)$ with $c - \delta < x < c$. Then $x_0 < x < c$.
7. Since $f$ is increasing, $L - \varepsilon < f(x_0) \le f(x)$. Since $x \in (a, c)$, also $f(x) \le L$. So $\abs{f(x) - L} < \varepsilon$.
8. By the definition of the [[one-sided limit|0909PWZR62]], steps 4 to 7 give $\lim_{x \to c^-} f(x) = L = \sup_{a < x < c} f(x)$.
9. Now let $T = \set{f(x) : c < x < b}$. It is nonempty, and $f(c)$ is a lower bound of $T$, since $f$ is increasing.
10. By the [[existence of the infimum|0EDH403M21]], $T$ has an [[infimum|04KFTA34C5]] $R$. Since $f(c)$ is a lower bound, $f(c) \le R$.
11. In the same way as step 4, $c$ is a limit point of $(c, b)$.
12. Let $\varepsilon > 0$. The number $R + \varepsilon$ is not a lower bound of $T$. So there is $x_1 \in (c, b)$ with $f(x_1) < R + \varepsilon$.
13. Put $\delta = x_1 - c > 0$. Let $x \in (a, b)$ with $c < x < c + \delta$. Then $c < x < x_1$, so $R \le f(x) \le f(x_1) < R + \varepsilon$. Thus $\abs{f(x) - R} < \varepsilon$.
14. So $\lim_{x \to c^+} f(x) = R = \inf_{c < x < b} f(x)$.
15. Steps 3, 8, 10 and 14 give the chain $\lim_{x \to c^-} f(x) = L \le f(c) \le R = \lim_{x \to c^+} f(x)$.

## Idea

To the left of $c$, the values of $f$ rise but never pass $f(c)$, so they have a least upper bound. Once one value comes within $\varepsilon$ of that bound, all later values up to $c$ stay within $\varepsilon$, because $f$ is increasing. The right side is the mirror image with the infimum.
