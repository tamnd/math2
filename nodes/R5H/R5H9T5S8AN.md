---
tag: R5H9T5S8AN
kind: statement
role: theorem
name: No free lunch theorem for optimization
msc: [90C59, 68T20, 90C26]
uses: [ZCFQEZ0A0V]
about: [ZCFQEZ0A0V]
sources:
  - url: https://en.wikipedia.org/wiki/No_free_lunch_in_search_and_optimization
same_as:
  wikidata: Q255847
  wikipedia: No free lunch in search and optimization
---

## Statement

Let $X$ and $Y$ be finite sets, with $Y \subseteq \R$, and let $F = Y^X$ be the set of all functions $f \colon X \to Y$.
A *search algorithm* $a$ chooses points $x_1, x_2, \dots$ of $X$ one at a time, never twice the same point.
Each choice $x_{i+1}$ depends only on the pairs $(x_1, f(x_1)), \dots, (x_i, f(x_i))$ seen so far, possibly with randomness.
For $1 \le m \le \abs{X}$, let $d^y_m = (f(x_1), \dots, f(x_m))$ be the sequence of values seen in the first $m$ steps.
Then for any two search algorithms $a_1$ and $a_2$, any $m$, and any sequence $c \in Y^m$,
$$\sum_{f \in F} P(d^y_m = c \mid f, m, a_1) = \sum_{f \in F} P(d^y_m = c \mid f, m, a_2).$$

## Remarks

The proof is by induction on $m$.
Once $m$ distinct points have been visited, the values of $f$ at the unvisited points are still arbitrary as $f$ ranges over $F$.
So, summed over all $f$, the next value seen is equally likely to be any element of $Y$, whatever point the algorithm picks.

Consequence: any performance measure that depends only on $d^y_m$, such as the best value found after $m$ steps, has the same average over all $f \in F$ for every algorithm.
For example, averaged over all $f \colon X \to Y$, a random search without repetitions does exactly as well as [[simulated annealing|578AX75H88]] run without repeated points.

The hypothesis that the average is over all of $Y^X$, the uniform prior, is essential.
More generally the conclusion holds for a set of functions closed under permutations of $X$.
For a restricted class, such as convex functions on a grid, some algorithms beat others on average.

The theorem was published by Wolpert and Macready in 1997.

## Explanations

### L1 human

No search method is better than any other when you average over every possible problem.
If a method does well on some functions, it must do worse on others to make up for it.
So an optimization method is good only relative to a class of problems with some structure that it exploits.

### L2 human

The theorem compares black-box algorithms that see only function values.
It does not say that all optimization methods are equally good in practice, since real problems are far from uniformly random.
It explains why methods such as [[simulated annealing|578AX75H88]] or genetic algorithms need assumptions about the problem class to be justified.
In [[global optimization|ZCFQEZ0A0V]], it is one reason why deterministic guarantees require structure such as Lipschitz bounds or convex relaxations.
