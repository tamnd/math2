---
tag: DCPFVVZZ54
kind: statement
role: theorem
name: Schauder fixed-point theorem
msc: [47H10, 54H25]
uses: [03J5RAKB30, 02AS45T3H9, 0R6EWFKRCF, 0X3WGX95FE]
about: [02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Schauder_fixed-point_theorem
same_as:
  wikidata: Q656176
  wikipedia: Schauder fixed-point theorem
---

## Statement

Let $X$ be a real [[normed vector space|03J5RAKB30]] and let $K \subseteq X$ be a nonempty [[compact|0R6EWFKRCF]] [[convex set|02AS45T3H9]].
Let $f \colon K \to K$ be a [[continuous map|0X3WGX95FE]].
Then $f$ has a fixed point: there is $x \in K$ with $f(x) = x$.

## Remarks

The proof reduces to the Brouwer fixed-point theorem.
For $\varepsilon > 0$, compactness gives a finite $\varepsilon$-net $\set{y_1, \ldots, y_m}$ of $K$.
The Schauder projection maps $K$ continuously into the convex hull of the $y_i$ and moves each point by less than $\varepsilon$.
Brouwer's theorem gives a fixed point of the projected map on this finite-dimensional convex set, and it is an $\varepsilon$-fixed point of $f$.
A limit as $\varepsilon \to 0$ gives a fixed point of $f$.

An equivalent form is often used in analysis.
Let $C$ be a nonempty closed convex subset of a Banach space and let $f \colon C \to C$ be continuous with $f(C)$ contained in a compact set; then $f$ has a fixed point.

Example: Peano's existence theorem for $y' = F(t, y)$, $y(0) = y_0$ with continuous $F$ follows.
The integral operator $y \mapsto y_0 + \int_0^t F(s, y(s)) \, ds$ maps a closed convex set of continuous functions into a compact set, by the Arzelà–Ascoli theorem.
Its fixed point is a solution.

Compactness cannot be dropped: on the closed unit ball of $\ell^2$, Kakutani's map $x \mapsto \big(\sqrt{1 - \norm{x}^2}, x_1, x_2, \ldots\big)$ is continuous with no fixed point.

## Explanations

### L1 human

Brouwer's theorem says that a continuous map of a disc or ball into itself fixes some point.
Schauder's theorem extends this to infinite-dimensional spaces, such as spaces of functions, provided the set is compact and convex.
It turns many existence problems for differential and integral equations into the search for a fixed point.

### L2 human

The theorem is the main tool for nonlinear problems without uniqueness, where the Banach fixed point theorem does not apply.
Compactness usually comes from an Arzelà–Ascoli argument or a compact Sobolev embedding.
Tychonoff extended it to compact convex subsets of locally convex spaces, and [[Schaefer's theorem|7H3YSSDEBK]] replaces the invariant set by an a priori bound.
For set-valued maps the analogue is the [[Kakutani fixed-point theorem|7V3HWGR32Z]] and its infinite-dimensional versions.
