---
tag: B5F5HB4YK7
kind: statement
role: theorem
name: Complexity of cut elimination
msc: ["03F05", "03F20"]
topics: [R10RMQCJQX]
audience: research
uses: [AYRZ98Y0NW, PZX9J3VEMT, RJ3MCAAZSV]
about: [HGVMPZ2DXA, 1Q046J0AW2]
proofs: [FZF2NPMSKS]
sources:
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
    locator: Cut elimination
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: lead section
history:
  first_stated: "1979"
  notes: "Statman and Orevkov proved that cut elimination has no elementary bound in work published in 1979."
---

## Statement

Let $2_0(n) = n$ and $2_{k+1}(n) = 2^{2_k(n)}$, so $2_k(n)$ is a tower of $k$ twos with $n$ on top.
The *size* of a derivation is its number of sequents, and its *length* is its number of symbols.
For part 2, the language has the constant $0$, function symbols $S$, $+$ and $e$, read as $x \mapsto 2^x$, and the predicate symbols $=$ and $I$.
Let $s_0 = 0$ and $s_{k+1} = e(s_k)$, so the value of $s_k$ in the natural numbers is $2_k(0)$.
For a finite set $T$ of sentences, let $S_\ell$ be the sequent $T, I(0), \forall x\, (I(x) \to I(S x)) \Rightarrow I(s_\ell)$ of [[LK|PZX9J3VEMT]].

1. **Upper bound.** In the one-sided propositional calculus of the [[cut-elimination theorem|AYRZ98Y0NW]], a derivation of height $h$ and cut rank $r$ turns into a cut-free derivation of height at most $2_r(h)$.
2. **Lower bound.** There is a finite set $T$ of universal sentences without $I$ that are true in the natural numbers, together with the equality axioms for $I$ and the function symbols, such that for every $\ell \geq 1$:
   - (a) $S_\ell$ has an LK derivation, with cuts, of length at most $2^{c \ell}$, for a constant $c$ that does not depend on $\ell$;
   - (b) every cut-free LK derivation of $S_\ell$ has size greater than $2_\ell(0)$.
3. **No elementary bound.** There is no [[elementary function|RJ3MCAAZSV]] $f$ such that every sequent with an LK derivation of length $n$ has a cut-free LK derivation of length at most $f(n)$.

## Remarks

### Why each hypothesis is needed

The lower bound is for cut-free derivations of first-order sequents.
For propositional LK, the gap is at most exponential: backward search in [[G3cp|KP5KA51FC4]] gives every tautology of length $n$ a cut-free derivation of size at most exponential in $n$.
The cuts in part 2(a) are on the formulas $\psi_i$ of the proof, whose quantifier nesting grows with $i$.
If the cut formulas have bounded nesting, part 1 and its first-order form give an elementary bound.

### Consequences

- Cut-free proofs, and the Herbrand disjunctions read off from them, can be too long to write down, even for short theorems.
- The size of a proof is not a reliable measure of the size of its witnesses.
- In [[proof complexity|1Q046J0AW2]], the result separates LK from cut-free LK by more than any elementary function.

### Converse

Part 3 cannot be strengthened to "no primitive recursive bound".
The first-order form of part 1 bounds the cut-free size by a tower whose height and top are at most linear in the length, and $n \mapsto 2_n(n)$ is primitive recursive.

### Generalizations

For first-order LK, the bound of part 1 holds in a similar form: a tower whose height grows with the largest nesting of a cut formula.
Buss sharpened the lower bound, so that the height of the tower nearly matches the upper bound as a function of the depth of the cut formulas.
Boolos gave a first-order inference, called Boolos's curious inference, that has a short derivation with cuts or in second-order logic and no feasible cut-free derivation.

## History

Statman and Orevkov proved superexponential lower bounds for cut elimination, in work published in 1979.
Orevkov's result is for predicate logic without function symbols.
Samuel Buss later gave sharpened lower bounds in his paper *Sharpened lower bounds for cut elimination*.

## Explanations

### L1 human

A lemma can shorten a proof enormously.
This theorem says how much: removing all lemmas from a proof can make it longer by a tower of powers of $2$.
The tower $2^{2^{2^2}}$ already has $5$ digits, and the next level has $19729$ digits.

### L2 human

To see why the lower bound holds, count instances.
A cut-free derivation of $S_\ell$ must use the axiom $I(x) \to I(Sx)$ at many values of $x$, one step at a time from $0$ up to the value of $s_\ell$.
The derivation with cuts avoids this by proving that $I$ is closed under adding $2^x$, then under adding $2^{2^x}$, and so on.
A trap is to measure length by the number of steps only: the formulas $\psi_i$ of the short derivation have length exponential in $i$.

### L3 human

The theorem shows that cut is a source of compression of non-elementary strength.
The short derivations use a cut on a formula with more quantifiers to lift closure under one operation to closure under its iterate.
Lower bounds use the Herbrand content of cut-free derivations: a cut-free derivation of a universal hypothesis must name all the instances it uses.
These results are a reason to study analytic proof formats other than cut-free sequent derivations, such as [[deep inference|4ZW0SHW2RG]].
