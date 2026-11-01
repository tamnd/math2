---
tag: 8SK3GQ4S0M
kind: statement
role: theorem
name: Tauber's theorem
msc: ["40E05", 40A30]
uses: [0VP56B4EMX, 0CVVKY7GY2, 0909PWZR62, 0S4EMDQS2F, 0RYTGBJAGN]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_and_Tauberian_theorems
    locator: Tauberian theorems
---

## Statement

Let $(a_n)_{n \ge 0}$ be a sequence of complex numbers such that the [[power series|0VP56B4EMX]] $f(x) = \sum_{n=0}^{\infty} a_n x^n$ converges for $0 \le x < 1$.
Assume that the [[one-sided limit|0909PWZR62]] $s = \lim_{x \to 1^-} f(x)$ exists.
Assume also that $n a_n \to 0$ as $n \to \infty$.
Then the series $\sum_{n=0}^{\infty} a_n$ [[converges|0CVVKY7GY2]], and its sum is $s$.

## Remarks

The idea of the proof is to compare the partial sum $s_N = \sum_{n \le N} a_n$ with $f(x)$ for $x = 1 - 1/N$.
The difference is at most $\sum_{n \le N} \abs{a_n} (1 - x^n) + \sum_{n > N} \abs{a_n} x^n$.
Use $1 - x^n \le n(1 - x)$ in the first sum, which is then at most the average of $n \abs{a_n}$ over $n \le N$, and this tends to $0$.
In the second sum, $\abs{a_n} \le \varepsilon / n \le \varepsilon / N$ for large $N$, so it is at most $\varepsilon / (N(1 - x)) = \varepsilon$.

The theorem is a partial converse of [[Abel's theorem|0S4EMDQS2F]], which gives $\lim_{x \to 1^-} f(x) = \sum a_n$ whenever the series converges.
The condition on $n a_n$ cannot be dropped.
For $a_n = (-1)^n$, one has $f(x) = 1/(1 + x) \to 1/2$, but $\sum (-1)^n$ diverges, and $n a_n$ does not tend to $0$.
Littlewood showed that the weaker condition $n a_n = O(1)$ is enough; see [[big O notation|0RYTGBJAGN]].

## Explanations

### L1 human

Abel's theorem says that a convergent series can be summed by plugging $x \to 1$ into its power series.
The converse is false in general: the power series can have a limit even when the series diverges.
Tauber's theorem says that the converse does hold when the terms shrink faster than $1/n$.

### L2 human

This is the first Tauberian theorem, and it gave its name to the whole family of Abelian and Tauberian theorems.
An Abelian theorem passes from ordinary convergence to convergence of a summation method; a Tauberian theorem goes back, under an extra size condition on the terms.
Later results of this type, such as the Hardy–Littlewood and Wiener Tauberian theorems, are central tools in analytic number theory.
