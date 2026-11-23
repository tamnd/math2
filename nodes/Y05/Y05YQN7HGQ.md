---
tag: Y05YQN7HGQ
kind: concept
name: AGM belief revision
msc: ["03B42", "68T27"]
topics: [CQM9SRN8PM]
audience: research
uses: [09K9MWD2QQ, CT4FZ84V45, 0VABYWJWH9]
aliases: [agm-postulates, belief-revision]
sources:
  - url: https://en.wikipedia.org/wiki/Belief_revision
    locator: The AGM postulates
  - url: https://en.wikipedia.org/wiki/Belief_revision
    locator: Contraction
  - url: https://en.wikipedia.org/wiki/Belief_revision
    locator: Conditions equivalent to the AGM postulates
  - book: isbn:9780262071093
    locator: Gärdenfors, Knowledge in Flux
---

## Summary

AGM belief revision is the theory of how a rational agent changes her beliefs when new information contradicts them: accept the news, stay consistent, and give up as little as possible.
Here is the standard first case.
You believe $p$ ("Tweety is a bird") and $q$ ("Tweety flies"), and you learn $\neg p$.
If dropping one belief is more plausible than dropping both, the revised beliefs are $\neg p$ and $q$.

A belief set is a set $K$ of formulas of [[propositional logic|09K9MWD2QQ]] that is closed under consequence, $K = \mathrm{Cn}(K)$, as in [[deductive closure|CT4FZ84V45]].
There are three operations on it.
Expansion is $K + \varphi := \mathrm{Cn}(K \cup \{\varphi\})$, contraction $K \div \varphi$ gives up $\varphi$, and revision $K * \varphi$ accepts $\varphi$ and stays consistent.
An AGM revision operator is a map $\varphi \mapsto K * \varphi$ that satisfies the eight postulates listed under Remarks.
Revision and contraction determine each other by two identities.
$$K * \varphi = (K \div \neg\varphi) + \varphi \quad \text{(Levi)}, \qquad K \div \varphi = K \cap (K * \neg\varphi) \quad \text{(Harper)}$$

## Motivation

Adding contradicting news by expansion gives an inconsistent belief set, from which everything follows.
So the agent must first give up some old beliefs, and she should give up as little as possible.
Logic alone does not say which beliefs to drop: after learning $\neg(p \wedge q)$ she can drop $p$, drop $q$, or suspend judgment.

The AGM postulates do not choose one method.
They list the properties that every rational method should have.
The representation theorems then show that the methods with these properties are exactly those that minimize change with respect to a plausibility ranking of possible worlds.
The theory is used in philosophy of science, in the maintenance of databases and knowledge bases, and in artificial intelligence.

## Notation

We write $K_\bot$ for the inconsistent belief set, the set of all formulas, and $\mathrm{Mod}(K)$ for the set of valuations that satisfy $K$.
Contraction is written $\div$, $-$ or $\dot{-}$ in different books.
The labels $K{*}1$ to $K{*}8$ and $K{\div}1$ to $K{\div}8$ name the revision and contraction postulates, and the first six of each are the basic postulates.
A plausibility ranking is a total preorder $\le$ on valuations, where $x \le y$ means "$x$ is at least as plausible as $y$".
With two atoms we write a valuation as $ab$, where $a$ is the value of $p$ and $b$ the value of $q$.

## Remarks

### The eight postulates

1. Closure: $K * \varphi = \mathrm{Cn}(K * \varphi)$.
2. Success: $\varphi \in K * \varphi$.
3. Inclusion: $K * \varphi \subseteq K + \varphi$.
4. Vacuity: if $\neg\varphi \notin K$, then $K + \varphi \subseteq K * \varphi$.
5. Consistency: if $\varphi$ is consistent, then $K * \varphi$ is consistent.
6. Extensionality: if $\vdash \varphi \leftrightarrow \psi$, then $K * \varphi = K * \psi$.
7. Superexpansion: $K * (\varphi \wedge \psi) \subseteq (K * \varphi) + \psi$.
8. Subexpansion: if $\neg\psi \notin K * \varphi$, then $(K * \varphi) + \psi \subseteq K * (\varphi \wedge \psi)$.

Postulates 3 and 4 together say that news consistent with $K$ is simply added.
Postulates 7 and 8 control revision by a conjunction, and they are what ties a revision operator to one ranking.

### Revising {p, q} by not p

Let $K = \mathrm{Cn}(p \wedge q)$, so $\mathrm{Mod}(K) = \{11\}$, and rank the valuations as follows, most plausible first.
$$11 \; < \; 10 \approx 01 \; < \; 00$$
To revise by $\varphi$, take the most plausible models of $\varphi$ and believe what holds in all of them.
The models of $\neg p$ are $01$ and $00$, and $01$ is more plausible.
So $\mathrm{Mod}(K * \neg p) = \{01\}$, and $K * \neg p = \mathrm{Cn}(\neg p \wedge q)$.
Check: success holds since $01$ satisfies $\neg p$, and consistency holds since $\{01\}$ is nonempty.

The same ranking gives $K * \neg(p \wedge q) = \mathrm{Cn}(p \leftrightarrow \neg q)$, because the models $10$ and $01$ are tied.
[[An AGM revision on two atoms|CC604TAP5T]] works these cases and checks postulates 7 and 8.
[[The Levi and Harper identities|J64RZ8B4Q5]] compute the contraction $K \div p = \mathrm{Cn}(q)$ from the same ranking.

### Rankings are exactly AGM revisions

For a finite language, an operator satisfies the eight postulates for $K$ if and only if it selects the minimal models in a total [[preorder|0VABYWJWH9]] whose minimal elements are the models of $K$.
This is the [[representation theorem|KV8J5H7KF2]].
For an arbitrary language, Grove showed that AGM revisions are given by systems of spheres of maximal consistent sets centered on the models of $K$.
On the contraction side, Alchourrón, Gärdenfors and Makinson showed that the contractions with the six basic postulates are exactly the partial meet contractions.
These select among the maximal subsets of $K$ that do not imply $\varphi$.

Full meet revision is the extreme case.
It ranks all models of $K$ first and puts every other valuation in one tie.
So $K * \varphi = K + \varphi$ when $\neg\varphi \notin K$, and $K * \varphi = \mathrm{Cn}(\varphi)$ otherwise, and all eight postulates hold.

### What it is not

Expansion is not an AGM revision: $\mathrm{Cn}(p) + \neg p$ is inconsistent, against postulate 5, as [[expansion is not revision|SQWDB0F00W]] shows.
The operator $K * \varphi := \mathrm{Cn}(\varphi)$ for all $\varphi$ is not one either.
It forgets $q$ when $\mathrm{Cn}(p \wedge q)$ is revised by $p$, against postulate 4.
Finally, with $K = \mathrm{Cn}(p \wedge q)$ and a third atom $r$, an operator with $K * \neg p = \mathrm{Cn}(\neg p)$ and $K * (\neg p \wedge q) = \mathrm{Cn}(\neg p \wedge q \wedge r)$ breaks postulate 7, since $r \notin \mathrm{Cn}(\neg p \wedge q)$.

### Watch out

The postulates do not fix one revision operator.
On the ranking above, $\neg(p \wedge q)$ gives $p \leftrightarrow \neg q$, while the ranking $11 < 10 < 01 < 00$ gives $p \wedge \neg q$, and both operators are AGM revisions.
The choice between them is the choice of a ranking.
The postulates also say nothing about revising twice, since the ranking belongs to $K$ alone, and iterated revision needs extra postulates.
Revision is also not update: update models a change in the world, not new information about a fixed world, and it obeys other postulates.

### History

Alchourrón, Gärdenfors and Makinson published the postulates and the partial meet construction in 1985.
Grove gave the sphere semantics in 1988, and Gärdenfors set out the theory in his book Knowledge in Flux (1988).
Katsuno and Mendelzon gave the form with total preorders on valuations in 1991.
Gärdenfors's [[triviality theorem|WMZ1QP7KQY]] of 1986 showed a limit of the theory when it is joined with the Ramsey test for conditionals.

### Try it

First, on the ranking above, compute $K * \neg q$.
The models of $\neg q$ are $10$ and $00$, the more plausible is $10$, so $K * \neg q = \mathrm{Cn}(p \wedge \neg q)$.

Second, compute $K * (p \vee q)$.
The news is consistent with $K$ and $11$ is its most plausible model, so $K * (p \vee q) = K$, as postulates 3 and 4 demand.

## Explanations

### L1 human

You believe that Tweety is a bird and that Tweety flies.
Then you learn that Tweety is not a bird after all.
You should drop "Tweety is a bird", and keep as much as you can of the rest, for example "Tweety flies" (perhaps Tweety is a toy plane).
AGM theory lists rules that every sensible way of doing this follows.
One rule says that the news is always accepted.
Another says that if the news does not contradict you, you just add it.

### L2 human

We build a revision operator for a small knowledge base from scratch.
The base says $p \wedge q$, and we decide that losing one fact is more plausible than losing both, and that losing $q$ and losing $p$ are equally plausible.
That decision is the ranking $11 < 10 \approx 01 < 00$.
Now news $\neg p \vee \neg q$ arrives, with models $10$, $01$ and $00$.
The most plausible are $10$ and $01$, so the new base is $p \leftrightarrow \neg q$: exactly one fact survives, and we do not know which.
This is the typical use of the theory: choose a ranking once, and every revision follows from it by "keep the most plausible models".
Watch out that belief sets are infinite, so in practice one stores a single formula $\kappa$ with $K = \mathrm{Cn}(\kappa)$.

### L3 human

A total preorder of worlds is the same structure as a system of spheres in [[conditional logic|ZGYG7WN7EC]], and the Ramsey test reads $(\varphi > \psi) \in K$ as $\psi \in K * \varphi$.
Postulates 7 and 8 match the laws of rational nonmonotonic consequence, so AGM revision and nonmonotonic logic are two views of one structure.
Dynamic epistemic logic brings belief change into the object language with plausibility models, where revision is an action that reorders worlds.
Iterated revision, in the work of Darwiche and Pearl, and Spohn's ranking functions extend the theory to sequences of changes.
