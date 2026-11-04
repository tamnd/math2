---
tag: Y7PDDFZZC3
kind: proof
name: Proof that rearrangements of an absolutely convergent series have the same sum
msc: [40A05]
proves: 0J76TP9FGD
uses: [0W3K3QPEWT, 0HRJ2Y74T3, 0MX1HZBBXJ, 03HF5PMY5T, 0XKWSSY8P2, 0Y123X48GA]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_convergence
    locator: Proof of the theorem
---

## Proof

Let $T = \sum_{n=0}^{\infty} \abs{a_n}$, and let $t_K = \sum_{k=0}^{K} \abs{a_k}$ and $s_K = \sum_{k=0}^{K} a_k$. The series $\sum a_n$ converges, with sum $A$, since [[absolutely convergent series converge|0Y123X48GA]]. Let $B_N = \sum_{n=0}^{N} a_{\sigma(n)}$ be the partial sums of the [[rearrangement|0HRJ2Y74T3]].

1. By the [[criterion for nonnegative series|0MX1HZBBXJ]], $t_K \le T$ for every $K$.
2. Let $N$ be a natural number and let $K = \max \set{\sigma(0), \dots, \sigma(N)}$. Since $\sigma$ is injective, the indices $\sigma(0), \dots, \sigma(N)$ are distinct elements of $\set{0, \dots, K}$.
3. So $\sum_{n=0}^{N} \abs{a_{\sigma(n)}} \le t_K \le T$, because the terms are nonnegative.
4. The partial sums of $\sum \abs{a_{\sigma(n)}}$ are bounded above by $T$. By the same criterion, the rearrangement [[converges absolutely|0W3K3QPEWT]].
5. Let $\varepsilon > 0$. Since $t_M \to T$ and $s_M \to A$, there is $M$ with $T - t_M < \varepsilon$ and $\abs{s_M - A} < \varepsilon$, by the definition of the [[limit|0XKWSSY8P2]].
6. Since $\sigma$ is surjective, each of $0, 1, \dots, M$ equals $\sigma(n)$ for some $n$. Let $N_0$ be the largest of these $M + 1$ values of $n$.
7. Let $N \ge N_0$. Then $\set{0, \dots, M} \subseteq \sigma(\set{0, \dots, N})$. Let $D = \sigma(\set{0, \dots, N}) \setminus \set{0, \dots, M}$, a finite set of indices larger than $M$.
8. Since $\sigma$ is injective, $B_N = \sum_{k \in \sigma(\set{0, \dots, N})} a_k = s_M + \sum_{k \in D} a_k$.
9. Let $K$ be an integer at least $M$ and every element of $D$. By the [[triangle inequality|03HF5PMY5T]] and step 1, $\abs{\sum_{k \in D} a_k} \le \sum_{k=M+1}^{K} \abs{a_k} = t_K - t_M \le T - t_M < \varepsilon$.
10. By steps 5, 8 and 9, $\abs{B_N - A} \le \abs{s_M - A} + \abs{\sum_{k \in D} a_k} < 2\varepsilon$ for all $N \ge N_0$.
11. So $B_N \to A$. The rearrangement converges absolutely, and its sum is $A$.

## Idea

Fix a long initial block $a_0, \dots, a_M$ whose sum is close to $A$ and whose tail of absolute values is small. A long enough partial sum of the rearrangement contains this whole block, plus some terms from the tail. Those extra terms have small total size, so they cannot move the sum much.
