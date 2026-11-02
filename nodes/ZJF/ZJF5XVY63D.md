---
tag: ZJF5XVY63D
kind: definition
name: C0-semigroup
msc: [47D06, 34G10]
defines: EVF180QJXY
uses: [06GZ956657, 06EKW1AKXF, 0XMEM406JM, 020M04FN1H]
sources:
  - url: https://en.wikipedia.org/wiki/C0-semigroup
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]] and let $\mathcal{L}(X)$ be the space of bounded linear operators on $X$.
A *$C_0$-semigroup* (strongly continuous semigroup) on $X$ is a map $T \colon [0, \infty) \to \mathcal{L}(X)$ such that:

1. $T(0) = I$, the identity operator;
2. $T(t + s) = T(t) T(s)$ for all $t, s \ge 0$;
3. $\lim_{t \to 0^+} \norm{T(t) x - x} = 0$ for every $x \in X$.

Its *generator* is the operator $A$ given by $A x = \lim_{t \to 0^+} \frac{T(t) x - x}{t}$, with domain $D(A)$ the set of $x \in X$ for which this limit exists.

## Remarks

Conditions 1 and 2 say that $T$ is a monoid homomorphism from $([0, \infty), +)$ into the multiplicative [[semigroup|0XMEM406JM]] $\mathcal{L}(X)$.

Example: for a bounded operator $A$, $T(t) = e^{tA}$, the [[exponential|020M04FN1H]] series, is a $C_0$-semigroup with generator $A$; here even $\norm{T(t) - I} \to 0$ in [[operator norm|06EKW1AKXF]].

Example: on $X = L^p(\R)$ with $1 \le p < \infty$, the left shifts $(T(t) f)(s) = f(s + t)$ form a $C_0$-semigroup.
Condition 3 holds because translation is continuous in $L^p$ norm for $p < \infty$, which follows by approximation with continuous functions of compact support.
The generator is $A f = f'$ on the Sobolev space $W^{1,p}(\R)$.

Non-example: the same shifts on $L^\infty(\R)$ fail condition 3.
For $f$ the indicator function of $[0, 1]$ and $0 < t < 1$, $T(t) f - f$ equals $1$ in absolute value on $[-t, 0)$, so $\norm{T(t) f - f}_\infty = 1$.

Every $C_0$-semigroup satisfies $\norm{T(t)} \le M e^{\omega t}$ for some constants $M \ge 1$ and $\omega \in \R$, and its generator is closed and densely defined.

## Explanations

### L1 human

A $C_0$-semigroup is a time-evolution made of linear maps that compose correctly and start continuously from the identity.
Its generator is the derivative at time $0$, which plays the role of $A$ in $e^{tA}$.
