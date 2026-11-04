---
tag: EQ5ETQ5XKV
kind: proof
name: Proof that the harmonic series diverges by grouping terms
msc: [40A05]
proves: 0E9M24KS9J
uses: [0CXTMAY5PX, 0D2Y6G4C4S, 09AZCV6GMC, 0A74SX55QP, 0S4JF619V7, 0NBRP6093V]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)
    locator: Comparison test
---

## Proof

We bound the [[harmonic numbers|0D2Y6G4C4S]] at powers of $2$ from below, by induction.

1. For $N \ge 1$, $H_N = \sum_{n=1}^{N} 1/n$. Since $H_{N+1} = H_N + 1/(N+1) > H_N$, the sequence $(H_N)$ is increasing.
2. Let $j \ge 1$. The block of terms $1/n$ with $2^{j-1} < n \le 2^j$ has $2^j - 2^{j-1} = 2^{j-1}$ terms.
3. Each term in that block satisfies $1/n \ge 1/2^j$. So the block has sum at least $2^{j-1}/2^j = 1/2$.
4. We claim $H_{2^k} \ge 1 + k/2$ for every natural number $k$. For $k = 0$, $H_1 = 1$.
5. Assume the claim for $k$. Then $H_{2^{k+1}} = H_{2^k} + \sum_{2^k < n \le 2^{k+1}} 1/n$. By step 3 with $j = k + 1$, this is at least $1 + k/2 + 1/2$.
6. By induction, steps 4 and 5 prove the claim for every $k$.
7. Let $M$ be a real number. By the [[Archimedean property|0A74SX55QP]] there is a natural number $k$ with $2(M - 1) < k$, that is, $1 + k/2 > M$.
8. Let $N_0 = 2^k$. For $N \ge N_0$, steps 1, 4 and 7 give $H_N \ge H_{N_0} \ge 1 + k/2 > M$.
9. So $H_N \to +\infty$, in the sense of a [[sequence tending to infinity|09AZCV6GMC]].
10. In particular $(H_N)$ is not bounded. [[Convergent sequences are bounded|0S4JF619V7]], so $(H_N)$ does not converge.
11. The $H_N$ are the partial sums of the [[harmonic series|0CXTMAY5PX]]. So the harmonic series is a [[divergent series|0NBRP6093V]].

## Idea

Group the terms in blocks that end at powers of $2$: $\frac12$, then $\frac13 + \frac14$, then $\frac15 + \cdots + \frac18$, and so on. Each block has sum at least $\frac12$. Infinitely many halves add up to infinity.
