---
tag: NQN8PB7V34
kind: proof
name: Proof of the comparison of a series and an integral
msc: [26A42]
proves: 069HKV4X1E
uses: [0QM4TXT3DR, 04YKAYDQPW, 05RCDKHZM6, 0MBWQKM8QR]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_test_for_convergence
    locator: Proof
---

## Proof

We compare $f$ with a constant on each interval of length $1$.

1. If $n = 0$, all three expressions are $0$: the sums are empty and the interval $[a, a]$ is a point. From now on let $n \ge 1$.
2. Since $f$ is decreasing, it is monotone. So $f$ is [[Riemann integrable|04YKAYDQPW]] on $[a, a+n]$ and on each subinterval, in the sense of the [[Riemann integral|0QM4TXT3DR]].
3. By [[additivity of the integral over intervals|05RCDKHZM6]], applied $n - 1$ times,
$$\int_a^{a+n} f(x)\, dx = \sum_{i=1}^{n} \int_{a+i-1}^{a+i} f(x)\, dx.$$
4. Let $1 \le i \le n$ and $x \in [a+i-1, a+i]$. Since $f$ is decreasing, $f(a+i) \le f(x) \le f(a+i-1)$.
5. The integral of a constant $c$ over an interval of length $1$ is $c$. By [[monotonicity of the integral|0MBWQKM8QR]] and step 4,
$$f(a+i) \le \int_{a+i-1}^{a+i} f(x)\, dx \le f(a+i-1).$$
6. Add the inequalities of step 5 over $i = 1, \dots, n$ and use step 3. This gives
$$\sum_{i=1}^{n} f(a+i) \le \int_a^{a+n} f(x)\, dx \le \sum_{i=1}^{n} f(a+i-1) = \sum_{i=0}^{n-1} f(a+i).$$

## Idea

On each interval $[a+i-1, a+i]$ of length $1$, a decreasing function lies between its value at the right end and its value at the left end. Integrating gives the bounds on each piece, and adding the pieces gives the two sums.
