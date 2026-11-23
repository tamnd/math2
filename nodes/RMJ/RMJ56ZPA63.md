---
tag: RMJ56ZPA63
kind: concept
name: Linear temporal logic
msc: ["03B44", "68Q60", "03B70"]
topics: [CQM9SRN8PM]
audience: grad
specializes: [C3RZY20ETK]
uses: [8XB117FKKV, 8S64VZ6A1S, RFQ8DJZNQT, 92DM43HQZT, VNY0VXVZ53, T9NTRY93ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_temporal_logic
    locator: lead section, section Relations with other logics
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 5
  - book: isbn:9780198537694
    locator: Gabbay, Hodkinson and Reynolds, Temporal Logic, volume 1
same_as:
  wikidata: Q1536492
  wikipedia: Linear temporal logic
---

## Summary

Linear temporal logic (LTL) states how a system that runs forever must behave, as a property of one infinite run.
A typical requirement is "every request is eventually granted":
$$G(\mathit{req} \to F\,\mathit{grant}).$$
On the run that repeats "request, idle, grant" forever, each request at step $3k$ is followed by a grant at step $3k + 2$, so the formula holds.
On the run that has a request at step $0$ and nothing afterwards, it fails at step $0$.

In general, LTL is the [[temporal logic|8XB117FKKV]] of the time line $0, 1, 2, \dots$.
Its formulas are built from atomic propositions with the Boolean connectives, the operator "next" $X$ and the operator "until" $U$, as in [[the definition|8S64VZ6A1S]].
A formula is evaluated on an infinite word $w = w_0 w_1 w_2 \cdots$ of sets of atomic propositions, and $\varphi \, U \, \psi$ holds when $\psi$ holds at some step and $\varphi$ holds at every step before it.
A state of a [[Kripke structure|RFQ8DJZNQT]] satisfies $\varphi$ when every infinite path from the state does.

## Motivation

An operating system or a communication protocol is not meant to stop.
So its correctness is not a property of an output, but of its infinite runs.
Typical requirements are "two processes are never both in the critical section" and "every request is eventually granted".
First-order logic over $(\mathbb{N}, <)$ can say these things, but only with explicit time variables and quantifiers.
Pnueli proposed to write them with temporal operators instead, which keep time implicit and give short formulas.

Nothing is lost by this choice.
Over $(\mathbb{N}, <)$ the operators $X$ and $U$ express exactly the first-order properties of runs, a form of [[Kamp's theorem|CQ0QCQK5JT]].
And every formula can be turned into a [[Büchi automaton|92DM43HQZT]], which is how [[model checkers|VNY0VXVZ53]] test a system against it.

## Notation

Next is written $X\varphi$ or $\bigcirc\varphi$, and until is $\varphi \, U \, \psi$ or $\varphi \, \mathcal{U} \, \psi$.
Eventually is $F\varphi = \top \, U \, \varphi$, also written $\lozenge\varphi$, and always is $G\varphi = \neg F \neg\varphi$, also written $\square\varphi$.
Weak until is $\varphi \, W \, \psi = (\varphi \, U \, \psi) \vee G\varphi$, and release is $\varphi \, R \, \psi = \neg(\neg\varphi \, U \, \neg\psi)$.
The suffix $w_i w_{i+1} \cdots$ is $w^i$, and $w \models \varphi$ means that $\varphi$ holds at step $0$.
Watch the convention: the LTL until is reflexive, so the present step counts, unlike the strict until of [[tense logic|8XB117FKKV]].

## Remarks

### Reading a lasso

A system with finitely many states produces runs that end in a loop, words of the form $u\,v^\omega$.
Take the prefix $u = \{\mathit{req}\}\,\{\mathit{req}\}$ and the loop $v = \{\mathit{grant}\}\,\emptyset\,\{\mathit{req}\}$.
The requests are at steps $0$, $1$ and $4 + 3k$, and the grants are at steps $2 + 3k$.
Every request has a grant at most three steps later, so the response formula holds.
The stronger formula $G(\mathit{req} \to X\,\mathit{grant})$ fails at step $0$, because step $1$ has no grant.
[[The response example|HHE6EGQ6YC]] works this word in full, and shows why only the steps $0$ to $4$ need checking.

### The shapes of requirements

Most specifications fall into a few shapes.
Safety, "nothing bad happens", is $G \neg(\mathit{crit}_1 \wedge \mathit{crit}_2)$.
Response is the formula above, and a timed form $G(\mathit{req} \to X\,\mathit{ack})$ asks for an answer at the very next step.
Recurrence $GFp$ says that $p$ holds infinitely often, and persistence $FGp$ says that $p$ holds from some step on; [[the two are compared|NQR665PX9T]] on the word $(\emptyset\,\{p\})^\omega$.
Precedence $\neg \mathit{grant} \, W \, \mathit{req}$ says that no grant comes before the first request.
Dwyer, Avrunin and Corbett collected such forms as specification patterns in 1999, each with a fixed LTL formula for scopes such as "globally" or "before $r$".

### Laws you can use

The operators unfold one step at a time, and these expansion laws drive both proofs and algorithms:
$$\varphi \, U \, \psi \equiv \psi \vee (\varphi \wedge X(\varphi \, U \, \psi)), \qquad F\varphi \equiv \varphi \vee XF\varphi, \qquad G\varphi \equiv \varphi \wedge XG\varphi.$$
The dualities $\neg X\varphi \equiv X\neg\varphi$ and $\neg F\varphi \equiv G\neg\varphi$ push negations inward.
Every formula $\varphi$ has a Büchi automaton with at most $2^{O(\lvert\varphi\rvert)}$ states that accepts exactly its models, by [[the translation theorem|BYMYN6GN8E]].
Satisfiability and model checking are [[PSPACE|T9NTRY93ZT]]-complete, and model checking takes time $\lvert M \rvert \cdot 2^{O(\lvert\varphi\rvert)}$, by [[the complexity theorem|RD9B213GJ5]].

### What LTL cannot say

LTL sees runs one at a time, so it cannot talk about branching.
The reset property $AG\,EF p$ of [[CTL|F6JA5C5BJX]], "from every reachable state a $p$-state can still be reached", is not an LTL property; [[two structures with the same runs|RDRSPX5MM7]] disagree on it.
LTL also cannot count: Wolper showed in 1983 that "$p$ holds at every even step" is not expressible, although a Büchi automaton with two states accepts it.
LTL and CTL have incomparable power, and both are fragments of [[CTL*|Y4XZ94GRXV]].

### Watch out

Do not swap $FGp$ and $GFp$.
The word $(\emptyset\,\{p\})^\omega$ satisfies $GFp$, since $p$ comes back at every odd step, but not $FGp$, since $p$ fails at every even step.
Only $FGp \to GFp$ is valid.

Do not assume that a state satisfies $\varphi$ or $\neg\varphi$.
A state with one path where $p$ holds now and one path where $p$ never holds satisfies neither $Fp$ nor $\neg Fp$, because both claims are about all paths.

### History

Amir Pnueli introduced LTL for program verification in "The temporal logic of programs" (1977), and he received the Turing Award in 1996 for this work.
Sistla and Clarke proved in 1985 that satisfiability and model checking are PSPACE-complete.
Vardi and Wolper gave the automata-theoretic approach: translate the negated formula into a Büchi automaton and test the product with the system for emptiness.

### Try it

First, does the word $\{p\}\,\{p\}\,\emptyset^\omega$ satisfy $p \, U \, \neg p$?
Yes: step $2$ has $\neg p$, and steps $0$ and $1$ have $p$.

Second, write "$p$ never holds twice in a row" in LTL.
One answer is $G(p \to X\neg p)$.

## Explanations

### L1 human

LTL talks about a run of a machine as an endless list of moments.
At each moment some basic facts are true, such as "a request is pending".
The letter $G$ means "at every moment from now on", $F$ means "at some moment from now on", and $X$ means "at the next moment".
For example, "every request is eventually granted" is $G(\mathit{req} \to F\,\mathit{grant})$.
If requests come at moments 0, 3, 6 and so on, and grants come at moments 2, 5, 8 and so on, the sentence is true.

### L2 human

Let us check $G(\mathit{req} \to X(\neg\mathit{req} \, U \, \mathit{grant}))$ on the periodic word $w = (\{\mathit{req}\}\,\emptyset\,\{\mathit{grant}\})^\omega$.
It says that after each request, no new request comes before the grant.
The requests are at the steps $3k$ and the grants at the steps $3k + 2$.
At step $3k$ we need $\neg\mathit{req} \, U \, \mathit{grant}$ at step $3k + 1$.
Step $3k + 1$ has no request, and step $3k + 2$ has a grant, so the until holds with witness $3k + 2$.
At every other step there is no request, so the implication holds there.
The typical use is to write a requirement as a formula like this one and give it to a model checker with a model of the system.
Watch out: a run where requests never stop but grants stop after some point violates the response formula, yet no finite prefix shows the violation.

### L3 human

Over $(\mathbb{N}, <)$, LTL defines the same properties of words as first-order formulas with one free variable, by Kamp's theorem in the form of Gabbay, Pnueli, Shelah and Stavi.
So LTL defines exactly the star-free $\omega$-regular languages, while [[Büchi automata|92DM43HQZT]] give all $\omega$-regular languages.
Fixpoint extensions, such as the linear-time version of the [[mu-calculus|MZ0M2KR9S0]], close this gap.
Over branching structures LTL is the path part of [[CTL*|Y4XZ94GRXV]], and satisfiability moves from PSPACE up to 2EXPTIME.
