---
tag: RJNDEG07R1
kind: concept
name: Hintikka set
aliases: [downward-saturated-set, model-set]
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
uses: [086QKPF0A6, DKFGQTRYZE, 6D3WA7N2W4, NCDZ969V7X, 983GZBQYT4, 2RBQPV02AS, QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Hintikka_set
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Hintikka_set
    locator: Propositional Hintikka sets
---

## Summary

A Hintikka set is a set of sentences in which every complex sentence comes with simpler sentences that explain why it is true.
Such a set always describes a model, and that is why it is the bridge from a failed proof search to a countermodel.
Here is a small one, in the language with one constant $c$ and unary relation symbols $P$ and $Q$:
$$H = \{ \exists x\, (P(x) \wedge \neg Q(x)),\ P(c) \wedge \neg Q(c),\ P(c),\ \neg Q(c) \}.$$
The existential sentence has the named witness $c$, the conjunction has both parts, and the literals $P(c)$ and $\neg Q(c)$ do not clash.
Check: in the one-element structure with $P = \{ c \}$ and $Q = \varnothing$, all four sentences are true.

In general, let $L$ be a [[first-order|086QKPF0A6]] language without equality with at least one constant symbol, and use the $\alpha, \beta, \gamma, \delta$ types of [[semantic tableaux|WGWBBVE8GX]].
A set $H$ of [[sentences|DKFGQTRYZE]] of $L$ is a Hintikka set for $L$ when it satisfies five conditions.

1. No atomic sentence $A$ has both $A \in H$ and $\neg A \in H$.
2. If $\alpha \in H$, then $\alpha_1 \in H$ and $\alpha_2 \in H$.
3. If $\beta \in H$, then $\beta_1 \in H$ or $\beta_2 \in H$.
4. If $\gamma \in H$, then $\gamma(t) \in H$ for every closed [[term|6D3WA7N2W4]] $t$ of $L$.
5. If $\delta \in H$, then $\delta(t) \in H$ for at least one closed term $t$ of $L$.

[[Hintikka's lemma|2A6QP78XN3]] says that every Hintikka set is [[satisfiable|QN7M1JCGT9]].

## Motivation

A completeness proof must build a [[structure|983GZBQYT4]] out of syntax alone.
The natural material is a set of sentences that says enough to fix a model.
Such a set must contain a reason for each of its complex members, in the form of simpler members.
For $\varphi \wedge \psi$ the reason is $\varphi$ and $\psi$, for $\varphi \vee \psi$ it is one of them, for $\exists x\, \varphi$ it is a named witness, and for $\forall x\, \varphi$ it is every instance.
If the reasons go all the way down to atomic sentences and do not clash there, then the atoms fix a structure, and the reasons carry truth back up.

An open branch of a finished tableau has exactly this downward closure, because the tableau rules add the reasons one by one.
So Hintikka sets connect the tableau method to models.
They differ from the maximal consistent sets of Henkin's proof of the [[model existence theorem|G0DTR159RN]], since a Hintikka set can be small and needs no notion of proof.

## Notation

We write $H$ for a Hintikka set and $T_L$ for the set of closed terms of $L$.
Condition 4 depends on $L$, so we say "Hintikka set for $L$" when the language matters.
In tableau proofs, $L$ is the language $L^{+}$ with the parameters, or the language of the symbols on one branch.
Hintikka called these sets model sets, and the names Hintikka set and downward saturated set are also common.
Some books state condition 1 for all sentences, add $\top$ and $\bot$, or use the signs $T$ and $F$ in place of negation; the idea stays the same.

## Remarks

### Hintikka sets you can check

The empty set is a Hintikka set, because each condition speaks only about members of $H$.
A set of literals with no clash, such as $\{ P(c), \neg Q(c) \}$, is one as well, since conditions 2 to 5 have no cases.

The [[finite Hintikka set with all four rule types|KMH75NABY0]] adds $\forall x(P(x) \vee Q(x))$ and its instance to the set of the Summary.
The $\gamma$ sentence needs only one instance there, because $c$ is the only closed term.

With a function symbol the picture changes.
In the [[infinite Hintikka set over 0, s(0), s(s(0)), …|F75D6CZ5EC]], condition 4 asks for an instance at each of infinitely many closed terms.

A whole theory gives another example.
If every element of an $L$-structure $\mathcal{M}$ is the value of a closed term, then the set of all $L$-sentences true in $\mathcal{M}$ is a Hintikka set.
Condition 5 holds because each witness of $\exists x\, \varphi$ has a name $t$, and then $\varphi[t/x]$ is true.

### Sets that are not Hintikka sets

The [[satisfiable set that is not a Hintikka set|RV5VSDKNBX]], $\{ \exists x\, P(x), \forall x\, \neg Q(x) \}$, fails conditions 4 and 5.
It is true in a structure, but it does not name a witness or list the instance $\neg Q(c)$.

The set $\{ P(c), \neg P(c) \}$ fails condition 1, and it has no model.
The set $\{ P(c) \vee Q(c) \}$ fails condition 3, because neither part is in it.
With a unary function symbol $f$, the set $\{ \forall x\, P(x), P(c) \}$ fails condition 4, because $P(f(c))$ is missing.

### The rules you can use

The main fact is [[Hintikka's lemma|2A6QP78XN3]]: every Hintikka set has a model whose domain is $T_L$, a [[Herbrand structure|HKW429DSDK]].
From it, a Hintikka set contains no pair $\chi, \neg\chi$ for any sentence $\chi$, since its model would make both true.

A Hintikka set need not be complete.
The set $\{ P(c) \}$ contains neither $Q(c)$ nor $\neg Q(c)$, and the model of the lemma makes $Q(c)$ false.
It need not be closed under consequence either, since $\{ P(c) \}$ does not contain $P(c) \vee Q(c)$.

The union of a chain of Hintikka sets for $L$ is a Hintikka set for $L$, because each condition involves at most two members, and they lie in one set of the chain.
Intersections can fail.
Both $\{ P(c) \vee Q(c), P(c) \}$ and $\{ P(c) \vee Q(c), Q(c) \}$ are Hintikka sets, but their intersection $\{ P(c) \vee Q(c) \}$ fails condition 3.
With the equality symbol, two more closure conditions are needed, as the remarks of [[Hintikka's lemma|2A6QP78XN3]] explain.

### Watch out

A Hintikka set is closed downward, from a sentence to its parts, and not upward.
It does not have to contain $\varphi \vee \psi$ when it contains $\varphi$.

Condition 4 ranges over all closed terms of the language, not only those that occur in $H$.
With the constants $c$ and $d$, the set $\{ \forall x\, P(x), P(c) \}$ fails, because $P(d)$ is missing.

Condition 1 is not the same as "consistent".
It is a check on atomic sentences only, and Hintikka's lemma is what turns it into satisfiability.

### History

Jaakko Hintikka introduced model sets in 1955.
Evert Willem Beth introduced semantic tableaux in the same year, independently.
Raymond Smullyan's book First-Order Logic (1968) used the name Hintikka set and proved Hintikka's lemma in the uniform notation.

### Try it

First, is $\{ P(c) \to Q(c), \neg P(c) \}$ a Hintikka set for the language with $c$, $P$ and $Q$?
Yes: the $\beta$ sentence $P(c) \to Q(c)$ has its first component $\neg P(c)$ in the set, and there is no clash.

Second, add $\forall x\, P(x)$ to that set.
Is the result contained in any Hintikka set for the same language?
No: condition 4 would force $P(c)$, which clashes with $\neg P(c)$.

## Explanations

### L1 human

Imagine a list of facts about a small world, such as "every ball is red or blue" and "some ball is red and not blue".
The list is a Hintikka set when every complicated fact comes with simple facts that explain it.
For "some ball is red and not blue", the list must name a ball, say ball $c$, and say "ball $c$ is red" and "ball $c$ is not blue".
For "every ball is red or blue", it must say "ball $c$ is red or blue" for each named ball, and then one of the two parts.
At the bottom, the simple facts must not contradict each other.
Then we can build the world from the simple facts, and every fact on the list is true in it.

### L2 human

We check that $H = \{ P(c) \wedge \neg P(d),\ P(c),\ \neg P(d),\ \exists x\, \neg P(x) \}$ is a Hintikka set for the language with the constants $c, d$ and the unary symbol $P$.

1. Condition 1: the only atom in $H$ is $P(c)$, and the only negated atom is $\neg P(d)$, so there is no clash.
2. Condition 2: the $\alpha$ sentence $P(c) \wedge \neg P(d)$ has both components in $H$.
3. Conditions 3 and 4: $H$ has no $\beta$ sentence and no $\gamma$ sentence.
4. Condition 5: the $\delta$ sentence $\exists x\, \neg P(x)$ has the instance $\neg P(d)$, with $t = d$.

The model of Hintikka's lemma has domain $\{ c, d \}$ and $P = \{ c \}$, and each member of $H$ is true in it.
The typical use is the last step of a completeness proof: build a Hintikka set that contains the given set, and let the lemma supply the model.
Watch out for condition 4: adding $\forall x\, P(x)$ to $H$ would require $P(d)$, which clashes with $\neg P(d)$.

### L3 human

Hintikka sets are the semantic half of the analytic proof systems.
A proof system has a cut-free completeness proof when every failed proof search produces a Hintikka set.
This pattern works for tableaux, for the cut-free [[sequent calculus|W72CA3R9MP]], and for many modal and intuitionistic systems, where the Hintikka sets become the worlds of a Kripke model.
In model theory the same idea appears as the term model of the Henkin construction.
The model of Hintikka's lemma is a [[Herbrand structure|HKW429DSDK]], the setting of [[Herbrand's theorem|VZ21F10WRS]].
With the equality symbol, the term model must be divided by a [[congruence relation|DCSXXT4SER]], which leads to the [[rules for equality|Y90Z13AXY8]].
