---
tag: JM1XJXWZYH
kind: statement
role: theorem
name: Heyting algebra semantics of intuitionistic logic
msc: ["03B20", "06D20", "03G10"]
topics: [38EQ20GR7M]
audience: grad
uses: [NG943XNQWH, 52XCYMK0WW, MGCVQXXQJH, GTS4DRRMZR, AJNZJD8442, 5083DHSK82]
about: [Q11N8X99FK, NG943XNQWH, H5NSKEP3P2]
proofs: [RQ0C4BC1KS]
sources:
  - url: https://en.wikipedia.org/wiki/Intuitionistic_logic
    locator: Heyting algebra semantics
  - url: https://en.wikipedia.org/wiki/Heyting_algebra
    locator: Heyting algebras as applied to intuitionistic logic
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Semantics
---

## Statement

Let $H$ be a [[Heyting algebra|NG943XNQWH]] with bottom $0$, top $1$ and implication $\to$.
A *valuation* in $H$ is a map $v$ from the propositional variables to $H$.
It extends to all formulas by $v(\bot) = 0$, $v(\varphi \wedge \psi) = v(\varphi) \wedge v(\psi)$, $v(\varphi \vee \psi) = v(\varphi) \vee v(\psi)$ and $v(\varphi \to \psi) = v(\varphi) \to v(\psi)$.
A formula $\varphi$ is *valid in* $H$ if $v(\varphi) = 1$ for every valuation $v$.

A *superintuitionistic logic* is a set of formulas that contains $\mathsf{IPC}$ and is closed under modus ponens and uniform substitution.
For such a logic $L$, let $\mathbf{V}(L)$ be the class of Heyting algebras in which every formula of $L$ is valid.
For a class $K$ of Heyting algebras, let $\mathrm{Log}(K)$ be the set of formulas valid in every member of $K$.

**Theorem.**

1. Soundness: if $\mathsf{IPC} \vdash \varphi$, then $\varphi$ is valid in every Heyting algebra.
2. The [[Lindenbaum algebra|MGCVQXXQJH]] of $\mathsf{IPC}$, the set of formulas modulo provable equivalence, is a Heyting algebra. It is the [[free Heyting algebra|GTS4DRRMZR]] on the classes $[p]$ of the variables.
3. Completeness: if $\varphi$ is valid in every Heyting algebra, then $\mathsf{IPC} \vdash \varphi$. It suffices that $\varphi$ is valid in the Lindenbaum algebra.
4. For every superintuitionistic logic $L$, the class $\mathbf{V}(L)$ is a [[variety|AJNZJD8442]] and $\mathrm{Log}(\mathbf{V}(L)) = L$.
5. For every variety $K$ of Heyting algebras, $\mathrm{Log}(K)$ is a superintuitionistic logic and $\mathbf{V}(\mathrm{Log}(K)) = K$.
6. So $\mathbf{V}$ and $\mathrm{Log}$ are inverse lattice anti-isomorphisms between superintuitionistic logics and varieties of Heyting algebras.

The proof is in [[the proof by the Lindenbaum algebra|RQ0C4BC1KS]].

## Remarks

### Why each hypothesis is needed

1. Uniform substitution is needed in item 4. The set of consequences of the variable $p$ is closed under modus ponens, but it is not the logic of any class of algebras.
2. Item 6 includes the inconsistent logic, the set of all formulas. It corresponds to the trivial variety of one-element algebras, because $\bot$ is valid only there.
3. The [[intermediate logics|H5NSKEP3P2]] are the consistent ones. They correspond to the nontrivial varieties.

### Consequences

1. Classical logic corresponds to the variety of [[Boolean algebras|0XADJKM699]], since $p \vee \neg p$ is valid in a Heyting algebra exactly when it is Boolean.
2. A formula $\varphi$ is a theorem of $\mathsf{IPC}$ if and only if the equation $\varphi \approx 1$ holds in all Heyting algebras. So questions about $\mathsf{IPC}$ become questions about equations.
3. The [[topological semantics|RKFTMQNWRC]] is the special case of the algebras of open sets.
4. The three-element chain refutes excluded middle; see [[the three-element chain|G4S6HY9SHK]].

### Converse

Items 1 and 3 form a biconditional.
Item 4 and item 5 are converse to each other.

### Generalizations

1. The same method gives completeness of intuitionistic predicate logic for complete Heyting algebras, with $\exists$ and $\forall$ read as joins and meets.
2. For a set $\Gamma$, $\Gamma \vdash_{\mathsf{i}} \varphi$ if and only if every valuation that sends $\Gamma$ to $1$ sends $\varphi$ to $1$.
3. Each superintuitionistic logic has its own Lindenbaum algebra, which is free in its variety.

## Explanations

### L1 human

Classical logic uses two truth values, true and false.
Intuitionistic logic uses truth values from a Heyting algebra, which can have many values between false and true.
The theorem says that the provable formulas are exactly those that get the top value under every choice of values.
The algebra built from the formulas themselves is enough to catch every formula that is not provable.

### L2 human

1. Take the three-element chain $0 < a < 1$, with $x \to y = 1$ if $x \leq y$ and $x \to y = y$ otherwise.
2. Put $v(p) = a$. Then $v(\neg p) = a \to 0 = 0$.
3. So $v(p \vee \neg p) = a \neq 1$, and by item 1, $\mathsf{IPC} \nvdash p \vee \neg p$.

The typical use of item 1 is to refute a formula in a small algebra, and of item 6 to study logics by their algebras.
A trap: in a Heyting algebra $\neg \neg x$ need not equal $x$; it does here only when $x$ is $0$ or $1$.

### L3 human

The correspondence of item 6 is the propositional case of algebraic logic, where a logic is studied through its equivalent algebraic semantics.
Properties of logics become properties of varieties: Craig interpolation becomes a form of amalgamation, and the disjunction property relates to well-connected algebras.
By Birkhoff's theorem, each variety is generated by its subdirectly irreducible members, which for Heyting algebras have a second greatest element.
