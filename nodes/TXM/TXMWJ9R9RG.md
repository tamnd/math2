---
tag: TXMWJ9R9RG
kind: statement
role: theorem
name: Udwadia–Kalaba equation
msc: [70F25, 70F20, 70G10]
uses: [BCF1EX9W2M, 9WQT2RMGTZ, AXA8HN8Y45, PTRV0QFSB9, 0KX66CZMBB, 0YY8VX28JR, FZWAHMFZM3]
about: [PTRV0QFSB9, AXA8HN8Y45]
sources:
  - url: https://en.wikipedia.org/wiki/Udwadia%E2%80%93Kalaba_formulation
same_as:
  wikidata: Q5508956
  wikipedia: Udwadia–Kalaba formulation
---

## Statement

Consider a mechanical system with [[generalized coordinates|BCF1EX9W2M]] $q \in \R^n$.
Let $M(q, t)$ be its mass matrix, a symmetric [[positive definite|0KX66CZMBB]] $n \times n$ matrix, and let $Q(q, \dot q, t)$ collect the given [[generalized forces|9WQT2RMGTZ]].
Without constraints the motion obeys $M \ddot q = Q$.
Suppose the system also obeys constraints, [[holonomic|AXA8HN8Y45]] or [[nonholonomic|PTRV0QFSB9]].
After differentiation in time, let them take the form $A(q, \dot q, t)\, \ddot q = b(q, \dot q, t)$, with $A$ an $m \times n$ matrix and $b \in \R^m$.
Assume this linear system in $\ddot q$ is consistent.
Assume the constraint forces are ideal, that is, they do no work in any virtual displacement $v$ with $A v = 0$.
Write $a = M^{-1} Q$ for the unconstrained acceleration, $M^{1/2}$ for the positive definite square root of $M$, and $B^{+}$ for the [[Moore–Penrose inverse|0YY8VX28JR]] of a matrix $B$.
Then the constrained motion satisfies
$$\ddot q = a + M^{-1/2} \big(A M^{-1/2}\big)^{+} (b - A a),$$
and the force of constraint is $Q_c = M^{1/2} \big(A M^{-1/2}\big)^{+} (b - A a)$.

## Remarks

The proof uses [[Gauss's principle of least constraint|FZWAHMFZM3]]: the actual $\ddot q$ minimizes $(\ddot q - a)^T M (\ddot q - a)$ subject to $A\ddot q = b$.
With $z = M^{1/2}(\ddot q - a)$ this asks for the solution of $(A M^{-1/2}) z = b - A a$ of least Euclidean norm, which is $z = (A M^{-1/2})^{+}(b - A a)$.
The formula needs no independence of the constraints: $A$ may have dependent rows, and the Moore–Penrose inverse handles this.
Example: take a particle of mass $m$ in the plane under gravity, so $M = m I$ and $a = (0, -g)$, constrained to the circle $x^2 + y^2 = \ell^2$.
Differentiating the constraint twice gives $x\ddot x + y\ddot y = -(\dot x^2 + \dot y^2)$.
The formula then returns the pendulum equation, with the rod tension as constraint force.
If the constraints are not ideal, an extra term for the work of the constraint forces must be added.

## Explanations

### L1 human

The equation tells how to correct the motion of a free system so that it obeys its constraints.
Start from the acceleration the forces alone would give, measure how much it violates the constraints, and add the smallest correction, measured with the masses, that removes the violation.
It gives the motion and the constraint forces in one explicit formula.

### L2 human

Unlike Lagrange's method with multipliers, the formula treats holonomic and nonholonomic constraints in one way and does not require the constraints to be independent.
It is a closed-form version of Gauss's principle of least constraint and of Appell's equations.
It is used in multibody dynamics and in control, where constraints may be imposed as desired trajectories.
