---
tag: RD3VPJH67B
kind: example
name: PA + Con(PA) is ω-consistent
msc: ["03F40", "03F30"]
topics: [HXHHWY3328]
audience: grad
instance_of: [4S29X1GTV4]
uses: [4S29X1GTV4, 5JKPMRAXZP, 4NBAX3VRQ7, MPSCREYC3M]
sources:
  - url: https://en.wikipedia.org/wiki/%CE%A9-consistent_theory
    locator: lead section
  - book: isbn:9780521857840
---

## Example

Adding a true sentence to Peano arithmetic gives a stronger theory that is still $\omega$-consistent.
Let $T := \mathsf{PA} + \mathrm{Con}(\mathsf{PA})$, where $\mathrm{Con}(\mathsf{PA})$ is the [[consistency statement|4NBAX3VRQ7]] $\neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner)$.
We show that $T$ is [[ω-consistent|4S29X1GTV4]].

1. The structure $\mathbb{N}$ is a model of $\mathsf{PA}$, as in [[Peano arithmetic is ω-consistent|5JKPMRAXZP]], so $\mathsf{PA}$ does not prove $0 = S0$.
2. So no number codes a proof of $0 = S0$ in $\mathsf{PA}$.
3. The formula $\mathrm{Prf}_{\mathsf{PA}}(y, x)$ defines the proof relation in $\mathbb{N}$.
   By step 2, $\mathbb{N} \models \neg \exists y \, \mathrm{Prf}_{\mathsf{PA}}(y, \ulcorner 0 = S0 \urcorner)$, that is, $\mathbb{N} \models \mathrm{Con}(\mathsf{PA})$.
4. By steps 1 and 3, $\mathbb{N}$ is a model of $T$.
5. A theory with $\mathbb{N}$ as a model is $\omega$-consistent.
   If it proves $\exists x \, \varphi(x)$, there is a witness $m$ in $\mathbb{N}$, and then the false sentence $\neg \varphi(\underline{m})$ is not provable.

## Remarks

The theory $T$ is stronger than $\mathsf{PA}$, since $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$ by the second incompleteness theorem.
It keeps $\omega$-consistency because its new axiom is true.

Flip the new axiom and the result changes.
The theory $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is also consistent, but [[it is not ω-consistent|FK06QR6A44]].
So of the two consistent extensions, by $\mathrm{Con}(\mathsf{PA})$ and by its negation, $\omega$-consistency picks out the true one.
Consistency alone cannot tell them apart.

The step can be repeated.
The theories $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$, then that theory plus its own consistency statement, and so on, are all true in $\mathbb{N}$.
These are the first stages of a [[Turing progression|F7Z4BV2KHD]].

## Explanations

### L1 human

The sentence "Peano arithmetic never proves $0 = 1$" is true.
Adding a true sentence to true axioms gives true axioms.
True axioms never claim that some number exists and then rule out every number.
So the larger theory is still $\omega$-consistent.

### L2 human

The proof has three moves, and each is worth naming.
First we check that the new axiom is true in $\mathbb{N}$, which needed the consistency of $\mathsf{PA}$.
Then we conclude that $\mathbb{N}$ is a model of the larger theory.
Last we use the general fact that theories true in $\mathbb{N}$ are $\omega$-consistent.
Watch out: the truth of $\mathrm{Con}(\mathsf{PA})$ comes from the model $\mathbb{N}$, an argument outside $\mathsf{PA}$, and not from a proof in $\mathsf{PA}$.
