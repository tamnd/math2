---
tag: BGKZTSQN3W
kind: concept
name: Interpretability logic
msc: ["03F45", "03F25"]
topics: [3E7M66WW6Q]
audience: research
uses: [WJK0YA4GP2, C3RZY20ETK, NGHWZ9Y7ZV, HACXBCM7SS, NB2BCZR40F, RY8KRKR097]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretability_logic
    locator: Logic ILM
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: Generalizations
---

## Summary

The theory $\mathsf{PA} + \mathrm{Con}(\mathsf{PA} + A)$ can build a model of $\mathsf{PA} + A$ inside itself, and so it interprets $\mathsf{PA} + A$.
Interpretability logic is the modal logic of such facts, the general laws of "one theory can imitate another" between extensions of a fixed theory.

Precisely, the language of [[provability logic|WJK0YA4GP2]] gets a binary operator $\rhd$, and $p \rhd q$ is read as "$T + p$ interprets $T + q$" for a fixed arithmetical theory $T$.
The basic system $\mathsf{IL}$ has as axioms all instances of tautologies, the axioms of $\mathsf{GL}$, and the five schemes J1 to J5 listed in the Notation.
Its rules are modus ponens and necessitation for $\square$.
The extension $\mathsf{ILM}$ is the interpretability logic of [[Peano arithmetic|HACXBCM7SS]], and $\mathsf{ILP}$ is the interpretability logic of finitely axiomatized theories such as $\mathsf{GB}$.

## Motivation

A theory $U$ is interpretable in a theory $V$ when each symbol of $U$ can be translated into a formula of $V$, with a formula for the domain, so that $V$ proves the translation of each axiom of $U$.
An interpretation of $U$ in $V$ shows that $U$ is consistent if $V$ is, and it is the standard way to compare the strength of theories.
For extensions $T + A$ and $T + B$ of one arithmetical theory $T$, the statement "$T + A$ interprets $T + B$" can be written in the language of $T$, just as provability can.

Provability is a special case.
$T$ proves $\neg A$ exactly when $T + A$ interprets the inconsistent theory $T + \bot$.
Indeed, an inconsistent theory interprets every theory, and a theory that interprets $T + \bot$ proves the translation of $\bot$, which is $\bot$.
So it is natural to ask which laws the binary relation of interpretability obeys, as $\mathsf{GL}$ collects the laws of provability.

## Notation

Formulas are built from propositional variables, $\bot$, $\to$, the unary operator $\square$ and the binary operator $\rhd$, and $\lozenge \varphi$ abbreviates $\neg \square \neg \varphi$.
The operator $\rhd$ binds more weakly than $\neg$, $\wedge$, $\vee$, $\square$ and $\lozenge$, and more strongly than $\to$, so $p \wedge q \rhd r \to s$ means $((p \wedge q) \rhd r) \to s$.
An arithmetical realization $*$ for $T$ sends $(\square \varphi)^*$ to $\mathrm{Prov}_T(\ulcorner \varphi^* \urcorner)$ and $(\varphi \rhd \psi)^*$ to a formalization of "$T + \varphi^*$ interprets $T + \psi^*$".
The axioms of $\mathsf{IL}$ beyond $\mathsf{GL}$ are the following.

- J1: $\square(p \to q) \to p \rhd q$.
- J2: $(p \rhd q) \wedge (q \rhd r) \to p \rhd r$.
- J3: $(p \rhd r) \wedge (q \rhd r) \to (p \vee q) \rhd r$.
- J4: $p \rhd q \to (\lozenge p \to \lozenge q)$.
- J5: $\lozenge p \rhd p$.

The two extra principles are M, $p \rhd q \to (p \wedge \square r) \rhd (q \wedge \square r)$, and P, $p \rhd q \to \square(p \rhd q)$.
Then $\mathsf{ILM} = \mathsf{IL} + \mathrm{M}$ and $\mathsf{ILP} = \mathsf{IL} + \mathrm{P}$.

## Remarks

### Reading the axioms in arithmetic

Take $T = \mathsf{PA}$ and a sentence $A$.
The realization of $\lozenge p$ is $\neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner \neg A \urcorner)$, the [[consistency statement|4NBAX3VRQ7]] $\mathrm{Con}(\mathsf{PA} + A)$.
So J5 says that $\mathsf{PA} + \mathrm{Con}(\mathsf{PA} + A)$ interprets $\mathsf{PA} + A$, the fact in the first line of the Summary.
It is the formalized [[Henkin construction|RY8KRKR097]], which defines a model of $\mathsf{PA} + A$ by arithmetical formulas inside $\mathsf{PA} + \mathrm{Con}(\mathsf{PA} + A)$; we cite it and do not reproduce it.

The other axioms read the same way.
J1 says that a theory interprets everything it proves, with the identity translation.
J2 says that interpretations compose, and J3 says that $T + (A \vee B)$ interprets what both $T + A$ and $T + B$ interpret, by a case split inside the interpretation.
J4 says that interpretability carries consistency from $T + A$ to $T + B$.

### First laws of IL

From the tautology $p \to p$, necessitation gives $\square(p \to p)$, and J1 gives $p \rhd p$.
In the same way $\square(\bot \to p)$ and J1 give $\bot \rhd p$.
J3 applied to $p \rhd q$ and $q \rhd q$ gives $p \rhd q \to (p \vee q) \rhd q$.

The operator $\square$ can be defined from $\rhd$, since $\mathsf{IL} \vdash \square p \leftrightarrow (\neg p \rhd \bot)$; see [[the box is definable from interpretability|AFGABSCBPK]].
This is the formal version of the special case in the Motivation.

### Veltman semantics

A *Veltman frame* is a triple $(W, R, \{S_w\}_{w \in W})$ with the following properties.

1. $W$ is a finite non-empty set and $R$ is a transitive irreflexive relation on $W$, so that $(W, R)$ is a frame of $\mathsf{GL}$.
   Some authors allow infinite $W$ with $R$ transitive and conversely well-founded.
2. For each $w$, $S_w$ is a relation on $R[w] = \{u : wRu\}$ that is reflexive on $R[w]$ and transitive.
3. If $wRu$ and $uRv$, then $u S_w v$.

A *Veltman model* adds a valuation, and truth is defined as in [[Kripke semantics|NGHWZ9Y7ZV]], with one new clause for $\rhd$.
$$w \Vdash \varphi \rhd \psi \iff \text{for every } u \text{ with } wRu \text{ and } u \Vdash \varphi \text{ there is } v \text{ with } u S_w v \text{ and } v \Vdash \psi.$$
Check: with $S_w$ the identity on $R[w]$, the clause says that every $\varphi$-successor of $w$ satisfies $\psi$.
The idea is that $S_w$ links a world $u$ to the worlds $v$ that the theory at $w$ can reach from $u$ by an interpretation.

### Why the axioms are sound

Every theorem of $\mathsf{IL}$ is true at every world of every Veltman model.

1. The axioms of $\mathsf{GL}$ hold, because $(W, R)$ is a finite transitive irreflexive frame; see [[Kripke completeness of GL|1DMFNR7FZT]].
2. J1: let $w \Vdash \square(p \to q)$, $wRu$ and $u \Vdash p$.
   Then $u \Vdash q$, and $u S_w u$ by reflexivity, so $v = u$ works.
3. J2: from $u \Vdash p$ we get $v$ with $u S_w v$ and $v \Vdash q$.
   Since $v \in R[w]$, we get $z$ with $v S_w z$ and $z \Vdash r$, and transitivity gives $u S_w z$.
4. J3: if $wRu$ and $u \Vdash p \vee q$, then $u \Vdash p$ or $u \Vdash q$, and in each case one hypothesis gives the needed $v$.
5. J4: let $w \Vdash p \rhd q$ and $w \Vdash \lozenge p$, and take $u \in R[w]$ with $u \Vdash p$, then $v$ with $u S_w v$ and $v \Vdash q$.
   Since $v \in R[w]$, $w \Vdash \lozenge q$.
6. J5: let $wRu$ and $u \Vdash \lozenge p$, and take $v$ with $uRv$ and $v \Vdash p$.
   Property 3 gives $u S_w v$.
7. Modus ponens and necessitation preserve truth at all worlds of a model, as in ordinary Kripke semantics.

### What IL does not prove

The converse of J1 fails.
A three-world Veltman model has $w \Vdash p \rhd q$ but $w \nVdash \square(p \to q)$; see [[a Veltman model where interpretability is weaker than provable implication|2T21D2P8RV]].
That model also meets the frame conditions of M and P below, so $p \rhd q \to \square(p \to q)$ is not a theorem of $\mathsf{ILM}$ or $\mathsf{ILP}$ either.

Property 3 of a Veltman frame cannot be dropped.
A structure with $wRuRv$ but not $u S_w v$ can falsify J5 at $w$; see [[a frame without the Veltman condition|874A7QW9HD]].

### The frame conditions of M and P

**M.** A Veltman frame validates M if and only if $u S_w v R z$ implies $u R z$.

1. Assume the condition, and let $w \Vdash p \rhd q$, $wRu$ and $u \Vdash p \wedge \square r$.
2. Take $v$ with $u S_w v$ and $v \Vdash q$.
   For each $z$ with $vRz$ the condition gives $uRz$, so $z \Vdash r$, and $v \Vdash q \wedge \square r$.
3. Conversely, assume $u S_w v$, $vRz$ and not $uRz$.
   Make $p$ true only at $u$, $q$ true only at $v$, and $r$ true everywhere except at $z$.
4. Then $w \Vdash p \rhd q$, and $u \Vdash p \wedge \square r$ because $z$ is not an $R$-successor of $u$.
5. The only $q$-world is $v$, and $v \nVdash \square r$ since $vRz$, so M fails at $w$.

**P.** A Veltman frame validates P if and only if $w R w' R u S_w v$ implies $u S_{w'} v$.

1. Assume the condition, and let $w \Vdash p \rhd q$, $wRw'$, $w' R u$ and $u \Vdash p$.
2. Transitivity gives $wRu$, so there is $v$ with $u S_w v$ and $v \Vdash q$.
   The condition gives $u S_{w'} v$, so $w' \Vdash p \rhd q$.
3. Conversely, assume $w R w' R u S_w v$ and not $u S_{w'} v$, and make $p$ true only at $u$ and $q$ true only at $v$.
4. Then $w \Vdash p \rhd q$, because $u$ is the only $p$-world and $u S_w v$.
   But $w' \nVdash p \rhd q$, because $v$ is the only $q$-world and not $u S_{w'} v$, so $w \nVdash \square(p \rhd q)$.

### Separating ILM from ILP

P is not a theorem of $\mathsf{ILM}$.
Take $wRw'Ru$, $wRu$ and $wRv$, let $S_w$ be the reflexive transitive closure of $\{(w', u), (u, v)\}$ on $R[w]$, and let $S_{w'}$ be the identity on $\{u\}$.
The only world in $R[w]$ with a successor is $w'$, and the only $x$ with $x S_w w'$ is $w'$ itself, which sees $u$, so the condition of M holds.
But $u S_w v$ and not $u S_{w'} v$, so P fails.
Since $\mathsf{ILM}$ is the logic of $\mathsf{PA}$, the principle P is not valid for $\mathsf{PA}$.

M is not a theorem of $\mathsf{ILP}$.
Take $wRu$, $wRv$, $wRz$ and $vRz$, let $S_w$ be the reflexive transitive closure of $\{(u, v), (v, z)\}$ on $R[w]$, and let $S_v$ be the identity on $\{z\}$.
The only chain $w R w' R x$ is $w R v R z$, and $z S_w y$ forces $y = z$, with $z S_v z$, so the condition of P holds.
But $u S_w v R z$ and not $u R z$, so M fails.

### Completeness and decidability

The following results are cited and not proved here.

- Modal completeness: $\mathsf{IL}$ is complete for finite Veltman frames, and $\mathsf{ILM}$ and $\mathsf{ILP}$ are complete for the finite frames with their conditions above.
- Arithmetical completeness for $\mathsf{PA}$: $\mathsf{ILM}$ is the interpretability logic of $\mathsf{PA}$.
- Arithmetical completeness for finitely axiomatized theories: $\mathsf{ILP}$ is the interpretability logic of finitely axiomatized theories with enough arithmetic, such as [[Gödel-Bernays set theory|JTPZ1HZ9KK]] $\mathsf{GB}$.

Completeness for finite frames makes $\mathsf{IL}$, $\mathsf{ILM}$ and $\mathsf{ILP}$ decidable.

### History

Visser and others developed interpretability logic in the 1980s and 1990s.
De Jongh and Veltman gave the semantics now named after Veltman and proved modal completeness for the main systems.
Visser found that $\mathsf{ILP}$ is the logic of finitely axiomatized theories.
Shavrukov in 1988 and Berarducci in 1990 proved, independently, that $\mathsf{ILM}$ is the logic of $\mathsf{PA}$.
De Jongh and Visser showed that the main interpretability logics have explicit fixed points, as $\mathsf{GL}$ has.

### Watch out

The direction of $\rhd$ is easy to reverse.
$p \rhd q$ says that $T + p$ interprets $T + q$, so $T + q$ is the theory that gets imitated, inside $T + p$.
Reading it as "$T + p$ is interpretable in $T + q$" breaks at once on $\bot \rhd p$.
That formula is a theorem, by J1 from $\square(\bot \to p)$, and it says that the inconsistent theory $T + \bot$ interprets $T + p$.
The reversed reading would make $T + \bot$ interpretable in every $T + p$, which fails whenever $T + p$ is consistent.

A second slip is to treat $p \rhd q$ as $\square(p \to q)$.
J1 gives only one direction, and the three-world model above refutes the other.

### Try it

First, show that $\mathsf{IL} \vdash (p \vee \bot) \rhd p$.
The formula $(p \vee \bot) \to p$ is a tautology, so necessitation and J1 give it.

Second, show that $\mathsf{IL} \vdash p \rhd q \to (q \rhd r \to p \rhd r)$.
This is J2 rewritten with the tautology $(a \wedge b \to c) \to (a \to (b \to c))$.

Third, in the [[three-world model|2T21D2P8RV]], with $S_w = \{(u, u), (v, v), (u, v)\}$, $p$ true only at $u$ and $q$ only at $v$, does $w \Vdash q \rhd p$ hold?
No: the only $q$-successor of $w$ is $v$, its only $S_w$-partner is $v$, and $p$ fails at $v$.

## Explanations

### L1 human

Some theories in mathematics can imitate other theories: one can define, inside the first theory, objects that behave like the objects of the second.
For example, set theory can imitate arithmetic, because one can build numbers from sets.
We then say that the first theory interprets the second.
Interpretability logic writes "the theory with $p$ interprets the theory with $q$" as $p \rhd q$, and studies the general rules of this relation.
One rule is that a theory interprets everything it proves.
Another rule is that every theory interprets itself.

### L2 human

We check $p \rhd q$ at a world of a small Veltman model.

1. Let $W = \{w, u, v\}$, $wRu$, $wRv$, and let $S_w$ be the identity on $\{u, v\}$ together with the pair $(u, v)$.
2. Let $p$ be true only at $u$ and $q$ only at $v$.
3. The only $R$-successor of $w$ where $p$ holds is $u$.
4. For $u$ we need some $x$ with $u S_w x$ and $x \Vdash q$, and $x = v$ works.
5. So $w \Vdash p \rhd q$.

The typical use is to refute a formula: build a small Veltman model where it fails, and use soundness.
The trap is to look for the witness $v$ through $R$.
It is found through $S_w$, the relation that belongs to $w$, and changing the root world changes the relation.

### L3 human

Interpretability logic extends the programme of $\mathsf{GL}$ from one unary operator to a binary one.
Its arithmetical completeness theorems are Solovay-type results.
The one for $\mathsf{PA}$ uses the Orey-Hájek characterization of interpretability over $\mathsf{PA}$ by $\Pi^0_1$-conservativity.
The one for finitely axiomatized theories uses that interpretability between such theories is provable when it holds.
Related systems are Japaridze's logic $\mathsf{TOL}$ of tolerance and the logics of $\Pi^0_1$-conservativity.
A long-standing open question asks for the interpretability logic of all reasonable arithmetical theories, the principles that hold in every such theory.
On the algebraic side, one adds a binary operation to a [[Magari algebra|YTA4C8QCB0]], as $\mathsf{IL}$ adds $\rhd$ to $\mathsf{GL}$.
