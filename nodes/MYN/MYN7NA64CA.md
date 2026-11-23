---
tag: MYN7NA64CA
kind: example
name: PA plus the consistency of PA is not a fragment of PA
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: research
not_instance_of:
  - target: T70PYM1F36
    note: "PA + Con(PA) proves Con(PA), which PA does not prove, so not all its theorems are theorems of PA."
uses: [T70PYM1F36, HACXBCM7SS, 4PZM5GJTR5, EQH7XTZ29V, 4A84VHDTHV, XQMNJF241J]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_principle
    locator: For arithmetic
---

## Example

Adding a true axiom can take a theory outside $\mathsf{PA}$.
Let $T$ be $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$, that is, [[Peano arithmetic|HACXBCM7SS]] with its consistency statement added as an axiom.
We show that $T$ is not a [[fragment of PA|T70PYM1F36]]: some theorem of $T$ is not a theorem of $\mathsf{PA}$.

1. $\mathsf{PA}$ is consistent, because $\mathfrak{N}$ is a model of it, by [[soundness|4A84VHDTHV]].
2. $\mathsf{PA}$ is recursively axiomatized and extends Robinson arithmetic $\mathsf{Q}$.
3. By steps 1 and 2 and the [[second incompleteness theorem|4PZM5GJTR5]], $\mathsf{PA}$ does not prove $\mathrm{Con}(\mathsf{PA})$.
4. $T$ proves $\mathrm{Con}(\mathsf{PA})$, since it is an axiom of $T$.
5. So $\mathrm{Con}(\mathsf{PA})$ is a theorem of $T$ that is not a theorem of $\mathsf{PA}$.

So $T$ is not a fragment of $\mathsf{PA}$, although it is consistent and true in $\mathfrak{N}$.

## Remarks

The contrast is with the fragments $\mathsf{I}\Sigma_n$.
For $n \ge 1$, $\mathsf{I}\Sigma_{n+1}$ proves $\mathrm{Con}(\mathsf{I}\Sigma_n)$, so $\mathsf{I}\Sigma_n + \mathrm{Con}(\mathsf{I}\Sigma_n)$ stays inside $\mathsf{PA}$ and is a fragment.
Adding its own consistency always lifts a theory strictly above itself.
For a fragment the lift stays inside $\mathsf{PA}$, and for $\mathsf{PA}$ itself the lift leaves $\mathsf{PA}$.

Since $\mathrm{Con}(\mathsf{PA})$ is a $\Pi_1$ sentence, $T$ is not even conservative over $\mathsf{PA}$ for $\Pi_1$ sentences, as [[the non-conservativity example|EQH7XTZ29V]] records.
In the same way, $\mathsf{PA} + \sigma$ is not a fragment for any sentence $\sigma$ that $\mathsf{PA}$ does not prove.
The true [[Goodstein sentence|XQMNJF241J]] is another such $\sigma$.

## Explanations

### L1 human

A fragment of Peano arithmetic proves only things that Peano arithmetic proves.
The statement "Peano arithmetic is consistent" is true, but Gödel showed that Peano arithmetic cannot prove it.
So a theory that has this statement as an axiom proves something new.
It is stronger than Peano arithmetic, not a part of it.

### L2 human

We compare $\mathsf{I}\Sigma_1 + \mathrm{Con}(\mathsf{I}\Sigma_1)$ with $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$.
$\mathsf{PA}$ proves $\mathrm{Con}(\mathsf{I}\Sigma_1)$, and it proves every axiom of $\mathsf{I}\Sigma_1$, so every theorem of the first theory is a theorem of $\mathsf{PA}$.
$\mathsf{PA}$ does not prove $\mathrm{Con}(\mathsf{PA})$, so the second theory has a theorem outside $\mathsf{PA}$.
So the first theory is a fragment and the second is not.

Watch out: the consistency of a true theory is true, but that does not make it provable.
Truth in $\mathfrak{N}$ and provability in $\mathsf{PA}$ are different things, and the second incompleteness theorem is exactly the gap between them here.
