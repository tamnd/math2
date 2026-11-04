---
tag: Q27VT9F4RN
kind: statement
role: proposition
name: The generalized repunit conjecture
sources:
  - wikipedia: en:215056@r1363388346
    locator: Repunit, section Repunit primes > The generalized repunit conjecture
    note: adopted
    mention: wikipedia://en/215056#8IYH
    sections: [Statement]
inventory: [946XAPYM06]
---

## Statement

A conjecture related to the generalized repunit primes: (the conjecture predicts where is the next generalized Mersenne prime, if the conjecture is true, then there are infinitely many repunit primes for all bases $b$)

For any integer $b$, which satisfies the conditions:

1. $$|b|>1.$$
1. $b$ is not a perfect power. (since when $b$ is a perfect $r$th power, it can be shown that there is at most one $n$ value such that $\frac{b^n-1}{b-1}$ is prime, and this $n$ value is $r$ itself or a [[root|TTEA3KA5KJ]] of $r$)
1. $b$ is not in the form $-4k^4$. (if so, then the number has aurifeuillean factorization)

has generalized repunit primes of the form

$$R_p(b)=\frac{b^p-1}{b-1}$$

for prime $p$, the prime numbers will be distributed near the best fit line

$$Y=G \cdot \log_{|b|}\left( \log_{|b|}\left( R_{(b)}(n) \right) \right)+C,$$

where limit $n\rightarrow\infty$, $G=\frac{1}{e^\gamma}=0.561459483566...$

and there are about

$$\left( \log_e(N)+m \cdot \log_e(2) \cdot \log_e \big( \log_e(N) \big) +\frac{1}{\sqrt N}-\delta \right) \cdot \frac{e^\gamma}{\log_e(|b|)}$$

base-*b* repunit primes less than *N*.

- $e$ is the [[base of natural logarithm|0MVCFMW7S4]].
- $\gamma$ is Euler–Mascheroni constant.
- $\log_{|b|}$ is the logarithm in base $|b|$
- $R_{(b)}(n)$ is the $n$th generalized repunit prime in base*b* (with prime *p*)
- $C$ is a data fit constant which varies with $b$.
- $\delta=1$ if $b>0$, $\delta=1.6$ if $b<0$.
- $m$ is the largest natural number such that $-b$ is a $2^{m-1}$th power.

We also have the following 3 properties:

1. The number of prime numbers of the form $\frac{b^n-1}{b-1}$ (with prime $p$) less than or equal to $n$ is about $e^\gamma \cdot \log_{|b|}\big(\log_{|b|}(n)\big)$.
1. The expected number of prime numbers of the form $\frac{b^n-1}{b-1}$ with prime $p$ between $n$ and $|b| \cdot n$ is about $e^\gamma$.
1. The probability that number of the form $\frac{b^n-1}{b-1}$ is prime (for prime $p$) is about $\frac{e^\gamma}{p \cdot \log_e(|b|)}$.
