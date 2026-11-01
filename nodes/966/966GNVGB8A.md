---
tag: 966GNVGB8A
kind: concept
name: Purely inseparable extension
msc: [12F15]
sources:
  - url: https://en.wikipedia.org/wiki/Purely_inseparable_extension
same_as:
  wikidata: Q7261176
  wikipedia: Purely inseparable extension
---

## Summary

A purely inseparable extension is an [[algebraic extension|0PTBM7K0R2]] in which every element has some $p$-power, $p^n$, in the base field, where $p$ is the [[characteristic|0F6ES3BRYP]].
It is the opposite of a [[separable extension|0WCX7NB4N7]]: the only elements that are both separable and purely inseparable over $K$ are those of $K$.
Every algebraic extension splits into a separable part followed by a purely inseparable part, so the two kinds together describe all algebraic extensions.
In characteristic $0$ the only purely inseparable extension of $K$ is $K$ itself.

## Explanations

### L1 human

In characteristic $p$, the map $x \mapsto x^p$ respects sums and products.
A purely inseparable extension adds elements that become old elements after you raise them to a $p$-th power a few times.
For example, over the field $\F_p(t)$ of rational functions, you may add an element $s$ with $s^p = t$.
The polynomial $x^p - t$ then becomes $(x - s)^p$, so it has a single root repeated $p$ times.
This repeated root is what "inseparable" refers to.
