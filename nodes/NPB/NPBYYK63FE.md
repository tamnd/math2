---
tag: NPBYYK63FE
kind: counterexample
name: Cantor function
msc: [26A30, 26A48]
uses: [0BXNDZFQME, 0WFF6AZPBP, 0P27W9RW0G, 0F1WR9C83K, ZT6F4C2YHK, P5AWRD2793, 0NHGY0N0JB]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor_function
    locator: Definition
same_as:
  wikidata: Q938883
  wikipedia: Cantor function
---

## Counterexample

Let $C \subseteq [0, 1]$ be the [[Cantor set|0BXNDZFQME]].
For $x \in [0, 1]$, write $x$ in base $3$ as $x = 0.a_1 a_2 a_3 \ldots$ with $a_k \in \set{0, 1, 2}$.
If some digit equals $1$, delete all digits after the first $1$.
Then replace each digit $2$ by $1$, and read the result $0.b_1 b_2 b_3 \ldots$ in base $2$.
The value is $c(x) = \sum_k b_k 2^{-k}$, and it does not depend on the choice of the base-$3$ expansion.

The function $c \colon [0, 1] \to [0, 1]$ is [[continuous|0P27W9RW0G]] and nondecreasing, with $c(0) = 0$ and $c(1) = 1$.
It is constant on each open interval removed in the construction of $C$, for example $c(x) = 1/2$ on $(1/3, 2/3)$.
So $c'(x) = 0$ at every point of $[0, 1] \setminus C$.
The Cantor set is a null set, so $c' = 0$ almost everywhere.
But $c$ is not constant.

## Remarks

The function refutes the claim that a continuous function with derivative $0$ almost everywhere is constant.
It also shows that the [[fundamental theorem of calculus|0NHGY0N0JB]] in the form $\int_0^1 f' = f(1) - f(0)$ can fail for a continuous [[monotone function|0WFF6AZPBP]] differentiable almost everywhere.
Here $\int_0^1 c'(x) \, dx = 0$, while $c(1) - c(0) = 1$.
So $c$ is not [[absolutely continuous|ZT6F4C2YHK]]; it is the standard example of a [[singular function|P5AWRD2793]].
It maps the null set $C$ onto all of $[0, 1]$.
Its graph is often called the devil's staircase.

## Explanations

### L1 human

The Cantor function climbs from $0$ to $1$ without jumps, yet it is flat almost everywhere.
All its growth happens on the Cantor set, a dust of points with total length zero.
On the middle third it sits at height $1/2$, on the next two middle thirds at heights $1/4$ and $3/4$, and so on.
So knowing that the derivative is zero almost everywhere does not tell you the function is constant.
