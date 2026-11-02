---
tag: B4FRQMWQKP
kind: concept
name: Codimension of a singularity
msc: [58K40, 58K35, 58K60]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
---

## Summary

The codimension of a singularity of a smooth function counts how many independent conditions a function must satisfy to have that singularity.
Equivalently, it is the number of parameters a family of functions needs before the singularity occurs in it in a persistent way.
Persistent means that small perturbations of the family do not remove it.
It is computed from the Jacobian ideal of the [[germ|7SWSRGDT4A]].
It is also the least number of parameters of a [[versal unfolding|KSAFWZVB8K]], not counting the constant term.
In [[catastrophe theory|6FKJ6SXP3G]] it sorts the elementary catastrophes: the fold has codimension $1$ and the cusp has codimension $2$.

## Explanations

### L1 human

A nondegenerate minimum, like the bottom of the bowl $x^2$, is typical: it survives any small change of the function, so its codimension is $0$.
A flat inflection like $x^3$ at $0$ is rare: a small change $x^3 + a x$ destroys it unless $a = 0$, so it costs one condition, and its codimension is $1$.
It appears unavoidably only in families with at least one parameter.
The flatter point $x^4$ needs two parameters, $x^4 + a x^2 + b x$, so its codimension is $2$.
