---
tag: PG8ZH3ZQ88
kind: statement
role: theorem
name: Kneser's theorem on solution sets
msc: [34A12]
uses: [098YP831QY, 075VBY4K4X, HG4S5HNWXF]
about: [0FXDW992DS]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_existence_theorem
---

## Statement

Let $t_0 \in \R$, $x_0 \in \R^n$ and $a, b > 0$, and let $f$ be continuous on $R = [t_0, t_0 + a] \times \set{x : \norm{x - x_0} \le b}$.
Let $M = \max_R \norm{f} > 0$ and $\alpha = \min(a, b/M)$.
For $c \in [t_0, t_0 + \alpha]$, let $S_c$ be the set of values $x(c)$ of all solutions $x : [t_0, t_0 + \alpha] \to \R^n$ of $x' = f(t, x)$ with $x(t_0) = x_0$.
Then $S_c$ is a [[continuum|HG4S5HNWXF]]: a nonempty, compact and connected subset of $\R^n$.

## Remarks

$S_c$ is nonempty by the [[Peano existence theorem|098YP831QY]].
Compactness follows from the Arzelà–Ascoli theorem, since all solutions are bounded and $M$-Lipschitz.
Connectedness is the heart of the proof: one approximates $f$ by functions for which solutions are unique.
For these the value at time $c$ depends continuously on parameters, and one passes to the limit.
Example: $x' = 2\sqrt{\abs{x}}$, $x(0) = 0$ has the solutions $x = 0$ and, for each $s \ge 0$, $x(t) = 0$ for $t \le s$ and $x(t) = (t - s)^2$ for $t \ge s$.
So $S_c = [0, c^2]$, an interval, as the theorem predicts.
In particular, the [[initial value problem|075VBY4K4X]] has either exactly one solution on $[t_0, t_0 + \alpha]$, or some $S_c$ has more than one point and is then uncountable.

## Explanations

### L1 human

When an initial value problem has many solutions, their positions at a later time do not scatter in separate pieces.
They fill a connected, closed and bounded region, the funnel of solutions.
So non-uniqueness, when it happens, comes as a whole continuum of solutions.

### L2 human

The theorem refines the [[Peano existence theorem|098YP831QY]]: it describes the whole set of solutions, not just one.
A stronger form says that the set of solutions itself, as a subset of the space of continuous functions, is compact and connected.
These results are used in the theory of differential inclusions and in the study of non-unique flows.
