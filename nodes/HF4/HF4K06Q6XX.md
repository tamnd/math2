---
tag: HF4K06Q6XX
kind: concept
name: Parametric oscillator
msc: [70J40, 34C25, 70K28]
uses: [0YG0ZJPTWG, BJVZXPB297]
sources:
  - url: https://en.wikipedia.org/wiki/Parametric_oscillator
same_as:
  wikidata: Q2632607
  wikipedia: Parametric oscillator
---

## Summary

A parametric oscillator is a [[harmonic oscillator|0YG0ZJPTWG]] whose parameters, such as its stiffness or its damping, change in time, usually periodically.
The energy is pumped in by varying a parameter, not by a direct external force.
When the parameter varies at about twice the natural frequency, small oscillations grow exponentially; this is parametric resonance.
Periodic coefficients make [[Floquet theory|BJVZXPB297]] the main tool, and the Mathieu equation is the standard model.

## Explanations

### L1 human

A child on a swing pumps it by standing up and squatting at the right moments, without anyone pushing.
Standing up raises the centre of mass and changes the effective length of the pendulum.
Doing this twice per swing, at the right phase, makes the swing go higher and higher.
In the same way, the equation $x'' + \omega_0^2 (1 + h \cos 2 \omega_0 t) x = 0$ with a small $h > 0$ has solutions that grow, although $x = 0$ is stable when $h = 0$.
