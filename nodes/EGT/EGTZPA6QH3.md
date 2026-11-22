---
tag: EGTZPA6QH3
kind: concept
name: Quantifiers in mathematical writing
msc: ["97E40", "03B10"]
topics: [WMY13MXY3W]
audience: school
uses: [S9MHMRAX88, 12QQ51VK01, FA6YZGR2SS]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Bounded_quantifier
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.1
---

## Summary

A quantifier says how many objects a claim is about: all of them, or at least one.
"Every positive real number has a square root" contains two quantifiers, one in "every" and one hidden in "has": for every real $x > 0$ there is a real $y$ with $y^2 = x$.

A *quantifier* in mathematical writing is a phrase that says for how many objects of a given set, the *domain*, an open sentence $P(x)$ is true.
The *universal quantifier* says that $P(x)$ is true for every $x$ in the domain.
Its English forms include "for all", "for every", "for each", "all", "every", "each" and often "any".
The *existential quantifier* says that $P(x)$ is true for at least one $x$ in the domain.
Its English forms include "there exists", "there is", "for some", "some" and "at least one".
A quantifier binds its variable, and the result is a [[statement|S9MHMRAX88]].
A *bounded quantifier* names its domain inside the phrase, as in "for every $\varepsilon > 0$" or "there is $n \in \mathbb{N}$".

## Motivation

Ordinary English uses quantifiers loosely.
"Everybody loves somebody" can mean that each person loves some person, or that one person is loved by everybody.
"A cat has four legs" means every cat, but "a cat is in the garden" means some cat.
Mathematical definitions stack several quantifiers, and a change of order or of domain changes the meaning.
The definition of the [[limit of a sequence|05M5SWSZZD]] has three quantifiers in a fixed order: for every $\varepsilon > 0$ there is $N$ such that for every $n \ge N$, $|a_n - L| < \varepsilon$.
So mathematics fixes the English forms of the two quantifiers, and careful authors write each one.
[[Negating mathematical statements|K930V33BSC]] shows what happens to quantifiers under "not", and [[existence and uniqueness statements|ACSC75R7R5]] adds the quantifier "exactly one".

## Notation

The [[universal quantifier|0GHS47PDAQ]] is $\forall$, and the [[existential quantifier|0MSRQHCNN9]] is $\exists$.
Books write "for all $x$ in $A$, $P(x)$" as $\forall x \in A, \; P(x)$, as $(\forall x \in A) \, P(x)$, or as $\forall x \in A : P(x)$.
Many authors put a universal quantifier after the formula, as in "$x^2 \ge 0$ for all real $x$".
The symbol $\exists!$ means "there is exactly one".
The word "any" is a trap: it can mean "every" or "some", as [[the word "any"|K0N4D582KJ]] shows, so it is safer to write "every" or "some".

## Remarks

### Taking a sentence apart

Go back to "every positive real number has a square root" and write it with symbols:
$$\forall x > 0 \;\; \exists y \in \mathbb{R} \;\; y^2 = x.$$
To check it, take any $x > 0$ and answer with $y = \sqrt{x}$.
The answer $y$ depends on $x$: for $x = 4$ it is $2$, and for $x = 9$ it is $3$.

Now swap the two quantifiers:
$$\exists y \in \mathbb{R} \;\; \forall x > 0 \;\; y^2 = x.$$
This says that one number $y$ is a square root of every positive number at once, and it is false.
If $y^2 = 1$ and $y^2 = 4$, then $1 = 4$.
So the [[order of quantifiers|0FYQMKFE77]] matters: "for every $x$ there is $y$" lets $y$ depend on $x$, and "there is $y$ for every $x$" does not.
Two quantifiers of the same kind, by contrast, can change places without changing the meaning.

### Hidden quantifiers

Many quantifiers are not written at all.
An identity such as $(a + b)^2 = a^2 + 2ab + b^2$ means "for all real $a$ and $b$", as [[the hidden quantifier in an algebraic identity|N3FERWCTTJ]] shows.
A theorem with a free letter means "for every" that letter: "if $n$ is even, then $n^2$ is even" is about every integer $n$.
Even definitions hide them.
"A function $f$ is increasing if $f(x) \le f(y)$ whenever $x \le y$" means: for all real $x$ and $y$, if $x \le y$, then $f(x) \le f(y)$.

The article "a" can hide either quantifier.
"A square is a rectangle" means every square.
"$x$ is a root of $p$" means one root, and there may be others.

### Bounded quantifiers

A bounded quantifier is a short form, and the two short forms expand differently:
$$\forall x \in A, \; P(x) \quad \text{means} \quad \forall x \, (x \in A \Rightarrow P(x)),$$
$$\exists x \in A, \; P(x) \quad \text{means} \quad \exists x \, (x \in A \text{ and } P(x)).$$
The same holds with a condition such as $\varepsilon > 0$ in place of $x \in A$.
Why "if" for one and "and" for the other?
Try the wrong word in each.
With "and", "every prime greater than $2$ is odd" would become "every integer $n$ is a prime greater than $2$ and is odd", which claims that $4$ is prime.
With "if", "some prime is even" would become "there is $n$ such that if $n$ is prime, then $n$ is even", which $n = 9$ makes true for a useless reason.
The right forms say what we mean: every $n$ that is a prime greater than $2$ is odd, and some $n$ is a prime and is even, namely $2$.
[[Bounded quantifiers in the definition of a bounded sequence|4KJ5K9MX21]] works through a full definition.

### What is not a quantifier

Not every letter is a variable that ranges over a domain.
[[The phrase "let $x = 3$"|7KW3CKEY4P]] gives $x$ one value, so it quantifies nothing.
In "solve $x^2 = 2$", the letter $x$ is an unknown, and the task is to find the solution set $\{\sqrt{2}, -\sqrt{2}\}$; the equation claims neither "for all $x$" nor "for some $x$".
In "the number $p = 2^{31} - 1$ is prime", the letter $p$ is a name for one number, and the sentence is a statement with no quantifier.

### The rules you can use

On a finite domain $\{a_1, \dots, a_n\}$, "for all $x$, $P(x)$" means "$P(a_1)$ and ... and $P(a_n)$", and "there is $x$ with $P(x)$" means "$P(a_1)$ or ... or $P(a_n)$".
So the quantifiers are long forms of "and" and "or", and they follow the same laws.
The [[negation of a universal statement|0P3A06QNDP]] is an existential statement, and the [[negation of an existential statement|05SZQKH75K]] is a universal one.
A universal statement over the empty domain is true, and an existential one is false, which is [[vacuous truth|0V4QXPGJQK]].
The name of a bound variable does not matter: "for all $x$, $x^2 \ge 0$" and "for all $t$, $t^2 \ge 0$" are the same statement.

### Watch out

The first error is to join "there is" with "if ... then".
"There is a real $x$ such that if $x > 0$, then $x^2 = -1$" is true, because $x = -1$ makes the hypothesis false.
The intended "there is $x > 0$ with $x^2 = -1$" is false.
The second error is to move a quantifier to the end of a sentence.
"There is $\delta > 0$ with $|f(x) - f(a)| < \varepsilon$ when $|x - a| < \delta$, for all $\varepsilon > 0$" can be read with $\delta$ chosen before $\varepsilon$, and that is a different statement.
The third error is to prove a universal statement by checking examples, which proves only the instances that were checked.

### History

Aristotle built his syllogisms from sentences with "all", "some" and "no".
Gottlob Frege introduced the quantifier with a bound variable in his Begriffsschrift of 1879, and this made statements with several quantifiers precise.
Giuseppe Peano used the symbol $\exists$, and Gerhard Gentzen introduced $\forall$ in 1935, by analogy with $\exists$.

### Try it

First, write "every integer has a larger integer" with symbols and decide whether it is true.
It is $\forall n \in \mathbb{Z} \; \exists m \in \mathbb{Z} \; m > n$, and it is true: take $m = n + 1$.

Second, swap the quantifiers and decide again.
$\exists m \in \mathbb{Z} \; \forall n \in \mathbb{Z} \; m > n$ claims an integer that is larger than every integer, and it is false, because $n = m$ itself fails $m > n$.

## Explanations

### L1 human

"Every child in the class has a pencil" is a claim about all the children.
One child without a pencil makes it false.
"Some child in the class has a pencil" claims that at least one child has one.
One child with a pencil makes it true.
In mathematics, "every number from $1$ to $5$ is less than $6$" is true, and "some number from $1$ to $5$ is even" is true, because $2$ is even.
The words "every" and "some" are the two quantifiers.

### L2 human

Write "$f \colon \mathbb{R} \to \mathbb{R}$ is increasing if $f(x) \le f(y)$ whenever $x \le y$" with explicit quantifiers, and test it.
The letters $x$ and $y$ have no values, so each has a hidden "for all" over $\mathbb{R}$, and "whenever" introduces a hypothesis:
$$\forall x \in \mathbb{R} \;\; \forall y \in \mathbb{R} \;\; \big( x \le y \Rightarrow f(x) \le f(y) \big).$$
For $f(x) = x^3$, take $x \le y$ and factor:
$$y^3 - x^3 = (y - x)(x^2 + xy + y^2), \qquad x^2 + xy + y^2 = \left(x + \tfrac{y}{2}\right)^2 + \tfrac{3}{4} y^2 \ge 0.$$
Both factors are at least $0$, so $f(x) \le f(y)$, and $x^3$ is increasing.

The negation says that $f$ is not increasing when there are $x \le y$ with $f(x) > f(y)$.
For $f(x) = x^2$ the pair $x = -2$, $y = 0$ gives $4 > 0$, so $x^2$ is not increasing.
A universal goal starts a proof with "let $x$ and $y$ be arbitrary", and an existential goal ends with a specific object, as here.
Watch out: the negation keeps "$x \le y$" and negates only the conclusion; it is not "for all $x \le y$, $f(x) > f(y)$".

### L3 human

In [[predicate logic|086QKPF0A6]], the two quantifiers bind variables in formulas, and a bounded quantifier is a quantifier relativized to a definable set.
Mathematical writing also uses quantifiers that are not first-order: "for infinitely many $n$", "for almost every $x$" and "for all sufficiently large $n$".
The last two are [[filter quantifiers|EAJH1P4MK9]], and all three are [[generalized quantifiers|MFV98WTF4G]].

A statement $\forall x \, \exists y \, P(x, y)$ is equivalent, with the axiom of choice, to the existence of a function $g$ with $P(x, g(x))$ for all $x$, a Skolem function.
In the square root example, $g(x) = \sqrt{x}$ is such a function.
In category theory, $\exists$ and $\forall$ are the left and the right adjoints of substitution, as Lawvere observed.
In arithmetic, formulas with only bounded quantifiers are decidable, and they form the base of the arithmetical hierarchy.
