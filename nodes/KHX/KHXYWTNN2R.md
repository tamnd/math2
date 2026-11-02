---
tag: KHXYWTNN2R
kind: statement
role: theorem
name: Ill-posedness of first-kind equations
msc: [45Q05, 47A52, 45B05]
uses: [W09B9NZ9B5, M2NEP1K5AE, 03J5RAKB30, 097C7KCAT5]
about: [W09B9NZ9B5, M2NEP1K5AE]
sources:
  - url: https://en.wikipedia.org/wiki/Well-posed_problem
---

## Statement

Let $X$ and $Y$ be [[normed vector spaces|03J5RAKB30]] with $X$ infinite-dimensional, and let $K \colon X \to Y$ be a [[compact linear operator|M2NEP1K5AE]].
Then there is no constant $c > 0$ with $\norm{K x} \ge c \norm{x}$ for all $x \in X$.
Consequently, the equation of the first kind $K x = y$ is not [[well posed|W09B9NZ9B5]].
That is, $K$ is not injective, or $K$ is not surjective onto $Y$, or the inverse $K^{-1} \colon K(X) \to X$ is not continuous.

## Remarks

Proof idea: if $\norm{K x} \ge c \norm{x}$ for all $x$, then $K$ is injective and $K^{-1}$ is bounded on $K(X)$ with norm at most $1/c$.
The identity of $X$ equals $K^{-1} K$, the product of a bounded and a compact operator, so it is compact.
Then the closed unit ball of $X$ is compact, which contradicts [[Riesz's lemma|097C7KCAT5]] since $X$ is infinite-dimensional.

The main application is to [[integral equations of the first kind|ZDS77Q0F06]].
Let $k$ be continuous on $[0, 1]^2$ and $(K x)(t) = \int_0^1 k(t, s) \, x(s) \, ds$ on $X = Y = L^2(0, 1)$; this operator is compact.
For $x_n(s) = \sin(n \pi s)$ one has $\norm{x_n}_2 = 1/\sqrt{2}$, but $(K x_n)(t) \to 0$ uniformly in $t$ by the [[Riemann–Lebesgue lemma|WVKDC011KP]] and the uniform continuity of $k$.
So the data $y + K x_n$ are close to $y$ while the solutions $x + x_n$ stay far from $x$.

The hypothesis that $X$ is infinite-dimensional is needed.
On a finite-dimensional space every linear operator is compact, and an invertible matrix gives a well-posed equation.

## Explanations

### L1 human

An integral operator with a smooth kernel averages out fast oscillations.
So two very different functions, one with an added fast wiggle, are sent to almost the same image.
Going backwards, from the image to the function, therefore amplifies small errors in the data without bound.
This is why first-kind integral equations, unlike second-kind ones, are ill posed.

### L2 human

The theorem explains why [[inverse problems|PCMW7KN5P4]] modelled by first-kind equations, such as deblurring an image or recovering a source from far-field measurements, need regularization.
Its quantitative form uses the [[singular values|QSJKPKPM7H]] $\sigma_n \to 0$ of $K$: the error in the component along the $n$-th singular vector is multiplied by $1/\sigma_n$.
[[Picard's criterion|MPB3QF09E5]] describes exactly which data lie in the range, and [[Tikhonov regularization|M68V0M5A3R]] gives stable approximate solutions.
By contrast, a second-kind equation $x - K x = y$ with compact $K$ is well posed as soon as it is uniquely solvable, by the [[Fredholm alternative|4HH8C9V8JQ]].
