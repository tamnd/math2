---
tag: F8C9XXMBRW
kind: example
name: Iterating the negation of consistency is not a progression of theories
msc: ["03F40", "03F15"]
topics: [HXHHWY3328]
audience: research
not_instance_of:
  - target: F7Z4BV2KHD
    note: "The step T ↦ T + ¬Con(T) adds the negation of a consistency statement, not a consistency or reflection principle; the stages are false in the standard model and the iteration stops growing after one step."
uses: [F7Z4BV2KHD, 4NBAX3VRQ7, 4PZM5GJTR5, MPSCREYC3M, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Second incompleteness theorem
---

## Example

Since $\mathsf{PA}$ does not prove $\mathrm{Con}(\mathsf{PA})$, the theory $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent.
So why not iterate this step, as a progression iterates $\mathrm{Con}$?
We show that the result is not a progression in the sense of [[Turing and Feferman progressions|F7Z4BV2KHD]]: the stages are false, and the iteration stops growing after one step.

Define $U_0 = \mathsf{PA}$ and $U_{k+1} = U_k + \neg \mathrm{Con}(U_k)$ for $k \in \mathbb{N}$, with the natural axiom formulas.

### The check

1. A progression adds at each step a [[consistency statement|4NBAX3VRQ7]] or a reflection principle for the previous theory.
   The sentence $\neg \mathrm{Con}(U_k)$ is the negation of such a statement, so the defining condition fails.
2. $U_1 = \mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent.
   By [[Gödel's second incompleteness theorem|4PZM5GJTR5]], $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$, and whenever $T \nvdash \varphi$ the theory $T + \neg \varphi$ is consistent.
3. $U_1$ is not sound.
   The axioms of $\mathsf{PA}$ are true in $\mathbb{N}$, so by [[soundness|4A84VHDTHV]] $\mathsf{PA}$ does not prove $0 = S0$, and $\mathrm{Con}(\mathsf{PA})$ is true.
   So the axiom $\neg \mathrm{Con}(\mathsf{PA})$ of $U_1$ is false.
4. For every $k \ge 1$, $U_k \vdash \neg \mathrm{Con}(U_k)$.
   The axiom $\neg \mathrm{Con}(\mathsf{PA})$ of $U_k$ says that some number codes a $\mathsf{PA}$-proof of $0 = S0$.
   $\mathsf{PA}$ proves that every $\mathsf{PA}$-proof is a $U_k$-proof, because the axiom formula of $U_k$ includes that of $\mathsf{PA}$.
   So $U_k$ proves that some number codes a $U_k$-proof of $0 = S0$, which is $\neg \mathrm{Con}(U_k)$.
5. By step 4, the new axiom of $U_{k+1}$ is already a theorem of $U_k$ when $k \ge 1$.
   So $U_1, U_2, U_3, \ldots$ all have the same theorems.

The family is not strictly increasing after $U_1$, and its stages from $U_1$ on are false in $\mathbb{N}$.
A progression over a sound base has sound stages and proper successor steps, so this family is not one.

## Remarks

The example shows that an effective step is not enough: the step of a progression must add true statements about the previous theory.
The negation of consistency is consistent with $\mathsf{PA}$, so the second incompleteness theorem does not exclude it; only the demand for soundness does.

$U_1$ is consistent but not [[ω-consistent|4S29X1GTV4]].
It proves $\exists x \, \mathrm{Prf}_{\mathsf{PA}}(x, \ulcorner 0 = S0 \urcorner)$, while for each number $n$ it proves $\neg \mathrm{Prf}_{\mathsf{PA}}(\underline{n}, \ulcorner 0 = S0 \urcorner)$, since that is a true decidable statement.

If we replace $\neg \mathrm{Con}$ by $\mathrm{Con}$, we get [[the finite stages of the consistency progression|7SRG8BJRJV]], which are sound and strictly increasing.

## Explanations

### L1 human

The usual progression adds at each step the true statement "the previous list of axioms is consistent".
Here we add the false statement "the previous list is inconsistent" instead.
Gödel's theorem shows that this causes no contradiction at once.
But the new list believes a false fact about proofs, and it already believes that it is itself inconsistent.
So adding the same kind of axiom again gives nothing new, and the chain stops growing.

### L2 human

Compute the first three stages.
$U_0 = \mathsf{PA}$ is sound.
$U_1 = \mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent by step 2 and unsound by step 3.
$U_2 = U_1 + \neg \mathrm{Con}(U_1)$, and $U_1$ already proves $\neg \mathrm{Con}(U_1)$ by step 4, so $U_2$ has the same theorems as $U_1$.
The typical use of the example is as a test of the definition of a progression.
Watch out: a consistent extension of $\mathsf{PA}$ need not be true in $\mathbb{N}$, and $U_1$ is consistent and false.
