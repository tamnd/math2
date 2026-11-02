---
tag: FWJ7CH6WG8
kind: definition
name: Almost split sequence
msc: [16G70]
defines: M5D95FN7G3
uses: [0B1261B5ED, 0NZ8JA25WK, JB7ZBFBA9C, E2P29GCD9T]
sources:
  - url: https://en.wikipedia.org/wiki/Auslander%E2%80%93Reiten_theory
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] and let $0 \to L \xrightarrow{f} E \xrightarrow{g} N \to 0$ be a short [[exact sequence|JB7ZBFBA9C]] of left $R$-[[modules|0NZ8JA25WK]].
The sequence is *almost split* if:

1. it does not split;
2. every morphism $u \colon L \to Y$ that is not a split monomorphism factors as $u = u' f$ for some $u' \colon E \to Y$;
3. every morphism $h \colon X \to N$ that is not a split epimorphism factors as $h = g h'$ for some $h' \colon X \to E$.

## Remarks

In an almost split sequence, $L$ and $N$ are [[indecomposable|E2P29GCD9T]] with local endomorphism rings.
Example: let $A$ be the path algebra of $1 \to 2$ over a field $k$, with modules $S_2 = (0 \to k)$, $P_1 = (k \xrightarrow{\id} k)$, $S_1 = (k \to 0)$.
The sequence $0 \to S_2 \to P_1 \to S_1 \to 0$ does not split, since $P_1$ is indecomposable.
For clause 3 it suffices to test indecomposable $X$: maps from $S_1$ are $0$ or isomorphisms, $\Hom(S_2, S_1) = 0$, and maps from the projective $P_1$ lift.
Clause 2 is checked in the same way.
Non-example: the split sequence $0 \to S_2 \to S_2 \oplus S_1 \to S_1 \to 0$ satisfies clauses 2 and 3, since $f$ is a split monomorphism and $g$ a split epimorphism, but it fails clause 1.
For a finite-dimensional algebra, the left end of the almost split sequence ending at $N$ is $\tau N$, the Auslander–Reiten translate.
