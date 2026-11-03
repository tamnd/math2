---
tag: CJ3JX5D3QJ
kind: statement
role: theorem
name: Reiter's condition
msc: ["43A07", "43A20"]
uses: [AHV05ZBCYW, VY0HXD3GC4, SASP14MA1Z, CEAT9BESKK]
about: [CEAT9BESKK]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_group
---

## Statement

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with a left [[Haar measure|VY0HXD3GC4]].
For $f \in L^1(G)$ and $x \in G$, let $(L_x f)(y) = f(x^{-1} y)$.
Then $G$ is [[amenable|CEAT9BESKK]] if and only if the following *Reiter condition* holds.
For every compact set $K \subseteq G$ and every $\varepsilon > 0$ there is $f \in L^1(G)$ with $f \ge 0$ and $\norm{f}_1 = 1$ such that
$$\norm{L_x f - f}_1 < \varepsilon \quad \text{for all } x \in K.$$

## Remarks

The functions $f$ are almost invariant probability densities.
From such densities, an invariant mean on $L^\infty(G)$ is obtained as a weak-$*$ cluster point of the functionals $\varphi \mapsto \int \varphi f$.
Conversely, an invariant mean gives densities that are almost invariant in the weak topology of $L^1(G)$.
A convexity argument, based on the Hahn–Banach theorem, upgrades them to the norm condition.

Example: for $G = \Z$ and $K = \set{-k, \ldots, k}$, take $f = \frac{1}{n} \mathbf{1}_{\set{0, \ldots, n-1}}$.
Then $\norm{L_j f - f}_1 = 2\abs{j}/n \le 2k/n$ for $j \in K$, which is less than $\varepsilon$ when $n$ is large.

For a discrete group the condition says that there are finitely supported probability vectors that are almost invariant in $\ell^1(G)$.
A [[Følner sequence|6WZR80CPBD]] gives such vectors by normalizing indicator functions.

## Explanations

### L1 human

A group is amenable when one can spread a unit of mass over it so that every small shift barely changes the distribution.
In $\Z$, a long flat block of mass works: shifting it moves only a little mass at the ends.
In a free group no distribution of mass has this property.

### L2 human

Reiter's condition is the bridge between invariant means and the [[Følner condition|82R5XGCART]].
The $L^2$ version, with $\norm{\cdot}_2$ and unit vectors, says that the left regular representation has almost invariant vectors, which is [[Hulanicki's theorem|P18JWQ7Y84]].
It is also the form of amenability used for the group algebra, as in Johnson's theorem that $L^1(G)$ is an amenable Banach algebra exactly when $G$ is amenable.
