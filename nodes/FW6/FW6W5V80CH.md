---
tag: FW6W5V80CH
kind: example
name: Type raising in the full Lambek calculus
msc: ["03B47", "03F05"]
topics: [98QF5J4W16]
audience: research
instance_of: [V5XVVN16GS]
uses: [Q47701D0E1]
sources:
  - url: https://en.wikipedia.org/wiki/Categorial_grammar
    locator: Lambek calculus
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 2.3 The Lambek Calculus
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
---

## Example

Let $A$ and $B$ be formulas.
The sequent $A \Rightarrow (B / A) \backslash B$ is derivable in the [[full Lambek calculus|Q47701D0E1]] $\mathsf{FL}$, without any structural rule.

1. $A \Rightarrow A$ and $B \Rightarrow B$ are axioms.
2. The rule ${/}\mathrm{L}$, from $\Gamma \Rightarrow A$ and $\Delta, B, \Sigma \Rightarrow \Pi$ infer $\Delta, B / A, \Gamma, \Sigma \Rightarrow \Pi$, with $\Gamma = A$ and $\Delta$, $\Sigma$ empty, gives $B / A, A \Rightarrow B$.
3. The rule ${\backslash}\mathrm{R}$, from $C, \Gamma \Rightarrow D$ infer $\Gamma \Rightarrow C \backslash D$, with $C = B / A$ and $\Gamma = A$, gives $A \Rightarrow (B / A) \backslash B$.

## Remarks

The example shows that $\mathsf{FL}$ proves a nontrivial law without exchange, weakening or contraction.
The mirror law $A \Rightarrow B / (A \backslash B)$ is derivable in the same way, with ${\backslash}\mathrm{L}$ and then ${/}\mathrm{R}$.
In a residuated lattice the law says $a \leq (b / a) \backslash b$, which is equivalent by residuation to $(b / a) \cdot a \leq b$.
In categorial grammar, with $A = np$ and $B = s$, the law turns a noun phrase into a functor that takes a verb phrase; see [[type raising in the Lambek calculus|DEAVBXZNX7]].

## Explanations

### L1 human

Type raising says: anything of type $A$ can also act on things that need an $A$.
Think of a key and a lock that needs that key.
The key "is" also a thing that opens such a lock.
The law needs no copying and no reordering of hypotheses.

### L2 human

We check the law in the residuated lattice $(\mathbb{Z}, \leq, +, 0)$, where $b / a = b - a$ and $a \backslash b = b - a$.

1. $(b / a) \backslash b = b - (b - a) = a$.
2. So the law says $a \leq a$, which is true.
3. In the lattice of languages over $\set{x, y}$ with concatenation, take $a = \set{x}$ and $b = \set{yx}$.
   Then $b / a = \set{y}$, since $w \cdot x \in \set{yx}$ only for $w = y$.
4. Then $(b / a) \backslash b$ is the set of words $w$ with $y w \in \set{yx}$, which is $\set{x}$, so the law says $\set{x} \subseteq \set{x}$.

The typical use of type raising is to change the type of a word so that it combines with its neighbors.
A trap: the order of $B / A$ and $A$ in step 2 is fixed, and $A, B / A \Rightarrow B$ is not derivable for atoms.
