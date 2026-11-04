---
tag: ECJEG3JHVM
kind: proof
name: Proof of the sum of independent Poisson random variables by the multinomial theorem
msc: ["60E05"]
proves: 0YH1M56SBN
uses: [0VEFSSKX18, 0XCE070V8B, 0XFC1VQYEK, 00K0RF9BFY, 0WF4EJP91W]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_distribution
    locator: Sums of Poisson-distributed random variables
---

## Proof

We compute the probability mass function of the sum directly.

1. Let $S = X_1 + \dots + X_n$ and $\Lambda = \lambda_1 + \dots + \lambda_n$. Then $\Lambda > 0$.
2. By the definition of the [[Poisson distribution|0VEFSSKX18]], $P(X_i = k) = e^{-\lambda_i} \lambda_i^k / k!$ for each integer $k \ge 0$. These values add up to $1$, so $X_i \in \set{0, 1, 2, \dots}$ almost surely.
3. Let $N$ be the event that every $X_i$ is a nonnegative integer. By step 2, its complement is a finite union of null events, so $P(N) = 1$.
4. On $N$, the sum $S$ is a nonnegative integer. So $S \in \set{0, 1, 2, \dots}$ almost surely.
5. Fix an integer $m \ge 0$. Let $K_m$ be the set of $n$-tuples $(k_1, \dots, k_n)$ of nonnegative integers with $k_1 + \dots + k_n = m$. It is a finite set.
6. Up to a null event, $\set{S = m}$ is the disjoint union over $(k_1, \dots, k_n) \in K_m$ of the events $\set{X_1 = k_1, \dots, X_n = k_n}$. So $P(S = m) = \sum_{K_m} P(X_1 = k_1, \dots, X_n = k_n)$.
7. By [[independence|0XCE070V8B]] with $B_i = \set{k_i}$, each term is $\prod_{i=1}^{n} P(X_i = k_i) = e^{-\Lambda} \prod_{i=1}^{n} \lambda_i^{k_i} / k_i!$.
8. Multiply and divide by $m!$. Then
$$P(S = m) = \frac{e^{-\Lambda}}{m!} \sum_{(k_1, \dots, k_n) \in K_m} \frac{m!}{k_1! \cdots k_n!} \lambda_1^{k_1} \cdots \lambda_n^{k_n}.$$
9. The fraction $m! / (k_1! \cdots k_n!)$ is the [[multinomial coefficient|00K0RF9BFY]]. By the [[multinomial theorem|0XFC1VQYEK]], the sum equals $(\lambda_1 + \dots + \lambda_n)^m = \Lambda^m$.
10. So $P(S = m) = e^{-\Lambda} \Lambda^m / m!$ for each integer $m \ge 0$. With step 4, the [[probability mass function|0WF4EJP91W]] of $S$ is that of $\operatorname{Poisson}(\Lambda)$.
11. Hence $X_1 + \dots + X_n \sim \operatorname{Poisson}(\lambda_1 + \dots + \lambda_n)$.

## Idea

The sum equals $m$ exactly when the counts $k_1, \dots, k_n$ add up to $m$. Independence turns each such case into a product of Poisson weights, and the multinomial theorem collects all the cases into $\Lambda^m$.
