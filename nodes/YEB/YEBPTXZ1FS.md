---
tag: YEBPTXZ1FS
kind: statement
role: theorem
name: Sturm separation theorem
msc: [34C10, 34A30]
uses: [0QQRP17Z7S, 0KC1NMG90B]
about: [0QQRP17Z7S]
sources:
  - url: https://en.wikipedia.org/wiki/Sturm_separation_theorem
same_as:
  wikidata: Q7629089
  wikipedia: Sturm separation theorem
---

## Statement

Let $I \subseteq \R$ be an interval and let $p, q \colon I \to \R$ be continuous.
Let $y_1$ and $y_2$ be linearly independent real solutions of the [[linear differential equation|0QQRP17Z7S]]
$$y'' + p(x) y' + q(x) y = 0 \quad \text{on } I.$$
Then the zeros of $y_1$ and $y_2$ in $I$ strictly alternate.
That is, $y_1$ and $y_2$ have no common zero.
Moreover, if $x_1 < x_2$ are two consecutive zeros of $y_1$ in $I$, then $y_2$ has exactly one zero in the open interval $(x_1, x_2)$.

## Remarks

The [[Wronskian|0KC1NMG90B]] $W = y_1 y_2' - y_1' y_2$ of two independent solutions never vanishes, so it has a constant sign on $I$.
A common zero would make $W$ vanish there.
If $y_2$ had no zero in $(x_1, x_2)$, the function $y_1 / y_2$ would be differentiable on $[x_1, x_2]$ with derivative $-W / y_2^2$ of constant sign.
Yet it vanishes at $x_1$ and $x_2$, which contradicts Rolle's theorem.
Applying the same argument with the roles exchanged shows that there is at most one zero.
Example: for $y'' + y = 0$, the solutions $\sin x$ and $\cos x$ have zeros at $k\pi$ and at $\pi/2 + k\pi$, which alternate.
Linear independence is needed: $y_1 = \sin x$ and $y_2 = 2 \sin x$ have the same zeros.

## Explanations

### L1 human

Take two genuinely different solutions of a second-order linear equation.
Between two crossings of the axis by one of them, the other crosses the axis exactly once.
So the zeros of the two solutions interlace like the zeros of sine and cosine.

### L2 human

The theorem shows that oscillation is a property of the equation and not of the solution.
If one nonzero solution has infinitely many zeros on an interval, then every nonzero solution does.
It also shows that the numbers of zeros of two solutions on an interval differ by at most one.
For equations $y'' + q y = 0$ it also follows from the [[Sturm comparison theorem|W7VXNYZQN2]] with $q_1 = q_2$, and it is a basic tool in Sturm–Liouville theory.
