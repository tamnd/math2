---
tag: QEP266HZKS
kind: example
name: Every graph has a bipartite subgraph with half of its edges
msc: ["05C35", "00A35"]
topics: [GB14W4SYPK]
audience: ug1
instance_of: [HXP9VMXV8S]
uses: [HXP9VMXV8S, 00C0BR7D7H, 0ZVQKTRKVQ, 0F8YBHF2W3, T9B8T3FKRA]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_cut
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Probabilistic_method
    locator: lead section
---

## Example

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]] with $n \ge 1$ vertices and $m$ edges.
For a subset $A \subseteq V$, the cut $\delta(A)$ is the set of edges with exactly one end in $A$.
The edges of $\delta(A)$ form a [[bipartite|0ZVQKTRKVQ]] subgraph, with the two parts $A$ and $V \setminus A$.
We prove by an [[averaging argument|HXP9VMXV8S]] that some $A$ has $|\delta(A)| \ge m/2$.

1. The family is the set of all $2^n$ subsets $A$ of $V$. The score of $A$ is $|\delta(A)|$.
2. We compute the sum $\sum_{A \subseteq V} |\delta(A)|$ by [[double counting|0F8YBHF2W3]] of the pairs $(A, e)$ with $e \in \delta(A)$.
3. Fix an edge $e = uv$. The edge $e$ is in $\delta(A)$ exactly when $A$ contains one of $u, v$ and not the other.
4. We count these sets $A$. There are $2$ choices for which of $u, v$ lies in $A$, and $2^{n-2}$ choices for the other $n - 2$ vertices. So $e$ lies in $\delta(A)$ for $2 \cdot 2^{n-2} = 2^{n-1}$ sets $A$.
5. So the sum over all pairs is $m \cdot 2^{n-1}$, and the average of $|\delta(A)|$ over the $2^n$ sets is $m \cdot 2^{n-1}/2^n = m/2$.
6. By the averaging argument, some set $A$ has $|\delta(A)| \ge m/2$. Its cut is a bipartite subgraph of $G$ with at least $m/2$ edges.

We check the count on the [[complete graph|03WKB2H474]] $K_4$, with $n = 4$ and $m = 6$.

1. The sets $A = \emptyset$ and $A = V$ cut no edge. This gives $2$ sets with score $0$.
2. A set with $1$ or $3$ vertices cuts the $3$ edges at the single vertex on its side. This gives $8$ sets with score $3$.
3. A set with $2$ vertices cuts the $2 \cdot 2 = 4$ edges between the two pairs. This gives $6$ sets with score $4$.
4. The sum is $2 \cdot 0 + 8 \cdot 3 + 6 \cdot 4 = 48$, and the average is $48/16 = 3 = m/2$, as step 5 says.

## Remarks

The example shows the typical shape of an averaging proof: the best cut is hard to find, but the average cut is easy to compute.
Finding a cut of maximum size is the [[maximum cut|T9B8T3FKRA]] problem, and its decision form is NP-complete.
The bound $m/2$ needs no search at all.

The bound changes with the graph.
For the $5$-cycle, $m = 5$ and the average is $5/2$, so some cut has at least $3$ edges, since a cut size is an integer.
The best cut of the $5$-cycle has $4$ edges, and no cut has $5$, because an odd cycle is not bipartite.
For a bipartite graph the best cut has all $m$ edges, so the average can be far below the maximum.

## Explanations

### L1 human

Split the people at a party into two rooms at random, for example by a coin flip for each person.
Each pair of friends ends up in different rooms half of the time.
So on average, half of the friendships cross between the rooms.
Then some split makes at least half of the friendships cross.
For four people who all know each other, there are $6$ friendships, and some split makes at least $3$ of them cross.

### L2 human

We find a cut with at least half of the edges for the path $P_4$ with vertices $1, 2, 3, 4$ and edges $12$, $23$, $34$.

1. Here $m = 3$, so the averaging argument gives a cut with at least $3/2$ edges, that is, at least $2$ edges.
2. The set $A = \set{1, 3}$ cuts the edges $12$, $23$ and $34$, because each edge joins an odd and an even vertex.
3. So this cut has all $3$ edges, which is more than the bound.

The typical use of the bound is as a first guarantee, before a search for a better cut.
A trap is to think that every split cuts half of the edges: the split $A = \emptyset$ cuts none.
The averaging argument says only that some split is at least as good as the average.
