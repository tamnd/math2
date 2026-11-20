---
tag: V0MZVC2XA9
kind: concept
name: Contraction
aliases: [contraction-rule]
msc: ["03F05", "03B47"]
topics: [98QF5J4W16]
audience: grad
uses: [PZX9J3VEMT, W72CA3R9MP]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_rule
    locator: Common structural rules
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 1.4 Contraction
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
  - url: https://en.wikipedia.org/wiki/Affine_logic
    locator: lead section
  - url: https://plato.stanford.edu/entries/logic-relevance/
    locator: 5. Some Systems of Relevance Logic
    note: Mares, Relevance Logic, Stanford Encyclopedia of Philosophy, revision of 2020-11-13
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 6.1 Different treatments of modality
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
  - doi: 10.1070/IM1982v018n01ABEH001382
    locator: pages 41-59
    note: Grišin, Predicate and set-theoretic calculi based on logic without contractions, Mathematics of the USSR Izvestiya 18 (1982)
---

## Summary

*Contraction* is the structural rule of a [[sequent calculus|W72CA3R9MP]] that merges two copies of a formula into one: from $\Gamma, A, A \Rightarrow \Delta$ infer $\Gamma, A \Rightarrow \Delta$, and the same on the right; see [[the definition|VGS1GCM047]].
It says that a hypothesis may be used more than once.
In Hilbert style it corresponds to the axiom $(A \to (A \to B)) \to (A \to B)$, and in residuated lattices to the inequality $x \leq x \cdot x$.
Logics without contraction, such as [[linear logic|2P2184B6HE]] and [[affine logic|K67C2N2QAH]], count the uses of each hypothesis, and they block [[Curry's paradox|40Q1NK471S]].

## Motivation

A proof may need the same hypothesis twice: to prove $A \wedge A$ from $A$ with a split context, or to apply $A \to (A \to B)$ to $A$ twice.
Contraction allows this reuse, and in classical logic it is harmless.
When a hypothesis is a resource, reuse is a real cost, so contraction is the rule to control.
Contraction is also the rule behind the paradoxes of naive set theory: Curry's paradox uses it, and without it these paradoxes cannot be derived.

## Notation

In [[LK|PZX9J3VEMT]] the rules are named CL and CR.
In one-sided sequents the rule reads: from $\vdash \Gamma, A, A$ infer $\vdash \Gamma, A$.
In linear logic the rule is restricted to formulas $?A$ and is named $?C$.
In the names $\mathsf{FL}_c$ and $\mathsf{FL}_{ec}$, the letter $c$ stands for contraction.
The Hilbert axiom $(A \to (A \to B)) \to (A \to B)$ is often called $\mathrm{W}$, after the combinator $\mathrm{W}xy = xyy$.

## Remarks

### Examples

1. In LJ, contraction derives $(p \to (p \to q)) \to (p \to q)$, and also $p \to p \wedge p$ with the split rule for $\wedge$.
2. Curry's paradox derives every formula from naive comprehension, and its key step is contraction; see [[Curry's paradox uses contraction|40Q1NK471S]].
3. In linear logic, contraction on $?$-formulas derives $!A \multimap A \otimes A$; see [[controlled contraction in linear logic|9ZMEDB2YP4]].
4. The relevance logic $\mathbf{R}$ has contraction: its axiom list contains $(A \to (A \to B)) \to (A \to B)$.

### Non-examples

1. In linear logic without exponentials, contraction is not admissible: $A \Rightarrow A \otimes A$ fails; see [[the sequent A to A tensor A|V444A285N3]].
2. In [[affine logic|K67C2N2QAH]], contraction also fails, although weakening holds; see [[contraction fails in affine logic|DPKJWDD7XN]].
3. In the three-element MV-algebra $\set{0, \tfrac12, 1}$, fusion is $\max(0, x + y - 1)$, so $\tfrac12 \cdot \tfrac12 = 0 < \tfrac12$, and $x \leq x \cdot x$ fails.

### Basic properties

1. Contraction is sound in a residuated lattice exactly when $x \leq x \cdot x$ for all $x$; see [[the definition|VGS1GCM047]].
2. With weakening and contraction, fusion equals meet in an integral residuated lattice, so the logic is intuitionistic in its $\cdot$, $\wedge$ part; see [[intuitionistic logic is not substructural|YAQY3P8BT0]].
3. In a cut-free derivation without contraction, each premise of a rule has fewer connectives and constants than the conclusion.
   So proof search terminates; this is the source of the [[decidability of MALL|BNRWJB2R8C]].
4. The reduction of a cut against a contracted formula duplicates a subproof.
   So with contraction, cut elimination can make a proof much larger.

### History

Wikipedia reports that Grišin used affine logic in 1974 and 1981, having observed that Russell's paradox cannot be derived without contraction, even with unrestricted comprehension.
Grišin's paper on predicate and set-theoretic calculi without contraction appeared in English in 1982.
The Stanford Encyclopedia of Philosophy entry on relevance logic lists Grišin, Brady, Restall and Priest among those who drop contraction to block Curry's paradox.

### Common errors

1. Thinking that contraction is harmless because "$A$ and $A$" says the same as "$A$".
   In a resource reading, two copies of a resource are more than one.
2. Confusing contraction with idempotence of a connective.
   In linear logic $A \mathbin{\&} A$ and $A$ prove each other, but $A \otimes A$ and $A$ do not.
3. Thinking that dropping contraction makes a logic weak.
   Linear logic recovers all of intuitionistic logic through the exponential $!$.

## Explanations

### L1 human

Contraction says: a fact that we may use twice, we may also use once.
In ordinary reasoning a fact does not wear out, so this is fine.
With money it is not fine: two coins are not one coin.
Logics without contraction count the copies of each hypothesis.

### L2 human

We derive $\Rightarrow (p \to (p \to q)) \to (p \to q)$ in LJ, and we mark the step that needs contraction.

1. Axioms: $p \Rightarrow p$ and $q \Rightarrow q$.
2. The rule ${\to}\mathrm{L}$ gives $p \to q, p \Rightarrow q$.
3. ${\to}\mathrm{L}$ again, with the axiom $p \Rightarrow p$, gives $p \to (p \to q), p, p \Rightarrow q$.
4. Exchange XL moves the two copies of $p$ to the front, and contraction CL merges them: $p, p \to (p \to q) \Rightarrow q$.
5. The rule ${\to}\mathrm{R}$ on the leftmost $p$ gives $p \to (p \to q) \Rightarrow p \to q$, and ${\to}\mathrm{R}$ again gives $\Rightarrow (p \to (p \to q)) \to (p \to q)$.

The typical use of contraction is to apply one hypothesis at two places of a proof.
A trap: in step 3 the two copies of $p$ come from two different axioms, and only contraction can identify them.

### L3 human

Contraction is the existence of diagonal maps $A \to A \otimes A$ in a category of proofs.
In linear logic these maps exist for $!A$, which is a commutative comonoid; this is why $!$ is called an exponential, since $!(A \mathbin{\&} B) \cong {!A} \otimes {!B}$.
Because cut elimination duplicates subproofs at contractions, [[light linear logics|E7JVJSSWBT]] restrict the exponential rules to get normalization in polynomial time.
In the theory of sets and truth, logics without contraction allow naive comprehension or naive truth without triviality, which is a theme of the later sub-area on paraconsistent logics.
