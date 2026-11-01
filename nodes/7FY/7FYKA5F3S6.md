---
tag: 7FYKA5F3S6
kind: counterexample
name: Fort space
msc: [54G20, 54D30]
uses: [0TVJZYB6SH, 0S1FJ8VEX9, 0CP5NDD21C, 091GJ3FYD7, 0GWN3CMRK8, 0W7FBYS1F1]
sources:
  - url: https://en.wikipedia.org/wiki/Fort_space
---

## Counterexample

Let $X$ be an infinite set and let $p \in X$.
Declare $U \subseteq X$ open if $p \notin U$, or if $p \in U$ and $X \setminus U$ is finite.
This is the Fort space on $X$ with point $p$.
It is [[compact|0TVJZYB6SH]] and [[Hausdorff|0S1FJ8VEX9]].
If $X$ is [[uncountable|0W7FBYS1F1]], it is not [[first-countable|0CP5NDD21C]], and so not [[metrizable|091GJ3FYD7]].

## Remarks

Compactness: in an open cover, one member $U$ contains $p$, and the finitely many points outside $U$ need finitely many more members.
Hausdorff: two points $x, y \ne p$ are separated by $\set{x}$ and $\set{y}$, and $x \ne p$ is separated from $p$ by $\set{x}$ and $X \setminus \set{x}$.
Let $X$ be uncountable and let $U_1, U_2, \dots$ be open sets containing $p$.
Their intersection has countable complement, so it contains a point $x \ne p$.
Then $X \setminus \set{x}$ is an open set containing $p$ that contains no $U_n$, so $p$ has no countable neighbourhood base.
The Fort space is the [[one-point compactification|0GWN3CMRK8]] of the discrete space $X \setminus \set{p}$.
If $X$ is countably infinite, it is homeomorphic to $\set{0} \cup \set{1/n : n \ge 1}$ with the usual topology, which is metrizable.

## Explanations

### L1 human

Take a set of isolated points and add one extra point $p$.
A set around $p$ is open when it leaves out only finitely many points.
This makes the space compact and keeps points apart.
With uncountably many points, no countable list of open sets can pin down $p$, so no distance function gives this topology.
