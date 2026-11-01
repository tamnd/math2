---
tag: BY5WRND0J1
kind: statement
role: theorem
name: Erdős–Kac theorem
msc: [11N60, 11K65]
uses: [08RQ62VAVA, 05AQE0QR0D, 04DXAFN2ES, 0EPZC4Z1FC]
about: [08RQ62VAVA]
sources:
  - url: https://en.wikipedia.org/wiki/Erdős–Kac_theorem
same_as:
  wikidata: Q846840
  wikipedia: Erdős–Kac theorem
---

## Statement

For an integer $n \ge 1$, let $\omega(n)$ be the [[number of distinct prime factors|08RQ62VAVA]] of $n$, and let $\log$ be the [[natural logarithm|04DXAFN2ES]].
For all real numbers $a < b$,
$$\lim_{x \to \infty} \frac{1}{x}\, \#\set{3 \le n \le x : a \le \frac{\omega(n) - \log\log n}{\sqrt{\log\log n}} \le b} = \frac{1}{\sqrt{2\pi}} \int_{a}^{b} e^{-t^2/2}\, dt.$$

## Remarks

In words, $\omega(n)$ has an approximately [[normal distribution|05AQE0QR0D]] with mean and variance $\log\log n$.
A heuristic proof: $\omega(n) = \sum_{p \le n} \mathbf{1}_{p \mid n}$, and for a random $n$ the events $p \mid n$ have probability $1/p$ and are nearly independent, so the central limit theorem applies with variance $\sum_{p \le x} 1/p \approx \log\log x$.
A rigorous proof restricts to small primes, shows near independence with a sieve, and compares moments with those of the normal law.
The earlier theorem of Hardy and Ramanujan says that $\omega(n)$ has normal order $\log\log n$: for every $\varepsilon > 0$, almost all $n$ satisfy $\abs{\omega(n) - \log\log n} < \varepsilon \log\log n$.
Since $\log\log n$ grows very slowly, the limit is reached slowly; for $n$ near $10^{9}$, $\log\log n \approx 3$.

## Explanations

### L1 human

Pick a large number at random and count its different prime factors.
The theorem says the count behaves like a bell curve: its average is about $\log\log n$, and the spread is about $\sqrt{\log\log n}$.
So most numbers have roughly $\log\log n$ prime factors, which is a very small number even for huge $n$.

### L2 human

The Erdős–Kac theorem is the founding result of probabilistic number theory.
It treats the indicators of divisibility by different primes as almost independent random variables, and turns this into a [[central limit theorem|0EPZC4Z1FC]] for the additive function $\omega$.
The same holds for $\Omega(n)$, the number of prime factors counted with multiplicity, and more generally for many additive functions.
It sharpens the Hardy–Ramanujan normal order result, which gives only the center and not the shape of the distribution.
