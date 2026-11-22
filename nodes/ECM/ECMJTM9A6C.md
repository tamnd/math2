---
tag: ECMJTM9A6C
kind: example
name: A build-up argument that graphs without isolated vertices are connected
msc: ["05C40", "00A35"]
topics: [EEH2F76CYQ]
audience: ug1
not_instance_of:
  - target: B2D8PTFNN1
    note: the step builds a larger graph from a smaller one instead of reducing an arbitrary larger graph, so it misses some graphs of each size
uses: [B2D8PTFNN1, 0FFAYNMAJZ, 0KS0KRDV4Y, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Connectivity_(graph_theory)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Description
---

## Example

Consider the false claim that every finite [[graph|0JD5C82QMB]] with $n \ge 2$ vertices and no isolated vertex is [[connected|0FFAYNMAJZ]].
An isolated vertex is a vertex of [[degree|0KS0KRDV4Y]] $0$.
Here is a "proof" by building up.

1. Base case $n = 2$: a graph with $2$ vertices and no isolated vertex has the edge between them, so it is connected.
2. Step: let $G$ be a graph with $n$ vertices and no isolated vertex, and assume that $G$ is connected.
3. Add a new vertex $v$ and join it by an edge to some vertex $u$ of $G$.
   The new graph $G'$ has $n + 1$ vertices and no isolated vertex.
4. Each vertex of $G$ reaches $u$ inside $G$, and $v$ reaches $u$ by the new edge, so $G'$ is connected.
5. "By induction", every graph with no isolated vertex is connected.

The claim is false, and the counterexample is small.

1. Let $H$ have the vertices $a, b, c, d$ and the two edges $ab$ and $cd$.
2. Each vertex has degree $1$, so $H$ has no isolated vertex.
3. No edge joins $\{a, b\}$ to $\{c, d\}$, so there is no path from $a$ to $c$, and $H$ is not connected.

The error is in the step.

1. The step proves the claim only for graphs of the form $G'$: a graph of the claim with $n$ vertices, plus one vertex joined to it by one edge.
2. The graph $H$ is not of this form.
   Deleting any vertex of $H$ leaves a graph in which the partner of that vertex is isolated, so no graph of the claim with $3$ vertices gives $H$ in step 3.
3. So the step covers only some graphs with $n + 1$ vertices, and the conclusion of step 5 does not follow.

## Remarks

The argument is not an [[induction on size|B2D8PTFNN1]], because its step does not start from an arbitrary graph with $n + 1$ vertices.
If we try the correct order, the error shows itself at once.
Take a graph $G$ with $n + 1$ vertices and no isolated vertex, and delete a vertex $v$.
The graph $G - v$ can have an isolated vertex, as $H - a$ does, and then the induction hypothesis does not apply.

The claim is true for $n = 2$ and $n = 3$, which makes the base case look convincing.
With $3$ vertices and no isolated vertex the graph is a path with $2$ edges or a triangle, and both are connected.
The first counterexample has $4$ vertices.

A true statement in the same spirit needs a stronger hypothesis.
A graph with $n$ vertices in which each vertex has degree at least $(n - 1)/2$ is connected.
Two vertices that are not adjacent have together at least $n - 1$ neighbors among the other $n - 2$ vertices, so they share a neighbor.

## Explanations

### L1 human

Picture a group of people in which each person has at least one friend in the group.
It is tempting to argue: start with two friends, and each newcomer makes friends with someone, so the whole group hangs together.
But the group could be two separate pairs of friends who never meet.
Each person has a friend, and still the group falls into two parts.
The argument only looked at groups built by adding one newcomer at a time, and the two pairs are not built in that way.

### L2 human

We show the breaking-down order on a true claim: every connected graph $G$ with $n \ge 2$ vertices has a vertex $v$ such that $G - v$ is connected.
Take an arbitrary connected graph $G$ with $n \ge 2$ vertices, and do not build it from a smaller graph.
The graph $G$ has a spanning tree $T$, a tree with the same vertices that uses only edges of $G$.
A tree with at least $2$ vertices has a leaf $v$, by the lemma in the [[tree example|RJB83Z4N9B]], and steps 5 and 6 of that example show that $T - v$ is again a tree.
So $T - v$ is connected, and it is a subgraph of $G - v$ with all of its vertices, so $G - v$ is connected.

Check on the path $a\,b\,c$: deleting the leaf $a$ leaves the edge $bc$, which is connected, while deleting $b$ would not.
The typical use of the breaking-down order is any induction over graphs with a hypothesis such as "connected" or "no isolated vertex".
Watch out: the building-up order feels more natural, because it starts from the smaller graph that the hypothesis is about, and that is exactly why it misleads.
