---
tag: YE7H8DGDPY
kind: example
name: Hill differential equation
msc: [34B30, 34C25, 34D20]
instance_of: [0QQRP17Z7S]
illustrates: [BJVZXPB297]
uses: [0PB7K8M7FG, 089KWVYD69, GW8SBF37K1, 09PS3S0EF6]
sources:
  - url: https://en.wikipedia.org/wiki/Hill_differential_equation
same_as:
  wikidata: Q1169848
  wikipedia: Hill differential equation
---

## Example

Let $T > 0$ and let $f : \R \to \R$ be continuous and $T$-periodic.
*Hill's equation* is the second-order [[linear differential equation|0PB7K8M7FG]]
$$y'' + f(t)\, y = 0.$$
The Mathieu equation $y'' + (a - 2q \cos 2t)\, y = 0$, with real constants $a$ and $q$, is the special case $f(t) = a - 2q\cos 2t$, of period $\pi$.

Floquet analysis: let $y_1, y_2$ be the solutions with $y_1(0) = 1$, $y_1'(0) = 0$ and $y_2(0) = 0$, $y_2'(0) = 1$.
The monodromy matrix of the equivalent system for $(y, y')$ is $M$ with columns $(y_1(T), y_1'(T))$ and $(y_2(T), y_2'(T))$.
The system matrix has trace $0$, so by [[Liouville's formula|09PS3S0EF6]] $\det M = 1$.
Hence the multipliers are the roots of $\mu^2 - \Delta \mu + 1 = 0$, where $\Delta = y_1(T) + y_2'(T)$ is the discriminant.

1. If $\abs{\Delta} < 2$, the multipliers are two distinct conjugate numbers of modulus $1$, and all solutions are bounded.
2. If $\abs{\Delta} > 2$, there is a real multiplier of modulus greater than $1$, and some solution is unbounded.

Check with constant $f = \omega^2$, $\omega > 0$, viewed as $T$-periodic: $y_1 = \cos \omega t$ and $y_2 = \sin(\omega t)/\omega$, so $\Delta = 2\cos \omega T$ and $\abs{\Delta} \le 2$, matching the bounded oscillations of the [[harmonic oscillator|0YG0ZJPTWG]].

## Explanations

### L1 human

Hill's equation describes an oscillator whose stiffness changes periodically in time.
Depending on the parameters, the oscillation stays bounded or grows without limit; the growth is called parametric resonance.
A single number $\Delta$, computed from two solutions over one period, decides which case occurs.
George William Hill studied the equation for the motion of the Moon, and it also describes particles in periodic potentials.
