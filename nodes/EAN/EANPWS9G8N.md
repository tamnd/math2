---
tag: EANPWS9G8N
kind: definition
name: Modality of a singularity
msc: [58K40, 32S05, 14B05]
defines: 8CFTJP1WN8
uses: [VZXF7RNFKS, 1QE0Z0756D, 0YTCMFB4HC, 0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
---

## Definition

Let $f \colon (\C^n, 0) \to (\C, 0)$ be a [[germ|VZXF7RNFKS]] of a [[holomorphic function|0NAHXR1FRH]] with an isolated [[critical point|0YTCMFB4HC]] at $0$.
Let $k$ be so large that $f$ is $k$-determined.
Let $J^k$ be the space of [[$k$-jets|1QE0Z0756D]] at $0$ of germs vanishing at $0$.
The group of $k$-jets of germs of biholomorphic maps $(\C^n, 0) \to (\C^n, 0)$ acts on $J^k$ by composition on the right.
The *modality* of $f$ is the least integer $m \ge 0$ with this property.
Some neighbourhood of $j^k f$ in $J^k$ is covered by finitely many families of orbits, each depending on at most $m$ parameters.
A germ of modality $0$ is called *simple*, of modality $1$ *unimodal*, and of modality $2$ *bimodal*.

## Remarks

Informally, a family of orbits depending on $m$ parameters is the union of the orbits of the points of an $m$-dimensional smooth submanifold of $J^k$.
The modality does not depend on the choice of $k$, as long as $f$ is $k$-determined.
Example: $f = x^3$ on $\C$ is simple.
Any small perturbation of the jet of $x^3$ in $J^3$ is $a_1 x + a_2 x^2 + a_3 x^3$ with $a_3 \ne 0$.
If $a_1 \ne 0$ it is right equivalent to $x$, a regular point.
If $a_1 = 0 \ne a_2$ it is right equivalent to $x^2$, a Morse point.
If $a_1 = a_2 = 0$ it is right equivalent to $x^3$.
Non-example: $f = x^4 + y^4$ on $\C^2$ is not simple.
For the germs $x^4 + y^4 + a x^2 y^2$ with $a^2 \ne 4$, the zero set is four distinct lines through $0$.
Their cross-ratio, taken up to the order of the lines, depends on $a$ and is invariant under right equivalence.
So infinitely many orbits meet every neighbourhood of $f$, and in fact the modality of $f$ is $1$.
