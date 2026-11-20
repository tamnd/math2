---
tag: C7YWCR87QJ
kind: concept
name: Paraconsistent logic
aliases: [paraconsistency, inconsistency-tolerant-logic]
msc: [03B53]
topics: [NJB94B39QK]
audience: ug2
uses: [TTKZGJEEK7, J78Y1M4GND, 029JBBF693, VM8TQ70CVJ]
sources:
  - url: https://en.wikipedia.org/wiki/Paraconsistent_logic
    locator: lead section; Applications
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), sections 1, 1.3 and 3
  - book: isbn:9780521670265
  - book: isbn:9783319332031
same_as:
  wikidata: Q426592
  wikipedia: Paraconsistent logic
---

## Summary

A *paraconsistent logic* is a logic whose [[consequence relation|J78Y1M4GND]] is not [[explosive|TTKZGJEEK7]].
So some formula $\varphi$ and some formula $\psi$ satisfy $\varphi, \neg\varphi \nvdash \psi$.
The precise [[definition|ETCVR65W3M]] says only what a paraconsistent logic does not do; it does not fix one system.
There are five main families: discussive logics, logics of formal inconsistency, relevance logics, many-valued logics such as the logic of paradox, and adaptive logics.
Paraconsistent logics let us reason from inconsistent information without deriving every statement.

## Motivation

In classical logic, one contradiction makes a theory trivial: every formula follows from it.
Real sources of information are often inconsistent: a database with conflicting records, two witnesses who disagree, or a scientific theory with a known anomaly.
We still want to draw useful conclusions from these sources and to refuse the useless ones.
A paraconsistent logic separates two notions that classical logic identifies: an inconsistent theory proves some $\varphi$ and its [[negation|029JBBF693]] $\neg\varphi$, and a trivial theory proves every formula.
Some authors also want a logic for theories that they think are inconsistent and true, such as a naive theory of truth; this is the position of dialetheism.

## Notation

We write $\Gamma \vdash_{\mathsf{L}} \psi$ when $\psi$ follows from $\Gamma$ in the logic $\mathsf{L}$.
We write $\circ\varphi$ for "$\varphi$ is consistent" in logics of formal inconsistency.
In three-valued semantics, the values are $\mathsf{T}$, $\mathsf{B}$ ("both") and $\mathsf{F}$, and a set $D$ of designated values replaces "true".

## Remarks

### Examples

- The [[logic of paradox|BXJZG67PX3]] designates $\mathsf{T}$ and $\mathsf{B}$, and the valuation $v(p) = \mathsf{B}$, $v(q) = \mathsf{F}$ refutes $p, \neg p \vDash q$; see the [[explicit valuation|AX6G3E9CQJ]].
- First-degree entailment, a four-valued logic, is paraconsistent and paracomplete; see [[FDE|KXTP4P3GHT]].
- [[Da Costa's systems|KN2VBRQB3Q]] $C_n$ keep positive classical logic and weaken negation; a contradiction about $A$ explodes only when $A$ is consistent.
- [[Jaśkowski's discussive logic|489SFB5NX2]] reads each premise as a claim of one participant in a discussion, so that $A$ and $\neg A$ do not combine.
- [[Adaptive logics|X8RW5F4261]] act like classical logic until a contradiction appears, and then withdraw only the affected inferences.
- Relevance logics require a connection of content between premises and conclusion; see the topic [[substructural and relevance logics|98QF5J4W16]].

### Non-examples

- Classical logic is explosive, by the [[principle of explosion|K33VPAPJQG]].
- [[Intuitionistic logic is explosive|EQ9DND41TR]], even though it rejects excluded middle.
- [[Strong Kleene logic K3 is explosive|2ZDYGB4J5N]], although it has the same tables as the logic of paradox.

### Basic properties

- A paraconsistent logic must give up at least one of the rules in the Lewis argument: disjunction introduction, disjunctive syllogism, or transitivity of consequence. Most systems drop disjunctive syllogism.
- A logic is *paracomplete* when excluded middle fails. Paraconsistency and paracompleteness are independent: LP is paraconsistent only, K3 is paracomplete only, and FDE is both.
- Paraconsistency does not imply that contradictions are true. A logic can tolerate inconsistent premises and still say that no contradiction is true; the glossary calls these views [[weak paraconsistency|V5AWSJJJ4G]] and [[strong paraconsistency|GYCRTA2TN9]].
- A theory can be inconsistent but not trivial only in a paraconsistent logic; in an explosive logic, [[consistency|VM8TQ70CVJ]] and non-triviality are equivalent.
- Applications include naive theories of truth and sets, belief revision, inconsistent databases, and inconsistencies in large software systems.

### History

Starting about 1910, Vasil'ev proposed a syllogistic that allows statements of the form "$S$ is both $P$ and not $P$".
In 1929, Orlov gave the first axiomatization of the relevant logic $R$, which is paraconsistent.
Jaśkowski, a student of Łukasiewicz, was the first formal logician to develop paraconsistent logic.
Asenjo and da Costa developed paraconsistent logics in their doctoral dissertations of 1954 and 1963.
Smiley in England in 1959, and Anderson and Belnap in the United States, proposed relevant logics.
Miró Quesada coined the word "paraconsistent" at the Third Latin American Conference on Mathematical Logic in 1976.

### Common errors

- To think that a paraconsistent logic accepts all contradictions. It only stops a contradiction from proving everything.
- To think that every many-valued logic is paraconsistent. The designated values decide it; K3 is explosive.
- To think that rejecting $\neg(p \land \neg p)$ is needed. LP keeps this law as a tautology and is still paraconsistent.

## Explanations

### L1 human

Suppose a company database lists a customer as living in Paris and also as not living in Paris.
In classical logic, this one error lets you prove anything, such as "the customer owns the Moon".
A paraconsistent logic blocks this.
You can still conclude things that follow from the good records.
The bad record causes trouble only near itself.

### L2 human

We test the definition on the logic of paradox LP.

1. LP has three values $\mathsf{T}$, $\mathsf{B}$ and $\mathsf{F}$, with designated values $\mathsf{T}$ and $\mathsf{B}$.
2. Negation swaps $\mathsf{T}$ and $\mathsf{F}$ and fixes $\mathsf{B}$.
3. Let $v(p) = \mathsf{B}$ and $v(q) = \mathsf{F}$.
4. Then $v(p) = \mathsf{B}$ and $v(\neg p) = \mathsf{B}$ are designated, and $v(q) = \mathsf{F}$ is not.
5. So $p, \neg p \nvDash_{\mathrm{LP}} q$, and LP is paraconsistent.

The same valuation makes $p \lor q$ and $\neg p$ designated and $q$ undesignated, so disjunctive syllogism fails.
This is the price of paraconsistency in LP.
A typical trap is to forget that you must lose some classical rule; paraconsistency is never free.

### L3 human

Paraconsistency is a property of a consequence relation, so the families differ in which structural or operational rule they change.
The logic of paradox and FDE change the semantics of negation and keep the structural rules; discussive logics drop adjunction; relevance logics change the conditional and, in substructural form, weakening.
Logics of formal inconsistency internalize consistency as a connective $\circ$ and recover classical reasoning for consistent formulas, the principle of gentle explosion.
Adaptive logics make consequence dynamic and nonmonotonic, so that a derived line can be withdrawn later.
A useful abstract test is the Lewis argument: each family breaks one of its links.
