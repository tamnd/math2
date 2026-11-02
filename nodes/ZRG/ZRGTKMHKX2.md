---
tag: ZRGTKMHKX2
kind: definition
name: Holomorphically convex domain
msc: ["32E05", 32T05]
defines: D5J6CP5V2Z
uses: [CD6SMMZSW8, 0R6EWFKRCF, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Definition

Let $D \subseteq \C^n$ be an [[open set|02BH3MCBQB]].
Then $D$ is *holomorphically convex* if for every [[compact set|0R6EWFKRCF]] $K \subseteq D$ the [[holomorphically convex hull|CD6SMMZSW8]] $\hat K_D$ is compact.

## Remarks

Since $\hat K_D$ is closed in $D$, the condition says that $\hat K_D$ has no limit points on the boundary of $D$.

Example: a convex open set $D$.
For compact $K \subseteq D$, the hull $\hat K_D$ lies in the convex hull $\operatorname{ch}(K)$, which is compact and contained in $D$.
A subset of $D$ that is closed in $D$ and contained in the compact set $\operatorname{ch}(K) \subseteq D$ is compact.

Non-example: $D = \set{z \in \C^2 : 0 < \abs{z} < 1}$ and $K = \set{\abs{z} = 1/2}$.
By [[Hartogs's extension theorem|FSGES670AZ]] every holomorphic $f$ on $D$ extends to the ball, and by the maximum principle $\abs{f(z)} \le \max_K \abs{f}$ for $0 < \abs{z} \le 1/2$.
So $\hat K_D$ contains $\set{0 < \abs{z} \le 1/2}$, which is not compact.

By the Cartan–Thullen theorem, a domain in $\C^n$ is holomorphically convex if and only if it is a domain of holomorphy.
