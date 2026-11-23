---
tag: D8SGFVA3RT
kind: statement
role: theorem
name: Self-verifying theories
msc: ["03F30", "03F40", "03F25"]
topics: [HXHHWY3328]
audience: research
about: [92SWXST1ZM, 4NBAX3VRQ7]
uses: [4PZM5GJTR5, 4NBAX3VRQ7, 3K1AKGXF8A, MPSCREYC3M, WQ1ZE255SF, 3PRW76471J, VM8TQ70CVJ]
sources:
  - url: https://en.wikipedia.org/wiki/Self-verifying_theories
    locator: lead section
history:
  notes: "Self-verifying theories were introduced and studied by Dan Willard. The main reference is Willard, 'Self-verifying axiom systems, the incompleteness theorem and related reflection principles', Journal of Symbolic Logic 66(2), 2001; a sequel, 'How to extend the semantic tableaux and cut-free versions of the second incompleteness theorem almost to Robinson's arithmetic Q', appeared in the same journal, 67(1), 2002."
---

## Statement

$\mathsf{PA}$ does not prove the sentence "no proof from my axioms ends in $0 = 1$", by Gödel's second theorem.
Dan Willard found weaker theories of arithmetic that do prove such a sentence about themselves, and are consistent.
They escape Gödel's theorem because they do not prove that multiplication is total, and because proofs are tableaux.

Exactly: there are first-order theories $W$ of arithmetic with the following properties.

1. The language of $W$ has subtraction and division as function symbols, and addition and multiplication are predicates defined from them.
2. $W$ is [[consistent|VM8TQ70CVJ]].
3. $W$ proves its own consistency, where provability is expressed by an arithmetic formula that describes closed analytic tableaux from the axioms of $W$.
4. $W$ does not prove the $\Pi_2$ sentence that says that multiplication is total, so $W$ contains neither [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$ nor [[Peano arithmetic|MPSCREYC3M]].
5. Any true $\Pi_1$ sentence of arithmetic can be added to $W$ while keeping it consistent.

Theories with these properties are called self-verifying.
A cited outline of the proof is in [[the proof of the existence of self-verifying theories|7ZAZDWRTAB]].

## Remarks

### Why each feature is needed

Compare with [[Gödel's second incompleteness theorem|4PZM5GJTR5]]: a consistent theory $T$ with decidable axioms that contains $\mathsf{PA}$ does not prove $\mathrm{Con}(T)$.
Willard's theories differ from such $T$ in three ways.

The base is weak.
$W$ does not contain $\mathsf{Q}$, because it does not prove that multiplication is total.
The usual diagonal argument of the incompleteness theorems uses the totality of multiplication, so it is not available inside $W$.

The language matters.
With subtraction and division as the basic operations, the axioms of $W$ speak about addition and multiplication as relations, without asserting that every product of two numbers exists.
With multiplication as a function symbol, its totality would be a law of logic.

The notion of proof matters.
Consistency is stated for tableau proofs, which are cut-free.
For weak theories, consistency statements for different proof systems need not be equivalent, because the translation between proof systems uses arithmetic that $W$ does not have.
The title of Willard's 2002 paper says that versions of the second incompleteness theorem for tableaux and cut-free proofs reach theories close to $\mathsf{Q}$; we do not state its precise results here.

### What it gives you

The hypothesis of enough arithmetic in the second incompleteness theorem cannot be dropped: some consistent arithmetic theories do prove their own tableau consistency.
By property 5, a self-verifying theory can also contain strong true statements, for example $\mathrm{Con}(\mathsf{PA})$, which is a true $\Pi_1$ sentence.

### Converse

The statement is an existence result, so it has no direct converse.
The related question "which theories can prove their own consistency?" has a negative side.
By the second incompleteness theorem, no consistent theory with decidable axioms that contains $\mathsf{PA}$ proves its own consistency in the usual sense.

### Generalizations

Willard studied a family of such systems with different base axioms and different notions of proof.
He also studied the boundary between the systems that can prove their own consistency and those that cannot.
We do not state these boundary results here.

### Watch out

Do not read "$W$ proves its own consistency" as "$W$ proves $\mathrm{Con}(W)$" with the Hilbert-style consistency statement of the incompleteness theorems.
Willard's statement is about tableau proofs, and the two statements need not be equivalent in $W$.

## History

Dan Willard introduced self-verifying theories in a paper of 2001 in the Journal of Symbolic Logic.
A paper of 2002 in the same journal extended the tableau version of the second incompleteness theorem almost to $\mathsf{Q}$.

## Explanations

### L1 human

Gödel showed that a good system of axioms for arithmetic cannot prove that it is free of contradictions.
"Good" includes being able to add and multiply any two numbers.
Willard asked what happens if the system is a little weaker: it can subtract and divide, but it does not claim that every two numbers have a product.
He found such systems that can prove "I am free of contradictions".
So Gödel's theorem really needs the totality of multiplication.

### L2 human

Compare a self-verifying theory $W$ with $\mathsf{Q}$.
$\mathsf{Q}$ has $+$ and $\cdot$ as function symbols, so $\mathsf{Q} \vdash \forall x \, \forall y \, \exists z \, (z = x \cdot y)$ by pure logic.
$W$ does not prove the corresponding sentence with its multiplication predicate.
The [[diagonal lemma|3PRW76471J]] holds in every theory that contains $\mathsf{Q}$, and it is the first step of the proof of the second incompleteness theorem.
$W$ proves the sentence "there is no tableau proof of $0 = 1$ from the axioms of $W$", and this sentence is true.
The typical use is to locate the strength of arithmetic that Gödel's second theorem needs.
Watch out: the consistency that $W$ proves is tableau consistency, not the Hilbert-style $\mathrm{Con}(W)$.

### L3 human

Self-verifying theories show that the second incompleteness theorem is a statement about a threshold of arithmetic strength, not about self-reference as such.
The analysis is close to [[bounded arithmetic|RA380RWEC0]] and to the study of weak fragments, where cut elimination and the totality of fast-growing functions are tied to consistency statements.
Willard's systems prove their consistency in a cut-free sense.
Proof systems with cut can shorten proofs a lot, and the step from cut-free proofs to proofs with cut uses functions that the weak theory does not prove total.
This links the topic with [[Gödel's speed-up theorem|37X5XBDBNX]], where the price of a consistency statement is measured in the length of proofs.
