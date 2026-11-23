---
tag: 7ZAZDWRTAB
kind: proof
name: Proof of the existence of self-verifying theories, a cited outline
msc: ["03F30", "03F40"]
topics: [HXHHWY3328]
audience: research
proves: D8SGFVA3RT
uses: [4NBAX3VRQ7, WQ1ZE255SF, 3PRW76471J, 6M12VR1GT6, 4A84VHDTHV]
methods: [0NTF6DMVAP, V2H30SA654]
sources:
  - url: https://en.wikipedia.org/wiki/Self-verifying_theories
    locator: lead section
---

## Proof

The plan: put the sentence "I am consistent" into the theory as an axiom, and then show that the resulting theory is consistent.
The first part is easy, and the second is the hard part of Willard's work.

This is an outline of Willard's construction in "Self-verifying axiom systems, the incompleteness theorem and related reflection principles", Journal of Symbolic Logic 66(2), 2001.
Steps 1 to 4 describe the construction, and we omit the details of the axioms.
Steps 5 and 6 are proved in full.
Step 7, the consistency of the theory, is cited and not outlined.

### The construction

1. Language (outlined).
   Take a language of arithmetic with constants for small numbers and with subtraction and division as function symbols.
   Define addition and multiplication as predicates $\mathrm{Add}(x, y, z)$ and $\mathrm{Mult}(x, y, z)$ from them; we omit Willard's exact definitions.
   There is no function symbol for addition or multiplication, so the totality of these operations is not a law of logic.
2. Base axioms (outlined).
   Take a set $A$ of axioms, all true in $\mathbb{N}$, that describe the basic properties of the operations.
   In Willard's analysis any true $\Pi_1$ sentence can be added to $A$ while keeping consistency; this is property 5 of the statement.
3. Proofs as tableaux (outlined).
   Code formulas and analytic tableaux by numbers, as in the [[arithmetization of syntax|6M12VR1GT6]].
   Write a formula $\mathrm{Tab}(y, x)$ that says "$y$ codes a closed tableau that refutes the sentence with code $x$ from the axioms".
   The coding is chosen so that the formula makes sense in the weak language of step 1, without the totality of multiplication.
4. The self-referential axiom (outlined).
   Let $\theta$ be a sentence that says "there is no tableau proof of $0 = 1$ from $A$ together with $\theta$".
   Such a sentence is obtained by a diagonal construction in the metatheory, as in the [[diagonal lemma|3PRW76471J]]; the construction is a computation on codes and is not carried out inside the theory.
   Let $W = A \cup \{ \theta \}$.

### Self-verification and consistency

5. $W$ proves its own tableau consistency (proved).
   The tableau consistency statement of $W$ is the sentence "there is no tableau proof of $0 = 1$ from $A \cup \{ \theta \}$", which is $\theta$.
   Since $\theta$ is an axiom of $W$, $W \vdash \theta$ by a one-line proof.
6. $W$ is consistent if and only if $\theta$ is true in $\mathbb{N}$ (proved).
   Tableau proofs are sound and complete for first-order logic, by the [[soundness|4A84VHDTHV]] and [[completeness|WQ1ZE255SF]] theorems for tableaux.
   If $W$ is consistent, then no tableau proof of $0 = 1$ from $W$ exists, which is what $\theta$ says, so $\theta$ is true.
   Conversely, if $\theta$ is true, there is no tableau proof of $0 = 1$ from $W$, so by completeness $W$ has a model and is consistent.
7. $W$ is consistent (cited, not outlined).
   Willard proves this by a relative consistency argument with respect to ordinary arithmetic.
   By step 6 this is the same as the truth of $\theta$, and the content of the theorem is in this step.
   The argument uses that $A$ does not prove the totality of multiplication.
   If the base $A$ contained $\mathsf{PA}$, the [[second incompleteness theorem|4PZM5GJTR5]] would make $W$ inconsistent, because $\mathsf{PA}$ proves that tableau consistency and Hilbert-style consistency are equivalent.
8. Properties 1 to 3 of the statement follow from steps 1, 5 and 7.
   Property 4 is part of Willard's analysis (cited): $W$ does not prove the $\Pi_2$ sentence that multiplication is total.
   Then $W$ does not contain $\mathsf{Q}$, since in $\mathsf{Q}$ the totality of multiplication holds by logic.
   Property 5 is part of the same cited analysis; see step 2.

## Idea

The usual diagonal argument inside a theory uses the totality of multiplication, so the self-reference is put into an axiom from outside.
That axiom says "I am consistent", so the theory proves its own consistency at no cost.
The whole difficulty moves to the question whether the theory with this axiom is consistent, which is the same as whether the axiom is true.
The axiom is true because the base is too weak for the argument of Gödel's second theorem.

## Variants

The same pattern works with many choices of base axioms and of the notion of proof.
Willard studied a family of such systems and the boundary where self-verification fails.

With Hilbert-style proofs in place of tableaux, the corresponding statement is harder to obtain.
A Hilbert-style proof can be much shorter than any tableau proof of the same sentence, and the translation between them uses arithmetic that the weak base does not have.
