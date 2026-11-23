---
tag: CRW82NARQV
kind: concept
name: Quantifier shift fallacy
aliases: [quantifier-shift-fallacy, quantifier-shift, illicit-quantifier-shift]
msc: ["00A35", "97E30"]
topics: [T6QQ749DM5]
audience: ug1
uses: [0FYQMKFE77, EGTZPA6QH3, 0X3WGX95FE, 0M4JJT780X]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_shift
    locator: Definition
  - url: https://en.wikipedia.org/wiki/List_of_incomplete_proofs
    locator: Status unclear
  - url: https://en.wikipedia.org/wiki/Uniform_continuity
    locator: lead section
  - book: isbn:9781108439534
---

## Summary

Here is a short proof of a surprising claim; find the step that breaks.

> Claim: some positive real number is smaller than every positive real number.
> Proof: for every positive real $x$ there is a positive real $y$ with $y < x$, namely $y = \frac{x}{2}$, so some positive real $y$ satisfies $y < x$ for every positive real $x$.

The claim is false, since such a $y$ would satisfy $y < y$ when we take $x = y$.
The first half of the proof is true, and the error is the word "so".
The proof turns $\forall x \, \exists y \, (y < x)$ into $\exists y \, \forall x \, (y < x)$, and the $y$ it found depends on $x$.

That move is the quantifier shift fallacy: the invalid inference from $\forall x \, \exists y \, P(x, y)$ to $\exists y \, \forall x \, P(x, y)$.
The premise lets each $x$ have its own $y$, and the conclusion demands one $y$ for all $x$ at once.
The correct version keeps the [[order of quantifiers|0FYQMKFE77]]: every positive real has a smaller positive real, and no positive real is smaller than all of them.
In analysis the same error confuses [[continuity|0X3WGX95FE]] with [[uniform continuity|0M4JJT780X]], and pointwise convergence with uniform convergence.

## Motivation

Words hide the order of [[quantifiers|EGTZPA6QH3]].
"Every lock has a key" lets each lock have its own key, and it does not promise one key that opens every lock.
In analysis the shift hides in the phrase "choose $\delta$".
A proof of continuity finds a $\delta$ for each point and each $\varepsilon$.
If a later step uses one $\delta$ for all points at once, it has shifted a quantifier, and it owes the reader a new argument.

## Notation

The formal name in logic is the quantifier shift fallacy, also called an illicit exchange of quantifiers, and teachers often say "swapping the quantifiers".
In symbols, $\forall x \, \exists y \, P(x, y) \not\Rightarrow \exists y \, \forall x \, P(x, y)$.
To show that $y$ may depend on $x$, authors write $y = y(x)$, or $\delta = \delta(\varepsilon, a)$ for a $\delta$ that depends on the point $a$.
A statement is called uniform when $\delta = \delta(\varepsilon)$ does not depend on the point.

## Remarks

### Examples to sort

Decide for each inference whether it is valid before you read the verdict.

1. "Every natural number has a larger one, so some natural number is larger than all." It shifts, and it is [[false|F1GYSA9TW0]].
2. "The function $\frac{1}{x}$ is continuous at each point of $(0, 1)$, so it is uniformly continuous there." It shifts, and the $\delta$ [[must depend on the point|2BZ4WGH7C3]].
3. "Each $x^n$ on $[0, 1]$ converges at every point, so the convergence is uniform." It shifts, and the limit is not even continuous, so the [[convergence is not uniform|0YSRR1JTKZ]].
4. "Some number bounds every element of $S$, so every element of $S$ has a bound." It is the [[valid direction|PR3VZMWQ6B]].
5. "For all $x$ and all $y$, $P(x, y)$; so for all $y$ and all $x$, $P(x, y)$." Two quantifiers of the same kind commute, so it is valid.

### The valid direction and the proved shifts

From $\exists y \, \forall x \, P(x, y)$ we may always conclude $\forall x \, \exists y \, P(x, y)$.
Take the $y_0$ of the premise; for each $x$, the same $y_0$ works.
The other direction needs an extra reason, and then it is a theorem, not a fallacy.
On a finite set of $x$'s, when $P(x, y)$ stays true as a real $y$ grows, the largest of the finitely many $y$'s works for every $x$.
Compactness is the general tool that reduces infinitely many choices to finitely many.
That is how a continuous function on a closed bounded interval is proved to be [[uniformly continuous|0W0TZDRF9C]].

### Watch out

The shift often happens in the order of choices, not in a formula.
A proof fixes $\varepsilon$, picks $N$ or $\delta$, and only later says "let $x$ be any point".
If the choice of $N$ used $x$, the proof has quietly put $\exists N$ before $\forall x$.
A related slip appears when negating: the negation of $\forall x \, \exists y \, P$ is $\exists x \, \forall y \, \neg P$, so both quantifiers flip, not only $P$.

### History

In his *Cours d'analyse* of 1821, Augustin-Louis Cauchy stated that a convergent series of continuous functions has a continuous sum.
In 1826 Niels Henrik Abel pointed to the series $\sin x - \frac{\sin 2x}{2} + \frac{\sin 3x}{3} - \cdots$ as an exception.
Its sum is $\frac{x}{2}$ for $-\pi < x < \pi$ and $0$ at $x = \pi$, so the sum jumps at $\pi$.
Historians still debate what Cauchy's hypotheses meant, but read with modern definitions his argument shifts a quantifier, and the correct theorem needs uniform convergence.

### Try it

Is the inference "every real polynomial of odd degree has a real root, so some real number is a root of every real polynomial of odd degree" valid?
No: it shifts the quantifiers, and $x$ and $x - 1$ have no common root.

A function $f$ on $[0, 1]$ satisfies "for every $x$ there is $M$ with $|f(x)| \le M$".
Is $f$ bounded?
Not from this alone, since the condition holds for every real function, with $M = |f(x)|$; boundedness is the shifted statement "there is $M$ with $|f(x)| \le M$ for every $x$".

## Explanations

### L1 human

"Everyone has a mother" is true.
"There is one woman who is the mother of everyone" is false.
The two sentences use the same words in a different order.
The first lets each person have a different mother, and the second asks for one mother for all.
Swapping "every" and "some" can turn a true sentence into a false one.

### L2 human

We test the inference: for each $\varepsilon > 0$ and each $x \in (0, 1)$ some $N$ gives $x^n < \varepsilon$ for all $n \ge N$, so some $N$ gives $x^n < \varepsilon$ for all $x \in (0, 1)$ and all $n \ge N$.
The premise is true, because $x^n \to 0$ for each fixed $x \in (0, 1)$.
The conclusion asks for one $N$ for every $x$.
Take $\varepsilon = \frac{1}{2}$ and suppose that $N$ works.
The point $x = \left(\frac{3}{4}\right)^{1/N}$ lies in $(0, 1)$, and $x^N = \frac{3}{4} > \frac{1}{2}$, a contradiction.
So the conclusion is false: the convergence is pointwise but not uniform.

The typical use of this check is to write an analytic statement in symbols, with its quantifiers in order, before using it.
Watch out for an $N$ or a $\delta$ chosen at the start of a proof whose formula secretly contains the point $x$.

### L3 human

By Skolemization, $\forall x \, \exists y \, P(x, y)$ says that some function $g$ satisfies $\forall x \, P(x, g(x))$, while $\exists y \, \forall x \, P(x, y)$ asks for a constant $g$.
So the shift is valid exactly when a choice function can be taken constant.
Uniform continuity, equicontinuity, uniform boundedness and uniform convergence are all statements of this kind.
Compactness arguments, the [[uniform limit theorem|0X9XT05JVC]], the Baire category theorem behind the uniform boundedness principle, and the Arzelà-Ascoli theorem prove such shifts under extra hypotheses.
In topology the same pattern separates "locally" from "globally", and in computability it separates "for each input some algorithm works" from "one algorithm works for all inputs".
