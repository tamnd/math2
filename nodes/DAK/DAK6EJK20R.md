---
tag: DAK6EJK20R
kind: statement
role: proposition
name: Fast marching method
msc: [65N06, 35F21, 65D18]
uses: [HGMX1QGTAZ, V389A4WGH9, H1ERJ3T75T]
about: [HGMX1QGTAZ]
sources:
  - url: https://en.wikipedia.org/wiki/Fast_marching_method
same_as:
  wikidata: Q5437042
  wikipedia: Fast marching method
---

## Statement

Let $h > 0$ and let $G$ be a finite set of $N$ nodes $x_{ij} = (ih, jh)$ of a square grid in $\R^2$.
Let $F_{ij} > 0$ be a speed at each node, and let $S \subset G$ be a nonempty set of source nodes with given values $T_{ij} \ge 0$.
For $T$ on $G$ write $a = \min(T_{i-1,j}, T_{i+1,j})$ and $b = \min(T_{i,j-1}, T_{i,j+1})$, with missing neighbours ignored.
The upwind discretization of the [[eikonal equation|HGMX1QGTAZ]] $\abs{\nabla T} = 1/F$ at a node $x_{ij} \notin S$ is
$$\big( \max(T_{ij} - a, 0) \big)^2 + \big( \max(T_{ij} - b, 0) \big)^2 = \frac{h^2}{F_{ij}^2}.$$
The *fast marching method* first marks the nodes of $S$ as accepted.
It then repeats two steps until all nodes are accepted.
First, it computes a tentative value at each non-accepted neighbour of an accepted node.
This value solves the equation above, with only accepted neighbours used in $a$ and $b$.
Second, it accepts the node with the smallest tentative value.
Assume the grid graph on $G$ is connected.
Then:

1. every node is accepted exactly once, and the method stops;
2. the nodes not in $S$ are accepted in nondecreasing order of their values;
3. the final values satisfy the upwind equation at every node not in $S$;
4. with the tentative values kept in a binary [[heap|V389A4WGH9]], the method uses $O(N \log N)$ operations.

## Remarks

The upwind equation has the causality property: its solution $T_{ij}$ is larger than every neighbour value that enters it with a nonzero term.
Hence a newly computed tentative value is never smaller than the last accepted value, which gives claim 2, and accepting the smallest tentative value never needs to be undone.
The source values are arbitrary, so claim 2 is only about the nodes outside $S$.
This is the same argument as for [[Dijkstra's algorithm|VZZMASEEC8]], which the method resembles; Dijkstra's algorithm on the grid graph would measure distance along grid edges only.
Each node is inserted and updated a bounded number of times, and each heap operation costs $O(\log N)$, which gives claim 4.

Example: with $F \equiv 1$ and one source with $T = 0$ at the origin, the computed $T$ approximates the Euclidean distance to the origin.
At the node $(h, h)$, both neighbours $(h, 0)$ and $(0, h)$ have value $h$, and the equation gives $T = h + h/\sqrt{2} \approx 1.71 h$, near the true value $\sqrt{2} h \approx 1.41 h$.
The error is of first order in $h$.

## Explanations

### L1 human

Imagine a fire that starts on a set of points and spreads at a given speed, which may vary from place to place.
The fast marching method computes the arrival time of the fire at every grid point.
It sweeps outward from the start like a front, always fixing the point that the fire reaches next.
Each point is fixed once, so the whole computation is nearly as fast as visiting every point once.

### L2 human

The eikonal equation is a stationary Hamilton–Jacobi equation, and its relevant solution is the [[viscosity solution|H1ERJ3T75T]].
The upwind scheme above is monotone and consistent, and as $h \to 0$ its solutions approximate the viscosity solution.
The fast marching method solves this nonlinear system in one pass, instead of by repeated sweeps or iterations.
It is used to build signed distance functions for the [[level-set method|7KWR08FJET]], to compute shortest paths around obstacles, and in seismic travel time computations.
