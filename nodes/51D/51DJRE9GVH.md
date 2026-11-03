---
tag: 51DJRE9GVH
kind: definition
name: Randomized algorithm
msc: [68W20, 68Q87]
defines: 2Y50S7GQTD
uses: [9DMSG5HAQX, K99S0Q0814, 0PNRKMRC55, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Randomized_algorithm
---

## Definition

A *randomized algorithm* is an [[algorithm|9DMSG5HAQX]] that, besides its input $x$, reads a sequence $r$ of independent uniformly random bits.
Its steps may depend on the values of these bits.
For a fixed input $x$, its output $A(x)$ and its running time $T(x)$ are [[random variables|0PNRKMRC55]] that depend on $r$.
Two kinds are standard.

1. A *Las Vegas algorithm* always gives a correct output, and its quality is measured by the [[expected value|0WQNRCNY3M]] of $T(x)$.
2. A *Monte Carlo algorithm* has a running time bounded by a function of the input size. It may give a wrong output with bounded probability.

A formal model is the [[probabilistic Turing machine|K99S0Q0814]].

## Remarks

Example: randomized quicksort chooses each pivot uniformly at random among the current items.
It always returns the sorted list, so it is Las Vegas, and its expected number of comparisons is $O(n \log n)$ for every input of $n$ distinct items.

Example: to test whether $AB = C$ for $n \times n$ matrices, Freivalds' algorithm picks a random vector $v \in \set{0, 1}^n$ and checks $A(Bv) = Cv$ in time $O(n^2)$.
If $AB = C$ it always says yes; if $AB \ne C$ it says yes with probability at most $1/2$, so it is Monte Carlo with one-sided error.

Non-example: an algorithm that runs on a fixed pseudorandom seed stored in its code makes no random choices, so it is deterministic.

The error probability of a Monte Carlo algorithm can be reduced by running it several times with independent random bits.
