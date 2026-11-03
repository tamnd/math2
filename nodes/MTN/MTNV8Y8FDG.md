---
tag: MTNV8Y8FDG
kind: statement
role: theorem
name: Shannon's perfect secrecy theorem
msc: [94A60, 68P25]
uses: [7YNRCX56CM, MATWVFGKTD, 0990W5PN13, 02MY6WZXEQ]
about: [MATWVFGKTD]
sources:
  - url: https://en.wikipedia.org/wiki/One-time_pad
---

## Statement

Let $\mathcal{M}$, $\mathcal{K}$ and $\mathcal{C}$ be finite sets of messages, keys and ciphertexts.
Consider a [[cryptosystem|7YNRCX56CM]] with encryption maps $e_k \colon \mathcal{M} \to \mathcal{C}$.
The key $K$ is drawn from a fixed distribution on $\mathcal{K}$, independently of the message $M$, and $C = e_K(M)$.
The system has *perfect secrecy* if the following holds for every distribution of $M$ on $\mathcal{M}$.
For every $m \in \mathcal{M}$ and every $c \in \mathcal{C}$ with $\Pr[C = c] > 0$, the [[conditional probability|0990W5PN13]] satisfies $\Pr[M = m \mid C = c] = \Pr[M = m]$.

1. The [[one-time pad|MATWVFGKTD]] has perfect secrecy.
2. If the system has perfect secrecy, then $\abs{\mathcal{K}} \ge \abs{\mathcal{M}}$.
3. Let $\abs{\mathcal{M}} = \abs{\mathcal{K}} = \abs{\mathcal{C}}$. Then it has perfect secrecy if and only if $K$ is [[uniform|02MY6WZXEQ]] on $\mathcal{K}$ and each pair $(m, c)$ has exactly one key $k$ with $e_k(m) = c$.

## Remarks

For part 1, each ciphertext $c$ arises from a message $m$ by exactly one key, $k = m \oplus c$.
So $\Pr[C = c \mid M = m] = 2^{-n}$ for every $m$, and Bayes' rule gives $\Pr[M = m \mid C = c] = \Pr[M = m]$.
For part 2, take $M$ uniform and a ciphertext $c$ with $\Pr[C = c] > 0$.
At most $\abs{\mathcal{K}}$ messages can be encrypted to $c$, one per key.
If $\abs{\mathcal{K}} < \abs{\mathcal{M}}$, some message $m$ has $\Pr[M = m \mid C = c] = 0 \ne 1/\abs{\mathcal{M}}$.
The shift cipher on a single letter, with a uniform key in $\Z/26\Z$, satisfies part 3, so it is perfectly secret.
Used with one key on messages of two letters, it is not, since then there are fewer keys than messages.

## Explanations

### L1 human

Perfect secrecy means that seeing the ciphertext does not change what an eavesdropper believes about the message, even with unlimited computing power.
The one-time pad achieves it.
The theorem also says that perfect secrecy is expensive: there must be at least as many keys as possible messages.

### L2 human

Part 2 is the reason modern cryptography works with computational security instead.
Definitions such as semantic security only ask that an efficient adversary learns almost nothing, and then short keys can encrypt long messages.
Part 3 characterizes the perfectly secret systems with the smallest key space, and the one-time pad is the main example.
In terms of entropy, perfect secrecy says that the message and the ciphertext are independent, so their mutual information is $0$.
