---
tag: 8E4S2WZTFA
kind: example
name: Eden growth model
msc: [82C24, 60K35]
illustrates: [RQ196EHXKC]
uses: [0E99F51GVB]
sources:
  - url: https://en.wikipedia.org/wiki/Eden_growth_model
same_as:
  wikidata: Q5336964
  wikipedia: Eden growth model
---

## Example

The *Eden growth model* on $\Z^d$ is a random growing sequence of finite connected sets $A_0 \subset A_1 \subset \cdots$.
Start with $A_0 = \set{0}$.
Given $A_n$, let $\partial A_n$ be the set of points of $\Z^d \setminus A_n$ adjacent to some point of $A_n$.
Choose $y$ uniformly at random in $\partial A_n$, independently of the past, and let $A_{n+1} = A_n \cup \set{y}$.

Check of the first two steps in $\Z^2$: $\partial A_0$ is the set of the $4$ neighbours of $0$, so $A_1 = \set{0, e}$ for a uniform neighbour $e$.
Then $\partial A_1$ has $6$ points: the $3$ further neighbours of $0$ and the $3$ further neighbours of $e$.
So each of these $6$ points is added at step $2$ with probability $1/6$.

## Remarks

The model was introduced by Murray Eden in 1961 as a model of the growth of cell colonies.
It is equivalent to site first-passage percolation with [[exponential|0E99F51GVB]] passage times.
Give each site an independent waiting time of law exponential with mean $1$, and add a boundary site when its waiting time, started when it joins the boundary, runs out.
By the memoryless property, at each addition every boundary site is equally likely to be the next one, so the sequence of sets is the Eden model.
The general shape theorem of first-passage percolation shows that the rescaled cluster $A_n / n^{1/d}$ converges to a deterministic compact convex set.
Simulations show that the fluctuations of its boundary follow the scaling of the [[Kardar–Parisi–Zhang equation|RQ196EHXKC]].

## Explanations

### L1 human

Start with one cell, and at each step let a random free spot next to the colony be filled by a new cell.
The colony grows into a blob with a rough boundary.
From far away the blob looks like a fixed round-ish shape, which is not exactly a disc because of the grid.
Its boundary is rough in a universal way shared by many growing interfaces, such as a burning sheet of paper.
