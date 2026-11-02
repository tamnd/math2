---
tag: K9JAYYA0WS
kind: statement
role: theorem
name: Fractional Helly theorem
msc: [52A35]
uses: [02AS45T3H9, F1W3QRBNGJ]
about: [02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Helly's_theorem
---

## Statement

Let $d \ge 1$ be an integer and let $\alpha \in (0, 1]$.
There is a number $\beta = \beta(d, \alpha) > 0$ with the following property.
Let $\mathcal{F}$ be a finite family of $n \ge d + 1$ [[convex sets|02AS45T3H9]] in $\R^d$.
Assume that at least $\alpha \binom{n}{d+1}$ of the subfamilies of $\mathcal{F}$ with $d + 1$ members have a common point.
Then some point of $\R^d$ lies in at least $\beta n$ members of $\mathcal{F}$.

## Remarks

The theorem is due to Katchalski and Liu.
One can take $\beta = 1 - (1 - \alpha)^{1/(d+1)}$, a value found by Kalai, and this value is the best possible.
A proof looks at the lexicographically smallest points of the nonempty intersections of $d$-element subfamilies and counts how often each such point is caught by the $(d+1)$-subfamilies.
For $\alpha = 1$ every $d + 1$ members meet, and [[Helly's theorem|F1W3QRBNGJ]] gives a point in all $n$ members.
The constant $\beta$ depends only on $d$ and $\alpha$, not on $n$ or on the sets.

## Explanations

### L1 human

Helly's theorem says: if every $d + 1$ convex sets of a family meet, then all of them meet.
The fractional version asks for less and gives less.
If only a fixed fraction of the $(d+1)$-tuples meet, then a fixed fraction of all the sets still share a point.
So "many local meetings" force "one big meeting".

### L2 human

The fractional Helly theorem is the key step in the proof of the $(p, q)$-theorem of Alon and Kleitman.
It is a basic tool in the theory of geometric transversals.
Together with [[Helly's theorem|F1W3QRBNGJ]] and the [[centerpoint theorem|BWEGTCW5RJ]], it belongs to the core of combinatorial convexity.
