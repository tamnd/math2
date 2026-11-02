---
tag: X5KD3X3VJ3
kind: definition
name: Algorithmic randomness
msc: [03D32, 68Q30]
defines: KW3V44GPPC
uses: [W9VYJRBF9N, TN9G24VABN, 8PY3K6NCKF]
sources:
  - url: https://en.wikipedia.org/wiki/Algorithmically_random_sequence
---

## Definition

Let $2^\omega$ be [[Cantor space|W9VYJRBF9N]], the set of infinite binary sequences.
For a finite binary string $\sigma$ of length $\abs{\sigma}$, let $[\sigma] \subseteq 2^\omega$ be the set of sequences that begin with $\sigma$.
Let $\mu$ be the uniform measure on $2^\omega$, with $\mu([\sigma]) = 2^{-\abs{\sigma}}$.
A *Martin-Löf test* is a sequence $(U_n)_{n \in \N}$ of subsets of $2^\omega$ such that:

1. there is a [[computably enumerable|TN9G24VABN]] set $W$ of pairs $(n, \sigma)$ with $U_n = \bigcup \set{[\sigma] : (n, \sigma) \in W}$ for every $n$;
2. $\mu(U_n) \le 2^{-n}$ for every $n$.

A sequence $X \in 2^\omega$ is *Martin-Löf random*, or *algorithmically random*, if $X \notin \bigcap_n U_n$ for every Martin-Löf test $(U_n)$.

## Remarks

Example: the binary expansion of Chaitin's halting probability $\Omega$ is Martin-Löf random.
Also, the set of non-random sequences has measure $0$, because there is a universal Martin-Löf test whose intersection contains every non-random sequence.

Non-example: a computable sequence $X$ is not random.
Let $X \upharpoonright n$ be the string of the first $n$ bits of $X$.
The sets $U_n = [X \upharpoonright n]$ form a Martin-Löf test: they are uniformly computable and $\mu(U_n) = 2^{-n}$.
And $X$ lies in all of them.

The Levin–Schnorr theorem gives an equivalent form with [[Kolmogorov complexity|8PY3K6NCKF]].
Let $K$ be prefix-free complexity.
Then $X$ is Martin-Löf random if and only if there is a constant $c$ with $K(X \upharpoonright n) \ge n - c$ for all $n$.
