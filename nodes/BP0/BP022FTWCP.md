---
tag: BP022FTWCP
kind: statement
role: theorem
name: Realization theorem for S4
msc: ["03B45", "03F45"]
topics: [CQM9SRN8PM]
audience: research
uses: [5HKWCXEFG1, N60RVXSA5W, W72CA3R9MP]
about: [5HKWCXEFG1, N60RVXSA5W]
proofs: [YSNQ7EG4AK]
history:
  first_stated: "Artemov, 1995"
  notes: "Artemov proved the theorem with a cut-free sequent calculus for S4; later proofs use semantic methods."
sources:
  - url: https://en.wikipedia.org/wiki/Sergei_N._Artemov
    locator: Research
  - book: isbn:9781108424912
    locator: "Artemov and Fitting, Justification Logic: Reasoning with Reasons"
---

## Statement

Every theorem of $\mathsf{S4}$ can be rewritten so that each box names an explicit proof, and the result is a theorem of the logic of proofs.
For example, axiom $\mathsf{K}$ becomes $x{:}(p \to q) \to (y{:}p \to (x \cdot y){:}q)$.

Let $\mathsf{LP}$ be the logic of proofs of [[justification logic|5HKWCXEFG1]], with the total constant specification.
For an $\mathsf{LP}$ formula $\varphi$, the forgetful projection $\varphi^\circ$ is the modal formula obtained by replacing every subformula $t{:}\psi$ by $\square\psi$, from the inside out.

A realization of a modal formula $A$ is an $\mathsf{LP}$ formula $A^r$ obtained by replacing each occurrence of $\square$ in $A$ by a term, so that $(A^r)^\circ = A$.
An occurrence of $\square$ is negative when it lies in the antecedent of an odd number of implications, with $\neg B$ read as $B \to \bot$.
A realization is normal when all negative occurrences of $\square$ get distinct proof variables.
Then the following hold.

1. If $\mathsf{LP} \vdash \varphi$, then $\mathsf{S4} \vdash \varphi^\circ$.
2. If $\mathsf{S4} \vdash A$, then $\mathsf{LP} \vdash A^r$ for some normal realization $r$.

So [[S4|N60RVXSA5W]] is exactly the forgetful projection of $\mathsf{LP}$, that is, $\mathsf{S4} = \{\varphi^\circ : \mathsf{LP} \vdash \varphi\}$.
[[The proof|YSNQ7EG4AK]] gives part 1 in full and part 2 with one lemma cited.

## Remarks

### Why each hypothesis is needed

The constant specification must contain $c{:}A$ for the axioms used.
With the empty specification, $\square(p \to p)$ is an $\mathsf{S4}$ theorem with no realization.
Every term $t$ gives a formula $t{:}(p \to p)$ that fails in an evidence model with $\mathcal{E}(t, p \to p) = \emptyset$.

Part 2 asks for more than some realization, since the realization must be normal.
This is what makes it meaningful, because otherwise one variable could stand for proofs of two unrelated hypotheses.

The axiom $t{:}\varphi \to {!t}{:}(t{:}\varphi)$ is needed for the axiom $\mathsf{4}$.
Without $!$, the projection is the logic $\mathsf{T}$, not $\mathsf{S4}$.

### What it gives you

Combined with the Gödel translation of intuitionistic logic into $\mathsf{S4}$ and the arithmetical completeness of $\mathsf{LP}$, the theorem gives a provability semantics for intuitionistic propositional logic in the sense of Brouwer, Heyting and Kolmogorov.
Every $\mathsf{S4}$ theorem has an explicit version in which each "provable" names a proof built from the proofs of the hypotheses.
The negative boxes can be read as "for every proof $x$", and the positive ones as "there is a proof, given by a term in these $x$".

### The converse

Part 1 is the converse of part 2: the projection of an $\mathsf{LP}$ theorem is an $\mathsf{S4}$ theorem.
So the theorem is an equivalence.
A stronger converse fails, since not every realization of an $\mathsf{S4}$ theorem is an $\mathsf{LP}$ theorem.
For example $x{:}p \to x{:}(p \wedge p)$ is not, as [[the non-example|RA808VJGHJ]] shows.

### Generalizations

Realization theorems hold for $\mathsf{K}$, $\mathsf{T}$, $\mathsf{K4}$, $\mathsf{D}$, $\mathsf{S5}$ and many other modal logics, with matching justification logics.
Fitting gave a semantic proof through a canonical evidence model, which avoids cut elimination.

## History

Artemov stated and proved the theorem in 1995, with a proof that extracts terms from a cut-free derivation in a [[sequent calculus|W72CA3R9MP]] for $\mathsf{S4}$.
The full account, with arithmetical completeness of $\mathsf{LP}$, appeared in the Bulletin of Symbolic Logic in 2001.

## Explanations

### L1 human

The logic $\mathsf{S4}$ talks about "provable" without naming any proof.
The theorem says that every law of $\mathsf{S4}$ can be rewritten so that each "provable" names an explicit proof.
The names are built from the proofs that we are given, by combining them.
For example, "if $p$ is provable, then $p$ or $q$ is provable" becomes "if $x$ proves $p$, then this combination of $x$ with a fixed step proves $p$ or $q$".

### L2 human

We realize $\square(p \to q) \to (\square p \to \square q)$.
The two boxes in the antecedents are negative, so they get variables, $x{:}(p \to q)$ and $y{:}p$.
The box of $\square q$ is positive, so it gets a term.
The application axiom gives $x{:}(p \to q) \to (y{:}p \to (x \cdot y){:}q)$, so the realization uses $x$, $y$ and $x \cdot y$, and it is an axiom of $\mathsf{LP}$.

The typical use of the theorem is to turn an $\mathsf{S4}$ argument about knowledge or provability into an argument with explicit evidence.
Watch out: a realization must keep the structure, and giving the two negative boxes the same variable makes a different, and often unprovable, formula.

### L3 human

The theorem says that the box of $\mathsf{S4}$ is an existential quantifier over proofs, and that this quantifier can be Skolemized by terms built from $\cdot$, $+$ and $!$.
This is close to Herbrand's theorem and to the extraction of witnesses from proofs.
The cut-free proof is constructive and gives an algorithm, and the size of the realizations it produces can be large.
Semantic proofs use canonical Fitting models, and they extend to logics where no cut-free calculus is known.
