---
tag: D2J0A8SACE
kind: definition
name: Topological transitivity
msc: [37B02, 37B05]
defines: FR49Y9GQHR
uses: [0CQHFPGJ45, 0VGFHTM75Y, 02BH3MCBQB, 0BSJSX7ME2]
sources:
  - url: https://en.wikipedia.org/wiki/Mixing_(mathematics)
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $f \colon X \to X$ be a [[continuous map|0VGFHTM75Y]].
The map $f$ is *topologically transitive* if for every pair of nonempty [[open sets|02BH3MCBQB]] $U, V \subseteq X$ there is an integer $n \ge 1$ with $f^n(U) \cap V \neq \emptyset$.

## Remarks

An equivalent form is $U \cap f^{-n}(V) \neq \emptyset$, since both say that some point of $U$ is sent into $V$ by $f^n$.
Let $X$ be a compact metric space without isolated points.
Then $f$ is topologically transitive if and only if some forward orbit $\set{f^n(x) : n \ge 0}$ is [[dense|0BSJSX7ME2]] in $X$.
In that case the points with dense forward orbit form a dense $G_\delta$ set.
Example: let $f(x) = x + \alpha \bmod 1$ on the circle $\R / \Z$ with $\alpha$ irrational.
Every forward orbit is dense, so for nonempty open $U, V$ and a point $x \in U$, some $f^n(x)$ with $n \ge 1$ lies in $V$.
Non-example: the identity map of $[0, 1]$, with $U = (0, 1/3)$ and $V = (2/3, 1)$, has $f^n(U) \cap V = U \cap V = \emptyset$ for all $n$.

## Explanations

### L1 human

A transitive map moves some point of each open region into each other open region, at some later time.
