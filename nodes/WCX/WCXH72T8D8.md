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

Primitive recursive arithmetic is arithmetic done with computable functions and free variables only, with no quantifier over all numbers.
Take the [[factorial|0XWG0JGDFW]].
Two equations define it:
$$0! = 1, \qquad (n + 1)! = n! \cdot (n + 1).$$
In $\mathsf{PRA}$ these equations are axioms for one function symbol, and they compute every value.
Unwind them for $3!$:
$$3! = 2! \cdot 3 = (1! \cdot 2) \cdot 3 = ((0! \cdot 1) \cdot 2) \cdot 3 = ((1 \cdot 1) \cdot 2) \cdot 3 = 6.$$
Check: $1 \cdot 2 \cdot 3 = 6$.

Exactly, $\mathsf{PRA}$ is the quantifier-free theory whose terms are built from variables, $0$ and one function symbol for each definition of a [[primitive recursive function|5NVA2JRHPV]].
Its formulas are equations $s = t$ combined with $\neg$, $\land$, $\lor$ and $\to$, and a free variable is read as "for every number".
Its axioms are the propositional tautologies, the equality axioms, $\neg (Sx = 0)$, $Sx = Sy \to x = y$, and the defining equations of every function symbol.
Its rules are modus ponens, substitution of a term for a variable, and the induction rule: from $\varphi(0)$ and $\varphi(x) \to \varphi(Sx)$ infer $\varphi(x)$.
The [[definition|330YAP9Y4Q]] lists the symbols and the rules in full.

## Motivation

Hilbert asked for consistency proofs by finitist means: reasoning about finite objects, with no appeal to a completed infinite totality.
A sentence "for all $n$" quantifies over the whole infinite set $\mathbb{N}$, so it is not finitist in this strict sense.
A formula with a free variable avoids the quantifier.
It says that each number, once it is given, has a property that we can check in finitely many steps.
For that, the functions in the formula must be computable by explicit recursion, and primitive recursion gives exactly such functions.
Induction on decidable properties is then the matching rule of proof, and $\mathsf{PRA}$ is the system that results.

$\mathsf{PRA}$ is the usual base theory of proof theory.
Consistency proofs, conservation results and translations of proofs are checked inside it.
Later pages place it among the other theories: [[elementary function arithmetic|2JD80TE553]] is weaker, and the [[fragment|T70PYM1F36]] $\mathsf{I}\Sigma_1$ of [[Peano arithmetic|HACXBCM7SS]] proves the same $\Pi_2$ sentences.
The [[incompleteness theorems|HXHHWY3328]] apply to it as well.

## Notation

We write $\mathsf{PRA}$ for the theory and $\mathsf{PRA} \vdash \varphi$ for its theorems.
Each primitive recursive definition $d$ gets its own function symbol $f_d$, but we use the familiar names: $x + y$, $x \cdot y$, $x^y$, $x!$, $\mathrm{pd}(x)$ for the predecessor and $x \mathbin{\dot -} y$ for truncated subtraction.
The symbols $+$ and $\cdot$ have the defining equations of axioms Q4 to Q7 of [[Robinson arithmetic|3K1AKGXF8A]], so $\mathsf{PRA}$ contains the [[language of arithmetic|D8SD54M5PN]] except for $<$.
We write $x < y$ for the equation $\chi_<(x, y) = 1$, where $\chi_<$ is the primitive recursive characteristic function of $<$.
Goodstein used a logic-free variant in which every formula is an equation.
Other books use classical first-order logic with the same function symbols and the induction schema for quantifier-free formulas; this variant proves the same quantifier-free formulas.

## Remarks

### Laws with one induction each

The law $0 + x = x$ is not a defining equation of $+$, but $\mathsf{PRA}$ proves it with one use of the induction rule.
The base case $0 + 0 = 0$ is an instance of $x + 0 = x$, and the step uses $0 + Sx = S(0 + x)$.
[[A derivation of 0 + x = x|PZ0QYV4KRS]] writes out every line.

The law $\neg (Sx = x)$ is proved in the same way, as L2 below shows.
Then $Sy + x = S(y + x)$ follows by induction on $x$, and $x + y = y + x$ by induction on $y$.
In the same style $\mathsf{PRA}$ proves the associative, commutative and distributive laws of $+$ and $\cdot$.

On numerals no induction is needed at all.
The defining equations compute each closed term, so $\mathsf{PRA}$ proves every true equation $f(\overline{n}) = \overline{m}$.
For example, the equations of $+$ and $\cdot$ give
$$\overline{2} \cdot \overline{2} = \overline{2} \cdot \overline{1} + \overline{2} = (\overline{2} \cdot 0 + \overline{2}) + \overline{2} = (0 + \overline{2}) + \overline{2} = \overline{4}.$$
Check: $2 \cdot 2 = 4$.

### What a free variable can say

A theorem $\varphi(x)$ asserts $\varphi(\overline{n})$ for every number $n$, so a free variable acts as a universal quantifier in front.
Every $\Pi_1$ sentence $\forall x \, \psi(x)$ with $\psi$ bounded has such a form, because a bounded formula defines a primitive recursive relation.
[[Goldbach's conjecture as one equation|7QDEKB8HC8]] carries this out: it becomes $g(x) = 1$ for a primitive recursive $g$.

A sentence $\forall x \, \exists y \, \psi(x, y)$ needs more.
$\mathsf{PRA}$ can state it only by naming the witness $y$ as a function of $x$.
For "there is a prime above $x$", every prime factor of $x! + 1$ is larger than $x$, so a prime lies in the interval from $x + 1$ to $x! + 1$.
Let $\mathrm{np}(x)$ be the least prime in that interval, found by a bounded search, which is primitive recursive.
The free-variable form of the sentence is
$$\mathrm{Prime}(\mathrm{np}(x)) \land x < \mathrm{np}(x).$$
Check: $\mathrm{np}(3)$ is the least prime from $4$ to $7$, which is $5$.

### What it is not

The [[Ackermann function|N470JF7ZJX]] is computable, but no term of $\mathsf{PRA}$ denotes it.
Every term denotes a primitive recursive function, and the Ackermann function grows faster than each of them; [[the Ackermann non-example|2YSJB6DJYM]] gives the details.

The sentence $\forall x \, \exists y \, (x < y)$ is not a formula of $\mathsf{PRA}$, because $\mathsf{PRA}$ has no quantifiers.
Its replacement is $x < Sx$, which names the witness $Sx$.

Induction on a formula $\exists y \, \psi(x, y)$ is not a rule of $\mathsf{PRA}$.
The induction rule applies only to quantifier-free formulas, and their instances can be decided by computation.

### How strong it is

Every axiom is true in the standard model $\mathfrak{N}$ for all values of its variables, and every rule keeps this property.
So $\mathsf{PRA}$ is [[sound|4A84VHDTHV]], and hence consistent.
By [[Gödel's second incompleteness theorem|4PZM5GJTR5]], it still does not prove its own consistency statement, which is a $\Pi_1$ sentence and so has a free-variable form.

[[Peano arithmetic|HACXBCM7SS]] defines each primitive recursive function with [[Gödel's β-function lemma|BM6P0C2AC2]] and proves its defining equations.
The fragment $\mathsf{I}\Sigma_1$ already does this, so every theorem of $\mathsf{PRA}$ becomes a theorem of $\mathsf{I}\Sigma_1$.
The converse holds for $\Pi_2$ sentences.
If $\mathsf{I}\Sigma_1$ proves $\forall x \, \exists y \, \psi(x, y)$ with $\psi$ bounded, then $\mathsf{PRA}$ proves $\psi(x, f(x))$ for some primitive recursive $f$.
So $\mathsf{I}\Sigma_1$ and $\mathsf{PRA}$ prove the same $\Pi_2$ sentences, and the [[provably total functions|Z742YPHPNS]] of $\mathsf{I}\Sigma_1$ are exactly the primitive recursive functions.

### The base of consistency proofs

[[Gentzen's consistency proof|QPV0HNP22S]] of $\mathsf{PA}$ works in $\mathsf{PRA}$ plus one extra principle.
That principle is induction for quantifier-free formulas along a primitive recursive well-ordering of type [[ε0|KT50SMH3EC]].
This became the pattern of [[ordinal analysis|C5E5TG8PGP]], and the proof-theoretic ordinal of $\mathsf{PRA}$ itself is $\omega^\omega$.
In [[reverse mathematics|7SQS69T17R]], Harvey Friedman showed that $\mathsf{WKL}_0$ proves the same $\Pi_2$ sentences as $\mathsf{PRA}$.
So the theorems of analysis that $\mathsf{WKL}_0$ proves have finitist consequences only, a partial realization of [[Hilbert's program|P1RW6JWX73]].

### Tait's thesis

William Tait argued in his 1981 paper "Finitism" that finitist reasoning about numbers is exactly the reasoning of $\mathsf{PRA}$.
On this thesis the finitist functions are the primitive recursive ones, so the Ackermann function is computable but not finitist.
The thesis is a philosophical analysis, not a theorem, and some authors argue that finitism reaches further.
The topic [[finitism and predicativism|PTA0GDJWZQ]] treats the philosophical side.

### History

Thoralf Skolem developed arithmetic in this quantifier-free style in 1923, with recursive definitions in place of quantifiers.
Gentzen's consistency proof of $\mathsf{PA}$ in 1936 made $\mathsf{PRA}$ the usual base theory for such proofs.
Around 1970, Charles Parsons, Grigori Mints and Gaisi Takeuti showed independently that $\mathsf{I}\Sigma_1$ proves the same $\Pi_2$ sentences as $\mathsf{PRA}$.

### Watch out

Do not confuse the induction rule with the induction axiom.
The rule gives $\varphi(x)$ only after both premises are proved.
It never gives the implication "if $\varphi(0)$ and $\forall x \, (\varphi(x) \to \varphi(Sx))$, then $\forall x \, \varphi(x)$" as one formula, since that formula has quantifiers.

Do not confuse $\mathsf{PRA}$ with $\mathsf{I}\Sigma_1$ either.
They agree on $\Pi_2$ sentences, but $\mathsf{I}\Sigma_1$ has quantifiers and proves sentences with more alternations, such as instances of $\Sigma_1$ induction itself.

### Try it

Write the defining equations of $x^y$ and compute $2^3$ from them.
The equations are $x^0 = 1$ and $x^{Sy} = x^y \cdot x$, so $2^3 = 2^2 \cdot 2 = (2^1 \cdot 2) \cdot 2 = ((1 \cdot 2) \cdot 2) \cdot 2 = 8$.

Give the free-variable form of "every number is less than some number".
It is $x < Sx$, since the witness can be named as $Sx$.

## Explanations

### L1 human

Primitive recursive arithmetic is a rule book for whole numbers that never speaks of "all numbers at once".
It only uses functions that we compute step by step, such as addition, multiplication, powers and factorials.
A law such as $x + 0 = x$ is read as: whatever number $x$ you pick, this equation holds.
For $x = 7$ the law says $7 + 0 = 7$, and you can check it.
To prove a law for every number, we prove it for $0$, and then we prove that it passes from each number to the next one.
Many logicians think that this rule book contains exactly the reasoning that Hilbert called finitist.

### L2 human

We derive $\neg (Sx = x)$ in $\mathsf{PRA}$, with $\varphi(x)$ the formula $\neg (Sx = x)$.

1. The base case $\varphi(0)$ is $\neg (S0 = 0)$.
   It is the axiom $\neg (Sx = 0)$ with the term $0$ substituted for $x$.
2. The injectivity axiom $Sx = Sy \to x = y$, with $Sx$ for $x$ and $x$ for $y$, gives $SSx = Sx \to Sx = x$.
3. Its contrapositive $\neg (Sx = x) \to \neg (SSx = Sx)$ follows by a propositional tautology and modus ponens.
4. Step 3 is $\varphi(x) \to \varphi(Sx)$, so the induction rule, applied to steps 1 and 3, gives $\varphi(x)$.

Check on a number: with $x = 2$ the theorem says $3 \ne 2$.
The typical use of $\mathsf{PRA}$ is to check a metamathematical argument, such as a primitive recursive translation of proofs from one theory to another.
The trap is to apply the induction rule to a formula with a quantifier, for example to get a witness $y$ for each $x$ without naming it as a function of $x$.

### L3 human

$\mathsf{PRA}$ sits near the bottom of the scale that ordinal analysis measures.
Its ordinal is $\omega^\omega$, the same as that of $\mathsf{I}\Sigma_1$, and the ordinal of $\mathsf{PA}$ is $\varepsilon_0$.
Its $\Pi_2$ consequences match those of $\mathsf{I}\Sigma_1$, $\mathsf{RCA}_0$ and $\mathsf{WKL}_0$, so a large part of reverse mathematics is finitistically reducible in Hilbert's sense.
Weaker relatives are [[elementary function arithmetic|2JD80TE553]], whose provably total functions are the elementary ones, and [[bounded arithmetic|RA380RWEC0]], whose functions are feasible.
The [[fragments of Peano arithmetic|T70PYM1F36]] and [[true arithmetic|DX0KPMH4QZ]] place $\mathsf{PRA}$ in the larger family of theories of the natural numbers.
