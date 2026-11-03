---
tag: 5JDS6QXG5S
kind: definition
name: Busy Beaver function
msc: [03D10, 68Q04]
defines: 14YM2HVGHA
uses: [W6ESDYBF8Z, KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Busy_beaver
---

## Definition

Let $n \ge 1$.
An *$n$-state busy beaver candidate* is a [[Turing machine|W6ESDYBF8Z]] with the following properties.

1. Its states are $q_1, \dots, q_n$ and one extra halting state $H$, with initial state $q_1$.
2. Its tape alphabet is $\set{0, 1}$, with blank symbol $0$, and the tape is infinite in both directions.
3. Its transition function is total on $\set{q_1, \dots, q_n} \times \set{0, 1}$, with values in $\set{q_1, \dots, q_n, H} \times \set{0, 1} \times \set{L, R}$.

Each candidate is run on the tape with all cells $0$.
The *Busy Beaver function* $\Sigma(n)$ is the largest number of $1$s on the tape when the run halts, over all $n$-state candidates whose run halts.
The *maximum shift function* $S(n)$ is the largest number of steps of such a halting run, where the step into $H$ counts.

## Remarks

There are $(4n + 4)^{2n}$ candidates, and at least one of them halts, so both maxima exist.
Example: for $n = 1$, the candidate with $\delta(q_1, 0) = (H, 1, R)$ halts after one step with one $1$, so $\Sigma(1) \ge 1$.
Every other $1$-state candidate either halts at once with at most one $1$ or never halts, so $\Sigma(1) = 1$ and $S(1) = 1$.
Known values: $\Sigma(2) = 4$, $\Sigma(3) = 6$, $\Sigma(4) = 13$, $\Sigma(5) = 4098$, and $S(2) = 6$, $S(3) = 21$, $S(4) = 107$, $S(5) = 47{,}176{,}870$.
Non-example: a machine that writes $1$s forever is not counted, because only halting runs enter the maximum.
For every total [[computable function|KZSB5E471K]] $g \colon \N \to \N$ there is $N$ with $\Sigma(n) > g(n)$ for all $n \ge N$.
Hence $\Sigma$ and $S$ are not computable.
If $S$ were computable, the halting problem on blank tape would be decidable: run an $n$-state candidate for $S(n)$ steps and see whether it has halted.
