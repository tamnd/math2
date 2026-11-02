---
tag: VA41ZY2HTF
kind: definition
name: Term evaluation
msc: [08A40, 03C07]
defines: DH30WTA26T
uses: [6D3WA7N2W4, WDVVEYD6AT, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Term_(logic)
---

## Definition

Let $\sigma$ be a [[signature|WDVVEYD6AT]] with only function symbols and let $X$ be a set of variables.
Let $A$ be a [[structure|983GZBQYT4]] of signature $\sigma$, that is, an algebra, with operations $f^A$.
Let $\alpha \colon X \to A$ be a map, called an *assignment*.
The *value* $t^A[\alpha]$ of a [[term|6D3WA7N2W4]] $t$ over $\sigma$ and $X$ is defined by recursion on $t$:

1. if $t$ is a variable $x \in X$, then $t^A[\alpha] = \alpha(x)$;
2. if $t$ is a constant symbol $c$, then $t^A[\alpha] = c^A$;
3. if $t = f(t_1, \ldots, t_n)$ for a function symbol $f$ of arity $n \ge 1$, then $t^A[\alpha] = f^A(t_1^A[\alpha], \ldots, t_n^A[\alpha])$.

## Remarks

The recursion is well defined because every term has a unique reading.
The value depends only on the values of $\alpha$ at the variables that occur in $t$.
If these variables are among $x_1, \ldots, x_n$ and $\alpha(x_i) = a_i$, one writes $t^A(a_1, \ldots, a_n)$.

Example: in the ring $(\Z, +, \cdot, 0, 1)$, let $t = x \cdot (y + 1)$ and $\alpha(x) = 3$, $\alpha(y) = 4$.
Clause 1 gives $x \mapsto 3$ and $y \mapsto 4$, clause 2 gives $1 \mapsto 1$, and clause 3 twice gives $y + 1 \mapsto 5$ and $t \mapsto 15$.

Non-example: computing $x \cdot (y + 1)$ at the same assignment as $3 \cdot 4 + 1 = 13$ is not term evaluation.
The outermost symbol of $t$ is $\cdot$ applied to $x$ and $y + 1$, so clause 3 requires the product of the values $3$ and $5$.

Homomorphisms commute with evaluation: if $h \colon A \to B$ is a homomorphism, then $h(t^A[\alpha]) = t^B[h \circ \alpha]$.
In Mathlib term evaluation is `FirstOrder.Language.Term.realize`.
