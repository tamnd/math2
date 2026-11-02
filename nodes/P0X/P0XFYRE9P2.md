---
tag: P0XFYRE9P2
kind: definition
name: Indirect method by shooting
msc: [49M05, 65L10, 49K15]
defines: RDTESNZTKQ
uses: [ECT6RNF865, 7RPV2T29CF, RACVWG5QTK, WS9MRAZMFW, 07EXVNF9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Shooting_method
---

## Definition

Let $T > 0$, $x_0, x_1 \in \R^n$, let $U \subseteq \R^m$ be nonempty, and let $f \colon \R^n \times U \to \R^n$ and $L \colon \R^n \times U \to \R$ be continuously differentiable in $x$.
Consider the problem of minimising $\int_0^T L(x, u) \, dt$ subject to $x' = f(x, u)$, $x(0) = x_0$, $x(T) = x_1$.
Let $H(x, u, p) = p \cdot f(x, u) - L(x, u)$ be the [[Hamiltonian|RACVWG5QTK]] in the normal case of [[Pontryagin's maximum principle|7RPV2T29CF]].
Assume that for all $(x, p)$ the function $u \mapsto H(x, u, p)$ has a unique maximiser $u^*(x, p)$ in $U$, and that $u^*$ is continuously differentiable.
For $p_0 \in \R^n$, let $(x(\cdot\,; p_0), p(\cdot\,; p_0))$ be the solution on $[0, T]$, if it exists, of
$$x' = f(x, u^*(x, p)), \qquad p' = -\frac{\partial H}{\partial x}(x, u^*(x, p), p), \qquad x(0) = x_0, \qquad p(0) = p_0.$$
The *shooting function* is $S(p_0) = x(T; p_0) - x_1$.
The *indirect method by shooting* computes a zero $p_0^*$ of $S$, for example by [[Newton's method|07EXVNF9VP]], and returns the control $u(t) = u^*(x(t; p_0^*), p(t; p_0^*))$.

## Remarks

The second equation is the [[costate equation|WS9MRAZMFW]].
Every normal extremal of the maximum principle with these endpoints comes from a zero of $S$, so the method computes candidates for optimality, not proven minimisers.
The method is a special case of the [[shooting method|ECT6RNF865]], with unknowns $p_0$ instead of an initial slope.
Free final time or other boundary conditions add unknowns and equations to $S$, from the transversality conditions.
Multiple shooting splits $[0, T]$ into pieces to reduce the sensitivity of $S$.

Example: $n = m = 1$, $T = 1$, $f = u$, $L = u^2 / 2$, $U = \R$, $x_0 = 0$ and $x_1 = 1$.
Here $H = p u - u^2 / 2$, so $u^* = p$, and $p' = 0$.
Hence $p(t) = p_0$, $x(t) = p_0 t$ and $S(p_0) = p_0 - 1$.
The zero is $p_0^* = 1$, which gives the optimal control $u = 1$.

Non-example: if $U = [-1, 1]$ and $L = 0$ with $f = u$, the maximiser of $H = p u$ is not unique when $p = 0$ and is not differentiable in $p$.
Then the map $u^*$ of the definition does not exist, and the method must be adapted to the bang-bang structure.

## Explanations

### L1 human

The method guesses the initial costate, integrates the optimality conditions forward, and corrects the guess until the trajectory ends where it must.
