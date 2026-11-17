---
tag: MESZ87G9ET
kind: concept
name: Herbrand analysis
aliases: [herbrand-analysis-of-proofs, herbrand-analyses, witnessing-by-herbrand-analysis]
msc: ["03F07", "03F05", "03F30"]
topics: [8XY7JYZKFW]
audience: research
uses: [VZ21F10WRS, AYRZ98Y0NW, W72CA3R9MP, 5NVA2JRHPV, 7CVJCQKY41, 0ASJVEFA9J, 0WCP0PVET6, 0DSHAVH45F, N238J43XNE]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand%27s_theorem
    locator: Generalizations of Herbrand's theorem
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Weak Kőnig's lemma WKL0
---

## Summary

*Herbrand analysis* is a method that turns a derivation of a $\Sigma_1$ formula $\exists y \, \varphi(\bar x, y)$, with $\varphi$ quantifier-free, in the arithmetic $\mathrm{I}\Sigma_1$ into a [[primitive recursive function|5NVA2JRHPV]] $f$ with $\varphi(\bar x, f(\bar x))$ for all $\bar x$.
It has four steps.
First, write $\mathrm{I}\Sigma_1$ as a [[sequent calculus|W72CA3R9MP]] with quantifier-free initial sequents and an induction rule for $\Sigma_1$ formulas.
Second, apply partial [[cut elimination|AYRZ98Y0NW]], so that every cut formula is $\Sigma_1$.
Third, observe that then every formula in the derivation is $\Sigma_1$.
Fourth, by induction on the derivation, build primitive recursive functions that compute witnesses for the existential formulas on the right of each sequent from witnesses for those on the left.
In this step the induction rule becomes a definition by primitive recursion, a case distinction becomes a definition by cases, and a cut becomes a composition.
The method matters because it extracts programs from classical proofs, and it proves that $\mathrm{I}\Sigma_1$ is $\Pi^0_2$-conservative over primitive recursive arithmetic ([[Parsons's theorem|2VYJXZZDGB]]).

## Motivation

A classical proof of $\forall x \, \exists y \, \varphi(x, y)$, with $\varphi$ decidable, always gives an algorithm: search $y = 0, 1, 2, \ldots$ until $\varphi(x, y)$ holds.
This search tells us nothing about the size of $y$ or about the cost of the computation.
Kreisel asked what more we know about a theorem when we know that it has a proof by restricted means.
[[Herbrand's theorem|VZ21F10WRS]] gives the answer for pure logic: a valid existential sentence has a finite disjunction of instances with explicit terms.
Herbrand analysis gives the answer for arithmetic with $\Sigma_1$-induction: the witness is a primitive recursive function of $x$, and the proof shows how to compute it.

## Notation

PRA is primitive recursive arithmetic: a quantifier-free theory with a function symbol for each primitive recursive function, its defining equations, and induction for quantifier-free formulas.
We use the language of PRA also for $\mathrm{I}\Sigma_1$.
This adds only definitional symbols, since $\mathrm{I}\Sigma_1$ proves that each primitive recursive function is total.
In this language a $\Sigma_1$ formula is a formula $\exists y \, \varphi$ with $\varphi$ quantifier-free; a bounded quantifier can be replaced by a primitive recursive function.
A $\Pi^0_2$ sentence has the form $\forall \bar x \, \exists y \, \varphi(\bar x, y)$ with $\varphi$ quantifier-free.
A sequent $\Gamma \Rightarrow \Delta$ is read "the conjunction of $\Gamma$ implies the disjunction of $\Delta$".
The $\Sigma_1$-induction rule, for a $\Sigma_1$ formula $A$ and a variable $a$ that does not occur in $\Gamma$, $\Delta$ or $A(0)$, is
$$\frac{\Gamma, A(a) \Rightarrow A(a + 1), \Delta}{\Gamma, A(0) \Rightarrow A(t), \Delta}.$$
The name "Herbrand analysis" is due to Sieg.

## Remarks

### The witnessing lemma

The fourth step proves the following lemma.
Let $\Gamma \Rightarrow \Delta$ have a derivation in which every formula is $\Sigma_1$.
Write the formulas of $\Gamma$ as $\exists u \, \gamma_j(\bar a, u)$ for $j \le m$ and those of $\Delta$ as $\exists v \, \theta_i(\bar a, v)$ for $i \le k$, with free variables $\bar a$.
Then there are primitive recursive functions $f_1, \ldots, f_k$ such that PRA proves
$$\gamma_1(\bar a, w_1) \land \cdots \land \gamma_m(\bar a, w_m) \to \theta_1(\bar a, f_1(\bar a, \bar w)) \lor \cdots \lor \theta_k(\bar a, f_k(\bar a, \bar w)).$$
The proof is by induction on the derivation, with one case for each rule.

1. Initial sequents are quantifier-free, so there is nothing to witness.
2. The rule that introduces $\exists v \, \theta(v)$ on the right from $\theta(t)$ gets the witness $t$, a primitive recursive term.
3. The rule that introduces $\exists u \, \gamma(u)$ on the left from $\gamma(b)$, with $b$ a fresh variable, substitutes the given witness $w$ for $b$.
4. A rule with two premises, such as the introduction of $\lor$ on the left, gives a definition by cases: a primitive recursive test of a quantifier-free formula selects the function of the right premise. This is the formal form of a [[proof by cases|0WCP0PVET6]].
5. A cut on a $\Sigma_1$ formula $C$ composes the two functions: the first premise computes a candidate witness for $C$, a quantifier-free test checks it, and the second premise uses it as an input.
6. The $\Sigma_1$-induction rule gives a function $g$ that sends $a$, $\bar w$ and a witness for $A(a)$ to a witness for $A(a + 1)$ or for $\Delta$. The function $h$ with $h(0) = $ the witness for $A(0)$ and $h(a + 1) = g(a, \bar w, h(a))$ is defined by [[primitive recursion|0DSHAVH45F]], together with a test at each step that records whether $\Delta$ is already witnessed.

The second step, partial cut elimination, is cited here and not proved.
Full cut elimination fails for theories with an induction rule: a cut on a formula that comes from an induction rule or from an initial sequent cannot in general be removed.
The free-cut elimination theorem removes all other cuts, and this is enough for the method.

### Main results

- Parsons's theorem: if $\mathrm{I}\Sigma_1 \vdash \forall \bar x \, \exists y \, \varphi(\bar x, y)$ with $\varphi$ quantifier-free, then there is a primitive recursive $f$ with $\mathsf{PRA} \vdash \varphi(\bar x, f(\bar x))$. Herbrand analysis is Sieg's proof of this theorem, which Parsons, Mints and Takeuti had proved independently.
- The provably total functions of $\mathrm{I}\Sigma_1$ are exactly the primitive recursive functions. Each primitive recursive function is provably total by $\Sigma_1$-induction, and the converse is Parsons's theorem.
- Friedman's theorem: the subsystem $\mathsf{WKL}_0$ of second-order arithmetic is $\Pi^0_2$-conservative over PRA. Sieg gave a proof of this theorem by Herbrand analysis. We state it without proof.

### Examples

- [[Herbrand analysis of the parity theorem|3SV55T75P1]]: the $\Sigma_1$-induction proof of $\forall x \, \exists y \, (x = 2y \lor x = 2y + 1)$ gives the primitive recursive witness $h(x) = \lfloor x/2 \rfloor$.
- [[A Herbrand disjunction for a common upper bound|MW71Q5G3JF]]: in the universal theory of a reflexive and total relation $\le$, the witness for $\exists z \, (a \le z \land b \le z)$ is $a$ or $b$, chosen by cases.
- Euclid's proof that there are infinitely many primes proves $\forall x \, \exists y \, (y > x \land y \text{ is prime})$ in $\mathrm{I}\Sigma_1$. The proof gives the witness "the least prime factor of $x! + 1$", which is primitive recursive, since the search is bounded by $x! + 1$.
- The Herbrand analysis of a proof by $\Sigma_1$-induction of $\forall x \, \exists y \, (y \cdot y \le x < (y + 1) \cdot (y + 1))$ gives $h(0) = 0$ and $h(x + 1) = h(x) + 1$ when $(h(x) + 1)^2 \le x + 1$, and $h(x + 1) = h(x)$ otherwise. So $h(x) = \lfloor \sqrt{x} \rfloor$.

### Non-examples

- [[Herbrand analysis fails for the Ackermann function in IΣ2|88FJKEX4SH]]: $\mathrm{I}\Sigma_2$ proves that the Ackermann function is total, by an induction on a $\Pi_2$ formula. The condition that fails is that each induction formula is $\Sigma_1$, and no primitive recursive witness exists.
- The pure logical theorem $\exists y \, \forall z \, (H(x, z) \to H(x, y))$, where $H(x, z)$ says "the Turing machine with code $x$ halts within $z$ steps". The conclusion is $\Sigma_2$, not $\Sigma_1$. A computable witness $f$ would decide the [[halting problem|Z7TN2B35B0]], because the machine $x$ halts exactly when $H(x, f(x))$ holds.
- A derivation that still contains a cut on a $\Pi_2$ formula. The witnessing lemma has no case for such a cut, so partial cut elimination must come first.

### Basic properties

- The witness $f$ is computed from the derivation by a primitive recursive transformation, so the method is uniform.
- For pure logic without induction, the method gives a Herbrand disjunction, as in [[Herbrand's theorem|VZ21F10WRS]]: the witnesses are terms, and the definitions by cases appear as a finite disjunction of instances.
- The method gives [[conservation results|N238J43XNE]]: a $\Pi^0_2$ theorem of the stronger theory becomes a quantifier-free theorem of PRA with a function symbol for the witness.
- The size of the witness reflects the induction in the proof: a proof with nested inductions gives a witness defined by nested primitive recursions.

### History

Herbrand proved his theorem for pure first-order logic in his thesis of 1930.
Parsons, Mints and Takeuti proved independently that $\mathrm{I}\Sigma_1$ is $\Pi^0_2$-conservative over PRA.
Sieg gave the proof by Herbrand analysis and used the same method for $\mathsf{WKL}_0$, whose conservativity over PRA is due to Friedman.
The same witnessing method, with polynomial time functions in place of primitive recursive ones, is the basis of Buss's work on bounded arithmetic.

### Common errors

- Assuming full cut elimination for $\mathrm{I}\Sigma_1$. Cuts on induction formulas remain; only the free cuts can be removed.
- Applying the witnessing lemma to a formula that is not $\Sigma_1$. For $\Sigma_2$ conclusions, or for induction on $\Pi_2$ formulas, no primitive recursive witness exists in general.
- Expecting a single term as the witness. In theories with induction the witness is a function defined by recursion, and even in pure logic a definition by cases may be needed.

## Explanations

### L1 human

Suppose that a proof shows "for each number $x$ there is a number $y$ with some property".
A computer could find $y$ by trying $0$, $1$, $2$ and so on, but this can take a very long time.
Herbrand analysis reads the proof itself and turns it into a program that computes $y$ directly.
Each step of the proof becomes a step of the program: a proof by induction becomes a loop, and a proof by cases becomes an "if ... then ... else".
For example, the usual proof that each number is even or odd becomes a program that computes half of $x$, rounded down: for $x = 7$ it gives $3$, since $7 = 2 \cdot 3 + 1$.

### L2 human

We extract a witness from Euclid's proof that there is a prime larger than $x$.

1. The proof: let $N = x! + 1$. Then $N \ge 2$, so $N$ has a least prime factor $p$.
2. Each number $d$ with $2 \le d \le x$ divides $x!$, so it does not divide $x! + 1$. So $p > x$.
3. The proof gives the witness $f(x) := $ the least $d$ with $2 \le d \le x! + 1$ and $d \mid x! + 1$.
4. The function $f$ is primitive recursive: $x!$ is defined by primitive recursion, and a search bounded by a primitive recursive bound is primitive recursive.
5. Check: $f(3)$ is the least prime factor of $3! + 1 = 7$, so $f(3) = 7 > 3$. And $f(4)$ is the least prime factor of $4! + 1 = 25$, so $f(4) = 5 > 4$.

The typical use is to read off a bound from a classical proof: here the prime above $x$ is at most $x! + 1$.
A trap is to expect the least witness: the method gives some witness, here $f(3) = 7$ while the least prime above $3$ is $5$.

### L3 human

Herbrand analysis is the simplest member of a family of proof interpretations that extract functions from proofs.
For full Peano arithmetic, the cut elimination of [[Gentzen's consistency proof|QPV0HNP22S]] and Kreisel's no-counterexample interpretation give witnesses by recursion along ordinals below $\varepsilon_0$, and Gödel's [[Dialectica interpretation|HZ17ES9PDY]] gives functionals of finite type.
In bounded arithmetic the same witnessing argument, applied to Buss's theory $S^1_2$, shows that its $\Sigma^b_1$-definable functions are computable in polynomial time.

Structurally, the method is a cut elimination that stops as soon as the derivation lives in the $\Sigma_1$ fragment, followed by a realizability-like reading of the remaining derivation.
Its conservation results compare theories in a proof-theoretic way, while [[interpretability|8H03GRMDYG]] compares them by translation, and for extensions of PA the two meet through $\Pi_1$-conservativity.
Proof mining applies the same idea, with functional interpretations, to proofs in analysis.
