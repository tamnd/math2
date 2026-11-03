---
tag: 7V5GDQZXN5
kind: statement
role: theorem
name: AKS sorting network
msc: [68P10, 68Q06, 05C48]
uses: [G854V12EC7, 0TGV80E6A4, DXJXVFV79H]
about: [G854V12EC7]
sources:
  - url: https://en.wikipedia.org/wiki/Sorting_network
---

## Statement

There is a constant $C > 0$ with the following property.
For every integer $n \ge 2$ there is a [[sorting network|G854V12EC7]] on $n$ inputs of depth at most $C \log n$.
In particular it uses at most $C n \log n$ comparators, that is, $O(n \log n)$ in [[big O notation|0TGV80E6A4]].

## Remarks

The result is due to Miklós Ajtai, János Komlós and Endre Szemerédi (1983), and the network is called the AKS network after them.
The construction moves elements in rounds towards their correct place in a tree of intervals.
Each round uses comparator layers placed along bipartite [[expander graphs|DXJXVFV79H]].
These layers separate small and large elements up to a small fraction of errors, which later rounds correct.
Both bounds are optimal up to the constant.
A network that sorts $n$ inputs must distinguish all $n!$ orders.
So it has at least $\log_2(n!)$ comparators, which is of order $n \log n$.
A layer has at most $n/2$ comparators, so the depth is at least of order $\log n$.
The constant in the original proof is very large, and a later simplification by Michael Paterson reduced it but did not make it practical.
For the sizes met in practice, [[Batcher odd–even mergesort|67V6XW3W1N]] and the [[bitonic sorter|RP5A709FVZ]], of depth of order $\log^2 n$, use fewer comparators.

## Explanations

### L1 human

A sorting network is a fixed wiring of compare-and-swap boxes that sorts any input.
Simple constructions need about $(\log n)^2$ parallel rounds.
The AKS theorem says that about $\log n$ rounds are enough, which is the best possible order.
The catch is that the hidden constant is enormous, so the result is mainly of theoretical interest.

### L2 human

In a parallel model where each round may do many disjoint comparisons, the theorem gives an oblivious sorting procedure of optimal depth $O(\log n)$ and optimal work $O(n \log n)$.
It matches the information-theoretic lower bound of order $n \log n$ for comparison sorting.
Its key tool is the expander graph: a sparse bipartite graph whose comparators push almost every element to the correct side in constant depth.
Batcher's networks remain the practical choice, and the AKS network shows what is possible in principle.
The [[zero–one principle|FMR0TZ9Z88]] is a common tool for checking that such networks sort.
