---
tag: E1V22QQHYJ
kind: concept
name: Semianalytic set
msc: [32B20, 14P15]
sources:
  - url: https://en.wikipedia.org/wiki/Subanalytic_set
---

## Summary

A semianalytic set is a subset of a [[real analytic manifold|Z7H98E1NHP]] with a simple local description.
Near each point it is given by finitely many equations and strict inequalities between [[real analytic functions|081WKEDK6C]].
It is the analytic analogue of a [[semialgebraic set|BX5WSK8ZCT]], with polynomials replaced by real analytic functions.
Semianalytic sets are locally finite unions of connected real analytic submanifolds, and they can be triangulated.
Since images of semianalytic sets under proper analytic maps need not be semianalytic, one also studies the larger class of [[subanalytic sets|K1HTQF26MA]].

## Explanations

### L1 human

Take some real analytic functions, such as polynomials, $\sin$ or $\exp$, and form sets by equations $f = 0$ and inequalities $g > 0$, combined with "and", "or" and "not".
A semianalytic set is a set that can be described this way near every point.
For example, the open half disc $\set{(x, y) : y > 0,\ x^2 + y^2 < 1}$ is semianalytic in $\R^2$.
The set $\set{0} \cup \set{1/n : n \ge 1}$ is not, because near $0$ it consists of infinitely many isolated points.
