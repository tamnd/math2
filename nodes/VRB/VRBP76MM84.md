---
tag: VRBP76MM84
kind: statement
role: theorem
name: Operator Cauchy equation and one-parameter semigroups
msc: [47D06, 39B42]
uses: [06GZ956657, 06EKW1AKXF, KX3QRA3CEP, EVF180QJXY, 60HSWZBTK9]
about: [EVF180QJXY, KX3QRA3CEP]
sources:
  - url: https://en.wikipedia.org/wiki/C0-semigroup
---

## Statement

Let $X$ be a [[Banach space|06GZ956657]] and let $\mathcal{L}(X)$ be the space of bounded linear operators on $X$ with the [[operator norm|06EKW1AKXF]].
Let $T \colon [0, \infty) \to \mathcal{L}(X)$ satisfy:

1. $T(0) = I$, the identity operator;
2. $T(s + t) = T(s) T(t)$ for all $s, t \ge 0$;
3. $\lim_{t \to 0^+} \norm{T(t) - I} = 0$.

Then there is a unique $A \in \mathcal{L}(X)$ such that $T(t) = e^{tA}$ for all $t \ge 0$, where $e^{tA}$ is the [[exponential|KX3QRA3CEP]] of $tA$.
Conversely, for every $A \in \mathcal{L}(X)$ the map $t \mapsto e^{tA}$ satisfies conditions 1 to 3.

## Remarks

Conditions 2 and 3 make $T$ continuous in operator norm on $[0, \infty)$.
Let $V(t) = \int_0^t T(s) \, ds$; since $V(t)/t \to I$ in norm, $V(t_0)$ is invertible for a small $t_0 > 0$.
The functional equation gives $(T(h) - I) V(t_0) = V(t_0 + h) - V(h) - V(t_0)$, and dividing by $h$ shows that $T$ is differentiable at $0$ with derivative $A = (T(t_0) - I) V(t_0)^{-1}$.
Then $T'(t) = A T(t)$, and uniqueness for this linear equation gives $T(t) = e^{tA}$.
The operator $A$ is the [[generator|60HSWZBTK9]] of the semigroup.
For $X = \R^n$ this says that the continuous solutions $F \colon [0, \infty) \to \R^{n \times n}$ of $F(s + t) = F(s) F(t)$ with $F(0) = I$ are exactly $F(t) = e^{tA}$.
Condition 3 cannot be weakened to strong continuity.
The left shifts $(T(t)f)(s) = f(s + t)$ on $L^2(\R)$ form a [[$C_0$-semigroup|EVF180QJXY]] with the unbounded generator $f \mapsto f'$, so they are not of the form $e^{tA}$ with $A$ bounded.
Condition 1 is needed: for a projection $P \ne I$, the constant map $T(t) = P$ satisfies condition 2 and is norm continuous, but $T(0) = P \ne e^{0A}$.

## Explanations

### L1 human

The only continuous real functions with $f(s + t) = f(s) f(t)$ and $f(0) = 1$ are $f(t) = e^{at}$.
This theorem is the same fact for operators: a family of operators that composes like exponentials, and moves continuously in norm, is an exponential $e^{tA}$.
The operator $A$ is the rate of change of the family at time $0$.

### L2 human

The theorem identifies the norm-continuous one-parameter semigroups with the bounded operators $A$.
Many evolution equations, such as the heat equation, give semigroups that are only strongly continuous, and then the generator is an unbounded operator.
For those semigroups the Hille–Yosida theorem takes the place of this result.
