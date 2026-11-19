---
tag: YTRVX6F3FX
kind: statement
role: theorem
name: Disjunction and existence properties
msc: ["03B20", "03F55"]
topics: [38EQ20GR7M]
audience: grad
uses: [52XCYMK0WW, 480TCT5CJ9, AYRZ98Y0NW]
about: [Q11N8X99FK, MW0RVDRFTA]
proofs: [JA85ANZZS2, 284EX5GB4A]
history:
  first_stated: "Gödel, 1932, Zum intuitionistischen Aussagenkalkül"
  notes: "Gödel stated the disjunction property of IPC without proof. Gentzen proved it in 1934 and 1935 and extended it to predicate logic. Kleene proved the disjunction and existence properties of Heyting arithmetic in 1945."
sources:
  - url: https://en.wikipedia.org/wiki/Disjunction_and_existence_properties
    locator: History
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 4.2 Admissible rules of intuitionistic logic and arithmetic
---

## Statement

A theory $T$ has the *disjunction property* if $T \vdash \varphi \vee \psi$ implies $T \vdash \varphi$ or $T \vdash \psi$, for closed $\varphi \vee \psi$.
A predicate theory $T$ has the *existence property* if $T \vdash \exists x\, \varphi(x)$, for closed $\exists x\, \varphi(x)$, implies $T \vdash \varphi(t)$ for some term $t$.

A formula is *Harrop* if it is built from atoms and $\bot$ with $\wedge$ and with implications $\chi \to \eta$ whose consequent $\eta$ is Harrop.

**Theorem.**

1. [[Intuitionistic propositional logic|Q11N8X99FK]] has the disjunction property.
2. More generally, let $\Gamma$ be a set of propositional Harrop formulas. If $\Gamma \vdash_{\mathsf{i}} \varphi \vee \psi$, then $\Gamma \vdash_{\mathsf{i}} \varphi$ or $\Gamma \vdash_{\mathsf{i}} \psi$.
3. [[Intuitionistic predicate logic|MW0RVDRFTA]] $\mathsf{IQC}$ has the disjunction property and the existence property.
4. Heyting arithmetic has the disjunction property and the numerical existence property: if $\mathsf{HA} \vdash \exists x\, \varphi(x)$, closed, then $\mathsf{HA} \vdash \varphi(\bar n)$ for some numeral $\bar n$.

Two proofs of items 1 and 2 are given: [[by gluing Kripke models|JA85ANZZS2]] and [[by the Kleene slash|284EX5GB4A]].
The second proof also gives item 3, by cut elimination.
Item 4 is cited here; it belongs to [[Heyting arithmetic|CK8ZQRN183]], and it is proved with [[realizability|4H35VQ16DC]] or with the slash.

## Remarks

### Why each hypothesis is needed

1. Classical logic fails the disjunction property: $\vdash p \vee \neg p$, but neither disjunct is a theorem.
2. In item 2, $\Gamma$ must be Harrop. With $\Gamma = \set{p \vee q}$, $\Gamma \vdash p \vee q$, but $\Gamma$ proves neither $p$ nor $q$.
3. The formulas must be closed for the existence property. With a free variable $y$, $\vdash \exists x\,(Px \to Py)$ already uses $y$ as a witness.

### Consequences

1. $p \vee \neg p$ is not a theorem of $\mathsf{IPC}$: otherwise $\vdash p$ or $\vdash \neg p$, and both fail under a classical valuation.
2. The disjunction property is the logical side of the [[BHK interpretation|7B53ZGXXEQ]]: a proof of a disjunction yields a proof of one disjunct.
3. The rule "from $\neg \varphi \to \psi \vee \chi$ infer $(\neg \varphi \to \psi) \vee (\neg \varphi \to \chi)$" is admissible in $\mathsf{IPC}$, by the slash method; see [[admissible rules|C5K35H0R4Y]].

### Converse

The converse of the disjunction property is immediate: $\vdash \varphi$ gives $\vdash \varphi \vee \psi$.
Among intermediate logics, many fail the property; for example [[Gödel-Dummett logic|474SGS2N0X]] proves $(p \to q) \vee (q \to p)$ but neither disjunct.

### Generalizations

1. The [[Kreisel-Putnam logic|669Y0EGM3N]] and [[Medvedev's logic|R2FD01J3PC]] are proper extensions of $\mathsf{IPC}$ with the disjunction property.
2. Friedman showed that for recursively enumerable extensions of $\mathsf{HA}$, the disjunction property implies the numerical existence property.

## Explanations

### L1 human

The theorem says that an intuitionistic proof of "$A$ or $B$" always decides which one holds.
A classical proof can show "$A$ or $B$" without saying which.
For example, classical logic proves "$p$ or not $p$" for every statement $p$.
Intuitionistic logic does not, because it would then have to prove $p$ or prove "not $p$".

### L2 human

1. Suppose $\vdash_{\mathsf{i}} \neg \neg p \vee \neg p$.
2. By item 1, $\vdash \neg \neg p$ or $\vdash \neg p$.
3. The valuation $p = $ false refutes $\neg \neg p$, and $p = $ true refutes $\neg p$. Both are classically refuted.
4. So $\mathsf{IPC} \nvdash \neg p \vee \neg \neg p$: weak excluded middle is not intuitionistic.

The typical use of the property is to show that a disjunction is not provable.
A trap: the property is about theorems; it says nothing about $\Gamma \vdash \varphi \vee \psi$ for arbitrary premises $\Gamma$.

### L3 human

Proofs fall into three families: cut elimination, gluing of models, and slash or realizability.
The gluing proof shows that the class of rooted models is closed under adding a common root below two models.
Algebraically, the disjunction property says that the free Heyting algebra is well connected: $x \vee y = 1$ implies $x = 1$ or $y = 1$.
