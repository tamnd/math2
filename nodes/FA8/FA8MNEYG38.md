---
about:
- 0KRH5157WP
kind: statement
msc:
- 60J10
name: Limiting distribution of a regular transition matrix
role: theorem
sources:
- url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_kitchensink_markov-chains.ptx#L41
  locator: source/s_kitchensink_markov-chains.ptx:41
tag: FA8MNEYG38
uses:
- 0F462493EA
- 033TJBZDG0
- 0KRH5157WP
---

## Statement

Let $P$ be an $n \times n$ [[transition matrix|0F462493EA]] of a finite [[Markov chain|033TJBZDG0]] with states $S_1, \dots, S_n$.
Call $P$ regular if some power $P^k$ has only positive entries.

Assume that $P$ is regular. Then there is a row vector $W = (w_1, \dots, w_n)$ with these properties:

1. every $w_i$ is a positive real number, and $w_1 + \dots + w_n = 1$;
2. as $m \to \infty$, every row of $P^m$ converges to $W$;
3. $WP = W$, so $W$ is a [[stationary distribution|0KRH5157WP]];
4. for each $i$, the number $w_i$ is the limiting probability that the chain is in state $S_i$, whatever the starting state.

## Remarks

The vector $W$ is unique. It is the only probability vector fixed by $P$.
