---
tag: VRTV602H8G
kind: definition
name: Periodic solution
msc: [34C25]
defines: FHNDX22WMK
uses: [07VX34QXAV, 0ATF6Q0633, 0AA97XA70K]
sources:
  - url: https://en.wikipedia.org/wiki/Periodic_function
---

## Definition

Let $U$ be an open subset of $\R^n$ and let $f \colon \R \times U \to \R^n$ be continuous.
A [[solution|07VX34QXAV]] $x \colon \R \to U$ of $x' = f(t, x)$ is periodic if there is a real number $T > 0$ with
$$x(t + T) = x(t) \quad \text{for all } t \in \R.$$
Such a $T$ is a period of $x$.
If $f$ is $T$-periodic in $t$, that is, $f(t + T, x) = f(t, x)$ for all $t$ and $x$, a $T$-periodic solution is a periodic solution with period $T$.

## Remarks

A periodic solution is a [[periodic function|0ATF6Q0633]] of $t$ that solves the equation.
For an autonomous equation $x' = f(x)$, each constant solution is periodic with every period, and the trajectory of a nonconstant periodic solution is a [[periodic orbit|0AA97XA70K]].
Example: for $x' = -x + \cos t$, the function $x(t) = \frac{1}{2}(\cos t + \sin t)$ has $x'(t) = \frac{1}{2}(\cos t - \sin t) = -x(t) + \cos t$.
It is a $2\pi$-periodic solution of an equation with $2\pi$-periodic right-hand side.
Non-example: the other solutions $x(t) = \frac{1}{2}(\cos t + \sin t) + c e^{-t}$ with $c \ne 0$ are not periodic, because $c e^{-t}$ is not.
A maximal solution of a $T$-periodic equation with $x(t_0 + T) = x(t_0)$ for one $t_0$ is $T$-periodic when solutions are unique.

## Explanations

### L1 human

A periodic solution returns to the same state after a fixed time and repeats forever.
For a periodically forced system, the most interesting periodic solutions have the same period as the forcing.
