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
We show that it is a [[partial truth predicate|Y2MF1EZAM7]] for $\Sigma_1$ sentences in the [[standard model|WP27CABPA4]]: $\N \models \mathrm{Prov}_{\mathsf{Q}}(\ulcorner \sigma \urcorner) \leftrightarrow \sigma$ for every $\Sigma_1$ sentence $\sigma$.

1. $\mathrm{Prov}_{\mathsf{Q}}$ defines provability in $\N$: $\N \models \mathrm{Prov}_{\mathsf{Q}}(\ulcorner \sigma \urcorner)$ exactly when $\mathsf{Q} \vdash \sigma$.
2. If $\sigma$ is true, then $\mathsf{Q} \vdash \sigma$, by $\Sigma_1$-completeness of $\mathsf{Q}$.
3. If $\mathsf{Q} \vdash \sigma$, then $\sigma$ is true, by [[soundness|4A84VHDTHV]], since $\N$ is a model of $\mathsf{Q}$.
4. So $\sigma$ is true exactly when $\mathsf{Q} \vdash \sigma$, and by step 1 exactly when $\N \models \mathrm{Prov}_{\mathsf{Q}}(\ulcorner \sigma \urcorner)$.
5. $\mathrm{Prov}_{\mathsf{Q}}$ is a $\Sigma_1$ formula, so this predicate has the same level as the sentences it covers.

## Remarks

The formula $\mathrm{Prov}_{\mathsf{Q}}(x) \wedge \mathrm{Sent}_{\Sigma_1}(x)$, where $\mathrm{Sent}_{\Sigma_1}$ defines the codes of $\Sigma_1$ sentences, is false at every code outside the class.
The same works for any $\Sigma_1$-sound c.e. theory that contains $\mathsf{Q}$ in place of $\mathsf{Q}$.
The equivalence holds in $\N$; it is not claimed that $\mathsf{Q}$ proves the biconditionals.

## Explanations

### L1 human

A statement of the form "some number has a checkable property" is true exactly when Robinson arithmetic proves it.
So "provable in Robinson arithmetic" and "true" agree on these statements.

### L2 human

1. True $\Sigma_1$ sentences are provable in $\mathsf{Q}$.
2. Provable sentences are true, since $\N$ is a model of $\mathsf{Q}$.
3. So provability defines $\Sigma_1$ truth.

The typical use is to get a $\Sigma_1$ truth definition without building one by recursion.
A trap: this fails one level up, for $\Pi_1$ sentences, because $\mathsf{Q}$ does not prove every true $\Pi_1$ sentence.
