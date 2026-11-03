---
tag: N0TPG3JZ2Y
kind: problem
name: Inhomogeneous Cauchy–Riemann equations
msc: [32W05, 32T05, 35N15]
uses: [9PT772R94A, M1VKCW3RFW, DC81TCR98Y, 0V33BNKZ9S, AHYZMSBBNH]
about: [M1VKCW3RFW, 9PT772R94A]
sources:
  - url: https://en.wikipedia.org/wiki/Dolbeault_cohomology
history:
  posed_by: "Pierre Dolbeault"
  first_stated: "1953"
  notes: "Dolbeault's 1953 work gave local solvability on polydiscs, now the Dolbeault–Grothendieck lemma, the earliest well-documented treatment in several variables; the one-variable case follows from the Cauchy integral formula. Global solutions on pseudoconvex domains came from the work of Kohn and Hörmander in the 1960s."
---

## Problem

Let $n \ge 1$ and let $\Omega \subseteq \C^n$ be an open set.
Let $g = \sum_{j=1}^n g_j \, d\bar z_j$ be a [[(0,1)-form|DC81TCR98Y]] on $\Omega$ whose coefficients $g_j$ are [[smooth functions|0V33BNKZ9S]].
Suppose that $g$ satisfies the compatibility condition $\bar\partial g = 0$, that is,
$$\frac{\partial g_j}{\partial \bar z_k} = \frac{\partial g_k}{\partial \bar z_j} \quad \text{for all } j, k = 1, \dots, n.$$
Find a smooth function $u \colon \Omega \to \C$ with $\bar\partial u = g$, that is,
$$\frac{\partial u}{\partial \bar z_j} = g_j \quad \text{for } j = 1, \dots, n,$$
where $\bar\partial$ is the [[dbar operator|M1VKCW3RFW]].
Determine for which $\Omega$ a solution exists for every such $g$, and with which estimates on $u$.

## Remarks

The compatibility condition is necessary, because $\bar\partial \bar\partial u = 0$ for every smooth $u$.
When $g = 0$ the system is the [[Cauchy–Riemann equations|9PT772R94A]], whose solutions are the holomorphic functions.
So two solutions differ by a holomorphic function on $\Omega$.
For $n = 1$ there is no compatibility condition, and the equation $\partial u / \partial \bar z = g$ is solvable on every open set of $\C$.
On a polydisc the problem is solvable for every compatible $g$.
The local form of this fact is the [[Dolbeault–Grothendieck lemma|5858M5PGN6]].
If $\Omega$ is [[pseudoconvex|AHYZMSBBNH]], a smooth solution exists for every compatible $g$.
This follows from [[Hörmander's L2 estimates|TPSH4ETK67]], which also bound the size of $u$.
Conversely, if the analogous equation $\bar\partial u = g$ for $\bar\partial$-closed $(0,q)$-forms $g$ is solvable for every $q$ with $1 \le q \le n-1$, then $\Omega$ is pseudoconvex.
For $n = 2$ this means that solvability for every compatible $g$ characterizes pseudoconvex open sets.
Example: on $\C^2$, the form $g = \bar z_2 \, d\bar z_1 + \bar z_1 \, d\bar z_2$ is compatible, and $u = \bar z_1 \bar z_2$ solves $\bar\partial u = g$.
On $\C^2 \setminus \set{0}$, which is not pseudoconvex, there are compatible forms with no solution.

## Explanations

### L1 human

A holomorphic function is one that is killed by the operator $\bar\partial$.
The inhomogeneous problem asks for a function whose $\bar\partial$ is a prescribed right-hand side.
In several variables the right-hand side must satisfy a consistency condition, just as a vector field must be curl-free to be a gradient.
Whether every consistent right-hand side can be reached depends on the shape of the domain.
Solving this equation is the standard tool to build holomorphic functions with given properties: one first builds a smooth function and then corrects it by a solution of $\bar\partial u = g$.
