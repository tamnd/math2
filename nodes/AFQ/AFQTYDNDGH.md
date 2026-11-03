---
tag: AFQTYDNDGH
kind: concept
name: Central path
msc: [90C51, 90C05, 90C25]
sources:
  - url: https://en.wikipedia.org/wiki/Interior-point_method
---

## Summary

The central path of a convex optimization problem is a curve of minimisers.
Its points minimise the objective plus a weighted [[barrier function|59ZC4Z9611]], as the weight goes to zero.
It runs through the interior of the feasible region and ends at the set of optimal solutions.
Path-following [[interior-point methods|M7HYT44ZJA]] produce iterates that stay close to this curve.

## Explanations

### L1 human

Picture the feasible region as a room and the optimum as a point on its wall.
When the barrier is strong, the best point sits near the middle of the room, far from all walls.
As the barrier is weakened step by step, the best point slides toward the optimum on the wall, and the trace of this point is the central path.
Take the problem "minimise $x$ subject to $x \ge 0$" with barrier $-\ln x$.
The minimiser of $t x - \ln x$ is $x = 1/t$, so the central path is $t \mapsto 1/t$.
It tends to the optimum $0$ as $t \to \infty$.
