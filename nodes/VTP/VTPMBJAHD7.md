---
tag: VTPMBJAHD7
kind: counterexample
name: Braess's paradox
msc: [90B20, 91A14, 90B10]
uses: [F2SMTMBDP0]
sources:
  - url: https://en.wikipedia.org/wiki/Braess%27s_paradox
same_as:
  wikidata: Q897194
  wikipedia: Braess's paradox
---

## Counterexample

Claim refuted: adding a road to a network never increases the travel time at [[Wardrop equilibrium|F2SMTMBDP0]].

Take vertices $s, v, w, t$ and one unit of traffic from $s$ to $t$.
The edges and latencies, as functions of the edge flow $x$, are $\ell_{sv}(x) = x$, $\ell_{vt}(x) = 1$, $\ell_{sw}(x) = 1$ and $\ell_{wt}(x) = x$.
The two paths $s \to v \to t$ and $s \to w \to t$ are symmetric.
The equilibrium sends $1/2$ on each, and each path has latency $1/2 + 1 = 3/2$.

Now add an edge $v \to w$ with $\ell_{vw}(x) = 0$.
Let all traffic use $s \to v \to w \to t$, so $f_{sv} = f_{wt} = 1$ and the other old edges are empty.
This path has latency $1 + 0 + 1 = 2$.
The path $s \to v \to t$ has latency $1 + 1 = 2$, and $s \to w \to t$ has latency $1 + 1 = 2$.
No path is quicker than the used one, so this flow is a Wardrop equilibrium.
Every driver now needs $2$ instead of $3/2$.

## Remarks

The new edge is attractive to each driver alone, but when everybody uses it both variable edges become congested.
In both networks the equilibrium latency is unique here, so the increase does not depend on a choice of equilibrium.
The ratio $2 / (3/2) = 4/3$ is the largest possible loss for affine latencies, by the [[price of anarchy bound|8RHK2M58B2]].
Dietrich Braess described the phenomenon in 1968.

## Explanations

### L1 human

Building a new shortcut can make everybody's trip slower.
Each driver takes the shortcut because it looks faster for them, but together they jam the roads that lead to it.
In the example, trips take $1.5$ hours before the shortcut and $2$ hours after.
Real cities have seen traffic improve after closing a road, as this paradox predicts.
