---
tag: E820CTMJVM
kind: statement
role: proposition
name: Convex functions of subharmonic functions
msc: [31B05, 31A05]
uses: [Z1MHMGFNFW, 07Q7CNM5WF, 0RWMRTPC87, 0DEB0JMN0W, 02BH3MCBQB]
about: [Z1MHMGFNFW]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
---

## Statement

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]].

1. Let $u$ be [[subharmonic|Z1MHMGFNFW]] on $\Omega$ and let $\varphi \colon \R \to \R$ be [[convex|07Q7CNM5WF]] and increasing.
Put $\varphi(-\infty) = \lim_{t \to -\infty} \varphi(t) \in [-\infty, \infty)$.
Then $\varphi \circ u$ is subharmonic on $\Omega$.
2. Let $h$ be [[harmonic|0DEB0JMN0W]] on $\Omega$ and let $\varphi \colon \R \to \R$ be convex.
Then $\varphi \circ h$ is subharmonic on $\Omega$.

## Remarks

Proof idea: a convex function on $\R$ is continuous, and an increasing continuous function preserves upper semicontinuity.
For the sub-mean inequality on a sphere with normalised measure $\sigma$, monotonicity and [[Jensen's inequality|0RWMRTPC87]] give
$$\varphi(u(a)) \le \varphi\Big(\int u \, d\sigma\Big) \le \int \varphi(u) \, d\sigma.$$
In part 2 the first step is an equality, by the mean value property of $h$, so monotonicity of $\varphi$ is not needed.
If $\int u \, d\sigma = -\infty$, then $u(a) = -\infty$ and $\varphi(u(a)) = \inf \varphi$, which is below every value of $\varphi \circ u$.

Examples: if $u$ is subharmonic, so are $e^{u}$ and $\max(u, 0)$; if $h$ is harmonic, so are $\abs{h}$ and $h^2$.
Monotonicity is needed in part 1: $u(x) = \abs{x}^2$ is subharmonic and $\varphi(t) = -t$ is convex, but $\varphi \circ u = -\abs{x}^2$ is not subharmonic.

## Explanations

### L1 human

Subharmonic functions sit below their averages.
Applying an increasing convex function keeps them below their averages, because a convex function of an average is at most the average of the convex function.
So for example $e^u$ is subharmonic whenever $u$ is.

### L2 human

This is the multi-dimensional analogue of the fact that an increasing convex function of a convex function is convex.
Combined with the subharmonicity of $\log\abs{f}$ for holomorphic $f$, it shows that $\abs{f}^p$ is subharmonic for all $p > 0$, which is the starting point of the theory of Hardy spaces.
It also shows that $\log u$ need not be subharmonic when $u$ is, since $\log$ is concave; functions with $\log u$ subharmonic form the smaller class of log-subharmonic functions.
