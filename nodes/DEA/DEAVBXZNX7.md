---
tag: DEAVBXZNX7
kind: example
name: Type raising in the Lambek calculus
msc: ["03B47", "03B65"]
topics: [98QF5J4W16]
audience: research
instance_of: [5FAC9KX4H0]
uses: [46AN6CZMRD]
sources:
  - url: https://en.wikipedia.org/wiki/Categorial_grammar
    locator: Lambek calculus
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 2.3 The Lambek Calculus
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
---

## Example

The sequent $np \Rightarrow s / (np \backslash s)$ is derivable in the [[Lambek calculus|46AN6CZMRD]].

1. $np \Rightarrow np$ and $s \Rightarrow s$ are axioms.
2. ${\backslash}\mathrm{L}$, from $\Gamma \Rightarrow A$ and $\Delta, B, \Sigma \Rightarrow C$ infer $\Delta, \Gamma, A \backslash B, \Sigma \Rightarrow C$, with $\Gamma = np$, $A = np$, $B = s$, gives $np, np \backslash s \Rightarrow s$.
3. ${/}\mathrm{R}$, from $\Gamma, A \Rightarrow B$ infer $\Gamma \Rightarrow B / A$, with $\Gamma = np$ and $A = np \backslash s$, gives $np \Rightarrow s / (np \backslash s)$.
4. In step 3 the list $\Gamma = np$ is nonempty, as $\mathsf{L}$ requires.

## Remarks

The example shows that a noun phrase can act as a functor that takes a verb phrase on its right.
So "John" of type $np$ also has the type $s / (np \backslash s)$, the type of a subject that waits for its verb phrase.
The same derivation with ${\backslash}\mathrm{R}$ in place of ${/}\mathrm{R}$ fails, since $np$ is on the left of $np \backslash s$; the mirror law is $np \Rightarrow (s / np) \backslash s$.
The converse sequent $s / (np \backslash s) \Rightarrow np$ passes the count check of [[the definition|46AN6CZMRD]], but it is not derivable.
In a cut-free search, the antecedent is one formula with main connective $/$, and ${/}\mathrm{L}$ needs a nonempty list $\Gamma$ to its right, which is missing.

## Explanations

### L1 human

"John" is a name, a noun phrase.
"John" can also be seen as a thing that waits for a verb phrase such as "sleeps" and then makes a sentence.
Type raising says that every noun phrase has this second type.

### L2 human

We use the raised type to parse "John sleeps".

1. The lexicon gives "John" type $np$ and "sleeps" type $np \backslash s$.
2. By the example, $np \Rightarrow s / (np \backslash s)$.
3. ${/}\mathrm{L}$ with $\Gamma = np \backslash s$, the axiom $np \backslash s \Rightarrow np \backslash s$ and the axiom $s \Rightarrow s$ gives $s / (np \backslash s), np \backslash s \Rightarrow s$.
4. Cut of step 2 with step 3 gives $np, np \backslash s \Rightarrow s$, the direct parse.

The typical use of type raising is to let a subject combine with a verb phrase by function application from the left.
A trap: type raising changes the type, not the meaning, and cut elimination removes it from any parse.
