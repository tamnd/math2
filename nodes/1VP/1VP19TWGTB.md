---
tag: 1VP19TWGTB
kind: proof
name: Proof of Ramsey's theorem by induction on r + s
msc: [05D10, 05C55]
proves: 00TQV3F5S4
uses: [03WKB2H474, 0G52BPNPKG]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Ramsey's_theorem
    locator: 2-colour case
---

## Proof

We argue by induction on $r + s$. Call a positive integer $n$ *good for $(r, s)$* if the following holds. Every colouring of the edges of $K_n$ in blue and red has a blue [[clique|0G52BPNPKG]] with $r$ vertices or a red clique with $s$ vertices. We show that some $n$ is good for $(r, s)$.

1. If $n$ is good for $(r, s)$, then every $n' \ge n$ is good for $(r, s)$. Indeed, a colouring of $K_{n'}$ restricts to a colouring of the [[complete graph|03WKB2H474]] on any $n$ of its vertices. A clique there is a clique in $K_{n'}$.
2. Base case: $r = 1$ or $s = 1$. A single vertex is a clique with $1$ vertex, and it is blue and red, since it has no edges. So $n = 1$ is good for $(r, s)$.
3. Induction step: let $r, s \ge 2$, and suppose the claim holds for all pairs with a smaller sum. Let $n_1$ be good for $(r - 1, s)$, and let $n_2$ be good for $(r, s - 1)$.
4. Let $n = n_1 + n_2$, and colour the edges of $K_n$ blue or red. Fix a vertex $v$.
5. Let $B$ be the set of vertices joined to $v$ by a blue edge, and $R$ the set joined to $v$ by a red edge. Then $\abs{B} + \abs{R} = n - 1 = n_1 + n_2 - 1$.
6. So $\abs{B} \ge n_1$ or $\abs{R} \ge n_2$. Otherwise $\abs{B} + \abs{R} \le (n_1 - 1) + (n_2 - 1) < n_1 + n_2 - 1$.
7. Case $\abs{B} \ge n_1$. The vertices of $B$ span a complete graph with at least $n_1$ vertices. By Step 1 and the choice of $n_1$, it has a blue clique with $r - 1$ vertices or a red clique with $s$ vertices.
8. A red clique with $s$ vertices in $B$ is what we want. Let $S \subseteq B$ be a blue clique with $r - 1$ vertices. All edges from $v$ to $B$ are blue, so $S \cup \set{v}$ is a blue clique with $r$ vertices.
9. Case $\abs{R} \ge n_2$. In the same way, $R$ contains a blue clique with $r$ vertices or a red clique $T$ with $s - 1$ vertices. In the second case, $T \cup \set{v}$ is a red clique with $s$ vertices.
10. So $n = n_1 + n_2$ is good for $(r, s)$. By induction, for all positive integers $r$ and $s$, some positive integer $n$ is good for $(r, s)$.

## Idea

Pick one vertex and split the others by the colour of their edge to it. One of the two groups is large enough to apply the induction hypothesis with one target lowered by one. The chosen vertex then extends the clique found in that group.
