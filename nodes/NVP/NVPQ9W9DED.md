---
tag: NVPQ9W9DED
kind: concept
name: Hybrid logic
aliases: [hybrid-modal-logic]
msc: ["03B45", "03B44"]
topics: [SPQVNPZDTB]
audience: research
uses: [C3RZY20ETK, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Hybrid_logic
    locator: lead section
---

## Summary

Let $i$ be a proposition that is true at exactly one world, so that $i$ works as a name.
Then $i \to \neg \lozenge i$ says "if I am the world called $i$, I do not see the world called $i$", that is, "I do not see myself".
On a frame this formula is valid exactly when no world sees itself, a property that no formula of plain [[modal logic|C3RZY20ETK]] defines.
Hybrid logic is modal logic with such names for worlds.

The names are called nominals: a nominal is an atom that every model makes true at exactly one world.
The satisfaction operator $@_i \varphi$ says that $\varphi$ holds at the world named $i$, wherever we stand.
The binder $\downarrow x . \varphi$ gives the name $x$ to the current world and then evaluates $\varphi$.
Pure formulas, the formulas built from nominals without propositional variables, define many frame properties, and every set of pure axioms gives a complete logic.

## Motivation

A modal formula is true or false at a world, but it cannot point at a world.
[[Kripke semantics|NGHWZ9Y7ZV]] gives an inside view of a model with no way to say "this world" or "the same world again".
Arthur Prior met this gap in [[tense logic|8XB117FKKV]].
A tense formula cannot say "at noon on that day", and it cannot say that time has no loop.
His idea was to treat an instant as a proposition that is true at that instant only.

Nominals keep the logic modal: they are formulas evaluated at worlds, not terms of a first-order language.
Yet they bring back enough of first-order logic to state equality of worlds.
The same idea appears in [[description logic|TXQ80B8ZSA]], where a nominal is a concept with one element and $@_i C$ asserts that the individual $i$ belongs to $C$.

## Notation

We use propositional variables $p, q$, nominals $i, j, k$, and state variables $x, y$.
The formulas of $\mathcal{H}(@, \downarrow)$ are given by $\varphi ::= p \mid i \mid x \mid \neg \varphi \mid \varphi \wedge \varphi \mid \lozenge \varphi \mid @_i \varphi \mid @_x \varphi \mid \downarrow x . \varphi$, with $\square \varphi = \neg \lozenge \neg \varphi$.
The fragment $\mathcal{H}(@)$ has no state variables and no binder.
A hybrid model $(W, R, V)$ has $V(p) \subseteq W$ for each variable and $V(i) = \{w\}$ for one world $w$, for each nominal.
An assignment $g$ sends state variables to worlds, and $g[x \mapsto w]$ changes $g$ at $x$ only.

The new truth clauses are these.
The nominal $i$ holds at $w$ when $V(i) = \{w\}$, and $x$ holds at $w$ when $g(x) = w$.
The formula $@_i \varphi$ holds at $w$ when $\varphi$ holds at the world $v$ with $V(i) = \{v\}$.
The formula $\downarrow x . \varphi$ holds at $w$ under $g$ when $\varphi$ holds at $w$ under $g[x \mapsto w]$.

## Remarks

### A first computation

The proof that $i \to \neg \lozenge i$ defines irreflexivity takes two lines, and [[the pure formula for irreflexivity|RK1RCGPAY6]] writes it out.
If no world sees itself, then at the world named $i$ every successor is another world, so $\lozenge i$ is false there.
If some $w$ has $w R w$, name it $i$, and $i \wedge \lozenge i$ holds at $w$.
Why can plain modal logic not do the same?
Modal validity is preserved under bounded morphic images, and [[the irreflexive successor chain maps onto a reflexive point|T3YJ84YDV4]].
So every modal formula valid on all irreflexive frames is also valid on a frame that is not irreflexive.

Other frame properties fall in the same way.
The formula $i \to \square \neg \lozenge i$ defines asymmetry: no successor of the world $i$ sees $i$ back.
The formula $i \to \square (\lozenge i \to i)$ defines antisymmetry: a successor that sees $i$ back must be $i$ itself.

### Two ways of naming

A nominal names a world fixed by the valuation, while $\downarrow x$ names whatever world we stand at.
In [[a three-world cycle|VAP32WQ8DY]], $@_i \lozenge j$ is true everywhere, because it only asks about the world named $i$.
The formula $\downarrow x . \lozenge \lozenge \lozenge x$ is true everywhere too, but for a different reason: each world lies on a cycle of length three.
So $\downarrow x . \lozenge x$ says "I see myself", a local property that no basic modal formula expresses at a world.

### Axioms and completeness

The axioms of $\mathcal{H}(@)$ add to $\mathsf{K}$ the axiom $\mathrm{K}$ and necessitation for each $@_i$, together with five axioms.
$$@_i p \leftrightarrow \neg @_i \neg p, \quad @_i i, \quad @_j @_i p \leftrightarrow @_i p, \quad i \wedge p \to @_i p, \quad \lozenge @_i p \to @_i p$$
There are two extra rules.
The Name rule infers $\varphi$ from $@_i \varphi$ when $i$ does not occur in $\varphi$.
The Paste rule infers $@_i \lozenge \varphi \to \theta$ from $@_i \lozenge j \wedge @_j \varphi \to \theta$, when $j$ differs from $i$ and occurs in neither $\varphi$ nor $\theta$.
With these rules, adding any set $\Sigma$ of pure axioms gives a logic that is strongly complete for the frames on which $\Sigma$ is valid.
So the irreflexive frames have the complete logic $\mathcal{H}(@)$ plus $i \to \neg \lozenge i$, which plain modal logic cannot give.

### Complexity and expressive power

Satisfiability for $\mathcal{H}(@)$ is [[PSPACE-complete|JWC9CE07Q2]], the same as for $\mathsf{K}$, so naming worlds costs nothing here.
The binder is expensive: satisfiability for $\mathcal{H}(\downarrow)$ on all frames is undecidable.
Every formula of $\mathcal{H}(@, \downarrow)$ translates into first-order logic, and the full language is equivalent to the bounded fragment, where each quantifier has the form $\exists y (x R y \wedge \dots)$.
Nominals also change the notion of sameness.
Two [[bisimilar|X27BR4YP2Y]] worlds can differ on $i$, so a bisimulation for $\mathcal{H}(@)$ must link worlds that agree on nominals and must link the two worlds named by each nominal.

### What it is not

A propositional variable is not a nominal.
On the irreflexive frame $u R v$, put $p$ true at both worlds; then $p \to \neg \lozenge p$ fails at $u$.
A valuation that makes a nominal true at two worlds is no hybrid valuation, and [[a nominal true at two worlds|NT4E0030NM]] shows the pure axioms failing in such a structure.
Nor is hybrid logic modal logic with a first-order predicate for the current world: the new symbols are formulas, and the syntax stays modal.

### Watch out

Truth in one model is not validity on a frame.
On the frame $W = \{u, v\}$ with $R = \{(u, v), (v, v)\}$, name $u$ by $i$.
Then $i \to \neg \lozenge i$ holds at both worlds, yet the frame has the loop $v R v$.
The formula defines irreflexivity only when you check all hybrid valuations, and the valuation $V(i) = \{v\}$ refutes it.
A second slip is to read $@_i \varphi$ as local: its truth does not depend on the current world, so $@_i \varphi \to \square @_i \varphi$ is valid.

### History

Arthur Prior used propositions true at a single instant in his tense logic of the 1960s, and his book Past, Present and Future (1967) discusses them.
Robert Bull studied tense logic with such propositions, and with quantification over them, in 1970.
In the 1990s Patrick Blackburn and others developed hybrid logic as a branch of modal logic with its own proof theory and model theory.

### Try it

First, which frame property does $i \to \square \square \neg i$ define?
It says that the world named $i$ is never two steps from itself, so the frame has no cycle $w R v R w$; a reflexive world counts, since $w R w R w$.

Second, is $@_i \lozenge p \to \lozenge p$ valid?
No: take $W = \{u, v\}$ with $u R v$, $p$ true at $v$, and $i$ naming $u$; at $v$ the antecedent holds and $\lozenge p$ fails, since $v$ has no successor.

## Explanations

### L1 human

In ordinary modal logic a statement is true or false at a place, but no statement can say "this is the place called home".
Hybrid logic adds such names.
A name is a statement that is true at exactly one place.
The formula $@_{\mathrm{home}} \varphi$ then says "at home, $\varphi$ is true", from wherever we are.
The arrow $\downarrow x$ says "call the place where I stand $x$", so that later we can ask whether we come back to $x$.

### L2 human

We show that the Back axiom $\lozenge @_i p \to @_i p$ is valid.
Fix a hybrid model, a world $w$, and let $v$ be the world with $V(i) = \{v\}$.
Assume $\lozenge @_i p$ holds at $w$, so $@_i p$ holds at some successor $u$ of $w$.
By the clause for $@$, this means that $p$ holds at $v$, and that fact does not mention $u$.
By the same clause, $@_i p$ holds at $w$.
The argument shows more: $@_i \varphi$ has the same truth value at every world of a model.
The typical use of the axioms is to move information between named worlds inside a derivation.
Watch out: the converse $@_i p \to \lozenge @_i p$ fails at a world with no successor.

### L3 human

Hybrid logic sits between modal logic and first-order logic.
The [[standard translation|YW6YGBMVQY]] sends $i$ to $x = c_i$, sends $@_i \varphi$ to $\varphi$ evaluated at $c_i$, and treats $\downarrow y$ as a restricted use of equality.
Pure formulas behave like first-order frame conditions.
The Name and Paste rules allow a Henkin-style canonical model in which each world has a name, and that is why pure axioms give strong completeness.
The language is also the natural home of labeled tableaux and sequent systems, since their labels are nominals.
