---
tag: KXTP4P3GHT
kind: concept
name: First-degree entailment
aliases: [first-degree-entailment-fde, belnap-dunn-logic, fde]
msc: ["03B50", "03B47"]
topics: [WZP584JQ06]
audience: research
uses: [DWYCKAKXZD, P7E926JK13, SZHA10A9X7]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section F
    note: adopted
    mention: wikipedia://en/76765067#26V4
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 2.3 True, False, Neither, and Both
  - url: https://plato.stanford.edu/entries/truth-values/
    locator: 3.1 The notion of a logical order
  - url: https://plato.stanford.edu/entries/logic-relevance/
    locator: 2. Semantics for Negation
  - url: https://en.wikipedia.org/wiki/Four-valued_logic
    locator: Belnap
inventory: [12BTK3EH85]
---

## Summary

Here are the four Belnap values, each the set of reports a sentence has received, placed in two orders at once.

| value | told true | told false | truth order | information order |
|---|---|---|---|---|
| $\mathbf{T} = \{T\}$ | yes | no | top | middle |
| $\mathbf{F} = \{F\}$ | no | yes | bottom | middle |
| $\mathbf{B} = \{T, F\}$ | yes | yes | middle | top |
| $\mathbf{N} = \emptyset$ | no | no | middle | bottom |

Drawn as a diamond, the truth order runs from $\mathbf{F}$ on the left to $\mathbf{T}$ on the right, and the information order runs from $\mathbf{N}$ at the bottom to $\mathbf{B}$ at the top.
Each order is a lattice, so the four values form a bilattice.
Conjunction is the meet in the truth order, so $\mathbf{N} \land \mathbf{B} = \mathbf{F}$: $\mathbf{B}$ brings a report of falsity, and $\mathbf{N}$ brings no report of truth.

*First-degree entailment* $\mathsf{FDE}$, also called Belnap-Dunn logic $\mathrm{BD}$, is the [[many-valued logic|DWYCKAKXZD]] of these values in $\neg$, $\land$ and $\lor$, with the values that contain $T$ designated; see [[the definition|AWEG5PR3GF]].
It contains [[strong Kleene logic|SZHA10A9X7]] and Priest's $\mathsf{LP}$ as three-valued extensions, it is not explosive, and it has no tautologies.

## Motivation

Belnap imagined a computer that collects facts from several users, with no guarantee that they agree.
One user may tell it that $p$ is true, and another that $p$ is false.
In classical logic $p$ and $\neg p$ entail every $q$, so one conflict would spoil all the other data.
$\mathsf{FDE}$ records for each sentence the set of values it was told.
A conflict about $p$ then says nothing about an unrelated $q$, and a sentence nobody mentioned simply has no report.

## Notation

The four values are written $\mathbf{T}$, $\mathbf{F}$, $\mathbf{B}$ (both) and $\mathbf{N}$ (neither), and also $\mathsf{t}$, $\mathsf{f}$, $\mathsf{b}$, $\mathsf{n}$.
The algebra $\langle \mathbf{4}, \neg, \land, \lor \rangle$ is the four-element De Morgan algebra $\mathbf{DM}_4$.
The structure with both orders is often called the bilattice $\mathrm{FOUR}_2$.

## Remarks

### Rules that hold

De Morgan's laws and double negation hold: $\neg \neg p \models p$, $p \models \neg \neg p$ and $\neg(p \land q) \models \neg p \lor \neg q$.
Conjunction elimination $p \land q \models p$ and addition $p \models p \lor q$ hold, as in classical logic.
Three definitions of consequence give the same relation: preserve "contains $T$", preserve "does not contain $F$", or compare the values in the truth order.

### Rules that fail

[[Explosion and excluded middle fail|5DFTBDQAR4]], with the value $\mathbf{B}$ for the first and $\mathbf{N}$ for the second.
$\mathsf{FDE}$ has no tautologies, because the valuation with every variable $\mathbf{N}$ gives every formula the value $\mathbf{N}$.
Classical logic is not $\mathsf{FDE}$, since $p \lor \neg p$ is a classical law.

### Two three-valued extensions

Every $\mathsf{FDE}$-valid inference is valid in $\mathsf{K}_3$ and in $\mathsf{LP}$, since their matrices are submatrices of the four-valued one.
Dropping $\mathbf{B}$ gives $\mathsf{K}_3$, and [[explosion separates it from FDE|QZ9FRRH7Y1]].
Dropping $\mathbf{N}$ gives $\mathsf{LP}$, and excluded middle separates it from $\mathsf{FDE}$.

### Worlds instead of values

[[The Routley star semantics|ZV62Y5X00V]] evaluates $\neg A$ at a partner world $a^*$ and gives the same consequence relation.
So one can build counter-models either from the four values or from pairs of worlds.

### Watch out

Do not take $\mathbf{B}$ as the top of the truth order.
In the truth order $\mathbf{T}$ is the top, $\mathbf{F}$ is the bottom, and $\mathbf{B}$ and $\mathbf{N}$ are incomparable.
Do not designate only $\mathbf{T}$, because that gives a different logic, the exactly true logic.
Do not expect $\mathbf{N} \land \mathbf{B} = \mathbf{N}$; it is $\mathbf{F}$.

### History

Anderson and Belnap studied first-degree entailment as the fragment of their logic of entailment without nested arrows.
Routley and Routley gave the star semantics for its negation in 1972.
Dunn gave the four-valued semantics in 1976.
Belnap presented it in 1977 as a logic for computers that handle incomplete and inconsistent information.

### Try it

First, compute $\mathbf{B} \lor \mathbf{N}$.
It is told true, because $\mathbf{B}$ is, and it is not told false, because $\mathbf{N}$ is not, so the value is $\mathbf{T}$.

Second, is $p \land \neg p \models q \lor \neg q$ valid in $\mathsf{FDE}$?
No: take $p = \mathbf{B}$ and $q = \mathbf{N}$, so the premise is $\mathbf{B}$ and the conclusion is $\mathbf{N}$.

## Explanations

### L1 human

Think of a database that collects reports.
About each fact it may have heard "true", "false", both, or nothing.
A conclusion follows when every way of hearing "true" about the premises also gives "true" for the conclusion.
A conflict about one fact does not make every other fact true.

### L2 human

To compute a value, track truth and falsity separately.
$A \land B$ is told true iff both parts are told true, and it is told false iff one part is told false.
$\neg A$ is told true iff $A$ is told false, and the other way around.
The typical use is to find counter-models with $\mathbf{B}$ for explosion and with $\mathbf{N}$ for excluded middle.
Watch out: $\land$ is the meet of the truth order, not of the information order.

### L3 human

$\mathsf{FDE}$ is the logic of order of the De Morgan algebra $\mathbf{DM}_4$, and also its matrix logic with the designated filter $\{\mathbf{T}, \mathbf{B}\}$.
Inclusion of subsets of $\{T, F\}$ is the information order, and the truth order is a second lattice on the same set; together they form the bilattice $\mathrm{FOUR}_2$.
The Routley star semantics, with an involution on worlds, extends to the [[Routley-Meyer semantics|H4Z8J0KMAY]] of relevance logics.
