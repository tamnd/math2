---
tag: ZY302KCKHR
kind: statement
role: theorem
name: Khachiyan's theorem that linear programming is in P
msc: [90C05, 90C60, 68Q25]
uses: [VNMXB0J2KA, TJR5MQHNYE, GVT2NKN37K, T00W8RQT8E]
about: [VNMXB0J2KA, GVT2NKN37K]
sources:
  - url: https://en.wikipedia.org/wiki/Ellipsoid_method
---

## Statement

There is an algorithm with the following properties.
Its input is a rational $m \times n$ matrix $A$, a vector $b \in \Q^m$ and a vector $c \in \Q^n$, written in binary with total bit length $L$.
It decides whether the [[linear program|VNMXB0J2KA]] "maximize $c^T x$ subject to $A x \le b$" is infeasible, unbounded, or has an optimal solution.
In the last case it outputs a rational optimal solution.
Its number of bit operations is bounded by a polynomial in $L$.
In particular, linear programming belongs to the [[complexity class P|GVT2NKN37K]].

## Remarks

Leonid Khachiyan proved this in 1979 with the [[ellipsoid method|TJR5MQHNYE]].
The ellipsoid method needs $O(n^2 L)$ iterations to decide feasibility of a system $A x \le b$.
Rational data are essential to the argument: a feasible system has a basic solution whose numerators and denominators have bit length polynomial in $L$.
If the system is feasible, a slightly relaxed system contains a ball whose radius has a computable lower bound.
The volumes of the ellipsoids drop below the volume of that ball within polynomially many steps.
Optimization reduces to feasibility, for example by binary search on the objective value or by writing primal and dual constraints together with $c^T x \ge b^T y$.

The bound is in terms of the bit length $L$, not of $m$ and $n$ alone.
For example, the data $A = (1)$, $b = (2^{k})$ have $m = n = 1$ but bit length about $k$.
So the result does not give a strongly polynomial algorithm; whether one exists is an open problem.

## Explanations

### L1 human

Before 1979 nobody knew whether linear programs can be solved in time that grows only polynomially with the size of the input.
The simplex method is fast in practice but slow on special examples.
Khachiyan showed that a different method, which traps the solution inside shrinking ellipsoids, always runs in polynomial time.

### L2 human

The result settled the complexity of linear programming, and through the equivalence of separation and optimization it gives polynomial algorithms for many combinatorial problems whose polytopes have exponentially many facets.
The ellipsoid method is too slow in practice; interior-point methods, starting with Karmarkar's algorithm, are polynomial and also practical.
The running time depends on the bit length of the data, so the method is polynomial but not strongly polynomial.
