---
tag: C7CV0XMSTT
kind: concept
name: Computability logic
aliases: [col, logic-of-computational-problems]
msc: ["03B70", "03B47"]
topics: [NJB94B39QK]
audience: research
uses: [D45Z7HETDA, KZSB5E471K, RWRNBS3Z7B, N238J43XNE, 2P2184B6HE]
sources:
  - url: https://en.wikipedia.org/wiki/Computability_logic
    locator: lead section, Language, Semantics, As a problem specification tool, As a problem solving tool
  - url: https://en.wikipedia.org/wiki/Cirquent_calculus
    locator: lead section and Overview
  - doi: 10.1016/S0168-0072(03)00023-X
---

## Summary

*Computability logic* (CoL) is a framework that develops logic as a formal theory of computability, not of truth.
Its formulas stand for computational problems, and a problem is a game between a machine and its environment.
A problem is computable if some machine wins the game against every behavior of the environment.
A formula is valid if it is always computable, that is, computable under every interpretation of its atoms.
Japaridze introduced and named computability logic in 2003.

## Motivation

Classical logic tells us when the truth of a statement follows from the truth of other statements.
Computability logic asks a similar question: when does the computability of a problem $A$ follow from the computability of problems $B_1, \dots, B_n$?
It also asks for a uniform way to build an algorithm for $A$ from algorithms for $B_1, \dots, B_n$.
Questions such as "decide $p$", "compute $f$" and "reduce $q$ to $p$" are interactive: the environment asks, and the machine answers.
So a logic of problems needs connectives for interaction, such as a choice made by one of the players.
Like [[game-theoretic semantics|D45Z7HETDA]], it gives meaning to formulas by games, but the player on the machine side must follow an algorithm.

## Notation

- $\neg A$ is $A$ with the roles of the two players switched.
- $A \wedge B$ and $A \vee B$ are the *parallel* conjunction and disjunction: both games are played at the same time on two boards. The machine must win both, or at least one.
- $A \to B$ is $\neg A \vee B$, the parallel implication.
- $A \sqcap B$ and $A \sqcup B$ are the *choice* conjunction and disjunction. In $A \sqcup B$ the machine must choose one component and then win it. In $A \sqcap B$ the environment makes the choice.
- $\sqcap x\, A(x)$ and $\sqcup x\, A(x)$ are the choice quantifiers: the environment, or the machine, chooses a value of $x$.
- $\forall x\, A(x)$ and $\exists x\, A(x)$ are the *blind* quantifiers: one play of $A(x)$ that the machine must win for all values, or for some value, of $x$.
- $!A$ is the branching recurrence of $A$, which Japaridze writes with the symbol ⫰. The environment may split the play of $A$ into parallel threads, and the machine must win every thread. The brimplication $A \multimap B$ is $!A \to B$.
- Lower-case atoms $p, q$ are *elementary*: games with no moves, won by the machine if true and lost if false. Upper-case atoms $P, Q$ are *general*: they stand for any game.

The domain of discourse is the set of natural numbers.

## Remarks

### Examples

- [[The copy-cat strategy wins P or not P|V4A5X64DZQ]]: the machine copies moves between the two boards of $P \vee \neg P$, so excluded middle with parallel disjunction is valid.
- [[Computing a function as a game|GAQBW6SB8E]]: the problem $\sqcap x \sqcup y\, (y = f(x))$ is computable if and only if $f$ is a [[computable function|KZSB5E471K]].
- [[Deciding the halting problem as a game|3CBR9YYH4T]]: $\sqcap x\, (h(x) \sqcup \neg h(x))$ is not computable for the halting predicate $h$, so $\sqcap x\, (p(x) \sqcup \neg p(x))$ is not valid.

### Non-examples

- The formula $P \sqcup \neg P$ is not valid. The machine must commit to one side, and for some interpretations of $P$ no algorithm can choose correctly.
- The formula $P \to P \wedge P$ is not valid, but $p \to p \wedge p$ is valid for an elementary atom $p$. One copy of a solution to $P$ is not two copies.
- A game where a player who thinks too long loses is not a *static* game. Computability logic does not use such games, so its problems never become contests of speed.

### Basic properties

- Classical fragment. Classical logic is the fragment of CoL without general atoms and with only $\neg, \wedge, \vee, \to, \forall, \exists$. On elementary games these operators behave as in classical logic. So CoL is a [[conservative extension|N238J43XNE]] of classical logic.
- Other fragments. [[Independence-friendly logic|DPMKT2KRB8]] and some proper extensions of [[linear logic|2P2184B6HE]] and [[intuitionistic logic|Q11N8X99FK]] are natural fragments of CoL.
- Four kinds of disjunction. Besides the parallel and choice disjunctions there are sequential and toggling disjunctions. With general atoms, $P \vee \neg P$ is valid, but excluded middle with any of the other three disjunctions is not.
- Problems as formulas. For a predicate $p$, $\sqcap x\, (p(x) \sqcup \neg p(x))$ is the problem of deciding $p$. The problem $\sqcap x\, (p(x) \sqcup \neg p(x)) \multimap \sqcap x\, (q(x) \sqcup \neg q(x))$ is computable if and only if $q$ is [[Turing reducible|PA4PYQ1PZ0]] to $p$. The problem $\sqcap x \sqcup y\, (q(x) \leftrightarrow p(y))$ is the [[many-one reduction|JTAH37JTHD]] of $q$ to $p$.
- Solutions from proofs. The known deductive systems for fragments of CoL let one extract an algorithm from a proof of a formula. So a proof of a formula is also a program that meets the formula as a specification.
- Applied theories. The *clarithmetics* are number theories based on CoL, in the way that [[Peano arithmetic|HACXBCM7SS]] is based on classical logic. Variants of their induction or comprehension rules characterize interactive complexity classes, so that a proof can give a solution that runs in polynomial time.
- Proof theory. [[Sequent calculus|PZX9J3VEMT]] and natural deduction do not suffice to axiomatize nontrivial fragments of CoL. Japaridze introduced *cirquent calculus* for this purpose.
- Cirquents. A cirquent is a graph-style object, like a Boolean circuit, in which two components can share one occurrence of a subformula. Cirquent calculi are [[deep inference|4ZW0SHW2RG]] systems. They give polynomial-size analytic proofs of the propositional pigeonhole principle.

### History

Japaridze introduced and named computability logic in 2003, in the paper "Introduction to computability logic".
He introduced cirquent calculus as an alternative proof theory for fragments of the logic that resisted axiomatization by traditional methods.
He argued that linear logic is incomplete as a logic of resources, because it cannot express the sharing of resources.
Xu later axiomatized a propositional independence-friendly logic with a semantics based on cirquent calculus.

### Common errors

- To read $\wedge$ and $\vee$ as the only conjunction and disjunction. CoL has several kinds of each, and they agree only on elementary games.
- To think that validity means truth in every model. In CoL, validity means computability under every interpretation, so $P \sqcup \neg P$ fails although $P \vee \neg P$ holds.
- To think that the environment must follow an algorithm. Only the machine is restricted to algorithmic strategies; the environment can behave in any way.
- To think that computability logic is a weakening of classical logic. It extends classical logic conservatively, and the clarithmetics usually extend Peano arithmetic.

## Explanations

### L1 human

In computability logic, a formula is a task, like a game that a computer plays against a user.
"A or B" can mean "play both and win one", or "choose one and win it".
The second meaning is harder, because the computer must decide which one it can win.
A formula is valid if a computer can always win its game.

### L2 human

Negation swaps the two players, so $\neg \text{Chess}$ is chess from the other side of the board.
The parallel disjunction $\text{Chess} \vee \neg \text{Chess}$ can be won by copying moves from board to board, against any opponent.
The choice disjunction $A \sqcup B$ asks the machine to commit to one side, so it expresses the problem of answering a question.
Choice quantifiers express input and output: $\sqcap x \sqcup y\, (y = f(x))$ means "for the input $x$ that you get, give the output $f(x)$".
A trap is to think that every classical tautology stays valid when its connectives are read as choice connectives; $P \sqcup \neg P$ shows that it does not.

### L3 human

The semantics uses static games between an algorithmic machine and an unrestricted environment, which generalizes the [[Church–Turing thesis|RWRNBS3Z7B]] to interaction.
The logic is a conservative extension of classical logic, and it contains natural fragments that extend intuitionistic logic.
Its recurrence operators recall the exponentials of linear logic, but the branching recurrence lets the environment replicate a position of a play.
The abstract resource semantics of cirquent calculus gives a logic properly stronger than affine linear logic.
The axiomatization of its fragments needs cirquent calculus, where shared subformulas are explicit nodes of a graph.
