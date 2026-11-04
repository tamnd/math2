---
tag: TKNNQY6RF9
kind: proof
name: Proof that open balls form a basis of the metric topology
msc: ["54E35"]
proves: 02EEX96DFS
uses: [06EX0FHBTF, 0A6YRNZB2R, 0B2305GNAZ, 0DC3MPR7C9, 0A3GWZ86AY]
sources:
  - url: https://en.wikipedia.org/wiki/Base_(topology)
    locator: Examples
---

## Proof

We check the second form of the definition of a [[basis|06EX0FHBTF]] for both families.

1. Let $\mathcal{B}$ be the set of all [[open balls|0DC3MPR7C9]] $B(x, r)$ with $x \in X$ and $r > 0$. Let $\mathcal{B}'$ be the set of balls $B(x, 1/n)$ with $x \in X$ and integer $n \ge 1$. Then $\mathcal{B}' \subseteq \mathcal{B}$.
2. By [[open balls are open|0B2305GNAZ]], each member of $\mathcal{B}$ is in the [[metric topology|0A6YRNZB2R]] $\tau_d$. So $\mathcal{B}' \subseteq \mathcal{B} \subseteq \tau_d$.
3. Let $U \in \tau_d$ and $x \in U$. By the definition of $\tau_d$, there is a real $\varepsilon > 0$ with $B(x, \varepsilon) \subseteq U$.
4. The ball $B(x, \varepsilon)$ is in $\mathcal{B}$ and contains $x$, since $d(x, x) = 0 < \varepsilon$. So $\mathcal{B}$ is a basis of $\tau_d$.
5. Since [[the reals are Archimedean|0A3GWZ86AY]], there is an integer $n \ge 1$ with $n \varepsilon > 1$, that is, $1/n < \varepsilon$.
6. If $d(x, y) < 1/n$, then $d(x, y) < \varepsilon$. So $x \in B(x, 1/n) \subseteq B(x, \varepsilon) \subseteq U$.
7. The ball $B(x, 1/n)$ is in $\mathcal{B}'$. So $\mathcal{B}'$ is also a basis of $\tau_d$.

## Idea

Balls are open, and by the very definition of the metric topology every open set contains a ball around each of its points. A ball of radius $1/n$ fits inside any given ball with the same centre once $n$ is large.
