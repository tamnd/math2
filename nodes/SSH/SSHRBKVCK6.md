---
tag: SSHRBKVCK6
kind: example
name: Fusion is commutative in FLe
msc: ["03F05", "03B47"]
topics: [98QF5J4W16]
audience: research
instance_of: [YAFD18WYJ8]
uses: [3ZNQNN1A45, Q47701D0E1]
sources:
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 1.2 Commutativity
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
  - book: isbn:9780444521415
    note: Galatos, Jipsen, Kowalski and Ono, Residuated Lattices
---

## Example

Let $p$ and $q$ be atoms.
The sequent $p \cdot q \Rightarrow q \cdot p$ is derivable in the [[full Lambek calculus with exchange|Q47701D0E1]], $\mathsf{FL}_e$.

1. $q \Rightarrow q$ and $p \Rightarrow p$ are axioms.
2. The right rule for fusion, from $\Gamma \Rightarrow A$ and $\Delta \Rightarrow B$ infer $\Gamma, \Delta \Rightarrow A \cdot B$, gives $q, p \Rightarrow q \cdot p$.
3. [[Exchange|3ZNQNN1A45]] gives $p, q \Rightarrow q \cdot p$.
4. The left rule for fusion, from $\Gamma, A, B, \Gamma' \Rightarrow C$ infer $\Gamma, A \cdot B, \Gamma' \Rightarrow C$, gives $p \cdot q \Rightarrow q \cdot p$.

## Remarks

The sequent is not derivable in $\mathsf{FL}$, which has no exchange.
By [[cut elimination for the full Lambek calculus|JSAH84Y9G2]], it suffices to search for a cut-free derivation.

1. The antecedent of $p \cdot q \Rightarrow q \cdot p$ is one formula.
   The right rule for fusion would need $\Rightarrow q$ or $\Rightarrow p$ with an empty antecedent, which are not derivable, since no rule ends in an atom with an empty antecedent.
2. So the last rule is the left rule for fusion, with premise $p, q \Rightarrow q \cdot p$.
3. For this premise, only the right rule for fusion applies.
   It splits $p, q$ into an initial part $\Gamma$ and a final part $\Delta$, with $\Gamma \Rightarrow q$ and $\Delta \Rightarrow p$.
4. The three splits give $\Rightarrow q$, or $p \Rightarrow q$, or $p, q \Rightarrow q$ with $\Rightarrow p$.
   Each split has a premise that is not derivable.

So exchange is exactly what the derivation needs at step 3.

## Explanations

### L1 human

In $\mathsf{FL}_e$, "$p$ and then $q$" gives "$q$ and then $p$".
The proof builds "$q$ and then $p$" from $q$ and $p$ in this order.
Then it swaps the two hypotheses, which needs the exchange rule.

### L2 human

We read the derivation in the residuated lattice $(\mathbb{Z}, \leq, +, 0)$, where fusion is addition.

1. Step 2 says $q + p \leq q + p$.
2. Step 3 uses $p + q = q + p$, since addition of integers is commutative.
3. Step 4 says $p + q \leq q + p$ for all integers $p$ and $q$, which is true.

The typical use of the example is to show that the subscript $e$ makes fusion commutative.
A trap: in step 2 the order of the premises fixes the order of the antecedent, so $q$ must come first.
