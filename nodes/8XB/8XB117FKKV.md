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

Temporal logic is [[modal logic|C3RZY20ETK]] read over time.
A temporal frame is a set $T$ of time points with a strict order $<$, read "earlier than".
Prior's tense language has the operators $F$ ("at some later time"), $P$ ("at some earlier time"), $G = \neg F \neg$ ("at all later times") and $H = \neg P \neg$ ("at all earlier times").
The formula $F\varphi$ is true at $t$ when $\varphi$ is true at some $u$ with $t < u$, and $P\varphi$ is true at $t$ when $\varphi$ is true at some $u$ with $u < t$.
The minimal tense logic $\mathsf{K}_t$ is the logic of all such frames, and stronger logics describe linear, dense, discrete or branching time.
The binary operators "until" $U$ and "since" $S$ extend the language, and over complete linear orders they express every first-order property of time.
Temporal logic matters because it gives precise laws of tense, and because its linear and branching forms are the specification languages of program verification.

## Motivation

The sentences "it will rain" and "it has rained" are true or false depending on the time at which we say them.
Classical predicate logic handles them with explicit variables for times, as in $\exists u\,(t < u \wedge \mathrm{Rain}(u))$.
Tense logic keeps the time implicit, as natural language does, and treats "will" and "was" as operators.
These operators are two [[Kripke-style|NGHWZ9Y7ZV]] modalities, one for each direction of the order.
So the methods of modal logic (frames, correspondence, completeness, filtration) apply to time.
Properties of time, such as "time has no end" or "between two times there is a third", then become modal axioms.
In computer science the time points are the states of a run of a program, and temporal formulas state its correct behaviour.

## Notation

1. Prior's notation: $F$, $P$, $G$, $H$. Some books write $\lozenge$ and $\square$ for $F$ and $G$, and $\blacklozenge$ and $\blacksquare$ for $P$ and $H$.
2. A temporal frame is a pair $(T, <)$, and a model is a triple $(T, <, V)$ with $V$ a valuation.
3. Strict until: $\varphi \, U \, \psi$ is true at $t$ when some $u > t$ has $\psi$, and every $v$ with $t < v < u$ has $\varphi$. Since $S$ is the mirror image towards the past.
4. Computer science writes $X$ or $\bigcirc$ for "next" and uses a reflexive until, see [[linear temporal logic|RMJ56ZPA63]].
5. The minimal tense logic is written $\mathsf{K}_t$.

## Remarks

### Examples

1. On the rational time line $(\mathbb{Q}, <)$ the density formula $Fp \to FFp$ is valid, because between two rationals there is a third, see [[the density example|14Z5TDHRV2]].
2. On the integers $(\mathbb{Z}, <)$ the density formula fails at $0$ when $p$ is true only at $1$, by the same example.
3. On the integers, "next" is definable as $\bot \, U \, p$, since every point has an immediate successor, see [[since and until on the integers|FJEN3XBRP1]].
4. The basic tense logic $\mathsf{K}_t$ as a bimodal logic, with the two interaction axioms, is worked in [[future and past in the basic tense logic|KXRMT4R9E8]].
5. Branching time: a tree of moments with a linear past and a branching future is a frame of $\mathsf{K}_t$ that refutes future linearity. It is the frame of [[computation tree logic|F6JA5C5BJX]].

### Non-examples

1. A bimodal frame in which the past relation is not the converse of the future relation is not a temporal frame. There the axiom $p \to GPp$ fails, see [[the non-example|ZYJ2VC7S74]].
2. A model of [[the logic S5|VC3A2VWXND]] with the universal relation is not a frame of linear strict time, since every point sees itself. The irreflexivity of $<$ cannot be expressed by a tense formula, but it changes the logic of $U$ and $S$.

### Basic properties

1. $\mathsf{K}_t$ is the smallest bimodal [[normal modal logic|D1TJYZZDCY]] in $G$ and $H$ with the axioms $p \to GPp$ and $p \to HFp$. It is sound and complete for all frames $(T, <)$ with $H$ read along the converse of $<$.
2. Correspondences on a frame $(T, <)$, each checked as for [[the common modal axioms|FDFQFWPM4X]]:
   - $Gp \to GGp$ holds on the frame if and only if $<$ is transitive;
   - $Gp \to Fp$ holds on the frame if and only if every point has a later point;
   - $Fp \to FFp$ holds on the frame if and only if $<$ is dense;
   - $(Fp \wedge Fq) \to F(p \wedge q) \vee F(p \wedge Fq) \vee F(Fp \wedge q)$ holds on a transitive frame if and only if no point has two incomparable later points.
3. Over the integers, $X\varphi$ ("next") equals $\bot \, U \, \varphi$, and $F\varphi$ equals $\top \, U \, \varphi$.
4. Over dense orders such as $\mathbb{Q}$ and $\mathbb{R}$, the operator $U$ cannot be defined from $F$ and $P$. Kamp proved this in his thesis.
5. Over Dedekind complete linear orders, $U$ and $S$ express every first-order formula with one free variable, by [[Kamp's theorem|CQ0QCQK5JT]].

### History

Arthur Prior introduced tense logic in Time and Modality (1957), with the operators $F$, $P$, $G$ and $H$.
Hans Kamp added the binary operators "since" and "until" in his doctoral thesis of 1968, and proved their expressive completeness.
Amir Pnueli proposed temporal logic for the verification of programs in 1977.

### Common errors

1. Reading $G\varphi$ as "$\varphi$ now and always". With the strict order, $G\varphi$ says nothing about the present; the reflexive reading is the convention of [[LTL|RMJ56ZPA63]].
2. Forgetting that $H$ uses the converse relation. Then $p \to GPp$ looks like an extra axiom, while it is valid on every temporal frame.
3. Confusing truth in a model with validity on a frame. A model on $\mathbb{Z}$ with $p$ true everywhere makes $Fp \to FFp$ true at every point, although $\mathbb{Z}$ is not dense.

## Explanations

### L1 human

Temporal logic is a logic of "will" and "was".
It writes "it will rain" as $F\,\mathit{rain}$, read "at some future time, rain".
The formula $G\,\mathit{rain}$ means "it will always rain from now on".
Picture time as the number line, and suppose it rains on day 3 only.
On day 1 the sentence "it will rain" is true, and on day 5 it is false.
On day 5 the sentence "it has rained" is true.

### L2 human

We check $Fp \to FFp$ on two time lines, with $p$ true at exactly one point $u = 1$.

1. On $(\mathbb{Z}, <)$ take $t = 0$. $Fp$ holds at $0$, since $0 < 1$ and $p$ holds at $1$.
2. $FFp$ at $0$ needs a $z$ with $0 < z$ and $Fp$ at $z$, so $z < 1$. No integer lies strictly between $0$ and $1$. So the formula fails at $0$.
3. On $(\mathbb{Q}, <)$ take any $t < 1$. The point $z = (t + 1)/2$ satisfies $t < z < 1$, so $Fp$ holds at $z$ and $FFp$ holds at $t$.
4. At points $t \ge 1$, $Fp$ is false, so the implication holds.

The typical use of such checks is to match a property of time with an axiom, and then to axiomatize the logic of $\mathbb{Q}$ or $\mathbb{Z}$.
A trap: the density axiom holds on $\mathbb{Q}$ for every valuation, while on $\mathbb{Z}$ it fails only for some valuations, so validity on a frame needs all valuations.

### L3 human

A tense frame is a [[multimodal|ERG3KAQWYF]] frame with two relations that are converse to each other, so tense logic is the simplest modal logic with converse.
The [[standard translation|YW6YGBMVQY]] sends tense formulas into first-order logic over $<$, and Kamp's theorem says that, with $U$ and $S$, the translation is onto the one-variable formulas over complete orders.
Branching time leads to [[computation tree logic|F6JA5C5BJX]] and [[CTL*|Y4XZ94GRXV]], linear discrete time to [[LTL|RMJ56ZPA63]], and time made of intervals to [[interval temporal logics|991B5RR6X4]].
Combinations with agents give [[STIT logic|WYY2JXWMYY]] and the temporal-epistemic logics of distributed systems.
