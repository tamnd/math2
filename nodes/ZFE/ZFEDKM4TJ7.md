---
tag: ZFEDKM4TJ7
kind: definition
name: Fundamental groupoid
msc: [55Q05, 18B40]
defines: ZBHGXJF24E
uses: [CCNKA8C711]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_groupoid
---

## Definition

Let $X$ be a topological space.
The *fundamental [[groupoid|FH3C0T643F]]* $\Pi_1(X)$ is the [[category|A2DE66937D]] in which:

1. the objects are the points of $X$;
2. a morphism from $x$ to $y$ is a [[path homotopy|CCNKA8C711]] class $[\gamma]$ of paths $\gamma \colon [0, 1] \to X$ with $\gamma(0) = x$ and $\gamma(1) = y$;
3. the composite of $[\alpha] \colon x \to y$ and $[\beta] \colon y \to z$ is $[\alpha \cdot \beta] \colon x \to z$, where $(\alpha \cdot \beta)(s)$ is $\alpha(2s)$ for $s \le 1/2$ and $\beta(2s - 1)$ for $s \ge 1/2$;
4. the identity of $x$ is the class of the constant path at $x$.

## Remarks

Every morphism $[\gamma]$ has the inverse $[\bar\gamma]$, where $\bar\gamma(s) = \gamma(1 - s)$, so $\Pi_1(X)$ is a groupoid.
The group of morphisms from $x$ to itself is the fundamental group $\pi_1(X, x)$.
Example: for a convex set $C \subseteq \R^n$, there is exactly one morphism between any two points, since any two paths with the same ends are path homotopic by the straight-line homotopy.
Non-example: if paths are taken without passing to path homotopy classes, composition is not associative, so clause 3 does not define a category.
Two points lie in the same connected component of $\Pi_1(X)$ exactly when they lie in the same path component of $X$.
