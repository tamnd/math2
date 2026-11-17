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

False claim: every finite [[graph|0JD5C82QMB]] with $n \ge 2$ vertices and no isolated vertex is [[connected|0FFAYNMAJZ]].
An isolated vertex is a vertex of [[degree|0KS0KRDV4Y]] $0$.
Here is a "proof" by building up, followed by the error.

The argument:

1. Base case $n = 2$: a graph with $2$ vertices and no isolated vertex has the edge between them, so it is connected.
2. Step: let $G$ be a graph with $n$ vertices, no isolated vertex, and assume that $G$ is connected.
3. Add a new vertex $v$ and join it by an edge to some vertex $u$ of $G$. The new graph $G'$ has $n + 1$ vertices and no isolated vertex.
4. Each vertex of $G$ reaches $u$ inside $G$, and $v$ reaches $u$ by the new edge. So $G'$ is connected.
5. "By induction", every graph with no isolated vertex is connected.

The claim is false, and the counterexample is small.

1. Let $H$ have the vertices $a, b, c, d$ and the two edges $ab$ and $cd$.
2. Each vertex has degree $1$, so $H$ has no isolated vertex.
3. No edge joins $\{a, b\}$ to $\{c, d\}$, so there is no path from $a$ to $c$. So $H$ is not connected.

The error is in the step.

1. The step proves the claim only for graphs of the form $G'$: a graph of the claim with $n$ vertices, plus one vertex joined to it.
2. The graph $H$ is not of this form. Removing any vertex of $H$ leaves a graph in which the partner of that vertex is isolated, so no graph of the claim with $3$ vertices gives $H$ by step 3.
3. So the step covers only some graphs with $n + 1$ vertices, and the conclusion of step 5 does not follow.

## Remarks

1. The argument is not an [[induction on size|B2D8PTFNN1]], because its step does not start from an arbitrary graph with $n + 1$ vertices. A correct step must take an arbitrary graph of size $n + 1$ and reduce it.
2. If we try the breaking-down order, the error shows itself. Let $G$ have $n + 1$ vertices and no isolated vertex, and remove a vertex $v$. The graph $G - v$ can have an isolated vertex, as $H - a$ does, and then the induction hypothesis does not apply.
3. The claim is true for $n = 2$ and $n = 3$. With $3$ vertices and no isolated vertex, the graph is a path with $2$ edges or a triangle, and both are connected. The first counterexample has $4$ vertices.
4. A correct statement in the same spirit: a graph with $n$ vertices in which each vertex has degree at least $(n - 1)/2$ is connected. Two vertices that are not adjacent have together at least $n - 1$ neighbours among the other $n - 2$ vertices, so they share a neighbour.
5. Building up is a valid step only with a proof that every graph of the claim with $n + 1$ vertices arises from a graph of the claim with $n$ vertices. Here that extra proof is impossible, because $H$ is a counterexample.

## Explanations

### L1 human

Picture a group of people in which each person has at least one friend in the group.
It is tempting to argue: start with two friends, and each newcomer makes friends with someone, so the whole group is one circle of friends.
But the group could be two separate pairs of friends who never meet.
Each person has a friend, and still the group falls into two parts.
The argument only looked at groups built by adding one newcomer at a time, and the two pairs are not built in that way.

### L2 human

We show the breaking-down order on a true claim: every connected graph $G$ with $n \ge 2$ vertices has a vertex $v$ such that $G - v$ is connected.

1. Breaking down: take an arbitrary connected $G$ with $n \ge 2$ vertices. We do not add a vertex to a smaller graph.
2. $G$ has a spanning tree $T$, a tree with the same vertices that uses only edges of $G$.
3. A tree with at least $2$ vertices has a leaf $v$, by the lemma in the [[tree example|RJB83Z4N9B]]. Step 6 of that example shows that $T - v$ is again a tree.
4. $T - v$ is a tree, so it is connected, and it is a subgraph of $G - v$ with all its vertices. So $G - v$ is connected.

This proof reduces an arbitrary graph, so it covers every graph.
The typical use of the breaking-down order is any induction over graphs with a hypothesis such as "connected" or "no isolated vertex".
The trap is that the building-up order feels more natural, because it starts from the smaller graph that the hypothesis is about.
