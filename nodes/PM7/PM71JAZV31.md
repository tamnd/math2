---
tag: PM71JAZV31
kind: definition
name: Valuation on convex bodies
msc: [52B45, 52A20]
defines: V0RBKHYTV7
uses: [437FSG3419, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Valuation_(geometry)
---

## Definition

Let $n \ge 1$ and let $\mathcal{K}^n$ be the set of nonempty compact convex subsets of $\R^n$ (the [[convex bodies|437FSG3419]] in the broad sense).
Let $G$ be an [[abelian group|082GHNPJ53]], for example $\R$.
A *valuation* on $\mathcal{K}^n$ is a map $\varphi \colon \mathcal{K}^n \to G$ such that
$$\varphi(K \cup L) + \varphi(K \cap L) = \varphi(K) + \varphi(L)$$
for all $K, L \in \mathcal{K}^n$ with $K \cup L \in \mathcal{K}^n$.

## Remarks

If $K \cup L$ is convex, then $K \cap L$ is nonempty, since a convex set is connected and cannot be the union of two disjoint nonempty closed sets.
So $K \cap L \in \mathcal{K}^n$ and the condition makes sense.
A valuation is *continuous* if it is continuous for the [[Hausdorff distance|F79WYYC07C]], and *invariant under rigid motions* if $\varphi(gK) = \varphi(K)$ for every rigid motion $g$ of $\R^n$.

Example: $\varphi = \operatorname{vol}$, Lebesgue measure on $\R^n$.
For measurable sets, $\operatorname{vol}(K \cup L) + \operatorname{vol}(K \cap L) = \operatorname{vol}(K) + \operatorname{vol}(L)$ always holds, so volume is a valuation.
The constant function $\chi(K) = 1$ is a valuation as well; it is the Euler characteristic.

Non-example: $\varphi(K) = \operatorname{vol}(K)^2$ on $\mathcal{K}^1$.
For $K = [0, 2]$ and $L = [1, 3]$ one gets $\varphi(K \cup L) + \varphi(K \cap L) = 9 + 1 = 10$, but $\varphi(K) + \varphi(L) = 4 + 4 = 8$.

Many authors include the empty set in $\mathcal{K}^n$ and require $\varphi(\emptyset) = 0$.
Then the Euler characteristic takes the value $0$ at $\emptyset$.
