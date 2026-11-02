---
tag: F5V7CXW30E
kind: statement
role: theorem
name: Hörmander–Mikhlin multiplier theorem
msc: [42B15, 42B20]
uses: [RAGR38Q40B, DPVM34ADZV, SASP14MA1Z, H4C888M5AZ]
about: [RAGR38Q40B]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplier_(Fourier_analysis)
---

## Statement

Let $n \ge 1$ and let $k = \floor{n/2} + 1$.
Let $m \colon \R^n \setminus \set{0} \to \C$ be a function of class $C^k$.
Assume that there is a constant $A$ such that
$$\abs{\partial^\alpha m(\xi)} \le A \abs{\xi}^{-\abs{\alpha}} \quad \text{for all } \xi \ne 0$$
and all multi-indices $\alpha$ with $\abs{\alpha} \le k$.
Then $m$ is an [[$L^p$ multiplier|RAGR38Q40B]] for every $1 < p < \infty$.
Let $\hat f$ be the [[Fourier transform|DPVM34ADZV]] of $f$.
There is a constant $C$, depending only on $n$ and $p$, with
$$\norm{(m \hat f)^\vee}_{L^p(\R^n)} \le C A \norm{f}_{L^p(\R^n)}$$
for every Schwartz function $f$.
Moreover, the operator $f \mapsto (m \hat f)^\vee$ is of weak type $(1, 1)$.

## Remarks

The condition with $\alpha = 0$ says that $m$ is bounded, so the operator is bounded on $L^2$ by the Plancherel theorem.
The derivative conditions make the inverse Fourier transform $K$ of $m$ a kernel that satisfies the Hörmander condition $\int_{\abs{x} > 2\abs{y}} \abs{K(x - y) - K(x)} \, dx \le CA$.
Then the [[Calderón–Zygmund theorem|AE1HJ8D8GV]] gives the weak type $(1, 1)$ bound, interpolation gives $1 < p \le 2$, and duality gives $2 \le p < \infty$.
Hörmander weakened the pointwise derivative bounds to bounds on the $L^2$ averages of the derivatives over dyadic shells.

Example: in $\R^n$, $m(\xi) = \xi_j / \abs{\xi}$ is smooth away from $0$ and homogeneous of degree $0$.
So $\partial^\alpha m$ is homogeneous of degree $-\abs{\alpha}$ and bounded on the unit sphere, which gives the hypothesis.
Hence the [[Riesz transforms|FRNDFJ9WQ5]] are bounded on $L^p(\R^n)$ for $1 < p < \infty$.

Some smoothness is needed.
The indicator of a ball is bounded but not smooth.
By [[Fefferman's ball multiplier theorem|4A5MJY4XPV]], it is not an $L^p$ multiplier for $p \ne 2$ when $n \ge 2$.

## Explanations

### L1 human

Take a multiplier that is smooth away from the origin, whose derivatives shrink at the right rate as the frequency grows.
Such a multiplier keeps $L^p$ size under control for every $p$ strictly between $1$ and $\infty$.
The typical case is a function that depends only on the direction of $\xi$, or that changes slowly on each dyadic scale.
One only needs to check about half as many derivatives as there are dimensions.

### L2 human

This is the most used multiplier criterion in PDE.
It shows at once that the Riesz transforms, the operators $\partial_i \partial_j \Delta^{-1}$, and the imaginary powers $(-\Delta)^{it}$ are bounded on $L^p(\R^n)$ for $1 < p < \infty$.
It sits between the [[Marcinkiewicz multiplier theorem|375ZGE0V2W]], which uses dyadic rectangles, and the general Calderón–Zygmund theory, which supplies its proof.
