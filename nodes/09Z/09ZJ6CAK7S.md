---
tag: 09ZJ6CAK7S
kind: statement
role: proposition
name: The number of Sylow subgroups is the index of the normaliser
msc: [20D20]
uses: [09GCQ5STVJ, 0AT1ZSNM25, 0E2HSCKZ6C]
sources:
  - url: https://en.wikipedia.org/wiki/Sylow_theorems
    locator: Statement
---

## Statement

Let $G$ be a finite [[group|G5S1M9]], let $p$ be a prime number, and let $P$ be a [[Sylow p-subgroup|0053CQE9Y2]] of $G$.
Then $n_p = [G : N_G(P)]$, where $N_G(P)$ is the [[normaliser|0YGN3VAA0D]] of $P$.

## Remarks

By the [[second Sylow theorem|09GCQ5STVJ]], $G$ acts transitively by conjugation on $\operatorname{Syl}_p(G)$.
The stabiliser of $P$ is $N_G(P)$, so the [[orbit-stabiliser theorem|0E2HSCKZ6C]] gives the formula.
In particular, $P$ is normal in $G$ if and only if $n_p = 1$.

## Explanations

### L1 human

All Sylow $p$-subgroups are conjugates of one of them, $P$.
The number of conjugates of $P$ is the number of cosets of the elements that do not move $P$.
These elements form the normaliser.
