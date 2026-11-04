---
tag: CT2QK2KGHG
kind: proof
name: Proof of the de Moivre–Laplace theorem from the central limit theorem
msc: [60F05]
proves: 065X9S8CM3
uses: [0EPZC4Z1FC, 02XPXR1FBK, 0J97P5KZY0, 0VRWZDWW6B, 0XCE070V8B, 092GEF38YD, 0JDAQHWA9N, 0MXMS3AE13, 07RXBVTVZB, 2HWVFHM13R]
sources:
  - url: https://en.wikipedia.org/wiki/De_Moivre–Laplace_theorem
    locator: Theorem
---

## Proof

We write a binomial variable as a sum of independent Bernoulli variables and apply the central limit theorem.

1. Let $B_1, B_2, \dots$ be a [[Bernoulli process|02XPXR1FBK]] with parameter $p$: i.i.d. variables with $P(B_i = 1) = p$ and $P(B_i = 0) = q$. Such a sequence exists on an [[infinite product|2HWVFHM13R]] of copies of $\set{0, 1}$.
2. Let $T_n = B_1 + \dots + B_n$. Claim: $T_n \sim \operatorname{Bin}(n, p)$. Fix $k \in \set{0, \dots, n}$.
3. The event $\set{T_n = k}$ is the disjoint union, over the sets $J \subseteq \set{1, \dots, n}$ with $k$ elements, of the events $E_J = \set{B_j = 1 \text{ for } j \in J, \ B_j = 0 \text{ for } j \notin J}$.
4. By [[independence|0XCE070V8B]], $P(E_J) = p^k q^{n-k}$. There are $\binom{n}{k}$ such sets $J$, by the definition of the [[binomial coefficient|092GEF38YD]].
5. So $P(T_n = k) = \binom{n}{k} p^k q^{n-k}$, which is the [[binomial distribution|0VRWZDWW6B]]. This proves the claim.
6. A [[Bernoulli variable|0J97P5KZY0]] $B_1$ has mean $p$, since $E[B_1] = 1 \cdot p + 0 \cdot q$. As $B_1^2 = B_1$, its variance is $E[B_1^2] - p^2 = p - p^2 = pq$. Since $0 < p < 1$, $0 < pq < \infty$.
7. Let $Z_n = (S_n - np)/\sqrt{npq}$ and $Z'_n = (T_n - np)/\sqrt{npq}$. Since $S_n$ and $T_n$ have the same law, $Z_n$ and $Z'_n$ have the same law. So $P(Z_n \in A) = P(Z'_n \in A)$ for each Borel set $A$.
8. By the [[central limit theorem|0EPZC4Z1FC]] with $\mu = p$ and $\sigma^2 = pq$, $P(Z'_n \le x) \to \Phi(x)$ for each $x \in \R$. Here $\Phi$ is the [[cumulative distribution function|0MXMS3AE13]] of the [[standard normal distribution|07RXBVTVZB]].
9. By step 7, $F_n(x) = P(Z_n \le x) \to \Phi(x)$ for each $x$. Since $\Phi$ is continuous, this is [[convergence in distribution|0JDAQHWA9N]] to $\mathcal{N}(0, 1)$.
10. Now fix reals $a < b$. Then $P(a \le Z_n \le b) = F_n(b) - P(Z_n < a)$.
11. For $\delta > 0$, $\set{Z_n \le a - \delta} \subseteq \set{Z_n < a} \subseteq \set{Z_n \le a}$. So $F_n(a - \delta) \le P(Z_n < a) \le F_n(a)$.
12. By step 9, $\Phi(a - \delta) \le \liminf_n P(Z_n < a) \le \limsup_n P(Z_n < a) \le \Phi(a)$.
13. The density of $\mathcal{N}(0, 1)$ is bounded by $1/\sqrt{2\pi}$, so $\Phi(a) - \Phi(a - \delta) \le \delta/\sqrt{2\pi}$. Let $\delta \to 0$ in step 12 to get $P(Z_n < a) \to \Phi(a)$.
14. By steps 9, 10 and 13, $P(a \le Z_n \le b) \to \Phi(b) - \Phi(a) = \int_a^b \frac{1}{\sqrt{2\pi}} e^{-x^2/2} \, dx$.

## Idea

A binomial count is a sum of $n$ independent Bernoulli trials with mean $p$ and variance $pq$. The central limit theorem gives the normal limit of the standardized count. Since the normal distribution function is continuous, the limit does not change if the end points are included or not.
