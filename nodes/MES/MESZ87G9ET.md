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

Take the theorem that any two numbers have a common upper bound, $\forall x \, \forall x' \, \exists y \, (x \le y \land x' \le y)$.
Its proof uses only reflexivity of $\le$ and the instance $x \le x' \lor x' \le x$ of totality.
[[Herbrand's theorem|VZ21F10WRS]] turns this proof into a finite disjunction of instances with explicit terms:
$$(x \le x \land x' \le x) \lor (x \le x' \land x' \le x').$$
The disjunction names two candidates, $y = x$ and $y = x'$, and a test of $x \le x'$ picks the right one.
So the proof bounds the witness by the largest of its terms, with no search at all.

*Herbrand analysis* carries this reading from pure logic to arithmetic with induction.
It turns a derivation in $\mathrm{I}\Sigma_1$ of $\exists y \, \varphi(\bar x, y)$, with $\varphi$ quantifier-free, into a [[primitive recursive function|5NVA2JRHPV]] $f$ with $\varphi(\bar x, f(\bar x))$ for all $\bar x$.
The method has four steps.
First, write $\mathrm{I}\Sigma_1$ as a [[sequent calculus|W72CA3R9MP]] with quantifier-free initial sequents and an induction rule for $\Sigma_1$ formulas.
Second, apply partial [[cut elimination|AYRZ98Y0NW]], so that every cut formula is $\Sigma_1$.
Third, observe that then every formula in the derivation is $\Sigma_1$.
Fourth, by induction on the derivation, build primitive recursive functions that compute witnesses on the right of each sequent from witnesses on the left.
In the fourth step an induction becomes a primitive recursion, a case distinction becomes a definition by cases, and a cut becomes a composition.
The method extracts programs from classical proofs, and it proves that $\mathrm{I}\Sigma_1$ is $\Pi^0_2$-conservative over primitive recursive arithmetic, which is [[Parsons's theorem|2VYJXZZDGB]].

## Motivation

A classical proof of $\forall x \, \exists y \, \varphi(x, y)$, with $\varphi$ decidable, always gives an algorithm.
Search $y = 0, 1, 2, \ldots$ until $\varphi(x, y)$ holds.
The search tells us nothing about the size of $y$ or about the cost of the computation.
Kreisel asked what more we know about a theorem when we know that it has a proof by restricted means.
Herbrand's theorem gives the answer for pure logic: a valid existential sentence has a finite disjunction of instances with explicit terms.
Herbrand analysis gives the answer for arithmetic with $\Sigma_1$-induction: the witness is a primitive recursive function of $x$, and the proof shows how to compute it.
For Euclid's proof that there is a prime above $x$, the analysis gives the bound $x! + 1$, as worked out in the L2 explanation below.

## Notation

PRA is primitive recursive arithmetic.
It is a quantifier-free theory with a function symbol for each primitive recursive function, its defining equations, and induction for quantifier-free formulas.
We use the language of PRA also for $\mathrm{I}\Sigma_1$.
This adds only definitional symbols, because $\mathrm{I}\Sigma_1$ in the language of PA proves that the $\Sigma_1$ definition of each primitive recursive function is total.
In this language a $\Sigma_1$ formula is a formula $\exists y \, \varphi$ with $\varphi$ quantifier-free, since a bounded quantifier can be replaced by a primitive recursive function.
A $\Pi^0_2$ sentence has the form $\forall \bar x \, \exists y \, \varphi(\bar x, y)$ with $\varphi$ quantifier-free.
A sequent $\Gamma \Rightarrow \Delta$ is read "the conjunction of $\Gamma$ implies the disjunction of $\Delta$".
The $\Sigma_1$-induction rule is stated for a $\Sigma_1$ formula $A$ and a variable $a$ that does not occur in $\Gamma$, $\Delta$ or $A(0)$:
$$\frac{\Gamma, A(a) \Rightarrow A(a + 1), \Delta}{\Gamma, A(0) \Rightarrow A(t), \Delta}.$$

## Remarks

### A first extraction

The theorem $\forall x \, \exists y \, (x = 2y \lor x = 2y + 1)$ says that each number is even or odd.
It has a proof by $\Sigma_1$-[[induction|0ASJVEFA9J]] on $x$.
The base case gives the witness $0$ for $x = 0$.
The step has two cases: if $x = 2y$, then $y$ still works for $x + 1$, and if $x = 2y + 1$, then $y + 1$ works.
The analysis turns the two cases into a definition by cases and the induction into a [[primitive recursion|0DSHAVH45F]].
We get $h(0) = 0$, with $h(x + 1) = h(x)$ if $x = 2h(x)$ and $h(x + 1) = h(x) + 1$ otherwise.
So $h(1) = 0$, $h(2) = 1$, $h(3) = 1$, and in general $h(x) = \lfloor x/2 \rfloor$.
The [[Herbrand analysis of the parity theorem|3SV55T75P1]] carries out every step.

### The witnessing lemma

The fourth step proves the following lemma.
Let $\Gamma \Rightarrow \Delta$ have a derivation in which every formula is $\Sigma_1$.
Write the formulas of $\Gamma$ as $\exists u \, \gamma_j(\bar a, u)$ for $j \le m$ and those of $\Delta$ as $\exists v \, \theta_i(\bar a, v)$ for $i \le k$.
Then there are primitive recursive functions $f_1, \ldots, f_k$ such that PRA proves the following implication:
$$\gamma_1(\bar a, w_1) \land \cdots \land \gamma_m(\bar a, w_m) \to \theta_1(\bar a, f_1(\bar a, \bar w)) \lor \cdots \lor \theta_k(\bar a, f_k(\bar a, \bar w)).$$
The proof is by induction on the derivation, with one case for each rule.

1. Initial sequents are quantifier-free, so there is nothing to witness.
2. The rule that introduces $\exists v \, \theta(v)$ on the right from $\theta(t)$ gets the witness $t$, a primitive recursive term.
3. The rule that introduces $\exists u \, \gamma(u)$ on the left from $\gamma(b)$, with $b$ fresh, substitutes the given witness $w$ for $b$.
4. A rule with two premises gives a definition by cases.
   A test of a quantifier-free formula selects the function of one premise, the formal form of a [[proof by cases|0WCP0PVET6]].
5. A cut on a $\Sigma_1$ formula $C$ composes the two functions.
   The first premise computes a candidate witness for $C$, a quantifier-free test checks it, and the second premise uses it as an input.

### The witnessing lemma, the induction rule

The induction rule is the only case that needs primitive recursion, and it takes two steps.

6. The induction rule gives $g$ that sends $a$, $\bar w$ and a witness for $A(a)$ to a witness for $A(a + 1)$ or for $\Delta$.
   Put $h(0) = $ the witness for $A(0)$ and $h(a + 1) = g(a, \bar w, h(a))$.
7. A bounded search finds the first $a < t$ at which $h(a + 1)$ fails to witness $A(a + 1)$.
   If there is none, $h(t)$ witnesses $A(t)$, and otherwise $g$ at that $a$ witnesses $\Delta$.

### Only free cuts are removed

The second step, partial cut elimination, is cited here and not proved.
Full cut elimination fails for theories with an induction rule.
A cut on a formula that comes from an induction rule or from an initial sequent cannot in general be removed.
The free-cut elimination theorem removes all other cuts, and this is enough for the method.
After it, the derivation contains no formula more complex than $\Sigma_1$, so steps 1 to 7 cover every rule that occurs.

### What the method proves

The first result is Parsons's theorem.
If $\mathrm{I}\Sigma_1 \vdash \forall \bar x \, \exists y \, \varphi(\bar x, y)$ with $\varphi$ quantifier-free, then there is a primitive recursive $f$ with $\mathsf{PRA} \vdash \varphi(\bar x, f(\bar x))$.
It follows that the provably total functions of $\mathrm{I}\Sigma_1$ are exactly the primitive recursive functions.
Each primitive recursive function is provably total by $\Sigma_1$-induction, and the converse is Parsons's theorem.

These are [[conservation results|N238J43XNE]]: a $\Pi^0_2$ theorem of the stronger theory becomes a quantifier-free theorem of PRA, with a function symbol for the witness.
The same method shows that the subsystem $\mathsf{WKL}_0$ of second-order arithmetic is $\Pi^0_2$-conservative over PRA, a theorem of Friedman that we state without proof.

The method is uniform, since the witness $f$ is computed from the derivation by an effective transformation.
The shape of $f$ reflects the inductions in the proof, and nested inductions give nested primitive recursions.
For Euclid's proof of $\forall x \, \exists y \, (y > x \land y \text{ is prime})$, the witness is the least prime factor of $x! + 1$.
For the $\Sigma_1$-induction proof of $\forall x \, \exists y \, (y \cdot y \le x < (y + 1) \cdot (y + 1))$, the witness is $\lfloor \sqrt{x} \rfloor$.
In pure logic without induction the witnesses are terms, and the definitions by cases become a Herbrand disjunction, as in the [[common upper bound example|MW71Q5G3JF]].

### Where the method stops

Each condition of the method can fail, and then the conclusion can fail too.
The theory $\mathrm{I}\Sigma_2$ proves that the Ackermann function is total, by an induction on a $\Pi_2$ formula.
There the induction formula is not $\Sigma_1$, and [[no primitive recursive witness exists|88FJKEX4SH]].

The conclusion must be $\Sigma_1$, too.
Let $H(x, z)$ say "the Turing machine with code $x$ halts within $z$ steps".
Pure logic proves $\exists y \, \forall z \, (H(x, z) \to H(x, y))$, a $\Sigma_2$ formula.
A computable witness $f$ would decide the [[halting problem|Z7TN2B35B0]], because the machine $x$ halts exactly when $H(x, f(x))$ holds.

Finally, a derivation that still contains a cut on a $\Pi_2$ formula is out of reach.
The witnessing lemma has no case for such a cut, so partial cut elimination must come first.

### Watch out

Do not assume full cut elimination for $\mathrm{I}\Sigma_1$.
Cuts on induction formulas remain, and only the free cuts can be removed.

Do not apply the witnessing lemma to a formula that is not $\Sigma_1$.
For $\Sigma_2$ conclusions, or for induction on $\Pi_2$ formulas, no primitive recursive witness exists in general.

Do not expect a single term as the witness.
In theories with induction the witness is a function defined by recursion, and even in pure logic a definition by cases may be needed.

Do not confuse the two conservation results for $\mathsf{WKL}_0$.
It is $\Pi^0_2$-conservative over PRA, by Friedman, and $\Pi^1_1$-conservative over $\mathsf{RCA}_0$, by Harrington.
It is not $\Pi^1_1$-conservative over PRA, since PRA has no second-order sentences to compare with.

### History

Herbrand proved his theorem for pure first-order logic in his thesis of 1930.
Kreisel asked in the 1950s what a proof by restricted means tells us beyond the truth of its conclusion.
Parsons in 1970, and Mints and Takeuti independently, proved that $\mathrm{I}\Sigma_1$ is $\Pi^0_2$-conservative over PRA.
Sieg's Herbrand analysis appeared in 1985, and the name is his.
Sieg gave the proof of Parsons's theorem by Herbrand analysis and used the same method for Friedman's conservation theorem for $\mathsf{WKL}_0$.
The same witnessing method, with polynomial time functions in place of primitive recursive ones, is the basis of Buss's work on bounded arithmetic in the 1980s.

### Try it

The theorem $\forall x \, \exists y \, (x < y \land y \text{ is even})$ has a proof by cases on the parity of $x$.
If $x$ is even, take $y = x + 2$, and if $x$ is odd, take $y = x + 1$.
Write the extracted witness $f$ as a definition by cases, and compute $f(4)$ and $f(5)$.
Read off a bound on $y$ in terms of $x$.

Check: $f(4) = 6$ and $f(5) = 6$, both even and above the input, and the bound is $y \le x + 2$.

## Explanations

### L1 human

Suppose that a proof shows "for each number $x$ there is a number $y$ with some property".
A computer could find $y$ by trying $0$, $1$, $2$ and so on, but this can take a very long time.
Herbrand analysis reads the proof itself and turns it into a program that computes $y$ directly.
Each step of the proof becomes a step of the program.
A proof by induction becomes a loop, and a proof by cases becomes an "if ... then ... else".
For example, the usual proof that each number is even or odd becomes a program that computes half of $x$, rounded down.
For $x = 7$ it gives $3$, since $7 = 2 \cdot 3 + 1$.

### L2 human

We extract a witness from Euclid's proof that there is a prime larger than $x$.

1. The proof: let $N = x! + 1$.
   Then $N \ge 2$, so $N$ has a least prime factor $p$.
2. Each number $d$ with $2 \le d \le x$ divides $x!$, so it does not divide $x! + 1$.
   So $p > x$.
3. The proof gives the witness $f(x) := $ the least $d$ with $2 \le d \le x! + 1$ and $d \mid x! + 1$.
4. The function $f$ is primitive recursive, since $x!$ is defined by primitive recursion and the search is bounded by $x! + 1$.

Check: $f(3)$ is the least prime factor of $3! + 1 = 7$, so $f(3) = 7 > 3$.
Check: $f(4)$ is the least prime factor of $4! + 1 = 25$, so $f(4) = 5 > 4$.

The typical use is to read off a bound from a classical proof, and here the prime above $x$ is at most $x! + 1$.
A trap is to expect the least witness.
The method gives some witness, here $f(3) = 7$, while the least prime above $3$ is $5$.

### L3 human

Herbrand analysis is the simplest member of a family of proof interpretations that extract functions from proofs.
For full Peano arithmetic, the cut elimination of [[Gentzen's consistency proof|QPV0HNP22S]] gives witnesses by recursion along ordinals below $\varepsilon_0$.
Kreisel's no-counterexample interpretation does the same, and Gödel's [[Dialectica interpretation|HZ17ES9PDY]] gives functionals of finite type.
In bounded arithmetic the same witnessing argument, applied to Buss's theory $S^1_2$, shows that its $\Sigma^b_1$-definable functions are computable in polynomial time.

Structurally, the method is a cut elimination that stops as soon as the derivation lives in the $\Sigma_1$ fragment.
It is followed by a realizability-like reading of the remaining derivation.
Its conservation results compare theories in a proof-theoretic way, while [[interpretability|8H03GRMDYG]] compares them by translation.
For extensions of PA the two meet through $\Pi_1$-conservativity.
Proof mining applies the same idea, with functional interpretations, to proofs in analysis.
