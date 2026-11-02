---
tag: TAMCTW7SA0
kind: statement
role: theorem
name: Kawamata–Viehweg vanishing theorem
msc: [14F17, "14E30"]
uses: [A4H4CZ2V35, EXKGG9X6J0, RZ66X0NAM5, W05VYY4HBR, PQ6Q143ARJ, NY77DQ2AX8]
about: [RZ66X0NAM5, PQ6Q143ARJ]
sources:
  - url: https://en.wikipedia.org/wiki/Kawamata–Viehweg_vanishing_theorem
same_as:
  wikidata: Q6379606
  wikipedia: Kawamata–Viehweg vanishing theorem
---

## Statement

Let $X$ be a [[smooth|EXKGG9X6J0]] [[projective variety|A4H4CZ2V35]] of dimension $n$ over a field of characteristic $0$, with [[canonical bundle|W05VYY4HBR]] $\omega_X$.
Let $L$ be a [[nef line bundle|RZ66X0NAM5]] on $X$ that is big, that is, whose top self-intersection number satisfies $(L^n) > 0$.
Then
$$H^i(X, \omega_X \otimes L) = 0 \quad \text{for all } i > 0,$$
where $H^i$ is [[sheaf cohomology|PQ6Q143ARJ]].

## Remarks

For a nef line bundle, bigness in the sense of maximal Iitaka dimension is equivalent to $(L^n) > 0$.
The idea of the proof: by Kodaira's lemma, some multiple of $L$ is an ample divisor plus an effective divisor.
A cyclic covering trick and a log resolution reduce the statement to the [[Kodaira vanishing theorem|NY77DQ2AX8]] on a covering variety.

There is a more general form for $\Q$-divisors: if $D$ is a nef and big $\Q$-divisor whose fractional part has simple normal crossing support, then $H^i(X, \omega_X \otimes \mathcal{O}_X(\lceil D \rceil)) = 0$ for $i > 0$.

Example: let $n \ge 2$, let $X \to \mathbb{P}^n$ be the blowing up of a point, and let $L$ be the pullback of $\mathcal{O}(1)$.
Then $L$ is nef and big but not ample, since it has degree $0$ on the lines in the exceptional divisor.
The theorem still gives $H^i(X, \omega_X \otimes L) = 0$ for $i > 0$, which Kodaira's theorem does not cover.

Bigness is needed: on $X = C \times \mathbb{P}^1$ with $C$ a curve of genus $g \ge 1$, the pullback $L$ of $\mathcal{O}_{\mathbb{P}^1}(2)$ is nef with $(L^2) = 0$, and $H^1(X, \omega_X \otimes L) \cong H^1(C, \omega_C) \otimes H^0(\mathbb{P}^1, \mathcal{O}) \ne 0$ by the Künneth formula.

## Explanations

### L1 human

The Kodaira vanishing theorem needs a positive (ample) line bundle.
The Kawamata–Viehweg theorem weakens this to a bundle that is never negative on curves and that has positive volume.
Such bundles appear naturally after blowing up, so the weaker hypothesis is much more flexible.

### L2 human

This theorem is the main cohomological tool of the minimal model program.
It is used in the proofs of the basepoint-free theorem and of the cone theorem, where one works with nef and big divisors that are not ample.
Its version for $\Q$-divisors allows rounding of fractional divisors, which is needed when one works with pairs $(X, \Delta)$.
