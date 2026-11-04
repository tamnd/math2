---
tag: TBBQ0H7R7E
kind: proof
name: Proof of Hall's theorem for bipartite graphs from Hall's marriage theorem
msc: [05C70]
proves: 0X2GJPNPFN
uses: [07DVHJ8N0A, 0Z87BHAFTB, 01T3TMGTTE, 08WCB90WND]
sources:
  - url: https://en.wikipedia.org/wiki/Hall's_marriage_theorem
    locator: Equivalence of the two formulations
---

## Proof

We translate matchings into transversals of the family of neighbourhoods.

1. Let $G$ be a finite [[bipartite graph|07DVHJ8N0A]] with parts $X$ and $Y$. For $x \in X$, let $N(x) \subseteq Y$ be its [[neighbourhood|01T3TMGTTE]]. For $W \subseteq X$, the set $N(W)$ of the statement equals $\bigcup_{x \in W} N(x)$.
2. Consider the finite family $(N(x))_{x \in X}$ of finite sets, indexed by $X$.
3. Suppose $M$ is a [[matching|0Z87BHAFTB]] that covers every vertex of $X$. For $x \in X$, let $f(x)$ be the other end of the edge of $M$ at $x$. This edge is unique, because no two edges of $M$ share an end.
4. Each edge joins $X$ to $Y$, so $f(x) \in N(x)$. If $f(x) = f(x')$ with $x \ne x'$, two edges of $M$ would share the end $f(x)$. So $f$ is injective, and it is a transversal of the family.
5. Conversely, let $f$ be a transversal of the family. Let $M = \set{x f(x) : x \in X}$. These are edges, since $f(x) \in N(x)$.
6. Two distinct edges $x f(x)$ and $x' f(x')$ of $M$ have $x \ne x'$ and $f(x) \ne f(x')$. Ends in $X$ and ends in $Y$ cannot coincide, as the parts are disjoint. So $M$ is a matching, and it covers $X$.
7. By Steps 3 to 6, $G$ has a matching covering $X$ if and only if the family $(N(x))_{x \in X}$ has a transversal.
8. By [[Hall's marriage theorem|08WCB90WND]], applied after numbering the elements of $X$, this holds if and only if $\abs{\bigcup_{x \in W} N(x)} \ge \abs{W}$ for every $W \subseteq X$.
9. By Step 1, this condition says $\abs{N(W)} \ge \abs{W}$ for every $W \subseteq X$.

## Idea

A matching that covers $X$ is the same thing as a choice of a distinct neighbour for each vertex of $X$. That is a transversal of the neighbourhoods, so the marriage theorem applies directly.
