---
tag: 23M4TSTPN8
kind: example
name: Con(PA) is a true Π1 sentence
msc: ["03F40", "03F30"]
topics: [HXHHWY3328]
audience: grad
instance_of: [4NBAX3VRQ7]
uses: [4NBAX3VRQ7, MPSCREYC3M, WP27CABPA4, 4A84VHDTHV, NB2BCZR40F, 4PZM5GJTR5]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel's_incompleteness_theorems
    locator: Second incompleteness theorem
  - book: isbn:9780521857840
---

## Example

Let $\mathrm{Con}(\mathsf{PA}) := \neg \exists y \, \mathrm{Prf}_{\mathsf{PA}}(y, \ulcorner 0 = S0 \urcorner)$, the [[consistency statement|4NBAX3VRQ7]] of [[Peano arithmetic|MPSCREYC3M]] for the standard $\Sigma_1$ axiom formula.
We check that it is a $\Pi_1$ sentence, that it is true, and that $\mathsf{PA}$ does not prove it.

1. $\mathrm{Prf}_{\mathsf{PA}}(y, x)$ is a $\Sigma_1$ formula $\exists z \, \delta(y, x, z)$ with $\delta$ in $\Delta_0$.
2. So $\mathrm{Con}(\mathsf{PA})$ is equivalent in logic to $\forall y \, \forall z \, \neg \delta(y, \ulcorner 0 = S0 \urcorner, z)$, a $\Pi_1$ sentence.
3. The [[standard model|WP27CABPA4]] $\N$ satisfies every axiom of $\mathsf{PA}$.
4. By [[soundness|4A84VHDTHV]], every theorem of $\mathsf{PA}$ is true in $\N$. Since $0 = S0$ is false in $\N$, $\mathsf{PA} \nvdash 0 = S0$.
5. So no number codes a proof of $0 = S0$ in $\mathsf{PA}$. The formula $\mathrm{Prf}_{\mathsf{PA}}$ defines the proof relation in $\N$, so $\N \models \mathrm{Con}(\mathsf{PA})$.
6. By step 4, $\mathsf{PA}$ is consistent. By the [[second incompleteness theorem|4PZM5GJTR5]], $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$.

## Remarks

Step 3 uses the standard model, which is a set-theoretic object; this argument is not a proof inside $\mathsf{PA}$.
Since $\mathsf{PA}$ is $\Sigma_1$-sound, $\mathsf{PA}$ also does not prove the false $\Sigma_1$ sentence $\neg \mathrm{Con}(\mathsf{PA})$.
So $\mathrm{Con}(\mathsf{PA})$ is independent of $\mathsf{PA}$.
Each instance $\neg \delta(\underline{m}, \ulcorner 0 = S0 \urcorner, \underline{n})$ is a true $\Delta_0$ sentence, so $\mathsf{PA}$ proves it.
Only the universal statement is unprovable.

## Explanations

### L1 human

The statement says "no number is the code of a proof of $0 = 1$ from the axioms of arithmetic".
It is true, because the axioms are true of the ordinary numbers and $0 = 1$ is not.
The axioms can check each number, but they cannot prove the statement for all numbers at once.

### L2 human

1. $\mathrm{Con}(\mathsf{PA})$ has the form "for all $y$, a decidable property of $y$ holds".
2. It is true, since $\N$ is a model of $\mathsf{PA}$.
3. It is unprovable in $\mathsf{PA}$, by the second theorem.

The typical use is as the simplest example of a true $\Pi_1$ sentence that $\mathsf{PA}$ does not decide.
A trap: the truth of $\mathrm{Con}(\mathsf{PA})$ is proved in set theory, using the model $\N$.
