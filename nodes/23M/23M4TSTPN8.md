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

Let $\mathrm{Con}(\mathsf{PA}) := \neg \exists y \, \mathrm{Prf}_{\mathsf{PA}}(y, \ulcorner 0 = S0 \urcorner)$ be the [[consistency statement|4NBAX3VRQ7]] of [[Peano arithmetic|MPSCREYC3M]] for the standard $\Sigma_1$ axiom formula.
We check three things: it is a $\Pi_1$ sentence, it is true, and $\mathsf{PA}$ does not prove it.

1. The proof predicate $\mathrm{Prf}_{\mathsf{PA}}(y, x)$ is a $\Sigma_1$ formula $\exists z \, \delta(y, x, z)$ with $\delta$ bounded.
2. So $\mathrm{Con}(\mathsf{PA})$ is logically equivalent to $\forall y \, \forall z \, \neg \delta(y, \ulcorner 0 = S0 \urcorner, z)$.
   This is a $\Pi_1$ sentence: a block of universal quantifiers in front of a bounded formula.
3. The [[standard model|WP27CABPA4]] $\mathbb{N}$ satisfies every axiom of $\mathsf{PA}$.
   The axioms of $\mathsf{Q}$ are the recursion equations of $+$ and $\cdot$, and each induction axiom holds by induction on the natural numbers.
4. By [[soundness|4A84VHDTHV]], every theorem of $\mathsf{PA}$ is true in $\mathbb{N}$.
   The sentence $0 = S0$ says $0 = 1$, which is false in $\mathbb{N}$, so $\mathsf{PA} \nvdash 0 = S0$.
5. So no number codes a proof of $0 = S0$ in $\mathsf{PA}$.
   The formula $\mathrm{Prf}_{\mathsf{PA}}$ defines the real proof relation in $\mathbb{N}$, so $\mathbb{N} \models \mathrm{Con}(\mathsf{PA})$.
6. Step 4 shows that $\mathsf{PA}$ is consistent.
   By the [[second incompleteness theorem|4PZM5GJTR5]], $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$.

## Remarks

The sentence is unprovable only as a whole.
For any numbers $m$ and $n$, the instance $\neg \delta(\underline{m}, \ulcorner 0 = S0 \urcorner, \underline{n})$ is a true bounded sentence, so $\mathsf{PA}$ proves it.
So $\mathsf{PA}$ can check each candidate proof, but it cannot prove that every candidate fails.

$\mathsf{PA}$ does not prove $\neg \mathrm{Con}(\mathsf{PA})$ either.
That sentence is $\Sigma_1$ and false, and $\mathsf{PA}$ proves no false $\Sigma_1$ sentence, because all its theorems are true in $\mathbb{N}$.
So $\mathrm{Con}(\mathsf{PA})$ is independent of $\mathsf{PA}$, and it is a concrete example of the true $\Pi_1$ sentences that the incompleteness theorems promise.

Step 3 uses the standard model as a completed object, so the argument is carried out in set theory, not in $\mathsf{PA}$.
[[ZFC proves Con(PA)|1KSQAD4BWM]] makes this precise.
If $\mathsf{PA}$ is replaced by a consistent theory $T \supseteq \mathsf{PA}$ that is not true in $\mathbb{N}$, steps 3 and 4 fail, but steps 1, 2 and 6 still hold, and $\mathrm{Con}(T)$ is still a true $\Pi_1$ sentence that $T$ does not prove.

## Explanations

### L1 human

The sentence says "no number is the code of a proof of $0 = 1$ from the axioms of arithmetic".
It is true, because the axioms hold for the ordinary numbers, proofs keep truth, and $0 = 1$ is false.
The axioms can check any single number and see that it is not such a code.
But they cannot prove the statement for all numbers at once.

### L2 human

We read the sentence in three ways.
As a formula it has the form "for all $y$ and $z$, a bounded property of $y$ and $z$ holds", so it is $\Pi_1$.
As a claim about $\mathbb{N}$ it is true, because $\mathbb{N}$ is a model of $\mathsf{PA}$ in which $0 \ne 1$.
As a candidate theorem of $\mathsf{PA}$ it fails, by the second incompleteness theorem.
The typical use is as the simplest true $\Pi_1$ sentence that $\mathsf{PA}$ does not decide.
Watch out: the truth of $\mathrm{Con}(\mathsf{PA})$ is proved outside $\mathsf{PA}$, with the model $\mathbb{N}$, so it gives no reason to think that $\mathsf{PA}$ should prove it.
