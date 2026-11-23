---
tag: D3ZS6WHPM1
kind: concept
name: Existential graphs
msc: ["03B05", "03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: ug1
uses: [09K9MWD2QQ, 086QKPF0A6, 029JBBF693, 025YZN3VJW, QPD3X471Q1]
sources:
  - url: https://en.wikipedia.org/wiki/Existential_graph
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Charles_Sanders_Peirce
    locator: lead section
---

## Summary

Existential graphs are Peirce's way of doing logic with drawings: a formula is a picture on a sheet of paper, and a proof is a sequence of small changes to the picture.
Everything rests on two devices, writing things side by side to assert them together and drawing a closed curve around something to deny it.

Write $P$ and $Q$ on the sheet side by side, and you assert "$P$ and $Q$".
Draw a closed curve, called a cut, around $Q$, and you assert "$P$ and not $Q$".
Draw one cut around $P$ and a second cut around $Q$ inside the first, and you assert "not ($P$ and not $Q$)", which is "if $P$ then $Q$".

In exact terms, the alpha system has propositional letters, juxtaposition for [[conjunction|025YZN3VJW]] and cuts for [[negation|029JBBF693]], and it is equivalent to classical [[propositional logic|09K9MWD2QQ]].
The beta system adds lines of identity, heavy lines that stand for individuals and join the predicates true of them, and it is equivalent to [[first-order logic|086QKPF0A6]] with identity.
Proofs in both use five [[rules of inference|QPD3X471Q1]]: erasure, insertion, iteration, deiteration and double cut.
Which rules may act at a place depends only on how many cuts enclose it.

## Motivation

Algebraic notation hides the structure of a formula in brackets and in the order of symbols.
Peirce wanted a notation in which the logical form can be seen at once and a proof is a sequence of visible steps.
"And" and "not" are enough for classical propositional logic, so one way to put assertions together and one way to deny an assertion are enough.
For quantifiers you need a way to say that an individual exists and to tie several statements to it.
A line drawn between predicates does both, and it also shows identity: two predicates on one line are about the same individual.

## Notation

In text a cut is a pair of square brackets, so $[P]$ is a cut around $P$, and juxtaposition is a space.
The area of a cut is the part of the plane inside it and outside every cut inside it.
The depth of an area is the number of cuts that enclose it, so the sheet has depth $0$.
An area of even depth is positive, and an area of odd depth is negative.

An alpha graph $G$ translates into a formula $\tau(G)$ of propositional logic as follows.

| Graph $G$ | Formula $\tau(G)$ |
|---|---|
| the empty graph | $\top$ (true) |
| a letter $P$ | $P$ |
| $G \ H$ (side by side) | $\tau(G) \land \tau(H)$ |
| $[G]$ | $\neg \tau(G)$ |

So $[P \ [Q]]$ is $\neg(P \land \neg Q)$, equivalent to $P \to Q$; Peirce called this shape a scroll.
The graph $[[P] \ [Q]]$ is $\neg(\neg P \land \neg Q)$, equivalent to $P \lor Q$, and an empty cut $[\ ]$ is $\neg \top$, false.

In a beta graph a line of identity stands for an individual, and predicate letters sit at its ends.
A line is read as an existential quantifier at the depth of its outermost part.
A line from $P$ on the sheet reads $\exists x\, P(x)$, and the same line inside a cut reads $\neg \exists x\, P(x)$.
A line that starts at $S$ inside one cut and runs into a second cut, inside the first, to reach $P$ reads $\neg \exists x\,(S(x) \land \neg P(x))$, that is, $\forall x\,(S(x) \to P(x))$.

## Remarks

### The five rules

Erasure removes any graph from a positive area.
Insertion adds any graph to a negative area.
Iteration copies a graph into its own area or into any area enclosed by it, and deiteration removes such a copy.
Double cut draws or removes two cuts with nothing between them, in any area.

The rules are sound: read through $\tau$, each step yields a graph that the previous one implies.
Erasure works because $A \land B$ implies $A$, and a negative area reverses the direction of implication, which is why insertion is allowed there instead.
Iteration and deiteration are inverse to each other, and the double cut can be drawn and removed, so those rules give equivalent graphs.

### Proofs at work

[[Modus ponens in the alpha graphs|1X5X03DYTA]] goes from $P$ and $[P \ [Q]]$ to $Q$ in three steps: deiteration, double cut and erasure.
[[Darii in the beta graphs|DXG8B0NGHC]] goes from "every $M$ is $P$" and "some $S$ is $M$" to "some $S$ is $P$" by joining lines of identity and removing a double cut.
The law of excluded middle $[[P] \ [[P]]]$ comes from the empty sheet by a double cut, an insertion and an iteration, as in the L2 explanation.
In beta, one line with $P$ at one end and $Q$ at the other reads $\exists x\,(P(x) \land Q(x))$, while two separate lines from $P$ and from $Q$ read $\exists x\, P(x) \land \exists y\, Q(y)$.

### Completeness

A theorem is a graph derived from the empty sheet.
Every theorem of alpha is a tautology and every tautology is a theorem of alpha, so alpha is sound and complete for classical propositional logic.
Beta, with the same five rules extended to lines of identity, is sound and complete for first-order logic with identity in a language of relation symbols.

### What is not an existential graph

An [[Euler diagram|E9GW8MRT8Z]] shows classes as regions, with "all $S$ are $P$" as a region inside a region, but it has no cut, no line of identity and no rules of transformation.
A [[Venn diagram|0KCT6DPXJK]] with shaded regions is not one either: shading says that a class is empty, and the diagram cannot express a relation between two individuals.
A truth table for $P \to Q$ lists valuations; it asserts nothing on a sheet and has no derivations.

### Watch out

Do not erase in a negative area.
From $[P \ Q]$, "not both $P$ and $Q$", you may not erase $Q$, because $[P]$, "not $P$", does not follow.
The double cut rule applies only when nothing lies between the two cuts; $[P \ [Q]]$ is not equivalent to $P \ Q$.
A line of identity is not "for all" by itself.
It is an existential quantifier at the depth of its outermost part, and "for all" arises from a line in a cut whose other end lies in a second cut.

### History

Charles Sanders Peirce developed the existential graphs from the late 1890s into the first years of the twentieth century.
He divided them into alpha, beta and gamma parts and stated their rules of inference.
He left the gamma part, with modal notions and graphs about graphs, unfinished.
The equivalence of alpha with propositional logic and of beta with first-order logic with identity was proved by later logicians, who also made Peirce's rules exact.

### Try it

Translate $[P \ [Q] \ [R]]$ into a formula.
It is $\neg(P \land \neg Q \land \neg R)$, which is equivalent to $P \to (Q \lor R)$.

Derive $P$ from the two graphs $[[P] \ [Q]]$ and $[Q]$ on the sheet.
The $[Q]$ inside the outer cut is a copy of the $[Q]$ on the sheet, so deiteration removes it and leaves $[[P]]$.
The double cut rule turns $[[P]]$ into $P$, and erasure removes $[Q]$ from the sheet, which is positive.

## Explanations

### L1 human

Imagine a large sheet of paper on which we write only things that we claim are true.
If we write "it rains" and "it is cold" next to each other, we claim both.
If we draw a loop around "it rains", we claim that it does not rain.
A big loop that contains "it rains" and a smaller loop around "it is cold" says "if it rains, then it is cold".
Proofs use a few moves, such as erasing something that is not inside any loop, or removing two loops that sit directly one inside the other.
Peirce designed the moves so that a true drawing can only become another true drawing.

### L2 human

We derive the law of excluded middle $P \lor \neg P$ from the empty sheet.

1. Start with the empty sheet, the only axiom.
2. Draw a double cut around the empty graph, giving $[[\ ]]$, which the double cut rule allows in any area.
3. The area between the two cuts has depth $1$, so it is negative, and insertion puts $[P]$ there: $[[P] \ [\ ]]$.
4. The inner cut lies inside the area that holds $[P]$, so iteration copies $[P]$ into it: $[[P] \ [[P]]]$.
5. By the translation, $[[P] \ [[P]]]$ is $\neg(\neg P \land \neg\neg P)$, which is equivalent to $P \lor \neg P$.

The pattern is common: a double cut makes room, insertion in a negative area adds what you need, and iteration copies it to where it is used.
The trap is step 3: inserting $[P]$ on the sheet itself would be unsound, since the sheet has depth $0$ and is positive.

### L3 human

The alpha rules resemble modern systems of deep inference: a rule may act at any depth inside a formula, and its direction depends on the polarity of the position.
Erasure and insertion say that a conjunction can be weakened in a positive position and strengthened in a negative one.
Iteration and deiteration do the work of contraction and reuse of hypotheses, which sequent calculi handle with structural rules.
Because all rules act inside the graph, existential graphs are closer to deep inference than to [[Hilbert systems|1MGMQX43B8]] or to [[natural deduction|6KT3BJZ7D1]].

The beta system shows that lines can do the work of variables.
A line of identity is a variable together with its quantifier, and a branching line is a variable shared between atomic formulas.
The idea returns in conceptual graphs in computer science and in string diagrams read in a category of relations.
Class diagrams such as Venn and Euler diagrams capture [[syllogistic|MZBNX2T6Q6]] and other reasoning with one-place predicates, while beta graphs reach full first-order logic with relations of any arity.
