---
tag: MQZG6X2TTN
kind: definition
name: Distributed source coding
msc: [94A29, 94A15]
defines: VKETGMSX5H
uses: [00MRN0FARV, 0D6J4B671D]
sources:
  - url: https://en.wikipedia.org/wiki/Distributed_source_coding
---

## Definition

Let $\mathcal{X}$ and $\mathcal{Y}$ be finite sets and let $(X_1, Y_1), (X_2, Y_2), \dots$ be [[i.i.d.|00MRN0FARV]] pairs with a joint [[probability mass function|0D6J4B671D]] $p$ on $\mathcal{X} \times \mathcal{Y}$.
Let $n \ge 1$ and $M_1, M_2 \ge 1$ be integers.
A *distributed source code* with parameters $(M_1, M_2, n)$ consists of the following maps.

1. An encoder $f_1 \colon \mathcal{X}^n \to \set{1, \dots, M_1}$, which sees only $X^n = (X_1, \dots, X_n)$.
2. An encoder $f_2 \colon \mathcal{Y}^n \to \set{1, \dots, M_2}$, which sees only $Y^n = (Y_1, \dots, Y_n)$.
3. A decoder $g \colon \set{1, \dots, M_1} \times \set{1, \dots, M_2} \to \mathcal{X}^n \times \mathcal{Y}^n$.

Its error probability is $P_e = \Pr\big(g(f_1(X^n), f_2(Y^n)) \ne (X^n, Y^n)\big)$.
A rate pair $(R_1, R_2)$ of non-negative reals is *achievable* if there are codes with parameters $(\ceil{2^{nR_1}}, \ceil{2^{nR_2}}, n)$ whose error probabilities tend to $0$ as $n \to \infty$.
*Distributed source coding* is the study of the set of achievable rate pairs, and of its analogues for more sources and for lossy recovery.

## Remarks

Example: if $X_i = Y_i$ for all $i$ and $X_1$ is a uniform bit, then $(1, 0)$ is achievable.
Take $M_1 = 2^n$, let $f_1$ send $X^n$ in full, let $f_2$ be constant, and let $g$ output $X^n$ twice; the error probability is $0$.
Non-example: a scheme in which the first encoder also sees $Y^n$ is not a distributed source code, since clause 1 forbids it.
The achievable pairs are described by the Slepian–Wolf theorem.
