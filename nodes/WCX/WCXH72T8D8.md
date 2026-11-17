---
tag: WCXH72T8D8
kind: concept
name: Primitive recursive arithmetic
aliases: [pra, skolem-recursive-arithmetic]
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: grad
uses: [5NVA2JRHPV, D8SD54M5PN, 1QD0KDDGYJ, HYJ10AF6RT, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_arithmetic
    locator: Language and axioms
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
  - book: isbn:9780521857840
---

## Summary

Primitive recursive arithmetic $\mathsf{PRA}$ is the quantifier-free theory of the natural numbers whose terms are built from variables, $0$ and one function symbol for each definition of a [[primitive recursive function|5NVA2JRHPV]].
Its formulas are equations $s = t$ between terms, combined with $\neg$, $\land$, $\lor$ and $\to$, and a free variable is read as "for every number".
Its axioms are the propositional tautologies, the equality axioms, $\neg (Sx = 0)$, $Sx = Sy \to x = y$, and the defining equations of every function symbol.
Its rules are modus ponens, substitution of a term for a variable, and the induction rule: from $\varphi(0)$ and $\varphi(x) \to \varphi(Sx)$ infer $\varphi(x)$, for every quantifier-free $\varphi$.
The [[definition node|330YAP9Y4Q]] gives the full list.
$\mathsf{PRA}$ is the standard formal model of finitist reasoning, and it is the usual base theory in which consistency proofs are carried out.

## Motivation

Hilbert asked for consistency proofs by finitist means: reasoning about finite objects, with no appeal to completed infinite totalities.
A statement "for all $n$" with a quantifier over the infinite set $\N$ is not finitist in this strict sense.
A formula with a free variable avoids the quantifier: it says that each number, when it is given, has a property that we can check.
For the check to be finite, the property must be decidable, and the functions in it must be computable by explicit recursion.
Primitive recursion gives exactly such functions, and induction on decidable properties is the matching principle of proof.
$\mathsf{PRA}$ is the formal system that results from these two decisions.

## Notation

We write $\mathsf{PRA}$ for the theory and $\vdash_{\mathsf{PRA}}$ for its derivability relation.
For each primitive recursive definition $d$ there is a function symbol $f_d$; in practice we use the familiar names, for example $x + y$, $x \cdot y$, $x^y$, $\mathrm{pd}(x)$ (predecessor) and $x \mathbin{\dot -} y$ (truncated subtraction).
Here $+$ and $\cdot$ are the function symbols with the defining equations of axioms Q4 to Q7 of [[Robinson arithmetic|3K1AKGXF8A]], so $\mathsf{PRA}$ contains the [[language of arithmetic|D8SD54M5PN]] $L_A$ up to the symbol $<$.
The relation $x < y$ is written as the equation $\chi_<(x, y) = 1$, where $\chi_<$ is the primitive recursive characteristic function of $<$.
Some books use a logic-free variant, due to Goodstein, in which every formula is an equation and the connectives are coded by arithmetic.
Other books use a first-order variant: classical first-order logic with the same function symbols and axioms, and the induction schema for quantifier-free formulas only.
The quantifier-free variant and the first-order variant prove the same quantifier-free formulas.

## Remarks

### Examples

- The formula $0 + x = x$ is a theorem of $\mathsf{PRA}$; [[this example|PZ0QYV4KRS]] derives it with one use of the induction rule.
- The formula $\neg (Sx = x)$ is a theorem: the base case is an axiom, and the step $Sx \ne x \to SSx \ne Sx$ is the contrapositive of the injectivity axiom.
- Goldbach's conjecture is a single equation $g(x) = 1$ of $\mathsf{PRA}$, because the property "$x$ is odd, or $x \le 2$, or $x$ is a sum of two primes" is primitive recursive; [[this example|7QDEKB8HC8]] builds $g$.
- For every primitive recursive function $f$, the defining equations of $f$ are axioms, so $\mathsf{PRA}$ proves every equation $f(\overline{n}) = \overline{m}$ that is true in $\mathfrak{N}$, by computing with the equations.
- The commutativity, associativity and distributivity laws of $+$ and $\cdot$ are theorems, proved with the induction rule as in [[Peano arithmetic|HACXBCM7SS]].

### Non-examples

- The [[Ackermann function|N470JF7ZJX]] is not a function of $\mathsf{PRA}$: every term denotes a primitive recursive function, and the Ackermann function is not primitive recursive; [[this non-example|2YSJB6DJYM]] gives the details.
- The sentence $\forall x \, \exists y \, (x < y)$ is not a formula of $\mathsf{PRA}$, since $\mathsf{PRA}$ has no quantifiers. Its finitist replacement is the free-variable formula $x < Sx$, which names the witness $Sx$.
- Induction for a formula of the form $\exists y \, \psi(x, y)$ is not a rule of $\mathsf{PRA}$. The rule applies only to quantifier-free formulas, whose instances are decidable.

### Basic properties

- Soundness. Every axiom of $\mathsf{PRA}$ is true in $\mathfrak{N}$ for all values of its variables, and every rule preserves this property. So every theorem of $\mathsf{PRA}$ is true in $\mathfrak{N}$ for all values, and $\mathsf{PRA}$ is consistent.
- Expressive power. A [[$\Delta_0$ formula|GE43CSZTS9]] $\varphi(x)$ defines a primitive recursive relation, so the $\Pi_1$ sentence $\forall x \, \varphi(x)$ has the free-variable form $\chi_\varphi(x) = 1$ in $\mathsf{PRA}$.
- Relation to Peano arithmetic. [[Peano arithmetic|HACXBCM7SS]] defines each primitive recursive function with [[Gödel's β-function lemma|BM6P0C2AC2]] and proves its defining equations. In this sense every theorem of $\mathsf{PRA}$ is a theorem of $\mathsf{PA}$, and in fact of $\mathsf{I}\Sigma_1$.
- Conservativity. If $\mathsf{I}\Sigma_1$ proves $\forall x \, \exists y \, \varphi(x, y)$ with $\varphi$ in $\Delta_0$, then there is a primitive recursive function $f$ such that $\mathsf{PRA}$ proves $\varphi(x, f(x))$. So the provably total functions of $\mathsf{I}\Sigma_1$ are exactly the primitive recursive functions.
- Incompleteness. $\mathsf{PRA}$ does not prove its own consistency statement $\mathrm{Con}(\mathsf{PRA})$, which is a $\Pi_1$ sentence and so a free-variable formula, by [[Gödel's second incompleteness theorem|4PZM5GJTR5]].
- Consistency proofs. [[Gentzen's consistency proof|QPV0HNP22S]] of $\mathsf{PA}$ uses $\mathsf{PRA}$ plus the induction rule along a primitive recursive well-ordering of type [[$\varepsilon_0$|KT50SMH3EC]], for quantifier-free formulas. This is the model for all [[ordinal analysis|C5E5TG8PGP]], and the proof-theoretic ordinal of $\mathsf{PRA}$ itself is $\omega^\omega$.
- Reverse mathematics. The second-order system $\mathsf{WKL}_0$ is conservative over $\mathsf{PRA}$ for $\Pi_2$ sentences, a result of Harvey Friedman. So the parts of analysis that $\mathsf{WKL}_0$ proves have finitist consequences, a partial realization of [[Hilbert's program|P1RW6JWX73]].

### Tait's thesis

William Tait argued, in his 1981 paper "Finitism", that the finitist functions are exactly the primitive recursive functions and that the finitist theorems are exactly the theorems of $\mathsf{PRA}$.
The thesis rests on an analysis of the functions of numbers that a finitist can accept.
On this thesis, the Ackermann function is computable but not finitist, since it is not primitive recursive.
The thesis is a philosophical analysis, not a theorem, and some authors argue that finitism reaches further.
The topic [[finitism and predicativism|PTA0GDJWZQ]] treats the philosophical side.

### History

Thoralf Skolem developed arithmetic in this quantifier-free style in 1923, with recursive definitions in place of quantifiers.
Gentzen's consistency proof of $\mathsf{PA}$ made $\mathsf{PRA}$ the standard base theory for consistency proofs.
The characterization of the provably total functions of $\mathsf{I}\Sigma_1$ was found independently by Charles Parsons, Grigori Mints and Gaisi Takeuti.

### Common errors

- To think that $\mathsf{PRA}$ cannot state general laws. A free variable is an implicit universal quantifier at the front of the formula, so $\mathsf{PRA}$ states every $\Pi_1$ sentence.
- To confuse $\mathsf{PRA}$ with $\mathsf{I}\Sigma_1$. The two theories have the same $\Pi_2$ consequences, but $\mathsf{I}\Sigma_1$ has quantifiers and proves sentences with more quantifier alternations.
- To think that the induction rule is the same as the induction axiom. The rule gives $\varphi(x)$ only from proofs of the premisses, and it never gives an implication with the premisses as hypotheses under a quantifier.

## Explanations

### L1 human

Primitive recursive arithmetic is a rule book for facts about whole numbers that never speaks of "all numbers at once".
It only uses functions that we can compute step by step, such as addition, multiplication and powers.
A law such as $x + 0 = x$ is read as: for every number $x$, this equation holds.
For example, with $x = 7$ the law says $7 + 0 = 7$, and we can check it.
To prove a law for every number, we prove it for $0$, and then we prove that it passes from each number to the next one.
Many logicians think that this rule book contains exactly the reasoning that Hilbert called finitist.

### L2 human

We derive the formula $\neg (Sx = x)$ in $\mathsf{PRA}$.

1. Let $\varphi(x)$ be the quantifier-free formula $\neg (Sx = x)$.
2. Base case: $\varphi(0)$ is $\neg (S0 = 0)$. It is an instance of the axiom $\neg (Sx = 0)$, by the substitution rule with the term $0$ for $x$.
3. The injectivity axiom $Sx = Sy \to x = y$, with the term $Sx$ for $x$ and the term $x$ for $y$, gives $SSx = Sx \to Sx = x$.
4. The contrapositive of step 3 is $\neg (Sx = x) \to \neg (SSx = Sx)$, by a propositional tautology and modus ponens.
5. Step 4 is $\varphi(x) \to \varphi(Sx)$.
6. The induction rule, applied to steps 2 and 5, gives $\varphi(x)$, that is, $\neg (Sx = x)$.

The typical use of $\mathsf{PRA}$ is as the theory in which a metamathematical argument is checked, for example "if $T$ proves $\varphi$, then $T'$ proves $\varphi^*$", where the translation of proofs is primitive recursive.
A trap is to apply the induction rule to a formula that contains a quantifier, for example to show that each $x$ has a witness $y$ without naming the witness as a function of $x$.

### L3 human

$\mathsf{PRA}$ sits at the bottom of the scale of strength that ordinal analysis measures: its ordinal is $\omega^\omega$, the ordinal of $\mathsf{I}\Sigma_1$ is the same, and the ordinal of $\mathsf{PA}$ is $\varepsilon_0$.
Its $\Pi_2$ consequences match $\mathsf{I}\Sigma_1$, $\mathsf{RCA}_0$ and $\mathsf{WKL}_0$, so a large part of [[reverse mathematics|7SQS69T17R]] is finitistically reducible in Hilbert's sense.
Weaker relatives are [[elementary function arithmetic|2JD80TE553]], whose functions are the elementary ones, and the bounded arithmetics of the topic [[bounded arithmetic|RA380RWEC0]], whose functions are feasible.
In category theory, the primitive recursive functions are the arrows $\N^k \to \N$ of the free category with finite products and a natural numbers object.
The [[fragments of Peano arithmetic|T70PYM1F36]] and [[true arithmetic|DX0KPMH4QZ]] place $\mathsf{PRA}$ in the larger family of arithmetic theories.
