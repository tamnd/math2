---
tag: ~de3d00df
kind: statement
role: theorem
name: WKL0 is Π⁰₂-conservative over primitive recursive arithmetic
msc: ["03B30", "03F35", "03F30"]
topics: [BY8AAFN7C5]
audience: research
about: [~e7c6fa0e, WCXH72T8D8, ~f3242591]
uses: [~b501e994, 330YAP9Y4Q, GE43CSZTS9, N238J43XNE]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: The big five subsystems of second-order arithmetic
---

## Statement

Let $\theta(n, m)$ be a $\Delta^0_0$ formula of first-order arithmetic: all its quantifiers are bounded, as in the [[arithmetical hierarchy of formulas|GE43CSZTS9]].
Suppose that [[WKL0|~b501e994]] proves the $\Pi^0_2$ sentence $\forall n\, \exists m\, \theta(n, m)$.
Then there is a primitive recursive function $f$ such that [[primitive recursive arithmetic|330YAP9Y4Q]] proves $\theta(n, f(n))$, with $n$ a free variable.

In particular, every $\Pi^0_1$ sentence provable in $\mathsf{WKL}_0$ is provable in $\mathsf{PRA}$.
So $\mathsf{WKL}_0$ is a [[conservative extension|N238J43XNE]] of $\mathsf{PRA}$ for $\Pi^0_2$ sentences.

## Remarks

### Why each hypothesis is needed

- The system cannot be replaced by $\mathsf{ACA}_0$: [[ACA0 proves the consistency of PRA|~6c9f5ed6]], which is a $\Pi^0_1$ sentence that $\mathsf{PRA}$ does not prove.

### Consequences

- If $\mathsf{WKL}_0$ proves $\forall n\, \exists m\, \theta(n, m)$, then a primitive recursive function computes a witness $m$ from $n$. See the [[example of a witness function|~497f54b6]].
- $\mathsf{WKL}_0$ is consistent if $\mathsf{PRA}$ is consistent, since $0 = 1$ is a $\Pi^0_1$ sentence.

### History

The theorem is due to Harvey Friedman.
Its proofs that can be formalized in $\mathsf{PRA}$ itself make it a partial realization of Hilbert's program, as described in the [[concept page|~f3242591]].

## Explanations

### L1 human

The theorem says that the infinite objects of $\mathsf{WKL}_0$ never prove a new statement of the form "for every $n$ there is $m$ with a computable property".
Such a statement proved in $\mathsf{WKL}_0$ already has a finitistic proof, and the witness $m$ is computed by a primitive recursive function.
