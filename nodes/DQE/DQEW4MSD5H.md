---
tag: DQEW4MSD5H
kind: definition
name: Hausdorff distance
msc: ["54E35", 52A20, 54B20]
defines: F79WYYC07C
uses: [0VKD1TP7F3, 0R3H5PANRQ, 0QF1MZ9FRG]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_distance
---

## Definition

Let $(M, d)$ be a [[metric space|0VKD1TP7F3]].
For $x \in M$ and a nonempty subset $S \subseteq M$, let $d(x, S) = \inf_{s \in S} d(x, s)$, an [[infimum|0QF1MZ9FRG]].
The *Hausdorff distance* between nonempty subsets $A, B \subseteq M$ is
$$d_H(A, B) = \max\Big\{ \sup_{a \in A} d(a, B), \ \sup_{b \in B} d(b, A) \Big\} \in [0, +\infty],$$
where $\sup$ is the [[supremum|0R3H5PANRQ]].

## Remarks

Equivalently, $d_H(A, B)$ is the infimum of the $\varepsilon \ge 0$ with $A \subseteq B_\varepsilon$ and $B \subseteq A_\varepsilon$, where $S_\varepsilon = \set{x \in M : d(x, S) \le \varepsilon}$.
In $\R^n$ with the Euclidean distance and closed unit ball $D$, this reads $d_H(A, B) = \inf\set{\varepsilon \ge 0 : A \subseteq B + \varepsilon D, \ B \subseteq A + \varepsilon D}$ for nonempty compact $A, B$, with [[Minkowski sums|SXS6D87PHE]].

Example: $A = [0, 1]$ and $B = [0, 2]$ in $\R$.
Every point of $A$ lies in $B$, so $\sup_{a \in A} d(a, B) = 0$; the points of $B$ have $d(b, A) = \max(b - 1, 0)$, with supremum $1$ at $b = 2$.
So $d_H(A, B) = 1$.

Non-example of a metric: on all nonempty subsets, $d_H$ is not a metric.
For $A = (0, 1)$ and $B = [0, 1]$ in $\R$ one has $d_H(A, B) = 0$ although $A \neq B$, and $d_H(\set{0}, [0, \infty)) = +\infty$.
On the nonempty closed bounded subsets of $M$, and in particular on the nonempty compact subsets, $d_H$ is a metric.
If $M$ is complete, then so is this space of closed bounded subsets; if $M$ is compact, then so is the space of nonempty compact subsets.
