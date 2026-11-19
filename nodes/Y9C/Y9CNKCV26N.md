---
tag: Y9CNKCV26N
kind: example
name: The polar question in inquisitive logic
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

Take two atoms $p$ ("it rains") and $q$ ("it is cold").
Write a world as $ab$, with $a$ the value of $p$ and $b$ the value of $q$, so $W = \set{11, 10, 01, 00}$.
We compute the meaning of $?p = p \vee \neg p$ in [[inquisitive logic|EX0ND8DCTN]].

1. $s \models p$ iff $s \subseteq \set{11, 10}$.
2. $s \models \neg p$ iff no world of $s$ makes $p$ true, iff $s \subseteq \set{01, 00}$.
3. So $s \models ?p$ iff $s \subseteq \set{11, 10}$ or $s \subseteq \set{01, 00}$.
4. The alternatives of $?p$ are the maximal supporting states, $\set{11, 10}$ and $\set{01, 00}$.
5. The informative content is $\set{11, 10} \cup \set{01, 00} = W$. So $?p$ rules out no world, and it is a question.
6. $W \not\models ?p$, because $W$ contains both $10$ and $00$.

Now compare $?p$ with $?(p \wedge q)$.

7. $s \models ?(p \wedge q)$ iff $s \subseteq \set{11}$ or $s \subseteq \set{10, 01, 00}$.
8. The state $\set{10}$ supports $?p$ and $?(p \wedge q)$, while $\set{11, 10}$ supports $?p$ but not $?(p \wedge q)$.
9. So $?p \not\models ?(p \wedge q)$: knowing whether it rains does not settle whether it is cold and rains.
10. But $?p \wedge ?q \models ?(p \wedge q)$. A state that supports $?p$ and $?q$ fixes the value of both atoms, so it has at most one world, and it decides $p \wedge q$.

## Remarks

The polar question is the simplest formula that is supported by some states and true at every world but not valid.
Its two alternatives are disjoint and cover $W$, which is typical of polar questions; an alternative question such as $p \vee q$ can have overlapping alternatives.
The entailment $?p \wedge ?q \models ?(p \wedge q)$ expresses that the answer to the second question is a function of the answers to the first two.

## Explanations

### L1 human

The question "does it rain?" has two possible answers, "yes" and "no".
Any information that gives one of the answers settles the question.
Knowing only that it is cold does not settle it.
Knowing whether it rains and whether it is cold settles the question "does it rain and is it cold?".

### L2 human

1. List the four worlds and mark the states that decide $p$.
2. The supporting states are exactly the subsets of the "yes" block and of the "no" block.
3. The full state lies in neither block, so it does not support $?p$.

The typical use is to check a dependency by testing all states.
A trap: $?p$ is true at every world, but truth at a world says only that the world gives some answer, not that the state does.
