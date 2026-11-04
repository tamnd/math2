---
tag: 2TGSAHD1K1
kind: proof
name: Proof of the monotonicity of the cumulative distribution function
msc: ["60E05"]
proves: 0XD22PBMWA
uses: [0MXMS3AE13, 0DKRR22AEQ, 0BVHZXWKCD, 0G5AV9Q4RR, 01ZQQDCERP, 0464Z0JP2E]
sources:
  - url: https://proofwiki.org/wiki/Cumulative_Distribution_Function_is_Increasing
---

## Proof

1. Let $X$ be a real [[random variable|0DKRR22AEQ]] on a probability space $(\Omega, \mathcal{F}, P)$, with [[cumulative distribution function|0MXMS3AE13]] $F_X(t) = P(X \le t)$.
2. Let $t \in \R$. The complement of $(-\infty, t]$ is $(t, \infty)$, which is [[open|01ZQQDCERP]]. So $(-\infty, t]$ is [[closed|0G5AV9Q4RR]].
3. The [[Borel σ-algebra|0BVHZXWKCD]] contains the open set $(t, \infty)$ and is closed under complements. So it contains $(-\infty, t]$.
4. Since $X$ is a random variable, $\set{X \le t} = X^{-1}((-\infty, t])$ is in $\mathcal{F}$.
5. Let $x \le y$ be real numbers. If $\omega \in \Omega$ satisfies $X(\omega) \le x$, then $X(\omega) \le y$. So $\set{X \le x} \subseteq \set{X \le y}$.
6. By step 4 both sets are events. By [[monotonicity of probability|0464Z0JP2E]], $P(X \le x) \le P(X \le y)$, that is, $F_X(x) \le F_X(y)$.

## Idea

Raising the threshold from $x$ to $y$ can only enlarge the event $\set{X \le x}$. A larger event has at least the same probability.
