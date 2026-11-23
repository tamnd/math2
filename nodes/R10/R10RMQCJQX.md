---
tag: R10RMQCJQX
kind: topic
name: Structural proof theory
msc: ["03F03", "03F05", "03F07"]
topics: [DYJ0KGTPMR]
---

## Summary

Structural proof theory is the part of [[mathematical logic|DYJ0KGTPMR]] that studies formal proofs as combinatorial objects, by transforming them into normal forms.
The story starts with a single rule.
In the sequent calculus, cut lets a proof use a lemma $A$ and then forget it, and Gentzen's Hauptsatz of 1934 and 1935 says that every cut can be removed.
A cut-free proof uses only pieces of what it proves, the subformula property, and this one fact gives consistency, decision procedures, the midsequent theorem and Herbrand's theorem.
Prawitz found the same phenomenon in natural deduction in 1965, where a detour, an introduction followed at once by an elimination, can always be removed.
The price is size, since removing cuts can make a proof non-elementarily longer, as Statman and Orevkov showed in 1979.
Two further questions follow.
Which rules deserve to define a connective is the question of harmony and proof-theoretic semantics, and Prior's tonk shows that the answer is not "any".
Which other logics admit cut elimination is answered by refined calculi: contraction-free, hypersequent, display, labeled and deep inference systems, and focused proofs for proof search.
The sub-area ends with two older and newer threads, Hilbert's epsilon substitution method and the open problem of when two proofs are the same.

## Remarks

### Reading order

1. [[Proof theory|N4EDJNMTEF]]: an overview of the field, from Hilbert's program to proof complexity, and a first consistency argument.
2. [[Cut rule|HGVMPZ2DXA]]: the rule for the use of a lemma, in its two forms, and why it is admissible but not derivable.
3. [[Cut-elimination theorem|AYRZ98Y0NW]]: Gentzen's Hauptsatz, with the mix proof and the rank-reduction proof.
4. [[Subformula property|Z2NXKDK06G]]: what cut-free proofs contain, and why this gives decision procedures.
5. [[Normalization theorem for natural deduction|W33WAE1XTC]]: Prawitz's detour reductions, normal proofs and strong normalization.
6. [[Midsequent theorem|1FPWTGE14W]]: the sharpened Hauptsatz for prenex sequents, and Herbrand's theorem.
7. [[Inversion lemma|EXMS77F2XN]]: which rules can be read backwards without loss, and proof search without backtracking.
8. [[Contraction-free sequent calculi|KP5KA51FC4]]: Kleene's G3 calculi and Dyckhoff's LJT.
9. [[Complexity of cut elimination|B5F5HB4YK7]]: the upper bound by a tower of exponentials, and a matching lower bound.
10. [[Proof-theoretic semantics|K97KZB5R7N]]: meaning given by rules, harmony and tonk.
11. [[Hypersequent calculus|3PR9PEMXJ4]]: sequents in parallel, and the communication rule.
12. [[Display calculus|1X7D5CBXB7]]: Belnap's display property and his general cut-elimination theorem.
13. [[Labeled sequent calculus|VW8XP95XCB]]: Kripke semantics written into the rules.
14. [[Deep inference|4ZW0SHW2RG]]: rules applied inside formulas.
15. [[Focusing|AMMKNENT3R]]: proof search with phases of invertible and non-invertible rules.
16. [[Identity of proofs|G7B4XWMS7Q]]: the open problem of when two proofs are the same.
17. [[Epsilon substitution method|F5HTHB46SH]]: Hilbert's method for consistency proofs with epsilon-terms.

### Prerequisites

- [[Proof systems for first-order logic|TTCRX3NFNY]], with the [[sequent calculus LK and LJ|PZX9J3VEMT]] and [[natural deduction|PAQ4ZX2TX1]].
- [[The propositional calculus|JDK63589SA]] and [[first-order languages and syntax|PSRDJXRW53]], for formulas, substitution and subformulas.
- [[Structures, satisfaction and truth|NJDME6F845]], for the soundness arguments.
