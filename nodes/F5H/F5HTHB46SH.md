---
tag: F5HTHB46SH
kind: concept
name: Epsilon substitution method
msc: ["03F05", "03F30"]
topics: [R10RMQCJQX]
audience: research
uses: [TH5ZKCKN3W, 0QFT7Z76N5, P1RW6JWX73, KT50SMH3EC]
sources:
  - url: https://en.wikipedia.org/wiki/Epsilon_calculus
    locator: Epsilon substitution method
  - url: https://en.wikipedia.org/wiki/Wilhelm_Ackermann
    locator: Bibliography
---

## Summary

The epsilon substitution method proves consistency by trial and error: guess numbers for the witnesses that a proof talks about, and repair each guess that some axiom shows to be wrong.
If the repairs always stop, every line of every proof comes out numerically true, so no proof ends in $0 = 1$.
Exactly: a proof in a theory of the [[epsilon calculus|TH5ZKCKN3W]] is turned into a quantifier-free proof from finitely many *critical formulas*, such as $A(t) \to A(\varepsilon x\, A(x))$.
A *substitution* assigns numbers to finitely many closed $\varepsilon$-terms and $0$ to all others.
Each step takes a false critical formula and gives its $\varepsilon$-term the least witness that the formula shows to exist.
A substitution that makes all the critical formulas true is a *solving substitution*, and the method is correct when it reaches one.

## Motivation

Take the critical formula $2 + 1 = 3 \to e + 1 = 3$, where $e$ is $\varepsilon x\, (x + 1 = 3)$, "the least $x$ with $x + 1 = 3$".
Start by giving $e$ the value $0$.
The premise $2 + 1 = 3$ is true and the conclusion $0 + 1 = 3$ is false, so the formula is false.
But its premise tells us that $2$ is a witness, so we search below it: $0 + 1 = 1$, $1 + 1 = 2$, $2 + 1 = 3$.
The least witness is $2$, we give $e$ the value $2$, and now the formula is true.

A consistency proof for [[Peano arithmetic|0QFT7Z76N5]] has to show that no proof ends in $0 = 1$.
The quantifiers range over all natural numbers, so their meaning is not finite, and that is what [[Hilbert's program|P1RW6JWX73]] wanted to avoid.
The epsilon calculus replaces each quantifier by a term that names a witness, and the substitution method is a finite search for numbers that make the witness terms behave.
Consistency becomes the termination of a computable process, which is the kind of statement Hilbert hoped to prove by finitary means.

## Notation

We take the language of arithmetic with $0$, $S$, $+$ and $\cdot$, extended by $\varepsilon$-terms.
In arithmetic, $\varepsilon x\, A(x)$ is read as the least $x$ with $A(x)$, or $0$ when there is none.
Besides $A(t) \to A(\varepsilon x\, A(x))$, a critical formula of a second kind expresses minimality, in one common form $A(t) \to \neg(t < \varepsilon x\, A(x))$.
A substitution evaluates a closed term from the inside out: once the closed subterms of an $\varepsilon$-term have numerals as values, it gives the resulting $\varepsilon$-term its value.
The process of Hilbert and Ackermann is often called the H-process.

## Remarks

### Why a solving substitution gives consistency

Suppose a proof of $0 = 1$ uses the critical formulas $C_1, \ldots, C_k$, and replace its free variables by $0$.
If a substitution makes $C_1, \ldots, C_k$ true, it makes every line of the proof true, because the other axioms are true numerical identities and the rules keep truth.
That is impossible for the last line $0 = 1$.
So if the process finds a solving substitution for every finite set of critical formulas, the theory is consistent.
Each single step is computable: it evaluates finitely many closed terms and formulas, and it searches for a least witness below a known bound.

### One term, then nested terms

For one term, the [[worked example|7PMV3HXK0K]] runs both kinds of critical formula for $e$ and stops after one step at the value $2$.
When no $\varepsilon$-term occurs inside another, each term changes at most once, because its least witness is final, so the process stops after at most as many steps as there are terms.

Nesting breaks this.
With $e_1 = \varepsilon y\, (y = 2)$ and $e_2 = \varepsilon x\, (x > e_1)$, a [[change of the inner term|GHJSNQ4VQW]] changes which term $e_2$ stands for, and an earlier repair is lost.
In that example the process needs three steps if we repair $e_2$ first, and two if we repair $e_1$ first.
In a long proof such losses can pile up, and the whole difficulty of the method is to show that they stop.

### What it is not

[[Gentzen's consistency proof|QPV0HNP22S]] for Peano arithmetic assigns no values to terms; it transforms derivations and gives them ordinals, as the [[non-example|JJ0FFJ5NYE]] checks.
A cut-elimination proof, as in the [[cut-elimination theorem|AYRZ98Y0NW]], also transforms derivations rather than values.
Taking the true least witness in $\mathbb{N}$ for every $\varepsilon$-term makes all critical formulas true at once, but it is not a step of the method, since such values cannot in general be computed.

### Strength of the method

For full first-order arithmetic, Ackermann proved in 1940 that the process stops, by induction up to [[epsilon nought|KT50SMH3EC]], and this gives the consistency of Peano arithmetic.
The termination proof cannot be formalized in Peano arithmetic itself.
If it could, Peano arithmetic would prove its own consistency, against [[Gödel's second incompleteness theorem|4PZM5GJTR5]].

### Watch out

A common slip is to think that each step makes more critical formulas true.
A new value can make other critical formulas false, as step 7 of the nested example shows, and those must be repaired again.
A second slip is to take any witness instead of the least one.
With $e = \varepsilon x\, (x > 3)$, the value $5$ makes $5 > 3 \to e > 3$ true, but then the second-kind formula $4 > 3 \to \neg(4 < e)$ is false.
A third is to think that the termination proof is finitary in Hilbert's sense; for arithmetic it needs transfinite induction up to $\varepsilon_0$.

### Try it

First, run the method on $5 > 3 \to e > 3$ with $e = \varepsilon x\, (x > 3)$, starting from $0$.
The formula is false at $0$, the witness $5$ bounds the search, and the least $m$ with $m > 3$ is $4$, so $e$ gets the value $4$.

Second, why does $7 + 1 = 3 \to e + 1 = 3$ need no step at all?
Its premise is false, so the implication is true for every value of $e$.

### History

Hilbert proposed the method in the 1920s as part of his program, and Ackermann's dissertation of 1924 gave a first consistency argument with it, which turned out to cover only a fragment of arithmetic.
Hilbert and Bernays presented the epsilon calculus in the second volume of *Grundlagen der Mathematik* in 1939.
Ackermann proved the consistency of full arithmetic by the method in *Mathematische Annalen* in 1940.
Later work, by Mints and others, gave new termination proofs and extended the method to stronger theories.

## Explanations

### L1 human

Suppose a long argument uses some unknown numbers, each described as "the smallest number with a certain property".
We do not know these numbers, so we guess $0$ for each one.
Then we check the claims of the argument that involve them.
If a claim fails, the failure shows us a number with the property, and we improve our guess.
For "the smallest number $x$ with $x + 1 = 3$", the guess $0$ fails, and the check shows that $2$ works.
Hilbert's hope was that the guessing always ends, and then the argument cannot prove a false statement.

### L2 human

Here is the method on the two critical formulas for $e = \varepsilon x\, (x + 1 = 3)$ with $t = 2$.
$$C_1 : 2 + 1 = 3 \to e + 1 = 3, \qquad C_2 : 2 + 1 = 3 \to \neg(2 < e).$$
At $e = 0$, $C_1$ is false and $C_2$ is true, since $\neg(2 < 0)$ holds.
Repair $C_1$ with the least witness $2$.
At $e = 2$, $C_1$ holds since $2 + 1 = 3$, and $C_2$ holds since $\neg(2 < 2)$.
Check: no number below $2$ is a witness, since $0 + 1 = 1$ and $1 + 1 = 2$.
In a consistency proof, the critical formulas come from a given proof, and the process must stop for all of them together.

### L3 human

The method is a form of learning in the limit: each $\varepsilon$-term changes its value finitely often, and the final values are reached after finitely many changes.
Its termination proofs are a form of [[ordinal analysis|C5E5TG8PGP]], since they assign ordinals to the stages of the process and show that the ordinals decrease.
The first epsilon theorem, proved by eliminating critical formulas, is closely related, and its extended form gives [[Herbrand's theorem|VZ21F10WRS]].
The method also connects with Kreisel's no-counterexample interpretation, in which a counterexample function is improved step by step in a similar way.
