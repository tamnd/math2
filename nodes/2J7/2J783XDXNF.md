---
tag: 2J783XDXNF
kind: definition
name: Secret sharing
msc: [94A62, 94A60]
defines: RF8K6DV805
uses: [0BBTH3YSZA, 0DKRR22AEQ, 02MY6WZXEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Secret_sharing
---

## Definition

Let $S$ be a [[finite set|0BBTH3YSZA]] of secrets, and let $1 \le t \le n$ be integers.
A *$(t, n)$ threshold secret sharing scheme* consists of a randomized dealing procedure and reconstruction functions.
The dealer maps each secret $s \in S$ to a [[random|0DKRR22AEQ]] tuple of shares $(X_1, \dots, X_n)$, with $X_i$ in a finite set $S_i$ for participant $i$.
It satisfies the following two conditions.

1. Correctness: for each set $A \subseteq \set{1, \dots, n}$ with $\abs{A} \ge t$, there is a function $R_A$ such that $R_A((X_i)_{i \in A}) = s$ with probability $1$, for every secret $s$.
2. Perfect privacy: for each set $A$ with $\abs{A} < t$, the distribution of $(X_i)_{i \in A}$ is the same for every secret $s \in S$.

## Remarks

Example: the $(n, n)$ additive scheme on $S = \Z/m\Z$.
The dealer draws $X_1, \dots, X_{n-1}$ [[uniformly|02MY6WZXEQ]] and independently in $\Z/m\Z$ and sets $X_n = s - X_1 - \cdots - X_{n-1}$.
Correctness: all $n$ shares sum to $s$.
Privacy: any $n - 1$ of the shares are independent and uniform, whatever $s$ is.

Non-example: cut a secret string of $2k$ bits into two halves and give one half to each of two participants.
Both halves together give the secret, but one half alone reveals $k$ bits of it, so condition 2 fails for $t = 2$.

Schemes in which an access structure other than a threshold decides which sets may reconstruct are also studied.
