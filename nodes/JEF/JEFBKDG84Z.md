---
tag: JEFBKDG84Z
kind: statement
role: corollary
name: Schauder fixed-point theorem for integral equations
msc: [45G10, 47H10]
uses: [DCPFVVZZ54, WZ4Z26XSVC, 0381S8Z5P0, 0X3WGX95FE, 0VK6VEH345, 7H3YSSDEBK, QGRBR04JJN]
about: [WZ4Z26XSVC]
sources:
  - url: https://en.wikipedia.org/wiki/Schauder_fixed-point_theorem
---

## Statement

Let $a < b$ and $R > 0$.
Let $K \colon [a, b] \times [a, b] \times [-R, R] \to \R$ and $f \colon [a, b] \to \R$ be [[continuous|0X3WGX95FE]], and let $M = \max \abs{K}$.
Assume that
$$\max_{x \in [a, b]} \abs{f(x)} + (b - a)\, M \le R.$$
Then the [[Urysohn equation|WZ4Z26XSVC]]
$$\varphi(x) = f(x) + \int_a^b K\bigl(x, t, \varphi(t)\bigr)\, dt, \quad x \in [a, b],$$
has a continuous solution $\varphi$ with $\abs{\varphi(x)} \le R$ for all $x \in [a, b]$.

## Remarks

Let $B$ be the set of continuous functions on $[a, b]$ with values in $[-R, R]$; it is closed, bounded and convex in $C[a, b]$ with the sup norm.
Let $T\varphi$ be the right side of the equation.
The hypothesis gives $T(B) \subseteq B$, and the uniform continuity of $K$ on its compact domain shows that $T$ is continuous and that $T(B)$ is equicontinuous.
By the [[Arzelà–Ascoli theorem|0381S8Z5P0]], $T(B)$ is relatively compact.
The [[Schauder fixed-point theorem|DCPFVVZZ54]], in its form for continuous maps of a closed convex set into a compact subset, gives a fixed point.

The theorem gives existence but not uniqueness.
Example: on $[0, 1]$ take $f = 0$, $R = 1$ and $K(x, t, u) = \sqrt{\abs{u}}$, so $M = 1$ and the hypothesis $0 + 1 \le 1$ holds.
Both $\varphi = 0$ and $\varphi = 1$ are solutions, since $\int_0^1 \sqrt{1}\, dt = 1$.
Here $K$ is not Lipschitz in $u$ near $0$, so the [[Banach fixed point theorem|0VK6VEH345]] does not apply.

The size condition cannot be dropped: for $f = 0$ and $K(x, t, u) = 1 + u^2$ on $[0, 1]$, any solution would be a constant $c = \int_0^1 (1 + c^2)\, dt = 1 + c^2$, which has no real root.

## Explanations

### L1 human

To solve an integral equation, one looks for a function that the right side of the equation leaves unchanged.
If the right side maps a ball of continuous functions into itself and squeezes it into a compact set, Schauder's theorem says that such a function exists.
The size condition makes sure the ball is mapped into itself.
The theorem says nothing about how many solutions there are, and there can be several.

### L2 human

This is the model for existence proofs with compactness, as opposed to proofs with contractions.
Compactness comes from the smoothing effect of integration and the Arzelà–Ascoli theorem; continuity of the kernel is all that is needed.
Peano's existence theorem for ordinary differential equations is the Volterra analogue.
Sometimes no invariant ball is easy to find.
Then [[Schaefer's fixed point theorem|7H3YSSDEBK]] or the [[Leray–Schauder method|QGRBR04JJN]] replaces it by an a priori bound for a family of equations.
