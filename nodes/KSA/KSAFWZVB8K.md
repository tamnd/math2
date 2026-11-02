---
tag: KSAFWZVB8K
kind: concept
name: Versal unfolding
msc: [58K60, 58K35, 58K40]
sources:
  - url: https://en.wikipedia.org/wiki/Catastrophe_theory
---

## Summary

An unfolding of a function [[germ|7SWSRGDT4A]] is a family of germs depending on parameters that reduces to the given germ when the parameters are zero.
An unfolding is versal if every other unfolding can be obtained from it by changes of a simple kind.
These are a change of parameters, a parameter-dependent change of coordinates and the addition of a function of the parameters.
So a versal unfolding contains, up to equivalence, every way of perturbing the germ.
A versal unfolding with the least number of parameters is called universal or miniversal, and that number is the [[codimension|B4FRQMWQKP]] of the germ.
Versal unfoldings are the normal forms of [[catastrophe theory|6FKJ6SXP3G]].

## Explanations

### L1 human

Take a degenerate function, such as $x^3$, whose flat point at $0$ is destroyed by almost any small change.
An unfolding lists the changes by parameters, for example $x^3 + a x + b x^2 + c x^4$.
A versal unfolding is a short list that is already enough.
For $x^3$, the one-parameter family $x^3 + a x$ captures every possible perturbation up to a change of coordinates and an added constant.
Indeed, the term $b x^2$ can be removed by shifting $x$, which only changes $a$ and adds a constant.
The term $c x^4$ can be removed by a smooth change of coordinates near $0$.
