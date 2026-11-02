---
tag: X629NF2CQS
kind: statement
role: theorem
name: Abel–Dini theorem
msc: [40A05]
uses: [0NB643K60Q, 0CVVKY7GY2, 0NBRP6093V, 06PVXMY0TH]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_tests
---

## Statement

Let $(a_n)_{n \ge 1}$ be a sequence of positive real numbers such that $\sum a_n$ [[diverges|0NBRP6093V]].
Let $s_n = a_1 + \cdots + a_n$ be the [[partial sums|0NB643K60Q]], and let $\alpha$ be a real number.
Then $\sum_{n=1}^{\infty} a_n / s_n^{\alpha}$ [[converges|0CVVKY7GY2]] if $\alpha > 1$, and diverges if $\alpha \le 1$.

## Remarks

For $\alpha = 1$ and $m > n$, the terms with index from $n+1$ to $m$ satisfy $\sum_{k=n+1}^{m} a_k / s_k \ge (s_m - s_n)/s_m$.
Since $s_m \to \infty$, this tends to $1$ as $m \to \infty$, so the [[Cauchy criterion|06PVXMY0TH]] fails.
For $\alpha < 1$, one has $s_n \ge 1$ for large $n$, so $a_n / s_n^{\alpha} \ge a_n / s_n$.
For $\alpha > 1$, one has $a_n / s_n^{\alpha} \le \int_{s_{n-1}}^{s_n} t^{-\alpha} \, dt$ for $n \ge 2$, and these integrals add up to at most $\int_{s_1}^{\infty} t^{-\alpha} \, dt < \infty$.
Example: with $a_n = 1$, one has $s_n = n$, and the theorem says that $\sum 1/n^{\alpha}$ converges exactly when $\alpha > 1$.

## Explanations

### L1 human

Start from any divergent series of positive terms.
Dividing each term by the partial sum so far gives a new series that still diverges, but more slowly.
Dividing by a slightly higher power of the partial sum makes it converge.

### L2 human

The theorem shows that there is no slowest divergent series: from any divergent series of positive terms, $\sum a_n / s_n$ diverges, and its terms are much smaller than $a_n$.
It also gives a supply of convergent series near the boundary.
So no single comparison series can decide all series of positive terms, which is one reason why there is a whole scale of [[convergence tests|FJKV01J9F1]].
