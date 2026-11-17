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

Let $T := \mathsf{PA} + \mathrm{Con}(\mathsf{PA})$, where $\mathrm{Con}(\mathsf{PA})$ is the [[consistency statement|4NBAX3VRQ7]] $\neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner)$.
We show that $T$ is [[ω-consistent|4S29X1GTV4]].

1. $\N$ is a model of $\mathsf{PA}$, as in [[Peano arithmetic is ω-consistent|5JKPMRAXZP]]. So $\mathsf{PA}$ does not prove $0 = S0$.
2. So no number codes a proof of $0 = S0$ in $\mathsf{PA}$.
3. The formula $\mathrm{Prf}_{\mathsf{PA}}(y, x)$ defines the proof relation in $\N$. By step 2, $\N \models \neg \exists y \, \mathrm{Prf}_{\mathsf{PA}}(y, \ulcorner 0 = S0 \urcorner)$, that is, $\N \models \mathrm{Con}(\mathsf{PA})$.
4. By steps 1 and 3, $\N$ is a model of $T$.
5. A theory with $\N$ as a model is $\omega$-consistent: a proved $\exists x \, \varphi(x)$ has a witness $m$ in $\N$, and the false sentence $\neg \varphi(\underline{m})$ is not provable.

## Remarks

The theory $T$ is stronger than $\mathsf{PA}$, since $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$, but it keeps $\omega$-consistency because its new axiom is true.
The theory $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is also consistent, but it is not $\omega$-consistent, see [[this example|FK06QR6A44]].
So between the two consistent extensions by $\mathrm{Con}(\mathsf{PA})$ and by its negation, $\omega$-consistency selects the true one.
Iterating gives $\mathsf{PA} + \mathrm{Con}(\mathsf{PA}) + \mathrm{Con}(\mathsf{PA} + \mathrm{Con}(\mathsf{PA}))$ and so on, all true in $\N$; these are the first steps of a [[Turing progression|F7Z4BV2KHD]].

## Explanations

### L1 human

The sentence "Peano arithmetic never proves $0 = 1$" is true.
Adding a true sentence to true axioms gives true axioms.
True axioms never claim the existence of a number and then rule out every number.
So the larger theory is still $\omega$-consistent.

### L2 human

1. Check that the new axiom is true in $\N$.
2. Conclude that $\N$ is a model of the larger theory.
3. Use the general fact that theories true in $\N$ are $\omega$-consistent.

The typical use is to see that the second incompleteness theorem gives true unprovable sentences.
A trap: the truth of $\mathrm{Con}(\mathsf{PA})$ depends on the consistency of $\mathsf{PA}$, which we know from the model $\N$ and not from a proof in $\mathsf{PA}$.
