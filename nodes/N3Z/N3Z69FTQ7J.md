---
tag: N3Z69FTQ7J
kind: definition
name: Semianalytic set
msc: [32B20, 14P15]
defines: E1V22QQHYJ
uses: [Z7H98E1NHP, 081WKEDK6C, 0ZCY0Z80B6]
sources:
  - url: https://en.wikipedia.org/wiki/Subanalytic_set
---

## Definition

Let $M$ be a [[real analytic manifold|Z7H98E1NHP]], for example an open subset of $\R^n$.
A subset $X \subseteq M$ is *semianalytic* if every point $p \in M$ has an open [[neighbourhood|0ZCY0Z80B6]] $U$ with the following property.
The set $X \cap U$ is a finite union of sets of the form
$$\set{x \in U : f(x) = 0,\ g_1(x) > 0, \dots, g_r(x) > 0},$$
where $r \ge 0$ and $f, g_1, \dots, g_r$ are [[real analytic functions|081WKEDK6C]] on $U$.

## Remarks

The condition is required at every point of $M$, not only at points of $X$.
Equivalently, $X \cap U$ belongs to the smallest family of subsets of $U$ that contains the sets $\set{g > 0}$ for real analytic $g$ on $U$.
Here the family is required to be closed under finite unions, finite intersections and complements.
Several equations $f_1 = \cdots = f_s = 0$ can be merged into the single equation $f_1^2 + \cdots + f_s^2 = 0$, and $f = 0$ gives no equation at all.
Example: $X = \set{(x, y) \in \R^2 : y > 0,\ x^2 + y^2 < 1}$ is semianalytic, with $U = \R^2$, $f = 0$, $g_1 = y$ and $g_2 = 1 - x^2 - y^2$.
Non-example: $X = \set{0} \cup \set{1/n : n \ge 1}$ is not semianalytic in $\R$.
Let $U$ be any open interval about $0$, and $f, g_i$ real analytic on $U$.
If $f$ vanishes at infinitely many of the points $1/n$, then $f = 0$ on $U$ by the identity theorem; otherwise $\set{f = 0}$ is finite near $0$.
So each set $\set{f = 0, g_i > 0}$ is, near $0$, either finite or a union of finitely many open intervals, and a finite union of such sets cannot equal $X$ near $0$.
Every semialgebraic subset of $\R^n$ and every real analytic subset of $M$ is semianalytic.
