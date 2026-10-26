---
tag: 0C5RDJE73X
kind: statement
role: theorem
name: Number of subsets of a finite set
msc: [05A05]
uses: [05099E1NMJ, 08QQH9F7G0]
sources:
  - url: https://en.wikipedia.org/wiki/Power_set
    locator: Properties
---

## Statement

Let $X$ be a finite set with $|X| = n$.
Let $\mathcal{P}(X)$ be the power set of $X$, the set of all subsets of $X$.
Then $|\mathcal{P}(X)| = 2^n$.

## Remarks

The map that sends a subset $S$ to its indicator function $1_S : X \to \{0, 1\}$ is a bijection. Thus the count follows from the [[number of functions between finite sets|08QQH9F7G0]].
Grouped by size, the count gives the identity in the node [[sum of binomial coefficients|0KAMF19NV8]].

## Explanations

### L1 human

To build a subset, decide for each element whether it is in or out.
That is 2 options per element, so $2 \cdot 2 \cdots 2 = 2^n$ subsets. For $\{a, b\}$ these are $\varnothing$, $\{a\}$, $\{b\}$ and $\{a, b\}$.
