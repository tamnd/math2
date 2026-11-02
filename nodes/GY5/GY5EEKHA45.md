---
tag: GY5EEKHA45
kind: definition
name: Quantum dilogarithm
msc: ["33B30", "33D05"]
defines: 6HMT17DVX7
uses: [Y1X8ZZQ7VM, G0X0NWSDB7]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_dilogarithm
---

## Definition

Let $q \in \C$ with $\abs{q} < 1$.
The *quantum dilogarithm* is the function of $x \in \C$ given by the infinite [[q-Pochhammer symbol|Y1X8ZZQ7VM]]
$$(x; q)_\infty = \prod_{n=0}^{\infty} (1 - x q^n).$$
For $\abs{x} < 1$ it is related to the series
$$\operatorname{Li}_2(x; q) = \sum_{n=1}^{\infty} \frac{x^n}{n (1 - q^n)}$$
by $(x; q)_\infty = \exp\big(-\operatorname{Li}_2(x; q)\big)$, and $\operatorname{Li}_2(x; q)$ is also called the quantum dilogarithm.

## Remarks

The product converges for every $x$, because $\sum_n \abs{x q^n} < \infty$, so $(x; q)_\infty$ is an entire function of $x$; for $q \neq 0$ its zeros are the points $x = q^{-n}$, $n \ge 0$.
The relation with the series comes from $\log(1 - x q^n) = -\sum_{k \ge 1} x^k q^{nk} / k$ and summing the geometric series in $n$.

Check of the classical limit: for fixed $x$ with $\abs{x} < 1$ and real $q \to 1^-$, one has $(1 - q) / (1 - q^n) \to 1/n$, so $(1 - q) \operatorname{Li}_2(x; q) \to \sum_{n \ge 1} x^n / n^2 = \operatorname{Li}_2(x)$, the [[dilogarithm|G0X0NWSDB7]].

Non-example: for $\abs{q} = 1$ and $x \neq 0$ the product $\prod_{n \ge 0} (1 - x q^n)$ does not converge, since its factors do not tend to $1$.
For $\abs{q} = 1$ other versions are used, such as the non-compact quantum dilogarithm of Faddeev, given by an integral.

Euler's expansion gives $\frac{1}{(x; q)_\infty} = \sum_{n \ge 0} \frac{x^n}{(q; q)_n}$ for $\abs{x} < 1$.
