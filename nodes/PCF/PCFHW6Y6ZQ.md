---
tag: PCFHW6Y6ZQ
kind: proof
name: Proof of the Poisson limit theorem
msc: [60F05]
proves: 0XKTZRWTXX
uses: [0VRWZDWW6B, 0VEFSSKX18, 0JDAQHWA9N, 0MXMS3AE13, 092GEF38YD, 012C7GFF20, 0RKW2X63YR]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_limit_theorem
    locator: First proof
---

## Proof

We split the binomial probability into three factors and find the limit of each one.

1. Fix an integer $k \ge 0$. Since $n p_n \to \lambda$, we have $p_n = (n p_n)/n \to \lambda \cdot 0 = 0$. So there is $n_0 \ge k$ with $p_n \le 1/2$ for $n \ge n_0$; from now on $n \ge n_0$.
2. By the definition of the [[binomial distribution|0VRWZDWW6B]] and of the [[binomial coefficient|092GEF38YD]],
$$P(S_n = k) = \binom{n}{k} p_n^k (1 - p_n)^{n-k} = a_n \cdot \frac{(n p_n)^k}{k!} \cdot (1 - p_n)^{n} \cdot (1 - p_n)^{-k},$$
with $a_n = \frac{n(n-1)\cdots(n-k+1)}{n^k} = \prod_{j=0}^{k-1} \left(1 - \frac{j}{n}\right)$.
3. Each of the $k$ factors $1 - j/n$ tends to $1$. So $a_n \to 1$, and for $k = 0$ the empty product is $1$.
4. Since $n p_n \to \lambda$, $(n p_n)^k / k! \to \lambda^k / k!$. Since $p_n \to 0$, $(1 - p_n)^{-k} \to 1$.
5. Claim: $-x - x^2 \le \ln(1 - x) \le -x$ for $0 \le x \le 1/2$. The upper bound is $1 - x \le e^{-x}$, the inequality [[$1 + y \le e^y$|012C7GFF20]] with $y = -x$.
6. For the lower bound, let $g(x) = \ln(1 - x) + x + x^2$. Then $g(0) = 0$ and $g'(x) = -\frac{1}{1-x} + 1 + 2x = \frac{x(1 - 2x)}{1 - x} \ge 0$ on $[0, 1/2]$. So $g \ge 0$ there.
7. By step 5 with $x = p_n$, $-n p_n - n p_n \cdot p_n \le n \ln(1 - p_n) \le -n p_n$.
8. Both bounds tend to $-\lambda$, since $n p_n \to \lambda$ and $n p_n \cdot p_n \to \lambda \cdot 0 = 0$. So $n \ln(1 - p_n) \to -\lambda$.
9. The exponential is continuous and is the [[inverse of the logarithm|0RKW2X63YR]]. So $(1 - p_n)^n = \exp(n \ln(1 - p_n)) \to e^{-\lambda}$.
10. By steps 2, 3, 4 and 9, $P(S_n = k) \to 1 \cdot \frac{\lambda^k}{k!} \cdot e^{-\lambda} \cdot 1 = e^{-\lambda} \lambda^k / k!$. This is the first claim.
11. Let $T \sim \operatorname{Poisson}(\lambda)$, with the [[Poisson distribution|0VEFSSKX18]]. Let $F_n$ and $F$ be the [[cumulative distribution functions|0MXMS3AE13]] of $S_n$ and $T$.
12. Both $S_n$ and $T$ take values in $\set{0, 1, 2, \dots}$. So for $x < 0$, $F_n(x) = 0 = F(x)$.
13. For $x \ge 0$, let $m = \floor{x}$. Then $F_n(x) = \sum_{k=0}^{m} P(S_n = k)$ and $F(x) = \sum_{k=0}^{m} e^{-\lambda} \lambda^k / k!$. These are finite sums, so step 10 gives $F_n(x) \to F(x)$.
14. Thus $F_n(x) \to F(x)$ for every real $x$, in particular at every continuity point of $F$. So $S_n \to T$ [[in distribution|0JDAQHWA9N]].

## Idea

For fixed $k$, choosing $k$ successes among $n$ trials gives about $n^k/k!$ choices, each with probability about $p_n^k$, so this part tends to $\lambda^k/k!$. The chance of no other success, $(1 - p_n)^{n}$, tends to $e^{-\lambda}$ because $\ln(1 - p) \approx -p$ for small $p$.
