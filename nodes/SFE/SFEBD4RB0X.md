---
tag: SFEBD4RB0X
kind: example
name: Provability in Q is a Σ1 truth predicate
msc: ["03F30", "03F40"]
topics: [HXHHWY3328]
audience: grad
instance_of: [Y2MF1EZAM7]
uses: [Y2MF1EZAM7, 3K1AKGXF8A, NB2BCZR40F, WP27CABPA4, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
    locator: Metamathematics
  - book: isbn:9780521857840
---

## Example

Let $\mathrm{Prov}_{\mathsf{Q}}(x)$ be the standard [[provability predicate|NB2BCZR40F]] of [[Robinson arithmetic|3K1AKGXF8A]].
We show that it is a [[partial truth predicate|Y2MF1EZAM7]] for $\Sigma_1$ sentences in the [[standard model|WP27CABPA4]]:
$$\mathbb{N} \models \mathrm{Prov}_{\mathsf{Q}}(\ulcorner \sigma \urcorner) \leftrightarrow \sigma \quad \text{for every } \Sigma_1 \text{ sentence } \sigma.$$
A sample sentence is $\sigma := \exists y \, (y \cdot y = \underline{9})$, which is true with witness $y = 3$.

1. $\mathrm{Prov}_{\mathsf{Q}}$ defines provability in $\mathbb{N}$: $\mathbb{N} \models \mathrm{Prov}_{\mathsf{Q}}(\ulcorner \sigma \urcorner)$ exactly when $\mathsf{Q} \vdash \sigma$.
2. If $\sigma$ is true, then $\mathsf{Q} \vdash \sigma$, by the [[Σ1-completeness of Robinson arithmetic|69234Z1V00]].
   For the sample, $\mathsf{Q}$ computes $\underline{3} \cdot \underline{3} = \underline{9}$ from its recursion axioms and then introduces $\exists y$.
3. If $\mathsf{Q} \vdash \sigma$, then $\sigma$ is true, by [[soundness|4A84VHDTHV]], since $\mathbb{N}$ is a model of $\mathsf{Q}$.
4. Steps 2 and 3 give: $\sigma$ is true exactly when $\mathsf{Q} \vdash \sigma$.
   With step 1, $\sigma$ is true exactly when $\mathbb{N} \models \mathrm{Prov}_{\mathsf{Q}}(\ulcorner \sigma \urcorner)$.
5. $\mathrm{Prov}_{\mathsf{Q}}(x)$ has the form $\exists y \, \mathrm{Prf}_{\mathsf{Q}}(y, x)$ with $\mathrm{Prf}_{\mathsf{Q}}$ a $\Sigma_1$ formula, so it is $\Sigma_1$.
   So this truth predicate has the same level as the sentences it covers.

## Remarks

The example gives a $\Sigma_1$ truth predicate without building one by recursion on formulas.
At codes of sentences that are not $\Sigma_1$, the formula $\mathrm{Prov}_{\mathsf{Q}}$ still says something, namely provability.
To get a formula that is false outside the class, take $\mathrm{Prov}_{\mathsf{Q}}(x) \wedge \mathrm{Sent}_{\Sigma_1}(x)$, where $\mathrm{Sent}_{\Sigma_1}$ defines the codes of $\Sigma_1$ sentences.

The same argument works with any $\Sigma_1$-sound theory $T \supseteq \mathsf{Q}$ with computable axioms in place of $\mathsf{Q}$.
If $T$ proves a false $\Sigma_1$ sentence, such as $\neg \mathrm{Con}(\mathsf{PA})$ in $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$, step 3 fails and so does the example.
The equivalence is a fact about $\mathbb{N}$, and the example does not claim that $\mathsf{Q}$ proves the biconditionals.
It fails one level up, as [[provability in Q is not a Π1 truth predicate|G7E1ZT2HST]] shows.

## Explanations

### L1 human

Consider statements of the form "some number has a property that can be checked by a finite computation".
Such a statement is true exactly when Robinson arithmetic proves it: the proof just exhibits the number and does the check.
So, for these statements, "provable in Robinson arithmetic" and "true" mean the same thing.

### L2 human

We run both directions on $\sigma := \exists y \, (y \cdot y = \underline{9})$.
It is true with $y = 3$, and $\mathsf{Q}$ proves $\underline{3} \cdot \underline{3} = \underline{9}$, hence $\sigma$.
In the other direction, $\mathsf{Q}$ proves nothing false, because $\mathbb{N}$ is a model of it.
For example, $\mathsf{Q}$ does not prove $\exists y \, (y \cdot y = \underline{8})$, which is false.
The typical use is to get a $\Sigma_1$ truth definition for free from $\Sigma_1$-completeness.
Watch out: this stops at $\Sigma_1$, because $\mathsf{Q}$ does not prove every true $\Pi_1$ sentence.
