---
tag: 10CAVBDDDS
kind: definition
name: Locally testable code
msc: [94B60, 68W20]
defines: V1D34JFQ1T
uses: [TAE6K8NQ46, EP5HNGSXFA, 2Y50S7GQTD, HSXZD57ABX, 7S3WHBHJTZ]
sources:
  - url: https://en.wikipedia.org/wiki/Locally_testable_code
---

## Definition

Let $\Sigma$ be a finite alphabet, let $n$ and $q$ be positive integers, and let $\rho > 0$ be a real number.
Let $C \subseteq \Sigma^n$ be a nonempty code, and for $w \in \Sigma^n$ let $\delta(w, C) = \min_{c \in C} d(w, c) / n$, where $d$ is the [[Hamming distance|EP5HNGSXFA]].
The code $C$ is $(q, \rho)$-*locally testable* if there is a [[randomized algorithm|2Y50S7GQTD]] $T$, the tester, with oracle access to a word $w \in \Sigma^n$, such that:

1. $T$ reads at most $q$ positions of $w$ and then accepts or rejects.
2. If $w \in C$, then $T$ accepts with probability $1$.
3. For every $w \in \Sigma^n$, $T$ rejects with probability at least $\rho \cdot \delta(w, C)$.

## Remarks

Example: the binary [[Hadamard code|HSXZD57ABX]] of length $2^k$ is the set of linear functions $\F_2^k \to \F_2$, written as words indexed by $\F_2^k$.
The linearity test of Blum, Luby and Rubinfeld picks $a, b \in \F_2^k$ at random, reads $w(a)$, $w(b)$, $w(a + b)$, and accepts if $w(a) + w(b) = w(a + b)$.
Linear functions are always accepted.
[[Fourier analysis on the Boolean cube|7S3WHBHJTZ]] shows that the rejection probability is at least $\delta(w, C)$, so the code is $(3, 1)$-locally testable.

Non-example: the tester that always accepts satisfies clauses 1 and 2, but it fails clause 3 for any word $w \notin C$, since then $\delta(w, C) > 0$.

Other versions of the definition only ask that words with $\delta(w, C) \ge \delta_0$ are rejected with probability at least a constant; the version above is often called strong local testability.
