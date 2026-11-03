---
tag: XQQVHNQ3FW
kind: definition
name: ZPP
msc: [68Q15, 68Q10, 68W20]
defines: QJZ5ZY0HJ8
uses: [K99S0Q0814, ESPYW94XGR, TPDMV6ZXN3]
sources:
  - url: https://en.wikipedia.org/wiki/ZPP_(complexity)
---

## Definition

A language $L \subseteq \set{0,1}^*$ is in *ZPP* if there are a polynomial $p$ and a [[probabilistic Turing machine|K99S0Q0814]] $M$ such that, for every input $x$:

1. $M$ halts with probability $1$, and when it halts it outputs $1$ if $x \in L$ and $0$ if $x \notin L$;
2. the expected number of steps of $M$ on $x$, over its coin flips, is at most $p(\abs{x})$.

## Remarks

Equivalently, $\mathrm{ZPP} = \mathrm{RP} \cap \text{co-RP}$, with [[RP|TPDMV6ZXN3]] the class of one-sided error.
Suppose $L$ has an RP machine $M_1$ and its complement has an RP machine $M_2$.
Run both in rounds until one of them accepts.
An accepting run of $M_1$ proves $x \in L$, and an accepting run of $M_2$ proves $x \notin L$.
Each round succeeds with probability at least $1/2$, so the expected number of rounds is at most $2$.
Conversely, by Markov's inequality a ZPP machine stopped after $2p(\abs{x})$ steps has halted with probability at least $1/2$, which gives RP machines for $L$ and its complement.

Example: every language in P is in ZPP, using a machine that ignores its coins.

Non-example: a machine that runs in polynomial time but answers wrongly with probability $1/10$ on some input fails clause 1.

Another equivalent form: there is a polynomial-time machine with outputs $0$, $1$ and "?" that never gives a wrong $0$ or $1$ and outputs "?" with probability at most $1/2$.
