---
tag: CPE1ANDDJ0
kind: concept
name: Translation equation
msc: [39B52, 37C10]
specializes: [SRAN4EKWS0]
sources:
  - url: https://en.wikipedia.org/wiki/Flow_(mathematics)
---

## Summary

The translation equation is the [[functional equation|SRAN4EKWS0]] $F(F(x, s), t) = F(x, s + t)$ for an unknown map $F \colon X \times \R \to X$.
Its solutions with $F(x, 0) = x$ are the flows on the set $X$, that is, actions of the additive group $\R$ on $X$.
So it is the basic equation of continuous-time [[dynamical systems|BBZP1R872N]] and of iteration with non-integer exponents.
With the real line replaced by a group, it becomes the equation of a [[group action|0WCY42EV9V]].

## Explanations

### L1 human

Think of $F(x, t)$ as the position at time $t$ of a particle that starts at $x$.
Moving for time $s$ and then for time $t$ should give the same position as moving for time $s + t$.
For example, $F(x, t) = x + t$ moves every point at unit speed along the line.
The map $F(x, t) = x e^t$ is another solution, in which points move away from $0$ exponentially fast.
