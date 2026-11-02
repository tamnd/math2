---
tag: YJ1M0FYXJD
kind: example
name: Chandrasekhar's X- and Y-functions
msc: [45G15, 85A25]
instance_of: [BSCYBP6AS6]
uses: [99879Z5Y1K, EX9YYRMAJA, BSCYBP6AS6]
sources:
  - url: https://en.wikipedia.org/wiki/Chandrasekhar%27s_X-_and_Y-function
same_as:
  wikidata: Q48996583
  wikipedia: Chandrasekhar's X- and Y-function
---

## Example

Let $\tau_1 > 0$ be the optical thickness of a plane-parallel slab.
Let $\Psi$ be an even polynomial, the characteristic function, with $\Psi \ge 0$ on $[0, 1]$ and $\int_0^1 \Psi\, d\mu \le \frac{1}{2}$.
*Chandrasekhar's X- and Y-functions* are the functions $X$ and $Y$ on $[0, 1]$ that solve the system
$$X(\mu) = 1 + \mu \int_0^1 \frac{\Psi(\mu')}{\mu + \mu'} \bigl[X(\mu) X(\mu') - Y(\mu) Y(\mu')\bigr]\, d\mu',$$
$$Y(\mu) = e^{-\tau_1/\mu} + \mu \int_0^1 \frac{\Psi(\mu')}{\mu - \mu'} \bigl[Y(\mu) X(\mu') - X(\mu) Y(\mu')\bigr]\, d\mu'.$$
In the second equation the bracket vanishes at $\mu' = \mu$, so the integrand has no singularity there.
This is a system of two coupled [[nonlinear integral equations|BSCYBP6AS6]] for the two unknowns.

Check of two limits.
For $\tau_1 = 0$, the constant functions $X = 1$ and $Y = 1$ solve the system: both brackets vanish and $e^{0} = 1$.
This is a slab of thickness $0$, which lets all light through.
As $\tau_1 \to \infty$, the term $e^{-\tau_1/\mu}$ tends to $0$; with $Y = 0$ the first equation becomes the equation of [[Chandrasekhar's H-function|99879Z5Y1K]], $X = H$.

## Remarks

The functions $X$ and $Y$ give the light reflected and transmitted by a slab of finite thickness in the [[radiative transfer equation|EX9YYRMAJA]], while $H$ handles a half-space.
In the conservative case $\int_0^1 \Psi\, d\mu = \frac{1}{2}$ the system does not determine $X$ and $Y$ uniquely, and an extra condition selects the physical solution.

## Explanations

### L1 human

When light falls on a slab of fog of finite thickness, part of it is reflected and part of it goes through.
Chandrasekhar described both parts with two functions, $X$ for the reflected light and $Y$ for the transmitted light.
They solve two equations that are tied together.
For a slab of zero thickness everything passes, and for an infinitely thick slab nothing passes and $X$ becomes the H-function.
