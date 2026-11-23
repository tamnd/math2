---
tag: VKSK35Y52Z
kind: statement
role: lemma
name: Generalization theorem
aliases: [generalization-theorem, generalization-on-constants]
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
about: [N95HV0VWSM]
uses: [2B00FE6K5W, NCDZ969V7X]
sources:
  - book: isbn:9780122384523
    locator: Section 2.4
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: Predicate logic (example system)
---

## Statement

The generalization theorem says that a deduction about an $x$ that the hypotheses do not mention is a deduction about every $x$, and the same holds for a constant that the hypotheses do not mention.

Let $\vdash$ be deducibility in the [[Hilbert-style predicate calculus|2B00FE6K5W]] $\mathsf{H}$, whose axioms are closed under generalization and whose only rule is modus ponens.
Let $\Gamma$ be a set of formulas and $\varphi$ a formula.

1. (Generalization theorem.) If $\Gamma \vdash \varphi$ and the variable $x$ does not occur free in any member of $\Gamma$, then $\Gamma \vdash \forall x\, \varphi$.
2. (Generalization on constants.) Suppose that $\Gamma \vdash \varphi$ and that the constant symbol $c$ does not occur in any member of $\Gamma$.
   Then there is a variable $y$ that does not occur in $\varphi$ such that $\Gamma \vdash \forall y\, \varphi_{c \mapsto y}$.

Here $\varphi_{c \mapsto y}$ is the formula obtained from $\varphi$ by replacing every occurrence of $c$ by $y$.
The [[proof|HFQG8BVXKS]] is an induction on deductions.

## Remarks

### A first use

Let $\Gamma = \{ \forall x\,(P(x) \to Q(x)),\ \forall x\, P(x) \}$.
Group 2 axioms and modus ponens give $\Gamma \vdash P(x) \to Q(x)$ and $\Gamma \vdash P(x)$, so $\Gamma \vdash Q(x)$.
Both members of $\Gamma$ are sentences, so $x$ is not free in $\Gamma$, and part 1 gives
$$\Gamma \vdash \forall x\, Q(x).$$
This is the formal version of "$x$ was arbitrary, so the claim holds for all $x$", as in [[proving universal statements|CX38X989TB]].

### Why each hypothesis is needed

Part 1 fails when $x$ is free in a member of $\Gamma$.
We have $\{ P(x) \} \vdash P(x)$, but not $\{ P(x) \} \vdash \forall x\, P(x)$.
Take the structure with domain $\{ 0, 1 \}$, $P$ true of $0$ only, and $x$ assigned to $0$: it satisfies $P(x)$ and not $\forall x\, P(x)$, so [[soundness|4A84VHDTHV]] rules out a deduction.

Part 2 fails when $c$ occurs in $\Gamma$.
We have $\{ P(c) \} \vdash P(c)$, but not $\{ P(c) \} \vdash \forall y\, P(y)$, by the same structure with $c$ naming $0$.

Part 2 also fails when $y$ is allowed to occur in $\varphi$.
The formula $\forall y\,(y = c) \to \forall y\, \forall z\,(y = z)$ is valid, since a domain in which everything equals $c$ has one element, so it is deducible by [[completeness|WQ1ZE255SF]].
Replacing $c$ by $y$ gives $\forall y\,(y = y) \to \forall y\, \forall z\,(y = z)$, which is false in every structure with two elements.

### What it gives you

If $\vdash \varphi$, then $\vdash \forall x\, \varphi$ for every variable $x$.
So the theorems of $\mathsf{H}$ are closed under generalization, although $\mathsf{H}$ has no rule of generalization.

With a lemma on renaming bound variables, part 2 gives the form that the proof of [[completeness|WQ1ZE255SF]] uses.
If $\Gamma \vdash \varphi[c/x]$ and $c$ occurs neither in $\Gamma$ nor in $\varphi$, then $\Gamma \vdash \forall x\, \varphi$.
Part 1 is also the step for $\forall$-introduction when a natural deduction proof is turned into a deduction in $\mathsf{H}$; see the [[equivalence of proof systems|A9AAHN4BMH]].

### The converse

The converse of part 1 holds with no condition on $x$.
If $\Gamma \vdash \forall x\, \varphi$, then the group 2 axiom $\forall x\, \varphi \to \varphi$, with $t = x$, and modus ponens give $\Gamma \vdash \varphi$.

### Generalizations

In Mendelson's variant $\mathsf{H}_G$, part 1 holds with no condition on $x$, because generalization is a rule there.
The price is a restriction in the [[deduction theorem for predicate logic|8M9ZFDR4DH]].
The same proof works for every Hilbert-style calculus whose axioms are closed under generalization and contain groups 3 and 4, for example the intuitionistic predicate calculus in this form.
For a first-order theory $T$ whose axioms are sentences, the condition on $x$ always holds, so $T \vdash \varphi$ gives $T \vdash \forall x\, \varphi$.

## History

Quine's *Mathematical Logic* of 1940 used axioms closed under generalization with modus ponens as the only rule.
In such systems the generalization theorem takes the place of the rule of generalization.
Enderton's textbook states both parts of the theorem in the form above.

## Explanations

### L1 human

Suppose we prove that a number $x$ has some property, and we assume nothing about $x$.
Then the same proof works for every number, so the property holds for all numbers.
The generalization theorem says that the formal calculus allows this step.
The condition "we assume nothing about $x$" is needed: from "$x$ is even" we can deduce "$x$ is even", but not "every number is even".
The second part says the same for a name $c$ that the assumptions never mention.

### L2 human

We show $\vdash \forall y\,(\forall x\, R(x) \to R(y))$ in two steps.
The formula $\forall x\, R(x) \to R(y)$ is a group 2 axiom with $t = y$, since $R(x)$ has no quantifier.
Its deduction uses no hypotheses, so $y$ is not free in any hypothesis, and part 1 gives the generalization.
In $\mathsf{H}$ this formula is also a logical axiom on its own, as a generalization of a group 2 formula, so both routes agree.
The typical use is the pattern of the first remark: remove the quantifiers, reason about an arbitrary $x$, and put the quantifier back.
Watch out: the condition is on the free variables of the hypotheses, not of $\varphi$, so check $\Gamma$ before you generalize.

### L3 human

The theorem says that the rule of generalization is admissible in $\mathsf{H}$: adding it does not change what is deducible from a $\Gamma$ in which $x$ is not free.
It is not a derivable rule in the strict sense, because its condition refers to $\Gamma$, and this is the difference between $\mathsf{H}$ and $\mathsf{H}_G$.
In [[natural deduction|6KT3BJZ7D1]] the same condition becomes the eigenvariable condition of $\forall$-introduction, and in the [[sequent calculus|W72CA3R9MP]] it is the eigenvariable condition of the right rule for $\forall$.
Part 2 is the syntactic reason why fresh constants act as arbitrary objects.
The Henkin proof of [[Gödel's completeness theorem|WQ1ZE255SF]] and the tableau rule for $\neg \forall$ both rely on this.
