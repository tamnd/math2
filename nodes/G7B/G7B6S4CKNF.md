---
tag: G7B6S4CKNF
kind: proof
name: Proof of epsilon-delta continuity at a point in metric spaces
msc: ["54E35"]
proves: 0EKGKY5TGH
uses: [063W5JMY85, 07N7W5C29X, 09CJ00H3NW, 0FGCFY1AZX, 0DC3MPR7C9, 0B2305GNAZ, 0A26X79RTB]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
---

## Proof

We prove each direction separately. Both metric spaces carry their metric topologies.

1. Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]], let $f \colon X \to Y$ and let $a \in X$.
2. Write $B_X(a, \delta)$ and $B_Y(f(a), \varepsilon)$ for the [[open balls|0DC3MPR7C9]] of $X$ and $Y$. By the symmetry of a metric, $x \in B_X(a, \delta)$ if and only if $d_X(x, a) < \delta$.
3. Recall that a set $N$ is a [[neighbourhood|09CJ00H3NW]] of a point $p$ when some open set $U$ satisfies $p \in U \subseteq N$.
4. First suppose that $f$ is [[continuous at|07N7W5C29X]] $a$. Let $\varepsilon > 0$ and put $V = B_Y(f(a), \varepsilon)$.
5. By [[open balls are open|0B2305GNAZ]], $V$ is open. Also $f(a) \in V$, as $d_Y(f(a), f(a)) = 0 < \varepsilon$. So $V$ is a neighbourhood of $f(a)$.
6. By continuity at $a$, the [[preimage|0FGCFY1AZX]] $f^{-1}(V)$ is a neighbourhood of $a$. So there is an open set $U$ with $a \in U \subseteq f^{-1}(V)$.
7. By the [[description of the open sets of a metric space|0A26X79RTB]], there is $\delta > 0$ with $B_X(a, \delta) \subseteq U$.
8. Let $x \in X$ with $d_X(x, a) < \delta$. By step 2, $x \in B_X(a, \delta) \subseteq f^{-1}(V)$, so $f(x) \in V$.
9. Thus $d_Y(f(a), f(x)) < \varepsilon$, and by symmetry $d_Y(f(x), f(a)) < \varepsilon$. This is the epsilon-delta condition.
10. Conversely, suppose the epsilon-delta condition holds at $a$. Let $V$ be a neighbourhood of $f(a)$. Choose an open set $W$ with $f(a) \in W \subseteq V$.
11. By the description of open sets, there is $\varepsilon > 0$ with $B_Y(f(a), \varepsilon) \subseteq W$. Take $\delta > 0$ as given by the condition for this $\varepsilon$.
12. Let $x \in B_X(a, \delta)$. By step 2, $d_X(x, a) < \delta$, so $d_Y(f(x), f(a)) < \varepsilon$.
13. By symmetry, $f(x) \in B_Y(f(a), \varepsilon) \subseteq V$. Hence $B_X(a, \delta) \subseteq f^{-1}(V)$.
14. The ball $B_X(a, \delta)$ is open, because open balls are open, and it contains $a$. So $f^{-1}(V)$ is a neighbourhood of $a$.
15. As $V$ was arbitrary, $f$ is continuous at $a$.

## Idea

In a metric space, the open balls about a point are small enough to stand in for all its neighbourhoods. Every neighbourhood contains a ball, and every ball is a neighbourhood. So the condition on neighbourhoods becomes a condition on balls, which is the epsilon-delta condition.
