---
tag: 4M1FGQ0HNZ
kind: concept
name: Mathematical jargon
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
uses: [QKEX4PD029, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Descriptive informalities
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof terminology
---

## Summary

A lecturer writes "the polynomial $p(x) = x^3 - x$ vanishes at $1$, so $x - 1$ divides it".
Nothing disappears here: "vanishes at $1$" means $p(1) = 0$, and indeed $1 - 1 = 0$.
The word is ordinary English with a special meaning that every mathematician knows and no textbook defines.

*Mathematical jargon* is the set of such words and phrases: "vanish", "nice", "well-behaved", "natural", "structure", "upstairs", "folklore", "morally true" and many more.
A jargon word differs from a defined term.
A defined term, such as "normal subgroup", has an exact definition that decides every case.
A jargon word has a meaning that the community shares and that the context makes precise.
Some jargon words are short names for exact conditions, and others express a judgment of the speaker.

## Motivation

A [[mathematical proof|0B94TKFQJX]] mixes formulas, defined terms and ordinary words.
Some ordinary words have gained a fixed sense among mathematicians, and that sense differs from the everyday one.
A "nice" function is not a pleasant function; it is a function with the properties that the current argument needs.
Experts use these words to talk fast, because one word replaces a list of conditions that both sides know.
You meet them in lectures and papers without a definition, so you need to know which ones are exact and which ones hide a choice.
The later pages on [[trivial, obvious and clearly|Y0HXCJRB9B]], [[canonical and natural|F8WNADZFMM]] and [[almost all, generic and in general|N1XSAXCQY3]] each study one family of jargon in depth.

## Notation

Jargon has no symbols of its own.
The site uses a jargon word only when it also states the exact condition behind it.
So when a page writes "$f$ vanishes on $A$", it means $f(x) = 0$ for every $x \in A$, and when it calls a function "nice", it says which property it means.

## Remarks

### A first sentence, made exact

Go back to the opening sentence and check every word.
"Vanishes at $1$" means $p(1) = 0$:
$$p(1) = 1^3 - 1 = 0.$$
The factor theorem then gives that $x - 1$ divides $p(x)$, and the division shows it:
$$x^3 - x = (x - 1)(x^2 + x) = (x - 1) \, x \, (x + 1).$$
So $p$ vanishes at $-1$, $0$ and $1$ and nowhere else, as [[the function x^2 - 4 vanishes at 2 and at -2|ZT7JBHZFHF]] works out for a second polynomial.
The related phrase "vanishes identically" means $p(x) = 0$ for every $x$, and this $p$ does not, since $p(2) = 6$.

### Words with an exact meaning

Some jargon becomes exact as soon as the setting is fixed.
"Vanish" means "equal zero", and "on the nose" means "equal exactly", not only up to an isomorphism or an approximation.
"Structure" means the extra data on a set, such as operations, an order or a topology, together with their axioms.
"Upstairs" and "downstairs" name the larger and the smaller object of a pair: a ring and a subring, a covering space and its base, or the numerator and the denominator of a fraction.
[[Upstairs and downstairs in the Gaussian integers|X49VTBJ08Z]] makes this exact: the prime $5$ downstairs in $\mathbb{Z}$ splits upstairs as $(2 + i)(2 - i)$, while $3$ stays prime.

"Natural" also belongs here in its stronger sense.
"The isomorphism $V \cong V^{**}$ is natural for a finite-dimensional space $V$" means that the map $v \mapsto (\varphi \mapsto \varphi(v))$ uses no choice of basis, as the [[canonical isomorphism with the double dual|0ZJM9D7NPS]] shows.

### Words that express a judgment

Other jargon cannot be proved or refuted, because it reports a view of the speaker.
"Let $f$ be a nice function on $[0, 1]$" often means "continuous" in a first course on integrals, and "smooth with compact support" in a course on distributions.
"Well-behaved" is a near synonym, and its opposite is [[pathological|WMBZPYPN2D]].
"Folklore" says that experts know and use a result but that it has no standard published proof or no known first author.
"Morally true" says that a claim holds in a model case, or after technical conditions are added, and the work is to find those conditions.
"For free" says that a result follows with no extra work from what is already proved.

### Two readings of "in general"

The phrase "in general" has two opposite readings, and you must tell them apart.
In "a polynomial of degree $n \geq 1$ has, in general, exactly $n$ complex roots counted with multiplicity", it means "always": the fundamental theorem of algebra gives it for every such polynomial.
In "the product of two irrational numbers is not irrational in general", it means "not always": $\sqrt{2} \cdot \sqrt{2} = 2$ is rational, although $\sqrt{2} \cdot \sqrt{3} = \sqrt{6}$ is irrational.
The clue is the negation.
"Not true in general" almost always means "has a counterexample", and the text usually gives one nearby.
A positive "in general" can mean "always" or "usually", and the second meaning is the subject of [[almost all, generic and in general|N1XSAXCQY3]].

### What is not jargon

[[The word normal in "normal subgroup" is a defined term|EZVF6MJEH9]] shows the difference.
The everyday word "normal" is vague, but "normal subgroup" has a definition that decides every subgroup, so it is a technical term, not jargon.
"Continuous" is not jargon either, because it has the exact $\varepsilon$-$\delta$ definition, and a claim of continuity can be proved or refuted.
The short form `iff` is not jargon, because it has one fixed expansion, as [[mathematical abbreviations|4ZNYMYRRY3]] explains.

### Watch out

Do not treat a jargon word as a hypothesis that needs no checking.
"Every nice function on $[0, 1]$ has a maximum" is true for continuous functions, but it fails for $f(x) = x$ on $[0, 1)$ extended by $f(1) = 0$, which is bounded and has no maximum.
Before you use such a sentence, replace "nice" by the exact condition and check that your function satisfies it.

Do not cite a "folklore" result as proved either.
It may have no complete proof in print, so give a proof or a source.

### History

Many jargon words began as informal speech in lectures and seminars and then entered print.
"Natural" is the best known case: Samuel Eilenberg and Saunders Mac Lane gave it an exact meaning in their 1945 paper that founded category theory, and the exact notion is a [[natural transformation|KYCPCC57FT]].

### Try it

First, make "the function $\sin x$ vanishes exactly at the integer multiples of $\pi$" exact and check it at one point.
It says $\sin x = 0$ if and only if $x = k\pi$ for an integer $k$; for example $\sin 2\pi = 0$, while $\sin(\pi/2) = 1 \neq 0$.

Second, decide which reading of "in general" is meant in "a continuous function is not differentiable in general".
It means "not always", and $\lvert x \rvert$ at $0$ is the counterexample.

## Explanations

### L1 human

Mathematicians use some everyday words in a special way.
When they say that a function "vanishes" at a point, they mean that its value there is zero.
The rule "subtract $3$" vanishes at $3$, because $3 - 3 = 0$.
When they call a function "nice", they mean that it has no strange behavior, such as jumps, that would break the argument.
These words help experts talk quickly, but a careful text also says exactly what they mean.

### L2 human

Make this sentence exact: "the polynomial $p(x) = x^2 + x$ vanishes at two points of $\mathbb{R}$, but over $\mathbb{Z}/2\mathbb{Z}$ it vanishes identically."
Over $\mathbb{R}$, factor and use that a product is zero only when a factor is zero:
$$x^2 + x = x(x + 1) = 0 \iff x = 0 \text{ or } x = -1.$$
So $p$ vanishes at exactly two real points.
Over $\mathbb{Z}/2\mathbb{Z}$ there are only two inputs, and both give zero:
$$p(0) = 0, \qquad p(1) = 1 + 1 = 0.$$
So $p$ vanishes at every point, which is what "identically" means.
Yet the coefficients of $p$ are $1$ and $1$, so $p$ is not the zero polynomial.
The example shows why the exact version matters: "vanishes identically" is a claim about values, not about coefficients, and over a finite field the two differ.

### L3 human

Jargon is the informal layer of the language of mathematics, and much of it points to a structure that is made formal elsewhere.
"Natural" became the theory of natural transformations, and "upstairs" and "downstairs" describe a morphism $Y \to X$ seen from its source and from its target.
"On the nose" separates strict equality from equality up to isomorphism, a distinction that higher category theory puts at the center.
"Morally true" often points to a statement that holds in a model case, such as the finite-dimensional or the smooth case, and the research is to find the hypotheses under which it holds in general.
Other words, such as "folklore", describe the sociology of a field and not its mathematics.
The later families of jargon, from [[sufficiently large, eventually and frequently|FEQ7WATMHF]] to [[sharp and best possible results|KWQV0G0VJ3]] and [[elementary proof|84SZZBACP3]], each turn one informal word into a precise statement.
