---
tag: BGNGQWVS6R
kind: example
name: Relevance indices in the natural deduction of Anderson and Belnap
msc: ["03B47", "03F03"]
topics: [98QF5J4W16]
audience: research
instance_of: [KXTCZ2FY5M]
uses: [KXTCZ2FY5M]
sources:
  - url: https://plato.stanford.edu/entries/logic-relevance/
    locator: 4 Proof Theory
    note: Mares, Relevance Logic, Stanford Encyclopedia of Philosophy, revision of 2020-11-13
  - book: isbn:9780691071923
    note: Anderson and Belnap, Entailment, The Logic of Relevance and Necessity, volume 1
---

## Example

In the natural deduction system of Anderson and Belnap for $\mathbf{R}$, each line carries a set of numbers, its *indices*.
The indices name the hypotheses that the line really uses.
The rules, as the SEP entry gives them, are:

1. A new hypothesis gets a new number $k$ and the index set $\set{k}$.
2. From $A_a$ and $(A \rightarrow B)_b$, the rule $\rightarrow$E gives $B_{a \cup b}$.
3. If $B_a$ is derived under the hypothesis $A_{\set{k}}$ and $k \in a$, the rule $\rightarrow$I gives $(A \rightarrow B)_{a \setminus \set{k}}$.
4. From $A_a$ and $B_a$, with the same index set, the rule $\wedge$I gives $(A \wedge B)_a$.

We derive the assertion axiom $A \rightarrow ((A \rightarrow B) \rightarrow B)$.

1. $A_{\set{1}}$, hypothesis.
2. $(A \rightarrow B)_{\set{2}}$, hypothesis.
3. $B_{\set{1, 2}}$, by $\rightarrow$E on lines 1 and 2.
4. $((A \rightarrow B) \rightarrow B)_{\set{1}}$, by $\rightarrow$I on lines 2 to 3, since $2 \in \set{1, 2}$.
5. $A \rightarrow ((A \rightarrow B) \rightarrow B)$ with the empty index set, by $\rightarrow$I on lines 1 to 4, since $1 \in \set{1}$.

## Remarks

The empty index set on the last line means that the formula is a theorem.
The SEP entry also derives contraction $(A \rightarrow (A \rightarrow B)) \rightarrow (A \rightarrow B)$, in which hypothesis $2$ is used twice.
This works because index sets do not count uses; the SEP entry states that contraction-free systems use multisets of indices instead.

## Explanations

### L1 human

Each line of the proof carries a label that lists the assumptions it really uses.
We may close an assumption only if its number is in the label.
So no proof can bring in an assumption that it never uses.

### L2 human

We try to derive $A \rightarrow (B \rightarrow B)$ and see where the rules block it.

1. $A_{\set{1}}$, hypothesis.
2. $B_{\set{2}}$, hypothesis.
3. $\rightarrow$I on lines 2 to 2 gives $(B \rightarrow B)_{\emptyset}$, since $2 \in \set{2}$.
4. $\rightarrow$I on lines 1 to 3 needs $1$ in the index set $\emptyset$ of line 3, so it is blocked.
5. The trick of the SEP entry forms $(A \wedge B)$ from $A_{\set{1}}$ and $B_{\set{2}}$ to get $B_{\set{1, 2}}$.
6. The rule $\wedge$I forbids this, since the index sets $\set{1}$ and $\set{2}$ differ.

The typical use of indices is to make the informal idea "the premise is really used" exact.
A trap: indices are sets, not multisets, so a hypothesis may be used twice, and $\mathbf{R}$ keeps contraction.
