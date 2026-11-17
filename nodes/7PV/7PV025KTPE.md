---
tag: 7PV025KTPE
kind: proof
name: Proof of Church's theorem from Robinson arithmetic
msc: ["03B25", "03F30"]
topics: [E4AVTNWE9E]
audience: ug2
proves: VA6BNNY2YC
uses: [3K1AKGXF8A, RZ42PP37MD, 5SDS9T8E7J, 1HK0VYWTV7, PPGD5KW8JC]
methods: [6F55216R53, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Undecidability
  - book: isbn:9780521857840
---

## Proof

We prove the theorem for the signature $L = \set{0, S, +, \cdot}$ of arithmetic.

1. [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$ has seven axioms. Let $\alpha$ be their conjunction, which is one $L$-sentence.
2. For every $L$-sentence $\sigma$, $\mathsf{Q} \models \sigma$ holds if and only if $\alpha \to \sigma$ is [[valid|5SDS9T8E7J]]. A structure satisfies $\alpha \to \sigma$ exactly when it satisfies $\sigma$ or fails one of the axioms.
3. The map $\sigma \mapsto (\alpha \to \sigma)$ is computable, since $\alpha$ is a fixed string.
4. Assume, for a contradiction, that the set of valid $L$-sentences is computable.
5. Then the set $\set{\sigma : \mathsf{Q} \models \sigma}$ is computable: to test $\sigma$, compute $\alpha \to \sigma$ and test its validity, which is correct by step 2.
6. But $\mathsf{Q}$ is consistent, since $\N$ is a model, and $\mathsf{Q}$ is undecidable, by the theorem that [[Robinson arithmetic is essentially undecidable|RZ42PP37MD]].
7. Steps 5 and 6 contradict each other. So the set of valid $L$-sentences is not computable.

## Idea

The set of consequences of a finitely axiomatized theory reduces to validity: put the conjunction of the axioms in front as a hypothesis.
So an undecidable, finitely axiomatized theory gives undecidable validity in its signature.
Robinson arithmetic is such a theory, and all the work lies in its undecidability.

## Variants

- Any undecidable theory with finitely many axioms works in place of $\mathsf{Q}$. For example, the theory of [[groups|RX9MB386C5]] is finitely axiomatized and undecidable, by a result of Tarski that uses interpretations; see the [[transfer theorem for undecidability|FMB2C20G8W]].
- A direct proof with Turing machines avoids arithmetic: [[proof of Church's theorem by encoding Turing machines|GF8VBT1R3N]].
