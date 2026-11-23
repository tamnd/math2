---
tag: 8XB117FKKV
kind: concept
name: Temporal logic
msc: ["03B44", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
uses: [C3RZY20ETK, NGHWZ9Y7ZV, ERG3KAQWYF, 0FRXBVVR03, D1TJYZZDCY]
sources:
  - url: https://en.wikipedia.org/wiki/Temporal_logic
    locator: lead section
  - book: isbn:9780198537694
    locator: Gabbay, Hodkinson and Reynolds, Temporal Logic, volume 1
  - book: isbn:9780521527149
    locator: Blackburn, de Rijke and Venema, Modal Logic, chapter 1
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section T
    note: adopted
    mention: wikipedia://en/76765067#EOJH
    sections: [Summary]
inventory: [TKWZ5JBB4V]
---

## Summary

Temporal logic is [[modal logic|C3RZY20ETK]] read over time: "it will rain" and "it has rained" become operators on a sentence, and the time stays implicit, as in ordinary speech.
Suppose it rains on day 3 and on no other day of the integer time line.
On day 1 "it will rain" is true, on day 5 it is false, and on day 5 "it has rained" is true.

A temporal frame is a set $T$ of time points with a binary relation $<$, read "earlier than"; for time as we know it, $<$ is a strict order.
Prior's tense language has four operators.
The formula $F\varphi$ is true at $t$ when $\varphi$ is true at some $u$ with $t < u$, and $P\varphi$ is true at $t$ when $\varphi$ is true at some $u$ with $u < t$.
Their duals are "always in the future" and "always in the past":
$$G\varphi = \neg F \neg \varphi, \qquad H\varphi = \neg P \neg \varphi.$$
The minimal tense logic $\mathsf{K}_t$ is the logic of all such frames.
Stronger logics describe linear, dense, discrete or branching time, and the binary operators "until" $U$ and "since" $S$ make the language as expressive as first-order logic over complete linear orders.

## Motivation

Classical predicate logic can talk about time, but only with explicit time variables, as in $\exists u\,(t < u \wedge \mathrm{Rain}(u))$.
Tense logic hides the variable and treats "will" and "was" as two [[Kripke-style|NGHWZ9Y7ZV]] modalities, one for each direction of the order.
So the whole toolkit of modal logic applies to time: frames, correspondence, completeness and filtration.
A property of time, such as "time has no end" or "between two times there is a third", becomes a modal axiom that you can add or drop.

The same idea moved into computer science.
There the time points are the states of a run of a program, and a temporal formula states how the program must behave, for example "every request is eventually granted".
The later pages on [[linear temporal logic|RMJ56ZPA63]], [[computation tree logic|F6JA5C5BJX]] and [[CTL*|Y4XZ94GRXV]] grow out of this, and [[Kamp's theorem|CQ0QCQK5JT]] explains why until and since are the right operators.

## Notation

Prior wrote $F$, $P$, $G$ and $H$, and many books still do.
Others write $\lozenge$ and $\square$ for $F$ and $G$, and $\blacklozenge$ and $\blacksquare$ for $P$ and $H$.
A frame is a pair $(T, <)$, and a model $(T, <, V)$ adds a valuation $V$.
In strict until, $\varphi \, U \, \psi$ is true at $t$ when some $u > t$ has $\psi$ and every $v$ with $t < v < u$ has $\varphi$; since, $S$, is the mirror image towards the past.
Computer science writes $X$ or $\bigcirc$ for "next" and uses a reflexive until that also looks at the present point, so check which convention a book uses before you compare answers.

## Remarks

### The minimal tense logic

The logic $\mathsf{K}_t$ is the smallest bimodal [[normal modal logic|D1TJYZZDCY]] in $G$ and $H$ that contains these two axioms:
$$p \to GPp, \qquad p \to HFp.$$
The first says that whatever is true now will always have been true, and the second is its mirror image.
Together they force the past relation to be the converse of the future relation, and $\mathsf{K}_t$ is sound and complete for all frames $(T, <)$ with $H$ read along the converse of $<$.
The basic tense logic as a [[bimodal logic|ERG3KAQWYF]] is worked in [[future and past in the basic tense logic|KXRMT4R9E8]].

### Properties of time as axioms

Each familiar property of the order matches a formula, in the sense of [[modal correspondence|FDFQFWPM4X]].
The axiom $Gp \to GGp$ is valid on a frame exactly when $<$ is transitive, and $Gp \to Fp$ exactly when every point has a later point.
Density, "between two times there is a third", corresponds to $Fp \to FFp$, and [[the density example|14Z5TDHRV2]] proves this and compares $\mathbb{Q}$ with $\mathbb{Z}$.
On a transitive frame, the axiom below holds exactly when no point has two incomparable later points, so it rules out branching of the future:
$$(Fp \wedge Fq) \to F(p \wedge q) \vee F(p \wedge Fq) \vee F(Fp \wedge q).$$
A tree of moments with a linear past and a branching future satisfies $\mathsf{K}_t$ and refutes this axiom, and it is the frame of [[computation tree logic|F6JA5C5BJX]].

### Until and since

The binary operators say more than $F$ and $P$ can.
On the integers, with $p$ true at $1$, $2$, $3$ and $q$ true at $-2$ and $4$, the formula $p \, U \, q$ is true at $0$, because $q$ holds at $4$ and $p$ holds at each of $1$, $2$, $3$ in between.
It is false at $-1$, because the point $0$ lies between $-1$ and $4$ and has no $p$.
On the integers "next" is definable as $\bot \, U \, p$, since the only $u > t$ with nothing strictly between is $t + 1$, and $F\varphi$ is $\top \, U \, \varphi$.
[[Since and until on the integers|FJEN3XBRP1]] works these values in full.
Over the real line, until cannot be defined from $F$ and $P$, and over Dedekind-complete linear orders $U$ and $S$ express every first-order property with one free variable, by [[Kamp's theorem|CQ0QCQK5JT]].

### What is not a temporal frame

A bimodal frame whose past relation is not the converse of its future relation is not a frame of time, and $p \to GPp$ fails on it, as [[the two-point non-example|ZYJ2VC7S74]] shows.
A model of [[the logic S5|VC3A2VWXND]] with the universal relation is not a frame of strict linear time either, since every point is related to itself.
Tense formulas cannot express irreflexivity, but it still matters: it changes the logic of $U$ and $S$.

### Watch out

Do not read $G\varphi$ as "$\varphi$ now and always".
With the strict order, $G\varphi$ says nothing about the present, so $Gp \to p$ fails at $0$ on $\mathbb{Z}$ when $p$ is true exactly at the points $t > 0$.
The reflexive reading belongs to [[LTL|RMJ56ZPA63]].

Do not confuse truth in one model with validity on a frame.
On $\mathbb{Z}$ with $p$ true everywhere, $Fp \to FFp$ is true at every point, yet $\mathbb{Z}$ is not dense.
Validity on a frame needs every valuation, and the valuation that makes $p$ true only at $1$ refutes the axiom at $0$.

### History

Arthur Prior introduced tense logic in the 1950s and 1960s, and his book Time and Modality (1957) has the operators $F$, $P$, $G$ and $H$.
Hans Kamp studied the binary operators since and until in his doctoral thesis of 1968 and proved their expressive completeness.
Amir Pnueli proposed temporal logic for the verification of programs in 1977.

### Try it

First, on $(\mathbb{Z}, <)$ with $p$ true exactly at $5$, where is $Pp$ true?
It is true exactly at the points $t > 5$, since $P$ looks strictly into the past.

Second, is $Gp \to GGp$ a theorem of $\mathsf{K}_t$?
No, because it needs transitivity: on the frame $\{0, 1, 2\}$ with $0 < 1$, $1 < 2$ but not $0 < 2$, put $p$ at $1$ only: $Gp$ holds at $0$, but $GGp$ fails because $p$ is false at $2$.

## Explanations

### L1 human

Temporal logic is a logic of "will" and "was".
It writes "it will rain" as $F\,\mathit{rain}$ and "it will always rain from now on" as $G\,\mathit{rain}$.
Picture time as the number line, and suppose it rains on day 3 only.
On day 1 the sentence "it will rain" is true, and on day 5 it is false.
On day 5 the sentence "it has rained" is true, and on day 1 it is false.

### L2 human

Let us check $Fp \to FFp$ on two time lines, with $p$ true at exactly one point $u = 1$.
On $(\mathbb{Z}, <)$ take $t = 0$.
Then $Fp$ holds at $0$, since $0 < 1$, and $FFp$ needs a point $z$ with $0 < z < 1$, which does not exist, so the formula fails at $0$.
On $(\mathbb{Q}, <)$ take any $t < 1$, and put $z = (t + 1)/2$:
$$t < z < 1.$$
So $Fp$ holds at $z$ and $FFp$ holds at $t$.
At points $t \ge 1$ the antecedent $Fp$ is false, so the implication holds there too.
This is the typical use of such checks: you match a property of time with an axiom, and then you axiomatize the logic of $\mathbb{Q}$ or $\mathbb{Z}$.
Watch out: $Fp \to FFp$ is density, and its converse $FFp \to Fp$ is transitivity; the two are often swapped.

### L3 human

A tense frame is a [[multimodal|ERG3KAQWYF]] frame with two relations that are converse to each other, so tense logic is the simplest modal logic with a converse modality.
The [[standard translation|YW6YGBMVQY]] sends tense formulas into first-order logic over $<$, and Kamp's theorem says that with $U$ and $S$ the translation reaches every one-variable formula over complete orders.
Branching time leads to [[computation tree logic|F6JA5C5BJX]] and [[CTL*|Y4XZ94GRXV]], discrete linear time to [[LTL|RMJ56ZPA63]], and time made of intervals to [[interval temporal logics|991B5RR6X4]].
Combinations with agents give [[STIT logic|WYY2JXWMYY]] and the temporal-epistemic logics of distributed systems.
