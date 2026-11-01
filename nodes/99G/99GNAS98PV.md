---
tag: 99GNAS98PV
kind: definition
name: Lebesgue covering dimension
msc: [54F45]
defines: A3W7RGXXK9
uses: [0CQHFPGJ45, 049PXYHW1T, 040CFNJEAP]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_covering_dimension
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
An [[open cover|049PXYHW1T]] $\mathcal{V}$ of $X$ *refines* an open cover $\mathcal{U}$ if each member of $\mathcal{V}$ lies in some member of $\mathcal{U}$.
The *order* of a family $\mathcal{V}$ is the largest $k$ such that some point of $X$ lies in $k + 1$ members of $\mathcal{V}$.
For an integer $n \ge -1$, write $\dim X \le n$ if every finite open cover of $X$ has a finite open refinement of order at most $n$.
The *Lebesgue covering dimension* $\dim X$ is the least $n$ with $\dim X \le n$, and $\dim X = \infty$ if there is no such $n$.

## Remarks

The empty space has $\dim \emptyset = -1$, and a nonempty finite discrete space has dimension $0$.
The interval $[0, 1]$ has $\dim [0, 1] = 1$.
Given a finite open cover, the [[Lebesgue number lemma|040CFNJEAP]] gives a number $\delta > 0$.
Refine the cover by finitely many relatively open intervals of length less than $\delta$ in which only neighbours overlap.
This refinement has order at most $1$.
The cover $\set{[0, 2/3), (1/3, 1]}$ has no open refinement of order $0$.
Such a refinement would be a cover by disjoint open sets, and by connectedness one of them would be all of $[0, 1]$.
But $[0, 1]$ lies in no member of the cover.
So $\dim [0, 1] \le 0$ fails.
Some authors use all open covers instead of finite ones; the two versions agree for compact spaces.
For every $n$, $\dim \R^n = n$.

## Explanations

### L1 human

Take the smallest number $k$ such that every finite open cover can be made finer with each point in at most $k$ of the sets.
The covering dimension of the space is $k - 1$.
