---
tag: N3RD9BNKQA
kind: statement
role: theorem
name: Converse of the channel coding theorem
msc: [94A24, 94A40]
uses: [B9C5RBFATB, J7MZ2XQP9M, E3A9MPV1QY, BGH1T3HKPV]
about: [J7MZ2XQP9M]
sources:
  - url: https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem
---

## Statement

Let $(\mathcal{X}, W, \mathcal{Y})$ be a discrete memoryless [[channel|B9C5RBFATB]] with [[capacity|J7MZ2XQP9M]] $C$ in bits.
Let $e \colon \set{1, \dots, M} \to \mathcal{X}^n$ and $d \colon \mathcal{Y}^n \to \set{1, \dots, M}$ be a code of length $n$ with $M \ge 2$ messages.
Let the message $U$ be uniform on $\set{1, \dots, M}$, sent as $e(U)$, and let $P_e = \Pr(d(Y^n) \ne U)$ be the average error probability.
If $M \ge 2^{nR}$ for some $R > 0$, then
$$P_e \ge 1 - \frac{C}{R} - \frac{1}{nR}.$$
In particular, if $R > C$ and codes with $M \ge 2^{nR}$ are used for every $n$, then $P_e$ does not tend to $0$.

## Remarks

The proof combines three facts.
[[Fano's inequality|E3A9MPV1QY]] gives $H(U \mid d(Y^n)) \le 1 + P_e \log_2 M$.
The [[data processing inequality|BGH1T3HKPV]] and memorylessness give $I(U; d(Y^n)) \le I(e(U); Y^n) \le nC$.
Since $\log_2 M = H(U) = H(U \mid d(Y^n)) + I(U; d(Y^n))$, one gets $\log_2 M \le 1 + P_e \log_2 M + nC$, and the bound follows.

Example: at rate $R = 2C$ the bound gives $P_e \ge 1/2 - 1/(nR)$, so the average error probability is at least about $1/2$.
The strong converse, due to Wolfowitz, says more: for $R > C$ the error probability tends to $1$.

## Explanations

### L1 human

Sending faster than the capacity always costs errors, however clever the code.
The faster one goes beyond capacity, the larger the unavoidable fraction of errors.

### L2 human

Together with the noisy-channel coding theorem, this shows that capacity is the exact threshold between possible and impossible rates.
The proof is a short chain of entropy inequalities, and the same pattern proves converses in many multi-user problems.
This is the weak form of the converse; it bounds the average error, and hence also the maximal error.
