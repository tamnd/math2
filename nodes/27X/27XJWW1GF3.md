---
tag: 27XJWW1GF3
kind: problem
name: Linear search problem
msc: [90B40, 68W27]
uses: [0DVDCMA2DK, 0WQNRCNY3M]
about: [WV2JPYXMW3]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_search_problem
same_as:
  wikidata: Q6553518
  wikipedia: Linear search problem
history:
  posed_by: "Richard Bellman"
  first_stated: "1963"
  notes: "Posed by Bellman and considered independently by Anatole Beck in 1964."
---

## Problem

A searcher starts at the origin of the real line $\R$ and moves with speed at most $1$.
A hidden object lies at an unknown point $X \ne 0$, which is a random variable with a known [[probability distribution|0DVDCMA2DK]].
A search path is a continuous map $t \mapsto z(t)$ with $z(0) = 0$ and $\abs{z(t) - z(s)} \le \abs{t - s}$, and the object is found at the first time $T$ with $z(T) = X$.
The *linear search problem* asks for a search path that minimizes the expected finding time $\mathbb{E}[T]$.
It also asks for conditions on the law of $X$ under which such a path exists.

## Remarks

A good path turns back and forth, going farther each time, because the searcher does not know on which side the object lies.
Beck showed that a path with finite expected finding time exists if and only if $\mathbb{E}\abs{X} < \infty$, and that an optimal path then exists.
In the deterministic version, also called the cow path problem, the object is at an unknown point at distance at least $1$.
There one compares the finding time with the distance $\abs{X}$.
The doubling strategy goes to $1$, then to $-2$, then to $4$, and so on; it finds the object within time $9 \abs{X}$.
No deterministic strategy has a better worst-case ratio than $9$.

## Explanations

### L1 human

You have lost your keys somewhere along a straight road, but you do not know in which direction from where you stand.
If you walk far in one direction, you may be wasting time on the wrong side.
The good plan is to zigzag: go a bit one way, come back, go a bit farther the other way, and keep increasing the distance.
The question is how fast to increase the distance to minimize the average time to find the keys.
