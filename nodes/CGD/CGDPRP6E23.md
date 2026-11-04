---
tag: CGDPRP6E23
kind: proof
name: Proof of the universal property of the quotient topology
msc: [54B15]
proves: 0FF2FJ8CH2
uses: [0V8046R0P9, 0SY9ECQ19Q, 05NK26G0DR, 0FGCFY1AZX, 07HF9YCWPP]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(topology)
    locator: Properties
---

## Proof

We prove the two directions separately. Let $\tau$ be the topology of $X$.

1. The quotient map $q$ is [[continuous|0SY9ECQ19Q]]. Indeed, if $V$ is open in $X / {\sim}$, then $q^{-1}(V) \in \tau$ by the definition of the [[quotient topology|0V8046R0P9]].
2. Let $g$ be continuous. Then $g \circ q$ is a [[composition of continuous maps|05NK26G0DR]], so it is continuous.
3. Conversely, let $g \circ q$ be continuous, and let $V$ be open in $Y$.
4. By the definition of the [[composition|07HF9YCWPP]], $x \in (g \circ q)^{-1}(V)$ if and only if $g(q(x)) \in V$. This holds if and only if $q(x) \in g^{-1}(V)$, that is, $x \in q^{-1}(g^{-1}(V))$.
5. So the [[preimages|0FGCFY1AZX]] agree: $q^{-1}(g^{-1}(V)) = (g \circ q)^{-1}(V)$. This set is in $\tau$ because $g \circ q$ is continuous.
6. By the definition of the quotient topology, $g^{-1}(V)$ is open in $X / {\sim}$.
7. So the preimage under $g$ of each open set of $Y$ is open, and $g$ is continuous.

## Idea

A set in the quotient is open exactly when its preimage under $q$ is open. The preimage under $q$ of $g^{-1}(V)$ is the preimage of $V$ under $g \circ q$. So continuity of $g \circ q$ is exactly what is needed for $g$.
