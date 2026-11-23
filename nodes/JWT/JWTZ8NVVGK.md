---
tag: JWTZ8NVVGK
kind: concept
name: Indicators
aliases: [kirby-paris-indicators, indicator-function-for-initial-segments]
msc: ["03C62", "03F30"]
topics: [T6FK1E7GJ1]
audience: research
uses: [1QWN5CV4CG, MPSCREYC3M, 1NR3HAWG9D]
sources:
  - url: https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic
    locator: Structure of countable non-standard models
  - url: https://en.wikipedia.org/wiki/Paris–Harrington_theorem
    locator: lead section
---

## Summary

An indicator is a definable function that measures the gap between two numbers of a [[non-standard model|1QWN5CV4CG]] of arithmetic, so that the measure is infinite exactly when a cut of a given kind fits into the gap.
Indicators turn the existence of special initial segments, which a model cannot define, into the size of a definable function, and they give the standard template for proofs that a sentence is unprovable in [[Peano arithmetic|MPSCREYC3M]].

Let $M$ be a countable non-standard model of $\mathsf{PA}$, with standard part $\mathbb{N}$.
A *cut* of $M$ is a set $I \subseteq M$ with $\mathbb{N} \subseteq I \ne M$ that is closed downward and under $x \mapsto x + 1$.
Let $\mathcal{K}$ be a class of cuts of $M$, for example the cuts $I$ with $I \models \mathsf{PA}$.
A function $Y : M^2 \to M$ is an *indicator for $\mathcal{K}$* if three conditions hold.

1. $Y$ is definable in $M$ by a formula of arithmetic without parameters.
2. $Y(a, b) \le b$, and $Y(a, b) \le Y(a', b')$ whenever $a' \le a \le b \le b'$.
3. For all $a \le b$ in $M$, $Y(a, b)$ is non-standard if and only if some $I \in \mathcal{K}$ has $a \in I$ and $b \notin I$.

## Motivation

To show that $\mathsf{PA}$ does not prove a sentence, we can build a model of $\mathsf{PA}$ in which the sentence fails.
Inside a non-standard model $M$, a natural source of such models is the initial segments $I$ of $M$ with $I \models \mathsf{PA}$.
These segments are not definable in $M$, so $M$ cannot talk about them directly.
An indicator is a definable function that sees them anyway, through the size of its values.

The method came from the model-theoretic proof of the [[Paris-Harrington theorem|509ZWA0R26]], and it returns in the [[Kanamori-McAloon theorem|NM5WYBK6BG]] and other independence results.
It also links model theory with growth: an indicator for the models of $\mathsf{PA}$ gives a function that grows faster than every [[provably total function|Z742YPHPNS]] of $\mathsf{PA}$.

## Notation

We write $a \in I < b$ for "$a \in I$ and $b \notin I$".
Since $I$ is closed downward, $b \notin I$ means that $b$ lies above every element of $I$, which explains the notation.
Books often write $I \subseteq_e M$ for an initial segment and $\mathbb{N} \subsetneq_e I \subsetneq_e M$ for a proper cut.
Watch the order in $a \in I < b$: it is a short form for two facts, not a comparison between a set and a number.

## Remarks

### A first computation

Let $c$ be a non-standard element of $M$, and use the difference $Y(a, b) = b - a$.
For $a = c$ and $b = c + 5$ we get $Y = 5$, a standard number.
Indeed no cut separates $c$ from $c + 5$, because a cut that contains $c$ contains $c + 1, \dots, c + 5$ by closure under $x \mapsto x + 1$.

For $a = c$ and $b = 2c$ we get $Y = c$, which is non-standard.
A cut does separate them: the set of $x$ with $x \le c + k$ for some standard $k$ contains $c$, is closed under $x \mapsto x + 1$, and misses $2c$, since $c \le k$ is false for each standard $k$.
So the [[difference indicator|1T6K132VVA]] answers the question "is there a cut between $a$ and $b$?" by a size.

### The template for unprovability

Let $T \supseteq \mathsf{PA}$, and let $Y$ be an indicator for the cuts that are models of $T$, in every countable non-standard model of $T$.

1. Assume that $Y(a, b) \ge c$ has a formula with bounded quantifiers, so that it has the same truth value in $M$ and in each cut that is a model of $\mathsf{PA}$.
2. Suppose that $T$ proves $\forall a \, \exists b \; Y(a, b) \ge a$.
   Take a countable non-standard model $M$ of $T$ and a non-standard $a \in M$.
3. Let $b$ be the least element with $Y(a, b) \ge a$.
   Then $Y(a, b)$ is non-standard, so some cut $I \models T$ has $a \in I < b$.
4. In $I$ some $b'$ has $Y(a, b') \ge a$, by step 2 inside $I$, and this holds in $M$ by step 1.
   But $b' < b$, which contradicts the choice of $b$.
5. So $T$ does not prove $\forall a \, \exists b \; Y(a, b) \ge a$.

The truth of the sentence in $\mathbb{N}$ is proved separately in each application, for example by compactness for the Paris-Harrington principle.

### Examples of indicators

The [[difference indicator|1T6K132VVA]] $Y(a, b) = b - a$ is an indicator for the class of all cuts.
The [[doubling indicator|K470Y7R628]] $Y(a, b) = \max \{ c : a \cdot 2^c \le b \}$ is an indicator for the cuts closed under $x \mapsto 2x$.
The function of the [[Paris-Harrington proof|D0Q498H0R5]], defined from the strengthened finite Ramsey theorem on $[a, b]$, is an indicator for the cuts that are models of $\mathsf{PA}$; that is the cited indicator lemma.
Faster operations in the definition give indicators for smaller classes of cuts, and the models of $\mathsf{PA}$ need a real combinatorial principle.

### What is not an indicator

The [[doubling indicator is not an indicator for models of PA|Q1WSA5TPC2]].
For non-standard $c$ the value $Y(c, c^2)$ is non-standard, but every model of $\mathsf{PA}$ that contains $c$ also contains $c^2$, so condition 3 fails.

A constant function is not an indicator for a nonempty class $\mathcal{K}$.
No cut has $a \in I < a$, so $Y(a, a)$ must be standard, while $Y(a, b)$ must be non-standard when a cut in $\mathcal{K}$ separates $a$ from $b$.

### Watch out

A common slip is to forget that the class $\mathcal{K}$ is part of the definition.
The doubling function is an indicator for the cuts closed under doubling, and it is not an indicator for the models of $\mathsf{PA}$.

A second slip is to argue inside $M$ about the cut that an indicator finds.
A non-standard value says that a cut exists, but the cut is not definable in $M$, so no formula of $M$ can name it.

A third slip is to prove condition 3 in one model only.
The template needs the indicator property in every countable non-standard model of the theory, and each application must say so.

### History

Laurence Kirby and Jeff Paris developed indicators in the late 1970s, in work on initial segments of models of $\mathsf{PA}$.
The model-theoretic proof of the Paris-Harrington theorem uses this method.

### Try it

First, compute the doubling indicator $Y(5, 200)$.
We have $5 \cdot 2^5 = 160 \le 200 < 320 = 5 \cdot 2^6$, so $Y(5, 200) = 5$.

Second, for non-standard $c$, is $c^2 - c$ standard?
No: $c^2 - c = c(c - 1) \ge c$ for $c \ge 2$, so it is non-standard, and the difference indicator finds a cut between $c$ and $c^2$.

## Explanations

### L1 human

A non-standard model of arithmetic has the ordinary numbers at the bottom and infinite numbers above them.
Between two infinite numbers $a$ and $b$ there may be a gap in which a whole smaller model of arithmetic lives.
An indicator is a formula that measures the distance from $a$ to $b$, so that the distance is infinite exactly when such a gap exists.
For example, the plain difference says that $c$ and $c + 5$ are close, while $c$ and $2c$ are far apart.
This lets us prove that a statement about growth is unprovable by finding such gaps.

### L2 human

We check the difference indicator $Y(a, b) = b - a$ for the class of all cuts.
If $b - a$ is non-standard, let $I$ be the set of the $x \le a + k$ for some standard $k$.
Then $I$ is closed downward and under $x \mapsto x + 1$, it contains $a$, and it misses $b$, because $b \le a + k$ would make $b - a \le k$ standard.

Conversely, if a cut $I$ has $a \in I < b$, then $a + k \in I$ for each standard $k$, so $b > a + k$ and $b - a > k$ for each standard $k$.
So $b - a$ is non-standard exactly when a cut separates $a$ from $b$.
The typical use is the template above, with an indicator for the cuts that are models of $\mathsf{PA}$ in place of this simple one.
The trap is that the cut found here is usually not a model of $\mathsf{PA}$, because it is not closed under addition.

### L3 human

Suppose $Y$ is an indicator for the models of $\mathsf{PA}$ in every countable non-standard model, and the function $g(x) = \min \{ b : Y(x, b) \ge x \}$ is total in $\mathbb{N}$.
For a provably total $f$ and a non-standard $x$, the cut $I \models \mathsf{PA}$ between $x$ and $g(x)$ contains $f(x)$, so $f(x) < g(x)$.
A [[compactness|1NR3HAWG9D]] argument then shows that $g$ eventually dominates $f$ in $\mathbb{N}$.
So indicators connect the model theory of $\mathsf{PA}$ with [[provably total functions|Z742YPHPNS]] and with the [[fast-growing hierarchy|R6ZC4BJGXV]], and this gives the lower bound for the growth of the Paris-Harrington function.
