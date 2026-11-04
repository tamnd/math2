---
tag: E0R6P2FMCM
kind: proof
name: Proof of the pigeonhole principle
msc: [05A05]
proves: 0HGVCWQGY3
uses: [0PVG1CRAJN, 0SNQEF7Z53, 0Q3F20XB0A, 0GV2573FP4, 03QC59M99B]
methods: [0J0XBKG64S]
sources:
  - url: https://proofwiki.org/wiki/Pigeonhole_Principle
---

## Proof

We argue by contradiction.

1. Suppose that $f : A \to B$ is [[injective|0PVG1CRAJN]], and let $C = f(A)$ be the [[image|0Q3F20XB0A]] of $A$.
2. Then $f$ is a [[bijection|0SNQEF7Z53]] from $A$ onto $C$: it is injective, and every element of $C$ is a value of $f$.
3. Composing a numbering of $A$ with $f$ numbers $C$. So $C$ is finite and $|C| = |A|$, as in the [[bijection principle|0GV2573FP4]].
4. The set $C$ is a subset of $B$. By the [[complement principle|03QC59M99B]], $|B \setminus C| = |B| - |C| = |B| - |A|$.
5. The left side is a natural number, but $|B| - |A| < 0$ because $|A| > |B|$. This is a contradiction.
6. Hence $f$ is not injective. So there are $a \ne a'$ in $A$ with $f(a) = f(a')$.

## Idea

An injective map copies $A$ onto a subset of $B$ of the same size.
A subset of $B$ cannot be larger than $B$, so this is impossible when $A$ has more elements than $B$.
