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

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]] with $n \ge 2$ vertices and $m$ edges.
For a subset $A \subseteq V$, the cut $\delta(A)$ is the set of edges with exactly one end in $A$.
The edges of $\delta(A)$ form a [[bipartite|0ZVQKTRKVQ]] subgraph, with the two parts $A$ and $V \setminus A$.
We prove by an [[averaging argument|HXP9VMXV8S]] that some $A$ has $|\delta(A)| \ge m/2$.

1. The family is the set of all $2^n$ subsets $A$ of $V$, and the score of $A$ is $|\delta(A)|$.
2. We compute the total $\sum_{A \subseteq V} |\delta(A)|$ by [[double counting|0F8YBHF2W3]] of the pairs $(A, e)$ with $e \in \delta(A)$.
3. Fix an edge $e = uv$.
   The edge $e$ is in $\delta(A)$ exactly when $A$ contains one of $u$ and $v$ but not the other.
4. There are $2$ choices for which of $u$ and $v$ lies in $A$, and $2^{n-2}$ choices for the other $n - 2$ vertices.
   So $e$ lies in $\delta(A)$ for $2 \cdot 2^{n-2} = 2^{n-1}$ sets $A$, half of all sets.
5. So the total is $m \cdot 2^{n-1}$, and the average score is
   $$\frac{m \cdot 2^{n-1}}{2^n} = \frac{m}{2}.$$
6. By the averaging argument, some set $A$ has $|\delta(A)| \ge m/2$.
   Its cut is a bipartite subgraph of $G$ with at least $m/2$ edges.

We check the count on the [[complete graph|03WKB2H474]] $K_4$, with $n = 4$ and $m = 6$.

1. The sets $A = \emptyset$ and $A = V$ cut no edge, so $2$ sets have score $0$.
2. A set with $1$ or $3$ vertices cuts the $3$ edges at the single vertex on its side, so $4 + 4 = 8$ sets have score $3$.
3. A set with $2$ vertices cuts the $2 \cdot 2 = 4$ edges between the two pairs, so $\binom{4}{2} = 6$ sets have score $4$.
4. The total is
   $$2 \cdot 0 + 8 \cdot 3 + 6 \cdot 4 = 48,$$
   and the average is $48/16 = 3 = m/2$, as step 5 says.

## Remarks

The best cut is hard to find, but the average cut is easy to compute, and this is the typical shape of an averaging proof.
Finding a cut of maximum size is the [[maximum cut|T9B8T3FKRA]] problem, and its decision form is NP-complete.
The bound $m/2$ needs no search at all.

A greedy procedure gives the same bound, and it also finds the cut.
Put the vertices on the two sides one at a time, each on the side opposite to the majority of its neighbors placed so far.
Each vertex then cuts at least half of its edges to earlier vertices, and each edge is counted once, at its later end, so at least $m/2$ edges cross.

How close is $m/2$ to the truth?
For the $5$-cycle, $m = 5$ and the average is $5/2$, so some cut has at least $3$ edges, since a cut size is an integer.
The best cut of the $5$-cycle has $4$ edges, and no cut has $5$, because an odd cycle is not bipartite.
For a bipartite graph the best cut has all $m$ edges, so the average can be far below the maximum.

## Explanations

### L1 human

Split the people at a party into two rooms by a coin flip for each person.
Each pair of friends ends up in different rooms half of the time.
So on average, half of the friendships cross between the rooms, and some split makes at least half of them cross.
For four people who all know each other there are $6$ friendships, and the split two and two makes $4$ of them cross, more than the promised $3$.

### L2 human

We find a cut with at least half of the edges for the path with vertices $1, 2, 3, 4$ and edges $12$, $23$ and $34$.
Here $m = 3$, so the averaging argument promises a cut with at least $3/2$ edges, that is, at least $2$ edges.
The set $A = \{1, 3\}$ cuts all three edges, because each edge joins an odd and an even vertex.
So the best cut has $3$ edges, more than the bound.

The bound is a first guarantee, before a search for a better cut.
Watch out: it is wrong to think that every split cuts half of the edges.
The split $A = \emptyset$ cuts none, and the averaging argument says only that some split is at least as good as the average.
