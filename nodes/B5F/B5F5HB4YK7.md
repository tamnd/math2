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

Removing the cuts from a derivation can make it longer by a tower of exponentials, and no elementary function bounds this growth.
Let $2_0(n) = n$ and $2_{k+1}(n) = 2^{2_k(n)}$, so $2_k(n)$ is a tower of $k$ twos with $n$ on top.
The *size* of a derivation is its number of sequents, and its *length* is its number of symbols.
For part 2, the language has the constant $0$, the function symbols $S$, $+$ and $e$, read as $x \mapsto 2^x$, and the predicate symbols $=$ and $I$.
Let $s_0 = 0$ and $s_{k+1} = e(s_k)$, so the value of $s_k$ in the natural numbers is $2_k(0)$.
For a finite set $T$ of sentences, let $S_\ell$ be the sequent $T, I(0), \forall x\, (I(x) \to I(S x)) \Rightarrow I(s_\ell)$ of [[LK|PZX9J3VEMT]].

1. **Upper bound.** In the one-sided propositional calculus of the [[cut-elimination theorem|AYRZ98Y0NW]], a derivation of height $h$ and cut rank $r$ turns into a cut-free derivation of height at most $2_r(h)$.
2. **Lower bound.** There is a finite set $T$ of universal sentences without $I$ that are true in the natural numbers, together with the equality axioms for $I$ and the function symbols, such that for every $\ell \geq 1$:
   - (a) $S_\ell$ has an LK derivation, with cuts, of length at most $2^{c \ell}$, for a constant $c$ that does not depend on $\ell$;
   - (b) every cut-free LK derivation of $S_\ell$ has size greater than $2_\ell(0)$.
3. **No elementary bound.** There is no [[elementary function|RJ3MCAAZSV]] $f$ such that every sequent with an LK derivation of length $n$ has a cut-free LK derivation of length at most $f(n)$.

## Remarks

### A first look at the numbers

The terms $s_k$ name the values of a tower of twos.
Compute them one at a time:
$$s_1 = 2^0 = 1, \quad s_2 = 2^1 = 2, \quad s_3 = 2^2 = 4, \quad s_4 = 2^4 = 16, \quad s_5 = 2^{16} = 65536.$$
For $\ell = 5$, part 2 gives a derivation with cuts of length at most $2^{5c}$, while every cut-free derivation has more than $65536$ sequents.
For $\ell = 6$, the derivation with cuts grows by the factor $2^c$, but the cut-free size passes $2^{65536}$.
That number has $19729$ digits.
Check: $65536 \cdot \log_{10} 2 \approx 65536 \cdot 0.30103 \approx 19728.3$, so $2^{65536}$ has $19728 + 1$ digits.

### Why each hypothesis is needed

The lower bound is about first-order sequents.
For propositional LK the gap is at most exponential, because backward search in [[G3cp|KP5KA51FC4]] gives every tautology of length $n$ a cut-free derivation of size at most exponential in $n$.

The cut rank matters as well.
When the cut rank $r$ is fixed, part 1 bounds the cut-free height by a tower of fixed height $r$, and that is an elementary function of $h$.
So the short derivations of part 2(a) must cut on formulas whose degree grows with $\ell$, and they do: they cut on the formulas $\psi_i$ of the [[proof|FZF2NPMSKS]].

Part 2(b) counts sequents and part 3 counts symbols.
The two fit together because every sequent has at least one symbol, the arrow, so the length of a derivation is at least its size.

### What it gives you

Cut-free proofs, and the Herbrand disjunctions that you read off from them, can be far too long to write down, even for short theorems.
So the size of a proof is not a reliable measure of the size of the witnesses that it contains.
In [[proof complexity|1Q046J0AW2]], the theorem separates LK from cut-free LK by more than any elementary function.

### How far the bound can be pushed

Part 3 cannot be strengthened to "no primitive recursive bound".
The standard proofs of cut elimination for first-order LK bound the cut-free derivation by a tower whose height and top grow at most linearly in the length of the derivation with cuts.
A function such as $n \mapsto 2_n(n)$ is primitive recursive, so a primitive recursive bound exists.

### Generalizations

Orevkov's form of the lower bound works in predicate logic without function symbols.
Samuel Buss sharpened the lower bounds, so that the height of the tower nearly matches the upper bound as a function of the degree of the cut formulas.
Boolos's curious inference, published in 1987, is a related example: it has a short proof in second-order logic, but every derivation of it in a standard first-order system is far too long to write down.

### Watch out

The theorem is about the worst case.
It does not say that cut elimination makes every derivation much longer.
A cut on an axiom $A \Rightarrow A$ disappears in one step and the derivation gets shorter.

A second slip is to count only the steps of the derivation with cuts.
Its cut formulas double in length at each level, since $\psi_{i+1}$ contains two copies of $\psi_i$.
So its length is exponential in $\ell$, and the theorem compares this $2^{c \ell}$ with the tower $2_\ell(0)$, not $\ell$ with the tower.

### Try it

Compute $2_3(1)$.
The answer is $16$, since $2_1(1) = 2$, $2_2(1) = 2^2 = 4$ and $2_3(1) = 2^4 = 16$.

Check the identity $2_k(2^m) = 2_{k+1}(m)$ for $k = 2$ and $m = 1$.
Both sides equal $16$: the left side is $2^{2^2} = 16$, and the right side is $2_3(1) = 16$ from the first exercise.

## History

Richard Statman and Vladimir Orevkov proved, independently and in work published in 1979, that cut elimination has no elementary bound.
Orevkov's examples need no function symbols.
Samuel Buss later sharpened the lower bounds in his paper *Sharpened lower bounds for cut elimination*.

## Explanations

### L1 human

A lemma can shorten a proof enormously.
The theorem says how much: if you remove all the lemmas from a proof, it can grow by a tower of powers of $2$.
The tower $2^{2^{2^2}}$ is $65536$, which already has $5$ digits.
The next level, $2^{65536}$, has $19729$ digits.
So a proof that fits on a page can turn into a proof that no computer could store.

### L2 human

Here is the mechanism for $\ell = 3$, where $s_3$ has the value $4$.
The formula $\psi_1(a)$ says that $I$ is closed under adding $2^a$, and $\psi_2(a)$ says that $\psi_1$ is closed under adding $2^a$.
The derivation with cuts proves $\psi_3(0)$, then $\psi_2(1)$, then $\psi_1(2)$, and finally $I(4)$, so it climbs one quantifier level for each level of the tower.
The middle claim $\psi_1(2)$ says that $I$ is closed under adding $4$, and with $I(0)$ it gives $I(4)$ in one step.
A cut-free derivation has no such lemmas.
It must use the instances $I(0) \to I(1)$, $I(1) \to I(2)$, $I(2) \to I(3)$ and $I(3) \to I(4)$ one at a time.
For $\ell = 5$ it needs $65536$ instances, and the derivation with cuts needs only two more levels.
The typical use of the theorem is as a warning: cut-free proofs are analytic, but analytic does not mean feasible.

### L3 human

The theorem shows that cut compresses proofs with non-elementary strength.
The short derivations cut on formulas with more and more quantifiers, and each new quantifier lifts closure under one operation to closure under its iterate.
The lower bounds use the Herbrand content of cut-free derivations: a cut-free derivation from a universal hypothesis must name every instance that it uses.
The same gap appears between normal and non-normal proofs in natural deduction, through the [[normalization theorem|W33WAE1XTC]].
These results are one reason to study analytic proof formats other than cut-free sequent derivations, such as [[deep inference|4ZW0SHW2RG]].
