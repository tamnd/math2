---
tag: 6X2ABCND9X
kind: example
name: Internalizing a conjunction in the logic of proofs
msc: ["03B45", "03F45"]
topics: [CQM9SRN8PM]
audience: research
instance_of: [5HKWCXEFG1]
uses: [5HKWCXEFG1]
sources:
  - book: isbn:9781108424912
    locator: "Artemov and Fitting, Justification Logic: Reasoning with Reasons"
---

## Example

From a proof $x$ of $p$ and a proof $y$ of $q$ we build an explicit proof of $p \wedge q$.
In the logic of proofs $\mathsf{LP}$ of [[justification logic|5HKWCXEFG1]] the claim is the following, where $c$ is a constant with $c{:}(p \to (q \to (p \wedge q)))$.
$$\mathsf{LP} \vdash x{:}p \wedge y{:}q \to ((c \cdot x) \cdot y){:}(p \wedge q).$$

1. $p \to (q \to (p \wedge q))$ is a propositional axiom, a tautology.
2. Axiom necessitation gives $\vdash c{:}(p \to (q \to (p \wedge q)))$.
3. The application axiom with $s = c$ and $t = x$ gives $c{:}(p \to (q \to (p \wedge q))) \to (x{:}p \to (c \cdot x){:}(q \to (p \wedge q)))$.
4. Modus ponens with steps 2 and 3 gives $\vdash x{:}p \to (c \cdot x){:}(q \to (p \wedge q))$.
5. The application axiom with $s = c \cdot x$ and $t = y$ gives $(c \cdot x){:}(q \to (p \wedge q)) \to (y{:}q \to ((c \cdot x) \cdot y){:}(p \wedge q))$.
6. Chaining steps 4 and 5 by propositional logic gives the claim.

The checker axiom adds $\vdash x{:}p \to {!x}{:}(x{:}p)$, so the hypothesis $x{:}p$ itself has the proof ${!x}$.

## Remarks

Steps 1 to 6 are an instance of the lifting lemma.
From the derivation $p, q \vdash p \wedge q$, it builds the term $(c \cdot x) \cdot y$ that proves $p \wedge q$ from proofs $x$ of $p$ and $y$ of $q$.
The term mirrors the derivation, with one constant for the axiom and one application for each use of modus ponens.
With a longer derivation the term grows in the same way.

The forgetful projection is the $\mathsf{S4}$ theorem $\square p \wedge \square q \to \square(p \wedge q)$.
If the hypotheses had the same variable, $x{:}p \wedge x{:}q$, the term $(c \cdot x) \cdot x$ would work too, but the realization would no longer be normal.

## Explanations

### L1 human

Suppose that $x$ is a written proof of $p$ and $y$ is a written proof of $q$.
Then we can write a proof of "$p$ and $q$": copy both proofs and add one line.
The term $(c \cdot x) \cdot y$ is a name for this new proof.
It records that we used the rule $c$, then $x$, then $y$.

### L2 human

The recipe has three steps.
Write the propositional proof of $p \wedge q$ from $p$ and $q$ as a chain of modus ponens steps.
Replace each axiom by a constant and each hypothesis by its proof variable.
Replace each modus ponens step by an application of the two terms.

The typical use is to compute the explicit content of a modal theorem.
Watch out: the order matters, since $c \cdot x$ is applied to $y$, and $(c \cdot y) \cdot x$ is not a proof of $p \wedge q$ under the same $c$.
