---
tag: YSQX3J8KE7
kind: proof
name: Proof that sums and products of continuous functions are continuous
msc: [26A15]
proves: 0VGMHCF4SC
uses: [0P27W9RW0G, 0PAQM3H57X, 0MVDQEAB60, 0RAM4E07NR, 0734RSVF2V]
sources:
  - url: https://www.jirka.org/ra/
    locator: Proposition 3.2.5
---

## Proof

We use [[sequential continuity|0PAQM3H57X]] and the limit rules for sequences.

1. Let $D \subseteq \R$ and let $f, g \colon D \to \R$ be [[continuous|0P27W9RW0G]].
2. By the equivalence of continuity and sequential continuity, $f$ and $g$ are [[sequentially continuous|0MVDQEAB60]].
3. Let $(x_n)$ be a sequence in $D$ that converges to a point $a \in D$. By step 2, $f(x_n) \to f(a)$ and $g(x_n) \to g(a)$.
4. By the [[sum rule for limits|0RAM4E07NR]], $(f + g)(x_n) = f(x_n) + g(x_n) \to f(a) + g(a) = (f + g)(a)$.
5. By the [[product rule for limits|0734RSVF2V]], $(f g)(x_n) = f(x_n) g(x_n) \to f(a) g(a) = (f g)(a)$.
6. Since $(x_n)$ and $a$ were arbitrary, $f + g$ and $f g$ are sequentially continuous.
7. By the equivalence again, $f + g$ and $f g$ are continuous.

## Idea

Sequential continuity turns the question into one about limits of sequences. The sum and product rules for limits of sequences then give the result at once.
