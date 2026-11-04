---
tag: ZGG7N7NC8G
kind: proof
name: Proof of continuity via open sets in metric spaces
msc: ["54E35"]
proves: 0YF82GBTND
uses: [063W5JMY85, 01ZQQDCERP, 0FGCFY1AZX, 0DC3MPR7C9, 0B2305GNAZ, 0A26X79RTB]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
---

## Proof

We prove each implication separately.

1. Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]] and let $f \colon X \to Y$.
2. Write $B_X(a, \delta)$ and $B_Y(b, \varepsilon)$ for the [[open balls|0DC3MPR7C9]] of $X$ and $Y$. By the symmetry of a metric, $x \in B_X(a, \delta)$ if and only if $d_X(x, a) < \delta$.
3. Assume condition 1. Let $V$ be an [[open set|01ZQQDCERP]] of $Y$, and let $a$ be in the [[preimage|0FGCFY1AZX]] $f^{-1}(V)$.
4. Then $f(a) \in V$. By the [[description of the open sets of a metric space|0A26X79RTB]], there is $\varepsilon > 0$ with $B_Y(f(a), \varepsilon) \subseteq V$.
5. Condition 1 gives $\delta > 0$ such that $d_X(x, a) < \delta$ implies $d_Y(f(x), f(a)) < \varepsilon$.
6. Let $x \in B_X(a, \delta)$. By step 2 and step 5, $d_Y(f(x), f(a)) < \varepsilon$.
7. By symmetry, $f(x) \in B_Y(f(a), \varepsilon) \subseteq V$, so $x \in f^{-1}(V)$. Thus $B_X(a, \delta) \subseteq f^{-1}(V)$.
8. Each point of $f^{-1}(V)$ has a ball about it inside $f^{-1}(V)$. By the description of open sets, $f^{-1}(V)$ is open. This is condition 2.
9. Now assume condition 2. Let $a \in X$ and $\varepsilon > 0$. Put $V = B_Y(f(a), \varepsilon)$.
10. By [[open balls are open|0B2305GNAZ]], $V$ is open. By condition 2, $f^{-1}(V)$ is open in $X$.
11. Since $d_Y(f(a), f(a)) = 0 < \varepsilon$, we have $f(a) \in V$, so $a \in f^{-1}(V)$.
12. By the description of open sets, there is $\delta > 0$ with $B_X(a, \delta) \subseteq f^{-1}(V)$.
13. Let $x \in X$ with $d_X(x, a) < \delta$. By step 2, $x \in B_X(a, \delta)$, so $f(x) \in V$.
14. So $d_Y(f(a), f(x)) < \varepsilon$, and by symmetry $d_Y(f(x), f(a)) < \varepsilon$. This is condition 1.

## Idea

An open set contains a ball about each of its points, and balls are open. Condition 1 says that a small ball about $a$ maps into a given ball about $f(a)$. Translating between balls and open sets gives each direction.
