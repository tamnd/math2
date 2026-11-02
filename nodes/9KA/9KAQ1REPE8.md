---
tag: 9KAQ1REPE8
kind: concept
name: Nevanlinna theory of difference equations
msc: [39A45, 30D35]
sources:
  - url: https://en.wikipedia.org/wiki/Nevanlinna_theory
---

## Summary

Nevanlinna theory of difference equations applies the value distribution theory of [[meromorphic functions|0ZZ7ZYDR8W]] to equations such as $f(z + 1) = R(z, f(z))$ in the complex plane.
Its central tool is a difference analogue of the lemma on the logarithmic derivative.
Let $f$ be meromorphic of finite order and let $c \in \C$.
Then the proximity function of $f(z + c)/f(z)$ is small compared with the [[Nevanlinna characteristic|YT6Z0GWS0W]] of $f$.
With this, the classical methods of [[Nevanlinna theory|1EHH63VNAD]] for complex differential equations carry over to difference equations.
It has been proposed as a test of integrability.
Equations with enough meromorphic solutions of finite order are expected to be discrete analogues of the Painlevé equations.

## Explanations

### L1 human

Nevanlinna theory measures how often a meromorphic function takes each value, using a growth function $T(r, f)$.
For differential equations, it is known that derivatives cannot make a function much bigger in this sense.
The difference version shows the same for shifts: $f(z + 1)$ is not much bigger than $f(z)$ on average, as long as $f$ grows at most like $e^{\abs{z}^\rho}$ for some $\rho$.
This lets one rule out meromorphic solutions of many difference equations and single out the special, integrable ones.
