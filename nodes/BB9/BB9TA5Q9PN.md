---
tag: BB9TA5Q9PN
kind: statement
role: theorem
name: Blok-Esakia theorem
msc: ["03B45", "03B55", "06D20"]
topics: [SPQVNPZDTB]
audience: research
uses: [BXVNEN55MR, EZ011FT3GT, 2Q8E4GQF3B, Q11N8X99FK, NG943XNQWH, BDEX7HET71]
about: [EZ011FT3GT, 2Q8E4GQF3B, Q11N8X99FK]
proofs: [2SZS6SSTA5]
history:
  first_stated: "Blok and Esakia, independently, 1970s"
  notes: "Esakia also proved that Grz is the greatest modal companion of intuitionistic logic."
sources:
  - url: https://en.wikipedia.org/wiki/Modal_companion
    locator: Blok–Esakia isomorphism
  - url: https://en.wikipedia.org/wiki/Modal_companion
    locator: Modal companions
  - url: https://en.wikipedia.org/wiki/Interior_algebra
    locator: Heyting algebras
---

## Statement

Classical logic is intuitionistic logic plus $p \vee \neg p$, and its translation is $\square p \vee \square \neg \square p$.
Adding that formula to Grzegorczyk's logic gives $\mathsf{Triv}$, the logic of one reflexive point.
The theorem says that every intuitionistic logic has exactly one such partner above $\mathsf{Grz}$, and that the partners are ordered in the same way.

A *superintuitionistic logic* is a set of intuitionistic formulas that contains [[intuitionistic propositional logic|Q11N8X99FK]] $\mathsf{IPC}$ and is closed under modus ponens and uniform substitution.
These logics, ordered by inclusion, form a lattice $\mathrm{Ext}(\mathsf{IPC})$.
Let $\mathrm{NExt}(\mathsf{Grz})$ be the lattice of normal modal logics that contain [[Grzegorczyk's logic|2Q8E4GQF3B]], inside [[the lattice of normal modal logics|EZ011FT3GT]].
Here $\mathsf{Grz}$ is $\mathsf{S4}$ plus the axiom $\square(\square(p \to \square p) \to p) \to p$.
Let $T$ be the [[Gödel-McKinsey-Tarski translation|BXVNEN55MR]].
For a superintuitionistic logic $L$, let $\sigma L$ be the least normal modal logic that contains $\mathsf{Grz}$ and every $T(A)$ with $A \in L$.
For a normal extension $M$ of $\mathsf{S4}$, let $\rho M$ be the set of intuitionistic formulas $A$ with $M \vdash T(A)$.

**Theorem.** The map $\sigma$ is a lattice isomorphism from $\mathrm{Ext}(\mathsf{IPC})$ onto $\mathrm{NExt}(\mathsf{Grz})$, and its inverse is the restriction of $\rho$ to $\mathrm{NExt}(\mathsf{Grz})$.
In particular, $\rho \sigma L = L$ for every superintuitionistic logic $L$, and $\sigma \rho M = M$ for every $M \in \mathrm{NExt}(\mathsf{Grz})$.

The proof is in [[the proof of the Blok-Esakia theorem|2SZS6SSTA5]].

## Remarks

### Why Grz

The base $\mathsf{Grz}$ cannot be replaced by $\mathsf{S4}$.
The logics $\mathsf{S4}$ and $\mathsf{Grz}$ both have $\rho M = \mathsf{IPC}$, so $\rho$ is not injective on the extensions of $\mathsf{S4}$.
The base also cannot prove the translation of a non-theorem of $\mathsf{IPC}$.
For example, $\mathsf{S4.2}$ proves $T(\neg p \vee \neg \neg p)$, so no extension of $\mathsf{S4.2}$ is sent to $\mathsf{IPC}$ by $\rho$.

### What it gives you

Each superintuitionistic logic $L$ has $\sigma L$ as its greatest modal companion, and $\mathsf{Grz}$ is the greatest modal companion of $\mathsf{IPC}$.
Under $\sigma$, the logic $\mathsf{KC}$ of weak excluded middle goes to $\mathsf{Grz.2}$, and the Gödel-Dummett logic $\mathsf{LC}$ goes to $\mathsf{Grz.3}$.
The least companions of $\mathsf{IPC}$, $\mathsf{KC}$, $\mathsf{LC}$ and classical logic are $\mathsf{S4}$, $\mathsf{S4.2}$, $\mathsf{S4.3}$ and $\mathsf{S5}$.

Any property defined from the order alone transfers along $\sigma$.
Jankov showed that $\mathrm{Ext}(\mathsf{IPC})$ has $2^{\aleph_0}$ elements, so $\mathrm{NExt}(\mathsf{Grz})$ has $2^{\aleph_0}$ elements too.
Classical logic is the only coatom of $\mathrm{Ext}(\mathsf{IPC})$, since every consistent superintuitionistic logic is contained in it.
So $\mathsf{Triv}$ is the only coatom of $\mathrm{NExt}(\mathsf{Grz})$.

### The fibers of rho

The map $\rho$ is defined on all normal extensions of $\mathsf{S4}$, and it is onto $\mathrm{Ext}(\mathsf{IPC})$ by the theorem.
The fiber of $\rho$ over $L$ is the set of modal companions of $L$, the interval $[\tau L, \sigma L]$.
Here $\tau L$ is $\mathsf{S4}$ plus every $T(A)$ with $A \in L$.
So the theorem picks the top element of each fiber, and these tops form exactly $\mathrm{NExt}(\mathsf{Grz})$.
The map $\tau$ is injective, since $\rho \tau L = L$, but it is not onto, since $\mathsf{Grz}$ is not $\tau L$ for any $L$.

### Algebraic form

The theorem is also a lattice isomorphism between the varieties of [[Heyting algebras|NG943XNQWH]] and the varieties of Grz-algebras.
These are the [[interior algebras|BDEX7HET71]] that satisfy the Grz equation.
Versions of the theorem exist for intuitionistic modal logics and their bimodal companions.

### Watch out

The map $\sigma$ adds $\mathsf{Grz}$, not $\mathsf{S4}$.
Different modal logics can have the same intuitionistic fragment, and only the largest of them lies in the range of $\sigma$.

### Try it

1. Compute $\rho\, \mathsf{Triv}$.
2. Show that $\mathsf{S5}$ is not in $\mathrm{NExt}(\mathsf{Grz})$, though $\rho\, \mathsf{S5}$ is classical logic.

Answers.
For 1, $\mathsf{Triv}$ proves $\square \varphi \leftrightarrow \varphi$, so $T(A)$ is equivalent to $A$ read classically, and $\rho\, \mathsf{Triv}$ is classical logic.
For 2, write $\mathsf{CPC}$ for classical logic.
Then $\mathsf{S5} = \tau\, \mathsf{CPC}$, and $\mathsf{S5}$ lies inside $\mathsf{Triv}$.
Since $\rho$ preserves inclusion, $\mathsf{CPC} = \rho \tau\, \mathsf{CPC} \subseteq \rho\, \mathsf{S5} \subseteq \rho\, \mathsf{Triv} = \mathsf{CPC}$.
But the two-point cluster is an $\mathsf{S5}$ frame that refutes the Grz axiom, as in L2 below, so $\mathsf{S5}$ does not contain $\mathsf{Grz}$.

## History

Blok and Esakia proved the theorem independently in the 1970s.
Blok's proof is algebraic, through varieties of interior algebras, and Esakia's uses the duality between Heyting algebras and Esakia spaces.
The theory of modal companions, with the maps $\tau$ and $\sigma$, grew at the same time in work of Esakia, Maksimova and Rybakov.

## Explanations

### L1 human

Intuitionistic logics are logics of proof, and modal logics above $\mathsf{Grz}$ are logics of a special "necessarily".
The theorem says that the two families match one to one.
Each intuitionistic logic has exactly one partner above $\mathsf{Grz}$.
The partners are ordered in the same way, so any fact about the order of one family is a fact about the other.

### L2 human

Take the two-point cluster: points $x$ and $y$ that see each other and themselves.
It is a frame for $\mathsf{S5}$.
Its up-sets are only $\emptyset$ and $\{x, y\}$, so intuitionistically it behaves like one point and validates classical logic.
Now let $p$ be true only at $x$.
Then $\square p$ fails at both points, so $p \to \square p$ fails at $x$, and $\square(p \to \square p)$ fails everywhere.
So $\square(\square(p \to \square p) \to p)$ holds everywhere, while $p$ fails at $y$, and the Grz axiom fails at $y$.
The intuitionistic side cannot tell the cluster from a point, and $\mathsf{Grz}$ is the axiom that rules clusters out.

### L3 human

The isomorphism comes from the free Boolean extension.
Every Heyting algebra $H$ generates a Boolean algebra $B(H)$ with an interior operator whose open elements are $H$, and $B(H)$ is a Grz-algebra.
Blok's lemma says that every Grz-algebra satisfies the same equations as its subalgebra generated by open elements.
So Grz-varieties are determined by their Heyting algebras of open elements.
On the dual side, Esakia's proof uses [[Esakia duality|CD9Y7YP4EJ]] between Heyting algebras and Esakia spaces.
