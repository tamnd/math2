---
tag: 3M9SNX43FA
kind: proof
name: Proof of the epsilon-net characterisation of total boundedness
msc: ["54E35"]
proves: 0NMGJJ19HD
uses: [0WE5BBHGM6, 0692CGQF00, 0DC3MPR7C9, 01M6CW9VM6]
sources:
  - url: https://en.wikipedia.org/wiki/Totally_bounded_space
    locator: In metric spaces
---

## Proof

We prove the two directions separately.

First, let $S$ be [[totally bounded|0WE5BBHGM6]], and fix a real $\varepsilon > 0$.

1. By the definition, there are sets $A_1, \ldots, A_n \subseteq X$ with $S \subseteq A_1 \cup \cdots \cup A_n$ and $\operatorname{diam}(A_k) < \varepsilon$ for each $k$. Here the [[diameter|0692CGQF00]] is defined, so each $A_k$ is nonempty.
2. Let $J$ be the set of $k$ with $A_k \cap S \ne \varnothing$. For each $k \in J$, choose a point $y_k \in A_k \cap S$.
3. Let $F = \set{y_k : k \in J}$. Then $F$ is a finite subset of $S$.
4. Let $s \in S$. By step 1, $s \in A_k$ for some $k$. Then $s \in A_k \cap S$, so $k \in J$.
5. Both $s$ and $y_k$ lie in $A_k$. So $d(s, y_k) \le \operatorname{diam}(A_k) < \varepsilon$, and $s$ is in the [[open ball|0DC3MPR7C9]] $B(y_k, \varepsilon)$.
6. Hence $S \subseteq \bigcup_{y \in F} B(y, \varepsilon)$.

Conversely, assume the condition on finite sets, and fix a real $\varepsilon > 0$.

7. Apply the condition with $\varepsilon / 3$. We get a finite set $F \subseteq S$ with $S \subseteq \bigcup_{y \in F} B(y, \varepsilon / 3)$.
8. Let $y \in F$. The ball $B(y, \varepsilon / 3)$ contains $y$, so it is nonempty.
9. Let $z, w \in B(y, \varepsilon / 3)$. By the [[triangle inequality|01M6CW9VM6]], $d(z, w) \le d(z, y) + d(y, w) < 2 \varepsilon / 3$.
10. So $\operatorname{diam} B(y, \varepsilon / 3) \le 2 \varepsilon / 3 < \varepsilon$.
11. By steps 7 and 10, the finitely many balls $B(y, \varepsilon / 3)$, $y \in F$, cover $S$ and have diameter less than $\varepsilon$.
12. This holds for each $\varepsilon > 0$, so $S$ is totally bounded.

## Idea

A small set that meets $S$ can be replaced by a ball around one point of $S$ inside it. Conversely, a ball of radius $r$ has diameter at most $2r$. Shrinking the radius to $\varepsilon / 3$ turns the balls into sets of diameter less than $\varepsilon$.
