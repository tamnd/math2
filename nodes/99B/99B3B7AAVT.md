---
tag: 99B3B7AAVT
kind: definition
name: Weierstrass product
msc: ["30D20", "30D10"]
defines: ACSF58HYDH
uses: [0419794R0T, 0RMVS7RXZX, 08FPABDQ4C, 0CEGEASY49]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_factorization_theorem
---

## Definition

For an integer $p \ge 0$, the *elementary factor* $E_p$ is the entire function
$$E_0(z) = 1 - z, \qquad E_p(z) = (1 - z) \exp\left(\sum_{k=1}^{p} \frac{z^k}{k}\right) \quad (p \ge 1).$$
Let $(a_n)_{n \ge 1}$ be a sequence of nonzero complex numbers with $\abs{a_n} \to \infty$, and let $(p_n)_{n \ge 1}$ be integers $p_n \ge 0$ such that
$$\sum_{n \ge 1} \left(\frac{r}{\abs{a_n}}\right)^{p_n + 1} < \infty \quad \text{for every } r > 0.$$
The *Weierstrass product* with zeros $(a_n)$ and indices $(p_n)$ is the function
$$P(z) = \prod_{n \ge 1} E_{p_n}\!\left(\frac{z}{a_n}\right).$$

## Remarks

Since $\abs{1 - E_p(z)} \le \abs{z}^{p+1}$ for $\abs{z} \le 1$, the product converges [[uniformly|08FPABDQ4C]] on compact subsets of $\C$.
So $P$ is an [[entire function|0419794R0T]], and its [[zeros|0CEGEASY49]] are exactly the $a_n$, with multiplicity the number of indices $n$ with $a_n = a$.
The choice $p_n = n - 1$ always satisfies the condition.
Example: $a_n = n$ and $p_n = 1$; then $\sum_n (r/n)^2 < \infty$, so $\prod_{n \ge 1} (1 - z/n) e^{z/n}$ is a Weierstrass product, with zeros at the positive integers.
Non-example: $a_n = n$ and $p_n = 0$ fail the condition, since $\sum_n r/n$ diverges; indeed $\prod_n (1 - z/n)$ diverges at $z = -1$.
When all $p_n$ equal the least integer $p \ge 0$ with $\sum_n \abs{a_n}^{-(p+1)} < \infty$, the product is called the canonical product, and $p$ is its genus.
