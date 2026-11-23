---
tag: QMZVVXT9Q2
kind: example
name: A formula with a free variable is not a sentence
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
not_instance_of:
  - target: Q85MMH5DEY
    note: the variable x is free, so the set of free variables is not empty
uses: [Y3FZTH5158, DKFGQTRYZE, 2RBQPV02AS]
sources:
  - url: https://en.wikipedia.org/wiki/Sentence_(mathematical_logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Example

Let $\sigma = \{ < \}$, and let $\psi = \exists y \, (x < y)$.
We show that $\psi$ is not a [[sentence|DKFGQTRYZE]], and that its truth in a structure depends on the value of $x$.

1. $\operatorname{FV}(x < y) = \{ x, y \}$, and $\exists y$ removes $y$, so $\operatorname{FV}(\psi) = \{ x \}$ by the [[definition|Y3FZTH5158]].
2. Since $\operatorname{FV}(\psi) \neq \emptyset$, the formula $\psi$ is not a sentence.
3. Let $\mathcal{M} = (\{ 0, 1, 2 \}, <)$.
   Under an assignment with $x \mapsto 0$, the formula $\psi$ is [[satisfied|2RBQPV02AS]], with the witness $y = 1$.
4. Under an assignment with $x \mapsto 2$, the formula $\psi$ is not satisfied, because no element of $\{ 0, 1, 2 \}$ is greater than $2$.
5. So neither $\psi$ nor $\neg \psi$ holds in $\mathcal{M}$ under every assignment.

## Remarks

The example shows the difference between a formula and a sentence.
In $\mathcal{M}$ the formula $\psi$ defines a set: the witness $y = 1$ works for $x = 0$, the witness $y = 2$ works for $x = 1$, and no witness works for $x = 2$.
So $\psi$ defines $\{ 0, 1 \}$, the elements that are not the largest.

The two closures are sentences.
The universal closure $\forall x \, \exists y \, (x < y)$ is false in $\mathcal{M}$, and the existential closure $\exists x \, \exists y \, (x < y)$ is true.

Watch out: in $(\mathbb{N}, <)$ the formula $\psi$ holds for every value of $x$, but it is still not a sentence.
Being a sentence is a property of the syntax, not of one structure, and in $\mathcal{M}$ the same formula fails at $x = 2$.

## Explanations

### L1 human

"There is a number larger than $x$" is not a complete claim, since we do not know $x$.
Among the numbers $0, 1, 2$ it is true for $x = 0$, because $1$ is larger.
It is false for $x = 2$, because nothing is larger than $2$.
So the claim has no fixed truth value until we say what $x$ is.

### L2 human

A formula with one free variable is a way to name a subset of a structure.
In $\mathcal{M} = (\{ 0, 1, 2 \}, <)$, the formula $\psi$ names $\{ 0, 1 \}$, as the remarks compute.
In $(\mathbb{Z}, <)$ the same formula names all of $\mathbb{Z}$, and in $(\{ 5 \}, <)$ it names the empty set.
A sentence would name a whole truth value instead, the same for every choice of variables.
