---
tag: WH94DG6D3Q
kind: concept
name: Truth-value glut
aliases: [glut, both-true-and-false, dialetheia]
msc: ["03A05", "03B53"]
topics: [6Q4JJ2MMV8]
audience: grad
uses: [SZHA10A9X7, TTKZGJEEK7, 4CBCWZQZ12]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section T
    note: adopted
    mention: wikipedia://en/76765067#HEFD
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 4.1.2 Paraconsistent"
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 4.1.3 Expressive power and 'revenge'"
inventory: [CPPSQS0EVZ]
---

## Summary

A *truth-value glut* is a sentence that is both true and false in a given semantics.
In a partial interpretation $(E, A)$ of a truth predicate $T$, a sentence $\varphi$ is a glut if $\ulcorner \varphi \urcorner \in E \cap A$.
In the *logic of paradox* $\mathrm{LP}$, the values are $1$, $\mathrm{b}$ (both) and $0$, and the designated values are $1$ and $\mathrm{b}$.
A glut has the value $\mathrm{b}$.
A theory that accepts gluts must use a [[paraconsistent logic|C7YWCR87QJ]], so that a contradiction does not imply every sentence.
*Dialetheism* is the view that some sentences, for example the [[liar|~005ac188]], are true gluts.

## Motivation

The [[naive truth schema|~34d21c75]] and the liar give a contradiction.
A [[gap theory|4CBCWZQZ12]] blocks the derivation by rejecting excluded middle.
A glut theory accepts the derivation up to the contradiction, and it rejects the next step, [[explosion|TTKZGJEEK7]].
The SEP entry reports Priest's argument that the T-schema and excluded middle both hold, so that the liar is both true and not true.
On this view the contradiction is real, but it stays local.

## Notation

1. $\mathrm{LP}$ uses the [[strong Kleene|SZHA10A9X7]] tables, with the middle value read as $\mathrm{b}$ in place of $\mathrm{u}$.
2. $\Gamma \models_{\mathrm{LP}} \varphi$ means: every valuation that gives every member of $\Gamma$ a designated value gives $\varphi$ a designated value.
3. A *dialetheia* is a true contradiction, that is, a true sentence of the form $\varphi \wedge \neg \varphi$.
4. In four-valued [[first-degree entailment|KXTP4P3GHT]], a glut has the value $\mathbf{B}$ and a gap has the value $\mathbf{N}$.

## Remarks

### Examples

1. The [[liar is a glut in every LP fixed point|~bba62832]].
2. In first-degree entailment, the liar is a gap or a glut in every fixed point, and both cases occur; see [[this example|~1fc35e2d]].
3. Let $v(p) = \mathrm{b}$ and $v(q) = 0$ in $\mathrm{LP}$. Then $p \wedge \neg p$ has the value $\mathrm{b}$, which is designated, and $q$ has the value $0$. So $p \wedge \neg p \not\models_{\mathrm{LP}} q$.
4. With the same valuation, $p \vee q$ and $\neg p$ are designated and $q$ is not. So disjunctive syllogism fails in $\mathrm{LP}$.
5. A [[contradictory theory in the logic of paradox|5D02W0KT45]] can be absolutely consistent: it does not prove every sentence.

### Non-examples

1. In [[Kripke's theory of truth|~1dd87a57]], $E$ and $A$ are disjoint, so no sentence is a glut. The liar is a [[gap|~c48c7e65]] there.
2. In a classical model, no sentence is both true and false.
3. In an LP fixed point, the [[truth-teller|~66f66b7a]] $\tau$ only needs the same value as $T(\ulcorner \tau \urcorner)$. Each of the three values meets this condition, so $\tau$ is not forced to be a glut.

### Basic properties

1. Every classical tautology is $\mathrm{LP}$-valid: a tautology takes value $1$ or $\mathrm{b}$ under every valuation. In particular $\models_{\mathrm{LP}} \varphi \vee \neg \varphi$.
2. Explosion fails, by Example 3.
3. Modus ponens for the material conditional fails: with $v(p) = \mathrm{b}$ and $v(q) = 0$, the sentences $p$ and $\neg p \vee q$ are designated, and $q$ is not.
4. If $\varphi$ is a glut, then $\neg \varphi$ is a glut, and $\varphi \wedge \neg \varphi$ is designated.
5. A compound sentence is a glut only if at least one component is a glut.

### History

The SEP entry names Priest (1984, 2006) as a leading advocate of the paraconsistent approach to the liar, with the logic $\mathrm{LP}$.
It states that the Kripke-style construction with overlapping extension and anti-extension was not given by Kripke.
It names Dowden (1984), Leitgeb (1999), Priest (1984, 2006), Visser (1984) and Woodruff (1984) for variants of it.

### Common errors

1. Thinking that a glut theory accepts every contradiction. It accepts a contradiction only for certain sentences, such as the liar.
2. Reading $\mathrm{LP}$ as $K_3$. They have the same tables, but different designated values, so different valid inferences.
3. Thinking that gluts avoid every revenge problem. The SEP entry explains that "the liar is neither true nor false" is equivalent, in such theories, to a contradiction about the liar.

## Explanations

### L1 human

The liar argument shows that the liar is true and also not true.
Most logicians reject this conclusion.
A glut theorist accepts it: the liar is both true and false.
To keep the rest of logic safe, the theory changes one rule.
From a contradiction, it no longer follows that every sentence is true.

### L2 human

1. In $\mathrm{LP}$, give the liar $\lambda$ the value $\mathrm{b}$.
2. Then $\neg \lambda$ has the value $\mathrm{b}$, and $\lambda \wedge \neg \lambda$ has the value $\mathrm{b}$, which is designated.
3. Let $q$ be the false sentence $0 = 1$, with value $0$.
4. The inference from $\lambda \wedge \neg \lambda$ to $q$ goes from a designated value to a non-designated value, so it is not valid.

The typical use is a transparent truth predicate with the full naive truth schema in the form of equal values.
The trap is to forget that modus ponens for the material conditional also fails, so the T-biconditionals are weak.

### L3 human

Gluts are the order dual of gaps in the four-element bilattice of first-degree entailment.
$\mathrm{LP}$ restricts first-degree entailment to the values $\mathbf{T}, \mathbf{B}, \mathbf{F}$, and $K_3$ restricts it to $\mathbf{T}, \mathbf{N}, \mathbf{F}$.
The glut fixed points of the jump are fixed points of the same Kripke operator on the four-valued pairs.
Philosophical dialetheism is broader than this formal notion; see [[dialethic logic|3P0FM0AQF3]].
