---
tag: RH1WTN38RQ
kind: object
name: Banach–Mazur compactum
msc: [46B07, 52A21]
instance_of: [0VKD1TP7F3]
uses: [03J5RAKB30, 06EKW1AKXF]
sources:
  - url: https://en.wikipedia.org/wiki/Banach%E2%80%93Mazur_compactum
same_as:
  wikidata: Q806050
  wikipedia: Banach–Mazur compactum
---

## Description

Let $n \ge 1$ be an integer.
For two real [[normed spaces|03J5RAKB30]] $X$ and $Y$ of dimension $n$, the Banach–Mazur distance is
$$d(X, Y) = \inf \set{\norm{T} \, \norm{T^{-1}} : T \colon X \to Y \text{ a linear isomorphism}}.$$
Here $\norm{T}$ is the [[operator norm|06EKW1AKXF]].
The Banach–Mazur compactum $\mathcal{Q}_n$ is the set of isometry classes of $n$-dimensional real normed spaces with the metric $\delta(X, Y) = \log d(X, Y)$.
It is a compact [[metric space|0VKD1TP7F3]].

## Remarks

The function $\delta$ is a metric on isometry classes.
It is symmetric because $\norm{T^{-1}} \, \norm{T}$ is the same number for $T$ and $T^{-1}$.
The triangle inequality comes from $\norm{ST} \le \norm{S} \, \norm{T}$, so $d(X, Z) \le d(X, Y) \, d(Y, Z)$.
If $d(X, Y) = 1$, then a compactness argument gives an isomorphism with $\norm{T} \, \norm{T^{-1}} = 1$, and a multiple of it is an isometry.

By John's theorem, $d(X, \ell_2^n) \le \sqrt{n}$ for every $n$-dimensional normed space $X$, where $\ell_2^n$ is $\R^n$ with the Euclidean norm.
So the diameter of $\mathcal{Q}_n$ in the multiplicative form is at most $n$.
Gluskin proved that this order is right: there are $n$-dimensional spaces at distance at least $c n$ from each other, for a constant $c > 0$ that does not depend on $n$.

## Explanations

### L1 human

Each point of the Banach–Mazur compactum is a way to measure length in $n$-dimensional space, up to a change of coordinates that keeps lengths.
Two such ways are close when a linear change of coordinates can squeeze one unit ball between the other unit ball and a slightly larger copy of it.
For $n = 2$, the square ball of the max norm and the round disc of the Euclidean norm are at distance $\log \sqrt{2}$.
