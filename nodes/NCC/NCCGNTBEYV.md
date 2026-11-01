---
tag: NCCGNTBEYV
kind: statement
role: theorem
name: Equidistribution theorem
msc: [11K06, 11J71]
uses: [XM6DH57BWY, 0DZXAXEJQ9, 07GJV36896]
about: [XM6DH57BWY]
sources:
  - url: https://en.wikipedia.org/wiki/Equidistribution_theorem
same_as:
  wikidata: Q3984052
  wikipedia: Equidistribution theorem
---

## Statement

Let $\alpha$ be an [[irrational number|0DZXAXEJQ9]].
Then the sequence $(n\alpha)_{n \ge 1}$ is [[equidistributed modulo one|XM6DH57BWY]].
That is, for all $0 \le a < b \le 1$, the proportion of $n \le N$ with $n\alpha - \floor{n\alpha} \in [a, b)$ tends to $b - a$ as $N \to \infty$.

## Remarks

A short proof uses Weyl's criterion.
For a nonzero integer $h$, the number $e^{2\pi i h \alpha}$ is not $1$, since $h\alpha \notin \Z$.
The sum $\sum_{n=1}^{N} e^{2\pi i h n \alpha}$ is a geometric sum, so its absolute value is at most $2 / \abs{1 - e^{2\pi i h \alpha}}$, a bound independent of $N$.
Dividing by $N$ gives a limit $0$, which is Weyl's condition.
The hypothesis that $\alpha$ is irrational is necessary: if $\alpha = p/q$ in lowest terms, then $n\alpha$ takes only $q$ values modulo one.
Example: $\log_{10} 2$ is irrational, so the fractional parts of $n \log_{10} 2$ are equidistributed.
Hence the leading digit of $2^n$ is $k$ for a proportion $\log_{10}(1 + 1/k)$ of the exponents $n$; for instance the digit $1$ occurs about $30.1\%$ of the time.

## Explanations

### L1 human

Walk around a circle of circumference $1$ in steps of an irrational length $\alpha$.
You never return to a point you have visited, and in the long run you visit every arc equally often.
This is a precise version of the idea that irrational rotations mix the circle well.

### L2 human

The theorem is the simplest case of Weyl's results on polynomial sequences.
If a real polynomial $p$ has at least one irrational coefficient other than the constant term, then $(p(n))$ is equidistributed modulo one.
Its proof shows the general pattern: equidistribution follows from cancellation in [[exponential sums|97PBMQCPPM]].
It strengthens Kronecker's theorem that $(n\alpha)$ is dense modulo one, and it expresses the unique ergodicity of the irrational rotation of the circle.
