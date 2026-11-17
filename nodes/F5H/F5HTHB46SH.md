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

The epsilon substitution method is Hilbert's method for proving the consistency of a theory written in the [[epsilon calculus|TH5ZKCKN3W]].
A proof in the theory is first turned into a proof of a quantifier-free formula from finitely many critical formulas, such as $A(t) \to A(\varepsilon x\, A(x))$.
A *substitution* assigns natural numbers to finitely many closed $\varepsilon$-terms, and every other $\varepsilon$-term gets the value $0$.
The method changes the substitution step by step: it takes a false critical formula, and it gives its $\varepsilon$-term the least witness that the false critical formula shows to exist.
When no critical formula is false, every formula of the proof is true, so the proof cannot end in $0 = 1$.
The method matters because it reduces consistency to the termination of a finite trial-and-error process, which is the kind of argument [[Hilbert's program|P1RW6JWX73]] asked for.

## Motivation

A consistency proof for [[Peano arithmetic|0QFT7Z76N5]] must show that no proof ends in $0 = 1$.
The quantifiers range over all natural numbers, and so their meaning is not finite.
The epsilon calculus replaces each quantifier by a term that names a witness.
If we could give each witness term a number that makes the finitely many critical formulas of a proof true, the proof would be numerically correct.
The substitution method is a search for such numbers.

## Notation

We take the language of arithmetic with $0$, $S$, $+$ and $\cdot$, extended by $\varepsilon$-terms.
For arithmetic, $\varepsilon x\, A(x)$ is read as the least $x$ with $A(x)$, or $0$ if there is none.
Besides $A(t) \to A(\varepsilon x\, A(x))$, a critical formula of a second kind expresses this minimality, in one common form $A(t) \to \neg(t < \varepsilon x\, A(x))$.
A substitution $S$ evaluates a closed term from the inside out: once the closed subterms of an $\varepsilon$-term have numerals as values, $S$ gives the value of the resulting $\varepsilon$-term.
A substitution under which all critical formulas of a proof are true is a *solving substitution*.
The process of Hilbert and Ackermann is often called the H-process.

## Remarks

### Examples

- One critical formula with $A(x)$ the equation $x + 1 = 3$: the process starts with the value $0$ and stops after one step with the value $2$, see [[this example|7PMV3HXK0K]].
- Two nested $\varepsilon$-terms, $\varepsilon y\, (y = 2)$ and $\varepsilon x\, (x > \varepsilon y\, (y = 2))$: a change of the inner term changes the outer one, see [[this example|GHJSNQ4VQW]].
- If no $\varepsilon$-term occurs inside another one, each $\varepsilon$-term is changed at most once, so the process stops after at most as many steps as there are $\varepsilon$-terms.
- For full first-order arithmetic, Ackermann proved in 1940 that the process stops, and this gives the consistency of Peano arithmetic.

### Non-examples

- [[Gentzen's consistency proof|QPV0HNP22S]] for Peano arithmetic does not assign values to terms. It transforms derivations, see [[this non-example|JJ0FFJ5NYE]].
- Taking the value of $\varepsilon x\, A(x)$ to be the true least witness in the natural numbers makes all critical formulas true at once. It is not a substitution in the sense of the method, since these values cannot in general be computed.
- A cut-elimination proof for pure logic, as in the [[cut-elimination theorem|AYRZ98Y0NW]], removes cuts from derivations and assigns no values to terms.

### Basic properties

- Let a proof of $0 = 1$, with its free variables replaced by $0$, use the critical formulas $C_1, \ldots, C_k$. If $S$ makes $C_1, \ldots, C_k$ true, then $S$ makes every line of the proof true, since the other axioms are true numerical identities and the rules keep truth. This is impossible for $0 = 1$.
- So if the process finds a solving substitution for every finite set of critical formulas, the theory is consistent.
- In the case of the third example: let $\varepsilon x\, A(x)$ get the least $m$ with $A(m)$, where $A$ has no $\varepsilon$-terms. Then all its critical formulas of both kinds are true, and no later step changes $A$ or $m$.
- Each single step can be computed: it evaluates finitely many closed terms and formulas, and it searches for a least witness below a known bound.
- The termination proof for Peano arithmetic cannot be formalized in Peano arithmetic. Such a proof would give a proof of the consistency of Peano arithmetic in itself, against [[Gödel's second incompleteness theorem|X9WYNYE29C]].

### History

Hilbert proposed the method in the 1920s as part of his program, and Ackermann's dissertation of 1924 gave a first consistency argument with it.
That argument turned out to cover only a fragment of arithmetic.
Hilbert and Bernays presented the epsilon calculus and its theorems in the second volume of *Grundlagen der Mathematik* in 1939.
Ackermann proved the consistency of full arithmetic by the method in *Mathematische Annalen* 117, in 1940, with induction up to [[epsilon nought|KT50SMH3EC]].
Later work, by Mints and others, gave new termination proofs and extended the method to stronger theories.

### Common errors

- Thinking that each step makes more critical formulas true. A new value can make other critical formulas false, and those must be repaired later.
- Choosing any witness, not the least one. Then the critical formulas of the second kind can stay false.
- Thinking that the termination proof is finitary in Hilbert's original sense. For arithmetic it needs transfinite induction up to $\varepsilon_0$.

## Explanations

### L1 human

Suppose a long argument uses some unknown numbers, each described as "the smallest number with a certain property".
We do not know these numbers, so we guess $0$ for each one.
Then we check the claims of the argument that involve them.
If a claim fails, the failure shows us a number with the property, and we improve our guess.
For example, for "the smallest number $x$ with $x + 1 = 3$", the guess $0$ fails, and the check shows that $2$ works.
Hilbert's hope was that the guessing always ends, and then the argument cannot prove a false statement.

### L2 human

We run the method on one critical formula.

1. Take $A(x)$ to be $x + 1 = 3$ and $t = 2$. The critical formula is $2 + 1 = 3 \to \varepsilon x\, A(x) + 1 = 3$.
2. Start with $S_0$, which gives $\varepsilon x\, A(x)$ the value $0$. The premise $2 + 1 = 3$ is true, and the conclusion $0 + 1 = 3$ is false.
3. So the critical formula is false, and $t = 2$ is a witness for $A$.
4. The least $m \leq 2$ with $m + 1 = 3$ is $m = 2$. Set $S_1(\varepsilon x\, A(x)) = 2$.
5. Under $S_1$, the conclusion $2 + 1 = 3$ is true, so the critical formula is true, and the process stops.

The typical use is in a consistency proof: the critical formulas come from a given proof, and the process must stop for all of them together.
A trap is to expect one pass to be enough: with nested terms, a later step can make an earlier critical formula false again.

### L3 human

The method is a form of learning in the limit: each $\varepsilon$-term changes its value finitely often, and the final values are reached after finitely many changes.
Its termination proofs are a form of [[ordinal analysis|C5E5TG8PGP]], since they assign ordinals to the stages of the process and show that the ordinals decrease.
The first epsilon theorem, proved by eliminating critical formulas, is closely related, and its extended form gives [[Herbrand's theorem|VZ21F10WRS]].
The method also connects with Kreisel's no-counterexample interpretation, where a counterexample function is improved step by step in a similar way.
