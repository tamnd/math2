---
tag: AXGTQ7091K
kind: example
name: Intuitionistic predicate logic is not a first-order Gödel logic
msc: ["03B52", "03B55"]
topics: [WZP584JQ06]
audience: research
not_instance_of:
  - target: H8C323CV3T
    note: IQC refutes prelinearity and the constant domain axiom, which every G_V proves
uses: [MW0RVDRFTA, 6S7TSV01WB, 42GA7FHGW2, D0ZADJFPQE, KTWJZCFJXY]
sources:
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 6.1 Subintuitionistic and Intermediate Logics
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 6.2 Many-valued first-order logics
---

## Example

We show that [[intuitionistic predicate logic|MW0RVDRFTA]] $\mathsf{IQC}$ differs from every [[first-order Gödel logic|H8C323CV3T]] $\mathrm{G}_V$.

1. The Gödel t-norm $\min$ is left-continuous, so [[prelinearity|D0ZADJFPQE]] gives $\max(x \to y, y \to x) = 1$ on $[0, 1]$.
2. $V$ is closed under $\min$, $\max$ and the Gödel implication, so $(p \to q) \lor (q \to p)$ has value $1$ in every $V$-structure.
3. [[The fork|6S7TSV01WB]] refutes $(p \to q) \lor (q \to p)$ in a Kripke model, so $\mathsf{IQC}$ does not prove it.
4. [[The constant domain axiom|KTWJZCFJXY]] has value $1$ in every $V$-structure.
5. [[A Kripke model with growing domains|42GA7FHGW2]] refutes it, so $\mathsf{IQC}$ does not prove it.
6. So for every $V$, $\mathrm{G}_V$ proves two sentences that $\mathsf{IQC}$ does not prove.

## Remarks

1. A $V$-structure is a model with values in the complete Heyting chain $V$, so every theorem of $\mathsf{IQC}$ is in $\mathrm{G}_V$; the inclusion is strict by step 6.
2. Step 3 is propositional, and step 5 is first-order: the countermodel of step 5 has a linear frame, so it validates prelinearity.
3. Prelinearity needs a linear order of truth values, and the constant domain axiom needs a fixed domain; every $V$-structure has both.

## Explanations

### L1 human

Intuitionistic logic allows knowledge to grow in branching ways, and allows new objects to appear.
Gödel logic measures truth on one line, with a fixed set of objects.
So Gödel logic proves more laws.

### L2 human

1. Find a law valid in every $V$-structure.
2. Find a Kripke countermodel for it.

A trap: a single linear Kripke model with growing domains validates prelinearity; it is the growing domain that breaks the constant domain axiom.
