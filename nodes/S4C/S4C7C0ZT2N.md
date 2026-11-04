---
tag: S4C7C0ZT2N
kind: proof
name: Proof that a composition of continuous functions is continuous
msc: [26A15]
proves: 0NRQPQX3VA
uses: [0EEE2CZB2A, 0P27W9RW0G]
sources:
  - url: https://proofwiki.org/wiki/Composite_of_Continuous_Mappings_is_Continuous/Point
---

## Proof

We work directly with the [[definition of continuity at a point|0EEE2CZB2A]] by open intervals.

1. Let $D, E \subseteq \R$, let $f \colon D \to \R$ with $f(D) \subseteq E$, and let $g \colon E \to \R$. Assume that $f$ is continuous at $a \in D$ and $g$ is continuous at $f(a)$.
2. Let $V$ be an open interval containing $g(f(a))$.
3. Continuity of $g$ at $f(a)$ gives an open interval $W$ containing $f(a)$ with $g(y) \in V$ for all $y \in W \cap E$.
4. Continuity of $f$ at $a$, applied to $W$, gives an open interval $U$ containing $a$ with $f(x) \in W$ for all $x \in U \cap D$.
5. Let $x \in U \cap D$. Then $f(x) \in W$ by step 4, and $f(x) \in E$ since $f(D) \subseteq E$. So $f(x) \in W \cap E$.
6. By step 3, $(g \circ f)(x) = g(f(x)) \in V$.
7. So $U$ works for $V$, and $g \circ f$ is continuous at $a$.
8. If $f$ and $g$ are [[continuous|0P27W9RW0G]], then step 7 applies at each $a \in D$, since $g$ is continuous at $f(a) \in E$. So $g \circ f$ is continuous.

## Idea

To land in a target interval $V$ around $g(f(a))$, it suffices that $f(x)$ lands in an interval $W$ that $g$ maps into $V$. Continuity of $f$ provides an interval around $a$ that $f$ maps into $W$. The two steps chain together.
