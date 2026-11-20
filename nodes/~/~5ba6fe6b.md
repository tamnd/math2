---
tag: ~5ba6fe6b
kind: concept
name: Preferential consequence relation
aliases: [preferential-consequence, klm-system-p, system-p, preferential-structure, rational-consequence-relation]
msc: ["68T27", "03B60"]
topics: [NJB94B39QK]
audience: grad
uses: [~37275fd2, 0QV2JS9RJ3, 1HK0VYWTV7]
sources:
  - url: https://plato.stanford.edu/entries/logic-nonmonotonic/
    locator: Non-monotonic Logic (SEP entry), sections 3.6, 3.6.1 and 3.6.3
  - book: isbn:9781904987000
---

## Summary

A *preferential consequence relation* is a relation $\alpha \mathrel{|\!\sim} \beta$ between propositional formulas that satisfies the six rules of the system $\mathbf{P}$ of Kraus, Lehmann and Magidor.
The rules are Reflexivity, Left Logical Equivalence, Right Weakening, Cut, Or and Cautious Monotony.
Semantically, $\alpha \mathrel{|\!\sim} \beta$ means that $\beta$ holds in the most normal states where $\alpha$ holds, for a [[partial order|0QV2JS9RJ3]] of normality.
Kraus, Lehmann and Magidor proved that the two descriptions give the same relations.
A preferential relation that also satisfies Rational Monotony is *rational*.

## Motivation

[[Nonmonotonic logics|~37275fd2]] come in many forms, with different syntax.
Shoham proposed a common semantic idea: a conclusion follows if it holds in the selected, most normal models of the premises, not in all of them.
Kraus, Lehmann and Magidor asked which properties every reasonable nonmonotonic relation should have.
The answer, system $\mathbf{P}$, is a small set of rules that is sound and complete for preferential models.
Other semantics, with possibility measures, rankings or plausibility measures, characterize the same core properties.

## Notation

We write $\alpha \mathrel{|\!\sim} \beta$ for "if $\alpha$, then normally $\beta$", and $\vDash$ for classical [[consequence|1HK0VYWTV7]].
A preferential model is $S = (\Omega, \ell, \prec)$, with states $\Omega$, a labeling $\ell$ of states by valuations, and a strict partial order $\prec$, where $s \prec t$ means "$s$ is more normal than $t$".
We write $\widehat{\alpha} = \set{s \in \Omega : \ell(s) \vDash \alpha}$, and $\mathrel{|\!\sim}_S$ for the relation of $S$.

## Remarks

### Examples

- [[A preferential relation that is not rational|~f37c5a32]]: a model with three states satisfies $\mathbf{P}$ but fails Rational Monotony.
- [[Rational closure of the penguin base|~c3ef01ad]]: rational closure concludes that red birds fly, which the preferential closure does not.
- Classical consequence, $\alpha \mathrel{|\!\sim} \beta$ if $\alpha \vDash \beta$, is preferential and also monotonic; it comes from the model with all valuations and the empty order.

### Non-examples

- [[Skeptical default consequence fails Cautious Monotony|~8f44dab0]]: Reiter's default logic does not give a preferential relation.
- The relation "$\alpha \mathrel{|\!\sim} \beta$ if $\beta \vDash \alpha$" fails Right Weakening, so it is not preferential.

### Basic properties

- System $\mathbf{P}$ derives And (from $\alpha \mathrel{|\!\sim} \beta$ and $\alpha \mathrel{|\!\sim} \gamma$ infer $\alpha \mathrel{|\!\sim} \beta \land \gamma$) and S (from $\alpha \land \beta \mathrel{|\!\sim} \gamma$ infer $\alpha \mathrel{|\!\sim} \beta \to \gamma$).
- Every preferential model gives a preferential relation: [[soundness of system P|~2b4be2dd]].
- Conversely, every preferential relation is $\mathrel{|\!\sim}_S$ for some preferential model $S$ (Kraus, Lehmann and Magidor 1990).
- Rational relations are exactly the relations of ranked models, where the states lie in linearly ordered levels.
- For a set $\mathbf{K}$ of conditional assertions, the *preferential closure* is the intersection of all preferential relations that contain $\mathbf{K}$; it equals the set of assertions that $\mathbf{P}$ derives from $\mathbf{K}$.
- The intersection of all rational relations that contain $\mathbf{K}$ is again the preferential closure; *rational closure* (Lehmann and Magidor 1992) is a different, stronger construction, and Pearl's system Z (1990) is equivalent to it.

### History

Shoham (1987) introduced the selection of preferred models.
Kraus, Lehmann and Magidor (1990) introduced system $\mathbf{P}$ and preferential models, and proved the representation theorem.
Lehmann and Magidor (1992) introduced rational closure.
Boutilier (1990) related system $\mathbf{P}$ to a fragment of the modal logic S4, and its rational strengthening to S4.3.

### Common errors

- To read $\alpha \mathrel{|\!\sim} \beta$ as a material conditional inside a theory. It is a statement about the relation, not a formula.
- To think that system $\mathbf{P}$ contains Monotony. It contains only Cautious Monotony, and Monotony fails in most preferential models.
- To forget the smoothness condition. Without it, Cautious Monotony can fail.
- To expect the preferential closure to ignore irrelevant information. It does not conclude "red birds fly" from "birds fly"; rational closure does.

## Explanations

### L1 human

"Birds fly" does not mean that every bird flies.
It means that normal birds fly.
A preferential relation says what holds in the most normal cases.
Its rules say, for example, that if normal birds fly and normal birds have feathers, then normal flying birds have feathers.

### L2 human

To check $\alpha \mathrel{|\!\sim} \beta$ in a preferential model, take the states where $\alpha$ holds and keep only the most normal ones.
If $\beta$ holds in all the kept states, then $\alpha \mathrel{|\!\sim} \beta$.
Adding a premise changes which states are most normal, so Monotony can fail.
A trap is to think that the most normal $\alpha \land \beta$ states are among the most normal $\alpha$ states; this holds only when $\alpha \mathrel{|\!\sim} \beta$.

### L3 human

The proof of the representation theorem builds a canonical preferential model from the relation itself.
Rational relations correspond to ranked models, and also to ordinal ranking functions on sets of valuations.
Under Boutilier's translation, a conditional assertion becomes a modal formula, and system $\mathbf{P}$ becomes a fragment of S4.
The SEP entry lists further semantics for the core properties, with possibility measures, ranking functions and plausibility measures.
