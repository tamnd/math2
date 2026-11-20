---
tag: A3TMWKAS31
kind: statement
role: theorem
name: Soundness of system P for preferential models
aliases: [klm-soundness, soundness-of-system-p]
msc: ["68T27", "03B60"]
topics: [NJB94B39QK]
audience: grad
about: [G4QC9MKFAG]
uses: [7J659YV5WA]
sources:
  - url: https://plato.stanford.edu/entries/logic-nonmonotonic/
    locator: Non-monotonic Logic (SEP entry), section 3.6.1
  - book: isbn:9781904987000
---

## Statement

Let $S = (\Omega, \ell, \prec)$ be a smooth [[preferential model|7J659YV5WA]].
Then $\mathrel{|\!\sim}_S$ is a preferential consequence relation: it satisfies Reflexivity, Left Logical Equivalence, Right Weakening, Cut, Or and Cautious Monotony.

## Remarks

### Why each hypothesis is needed

Smoothness is needed for Cautious Monotony.
Let $\Omega = \set{m} \cup \set{c_n : n \in \mathbb{N}}$, with $c_{n+1} \prec c_n$ and $c_n \prec m$ for all $n$, and the transitive closure of these.
Label every $c_n$ with a valuation of $\alpha \land \neg\beta$, and $m$ with a valuation of $\alpha \land \beta \land \neg\gamma$.
Then $\widehat{\alpha}$ has no minimal state, so $\alpha \mathrel{|\!\sim}_S \beta$ and $\alpha \mathrel{|\!\sim}_S \gamma$ hold vacuously.
But $\widehat{\alpha \land \beta} = \set{m}$, so $m$ is minimal there, and $\alpha \land \beta \mathrel{|\!\not\sim}_S \gamma$.
The other five rules hold without smoothness.

### Consequences

- The derived rules And and S hold in every preferential model.
- Every relation that fails one of the six rules, such as skeptical consequence in default logic, has no preferential model.

### Converse

Kraus, Lehmann and Magidor (1990) proved the converse: every preferential consequence relation equals $\mathrel{|\!\sim}_S$ for some preferential model $S$.
So system $\mathbf{P}$ is sound and complete for preferential models.

### Generalizations

Ranked models give rational relations, which also satisfy Rational Monotony, and every rational relation comes from a ranked model.

## History

Kraus, Lehmann and Magidor introduced system $\mathbf{P}$ and preferential models in 1990, following the selection semantics of Shoham (1987).
The SEP entry calls the six rules the core properties, or the KLM properties.

## Explanations

### L1 human

The rules of system $\mathbf{P}$ are safe for the reading "in the most normal cases".
If a rule takes true statements about the most normal cases as input, its output is again true about the most normal cases.

### L2 human

Most rules follow at once from the definition of minimal states.
The two interesting rules are Or and Cautious Monotony.
For Or, a minimal $(\alpha \lor \beta)$-state that satisfies $\alpha$ is also a minimal $\alpha$-state.
For Cautious Monotony, smoothness shows that a minimal $(\alpha \land \beta)$-state is a minimal $\alpha$-state when $\alpha \mathrel{|\!\sim} \beta$.
A trap is to prove Cautious Monotony without smoothness; the infinite chain above is a counterexample.
