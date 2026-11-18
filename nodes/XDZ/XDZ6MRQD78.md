---
tag: XDZ6MRQD78
kind: example
name: Inquisitive disjunction
msc: ["03B65"]
topics: [CQM9SRN8PM]
audience: research
instance_of: [EX0ND8DCTN]
uses: [EX0ND8DCTN]
sources:
  - url: https://en.wikipedia.org/wiki/Inquisitive_semantics
    locator: Basic notions
  - book: isbn:9780198814795
    locator: Ciardelli, Groenendijk and Roelofsen, Inquisitive Semantics
---

## Example

Take two atoms $p$ and $q$ and write a world as $ab$, with $a$ the value of $p$ and $b$ the value of $q$.
We compare $p \vee q$ with its non-inquisitive projection $!(p \vee q) = \neg\neg(p \vee q)$ in [[inquisitive logic|EX0ND8DCTN]].

1. $s \models p$ iff $s \subseteq \set{11, 10}$, and $s \models q$ iff $s \subseteq \set{11, 01}$.
2. So $s \models p \vee q$ iff $s \subseteq \set{11, 10}$ or $s \subseteq \set{11, 01}$.
3. The alternatives of $p \vee q$ are $\set{11, 10}$ and $\set{11, 01}$. They overlap in $11$.
4. The informative content is $\set{11, 10, 01}$, the classical truth set of $p \vee q$.
5. The state $s = \set{10, 01}$ is inside the informative content, but $s \not\models p$ and $s \not\models q$. So $s \not\models p \vee q$.
6. $s \models \neg\neg(p \vee q)$ iff every world of $s$ makes $p \vee q$ true, iff $s \subseteq \set{11, 10, 01}$. So $\set{10, 01} \models !(p \vee q)$.
7. Hence $!(p \vee q) \not\models p \vee q$, while $p \vee q \models !(p \vee q)$ by steps 2 and 6.

The formula $p \vee q$ both informs, by ruling out $00$, and asks which of $p$ and $q$ holds.

## Remarks

The two disjunctions agree at every world: $\set{w} \models p \vee q$ iff $\set{w} \models !(p \vee q)$.
They differ only on states with two or more worlds, where support asks for a decision between the disjuncts.
For statements $\alpha$ and $\beta$, the formula $\alpha \vee \beta$ is a statement iff one of $\mathrm{info}(\alpha), \mathrm{info}(\beta)$ includes the other.
The same clause gives InqB the disjunction property: if $\varphi \vee \psi$ is valid, then $W$ supports $\varphi$ or $\psi$, and by persistence that disjunct is valid.

## Explanations

### L1 human

"John is in Paris or in London" can be said as information or asked as a question.
As information, it rules out his being elsewhere.
As a question, it also asks which of the two cities he is in.
Someone who knows only that he is in one of the two cities has the information but not the answer.

### L2 human

1. Find the states that support each disjunct: the subsets of $\set{11, 10}$ and of $\set{11, 01}$.
2. Their union is the meaning of $p \vee q$.
3. The state $\set{10, 01}$ makes $p \vee q$ true at each world but supports neither disjunct.

The typical use is to model alternative questions and the answers they allow.
A trap: the informative content of $p \vee q$ is classical, so a check at single worlds never shows the difference.
