---
tag: 3GCMXQCZCX
kind: proof
name: Proof that (1 + x/n)^n tends to exp(x), by the binomial theorem
msc: [26A09]
proves: 0FEMF8JKAF
uses: [0RMVS7RXZX, 0K0H5E3Z5N, 0NB643K60Q, 0EHWPWGHB2, 033KTKKRV6, 0N32V0E3XJ, 08QAX4H1PF, 0RAM4E07NR, 0734RSVF2V, 09G6KHS6GY, 0A3GWZ86AY, 0M1MX28VXK, 0XMF00T4XQ, 03S6GWWKEZ, 0P9BNBW2W3, 0E8HNVBCSP, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Characterizations_of_the_exponential_function
    locator: Equivalence of the characterizations
---

## Proof

We first treat $x \ge 0$ with the binomial theorem, and then reduce $x < 0$ to that case. Here $e^x$ means $\exp(x)$.

1. Fix a real number $x$. For integers $n \ge 1$, let $t_n = (1 + x/n)^n$. For $m \in \mathbb{N}$, let $s_m = \sum_{k=0}^{m} x^k / k!$ be the [[partial sums|0NB643K60Q]] of the series of the [[exponential function|0RMVS7RXZX]].
2. By the definition of the [[sum of a series|0K0H5E3Z5N]], $s_m \to \exp(x)$ as $m \to \infty$.
3. For $0 \le k \le n$, let $p_{n,k} = \prod_{j=0}^{k-1} (1 - j/n)$, with $p_{n,0} = 1$. By the [[factorial formula|033KTKKRV6]],
$$\binom{n}{k} \frac{1}{n^k} = \frac{n (n-1) \cdots (n-k+1)}{k!\, n^k} = \frac{p_{n,k}}{k!}.$$
4. By the [[binomial theorem|0EHWPWGHB2]] and step 3, $t_n = \sum_{k=0}^{n} \frac{x^k}{k!} p_{n,k}$.
5. For $0 \le j < k \le n$ we have $0 \le 1 - j/n \le 1$. So $0 \le p_{n,k} \le 1$.

Case $x \ge 0$.

6. Each term $x^k/k!$ is now $\ge 0$. By steps 4 and 5, $t_n \le s_n$.
7. Fix $m$. For $n \ge m$ we have $s_m \le s_n$, since the added terms are $\ge 0$. By [[preservation of non-strict inequalities|0N32V0E3XJ]] and step 2, $s_m \le \exp(x)$. With step 6, $t_n \le \exp(x)$ for all $n \ge 1$.
8. Fix $m$. For $n \ge m$, drop the terms with $k > m$ in step 4. They are $\ge 0$, so $t_n \ge u_n$, where $u_n = \sum_{k=0}^{m} \frac{x^k}{k!} p_{n,k}$.
9. For fixed $j$, we have $1 - j/n \to 1$, by the example [[1/n tends to zero|08QAX4H1PF]], the [[product rule|0734RSVF2V]] and the [[sum rule|0RAM4E07NR]].
10. By [[induction|0ASJVEFA9J]] on $k$ and the product rule, $p_{n,k} \to 1$ as $n \to \infty$, for each fixed $k$. By induction on the number of terms and the sum rule, $u_n \to s_m$ as $n \to \infty$.
11. Let $\varepsilon > 0$. By step 2 and the [[epsilon-N definition|09G6KHS6GY]], there is $m$ with $s_m > \exp(x) - \varepsilon/2$.
12. For this $m$, step 10 gives $N \ge \max(m, 1)$ with $u_n > s_m - \varepsilon/2$ for all $n \ge N$.
13. For $n \ge N$, steps 7, 8, 11 and 12 give $\exp(x) - \varepsilon < u_n \le t_n \le \exp(x)$. So $|t_n - \exp(x)| < \varepsilon$, and $t_n \to \exp(x)$.
14. In particular, for $x = 1$ we get $(1 + 1/n)^n \to \exp(1) = e$.

Case $x < 0$.

15. Let $y = -x > 0$. By the [[Archimedean property|0A3GWZ86AY]], there is an integer $N_0 \ge 1$ with $N_0 > y$. For $n \ge N_0$, we get $0 < y/n < 1$, so $0 < 1 - y^2/n^2 < 1$.
16. For $n \ge N_0$, let $w_n = (1 - y^2/n^2)^n$. Then $w_n = (1 - y/n)^n (1 + y/n)^n$, and $w_n \le 1$ by step 15.
17. Since $-y^2/n^2 \ge -1$, [[Bernoulli's inequality|0M1MX28VXK]] gives $w_n \ge 1 - n \cdot y^2/n^2 = 1 - y^2/n$.
18. By step 9's argument, $1 - y^2/n \to 1$. By the [[squeeze theorem|0XMF00T4XQ]] with steps 16 and 17, $w_n \to 1$.
19. By the case $x \ge 0$ applied to $y$, $(1 + y/n)^n \to \exp(y)$. By [[positivity of the exponential|0P9BNBW2W3]], $\exp(y) \ne 0$.
20. For $n \ge N_0$, $(1 - y/n)^n = w_n / (1 + y/n)^n$. By the [[limit of a quotient|03S6GWWKEZ]], this tends to $1/\exp(y)$.
21. The series gives $\exp(0) = 1$. By the [[exponential of a sum|0E8HNVBCSP]], $\exp(y) \exp(-y) = \exp(0) = 1$. So $1/\exp(y) = \exp(-y) = \exp(x)$.
22. Since $1 + x/n = 1 - y/n$, step 20 shows $(1 + x/n)^n \to \exp(x)$. The terms with $n < N_0$ do not change the limit, by the epsilon-N definition.
23. So $(1 + x/n)^n \to e^x$ for every real $x$, and $(1 + 1/n)^n \to e$.

## Idea

The binomial theorem writes $(1 + x/n)^n$ as the exponential series cut off at $n$, with each term multiplied by a factor between $0$ and $1$. These factors tend to $1$, so for $x \ge 0$ the expression is squeezed against the partial sums. For $x < 0$, the product with $(1 - x/n)^n$ tends to $1$, which turns the positive case into the negative one.
