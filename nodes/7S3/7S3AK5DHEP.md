---
tag: 7S3AK5DHEP
kind: proof
name: Proof of the probability of the complement
msc: [60A05]
proves: 0PQEBTYDZM
uses: [0ZYBZ34RT2, 0VGMEBVW1M, 00SQGJNRTB, 0B1FSS1VZW, 04WSW8T3SY, 0A3GWZ86AY]
sources:
  - url: https://en.wikipedia.org/wiki/Probability_axioms
    locator: Elementary consequences
---

## Proof

1. Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]] and let $A \in \mathcal{F}$ be an [[event|00SQGJNRTB]].
2. The family $\mathcal{F}$ is a [[σ-algebra|04WSW8T3SY]]. So the [[complement|0B1FSS1VZW]] $A^c$ is in $\mathcal{F}$, and so is $\varnothing = \Omega^c$.
3. We first show $P(\varnothing) = 0$. Let $c = P(\varnothing)$, a number in $[0, 1]$.
4. The sets $E_n = \varnothing$ for $n \ge 1$ are pairwise disjoint and their union is $\varnothing$. By the countable additivity of the [[probability measure|0VGMEBVW1M]] $P$, we get $c = \sum_{n=1}^{\infty} c$.
5. Suppose that $c > 0$. By the [[Archimedean property|0A3GWZ86AY]], there is $N$ with $N c > 1$. Then the partial sums of $\sum_n c$ exceed $1$ from the index $N$ on, so the series does not converge to $c \le 1$.
6. This contradicts step 4. So $c = 0$, that is, $P(\varnothing) = 0$.
7. Now let $E_1 = A$, $E_2 = A^c$ and $E_n = \varnothing$ for $n \ge 3$. These sets are pairwise disjoint, because $A \cap A^c = \varnothing$ and $\varnothing$ meets no set.
8. Their union is $A \cup A^c = \Omega$.
9. Countable additivity and step 6 give $P(\Omega) = P(A) + P(A^c) + \sum_{n \ge 3} 0 = P(A) + P(A^c)$.
10. Since $P(\Omega) = 1$, we get $P(A) + P(A^c) = 1$. Hence $P(A^c) = 1 - P(A)$.

## Idea

An event and its complement split the sample space into two disjoint pieces. Additivity turns this split into a sum of probabilities, and the whole space has probability $1$. The only care needed is to get finite additivity from countable additivity, which uses $P(\varnothing) = 0$.
