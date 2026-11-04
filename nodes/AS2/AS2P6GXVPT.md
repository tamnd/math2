---
tag: AS2P6GXVPT
kind: proof
name: Proof that every connected graph has a spanning tree, by a maximal acyclic edge set
msc: [05C05]
proves: 04XPQT2XTC
uses: [0FFAYNMAJZ, 0FQ5B8S1ZC, 0MJ0JS72DZ, 0XNN9Z8E5A, 07CT9RDY7Q, 0P11X5HKAX, 0J8XE7W68F, 0VJZM0F9YM, 04RXTQA5ZA]
sources:
  - url: https://en.wikipedia.org/wiki/Spanning_tree
---

## Proof

We use [[Zorn's lemma|04RXTQA5ZA]] to get a maximal acyclic set of edges. For a finite graph, simply take an acyclic edge set of largest size instead.

1. Let $G = (V, E)$. Let $\mathcal{P}$ be the set of all $F \subseteq E$ such that the [[subgraph|0P11X5HKAX]] $(V, F)$ is [[acyclic|0XNN9Z8E5A]]. Order $\mathcal{P}$ by inclusion.
2. $\varnothing \in \mathcal{P}$, because a [[cycle|07CT9RDY7Q]] has positive length and so uses an edge. So $\mathcal{P}$ is nonempty.
3. Let $\mathcal{K}$ be a nonempty chain in $\mathcal{P}$, and let $U = \bigcup \mathcal{K}$. Suppose $(V, U)$ has a cycle with edges $e_1, \dots, e_k$.
4. Each $e_t$ lies in some $F_t \in \mathcal{K}$. Since $\mathcal{K}$ is a chain, the largest of $F_1, \dots, F_k$ contains all $e_t$.
5. Then the cycle lies in $(V, F)$ for that $F \in \mathcal{P}$, a contradiction. So $U \in \mathcal{P}$, and $U$ is an upper bound of $\mathcal{K}$. The empty chain has the upper bound $\varnothing$.
6. By Zorn's lemma, $\mathcal{P}$ has a maximal element $F$. Let $H = (V, F)$. It is acyclic, and it contains every vertex of $G$.
7. Suppose $H$ is not connected. Since $V$ is nonempty, there are $u, v \in V$ such that $v$ is not [[reachable|0J8XE7W68F]] from $u$ in $H$.
8. Since $G$ is [[connected|0FFAYNMAJZ]], there is a [[walk|0VJZM0F9YM]] $(w_0, \dots, w_k)$ from $u$ to $v$ in $G$.
9. If $w_t$ were reachable from $w_{t-1}$ in $H$ for each $t$, then $v$ would be reachable from $u$ in $H$, by transitivity of reachability. So some $t$ has $w_t$ not reachable from $w_{t-1}$ in $H$.
10. Let $x = w_{t-1}$ and $y = w_t$. Then $xy \in E$, and $xy \notin F$, since otherwise $(x, y)$ would be a walk in $H$.
11. Let $F^+ = F \cup \set{xy}$. Suppose $(V, F^+)$ has a cycle $(z_0, \dots, z_m)$. Since $H$ is acyclic, one of its edges is $xy$, say $xy = z_{s-1} z_s$.
12. The edges of a cycle are pairwise distinct. So all other edges of the cycle lie in $F$.
13. Then $(z_s, z_{s+1}, \dots, z_m, z_1, \dots, z_{s-1})$ is a walk in $H$ from $z_s$ to $z_{s-1}$, using $z_m = z_0$. For $s = 1$ it is $(z_1, \dots, z_m)$.
14. The ends of this walk are $x$ and $y$. Reachability is symmetric, so $y$ is reachable from $x$ in $H$. This contradicts step 9. Hence $F^+ \in \mathcal{P}$.
15. But $F \subsetneq F^+$, which contradicts the maximality of $F$. So $H$ is connected.
16. By steps 6 and 15, $H$ is a connected acyclic subgraph of $G$ with all the vertices of $G$. So $H$ is a [[tree|0MJ0JS72DZ]], and it is a [[spanning tree|0FQ5B8S1ZC]] of $G$.

## Idea

Keep as many edges as possible without making a cycle. If the result were disconnected, some edge of $G$ would join two of its pieces. Adding that edge cannot close a cycle, so the set was not as large as possible.
