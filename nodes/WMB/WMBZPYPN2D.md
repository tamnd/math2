---
tag: WMBZPYPN2D
kind: concept
name: Pathological object
aliases: [pathology, pathological-example, pathological-function]
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug2
uses: [0ED72CTBNP, 0X3WGX95FE, 0K57YG3BB8, 0XGCZ4GDZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Philosophy of mathematics
  - url: https://en.wikipedia.org/wiki/Pathological_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Pathological_(mathematics)
    locator: In analysis
---

## Summary

A pathological object is one that breaks the picture we have of its kind, and it is usually built to show that a plausible guess is false.
You meet the word in sentences such as "the Weierstrass function is a pathological example": the function is [[continuous|0X3WGX95FE]] at every point and [[differentiable|0K57YG3BB8]] at no point, while every graph you can draw by hand has a slope almost everywhere.

A mathematical object is called *pathological* when it fails a regularity property that the familiar members of its class have, or when it behaves against the intuition that those members give.
The opposite informal words are *well-behaved* and *nice*.
The word is informal and relative: it depends on the class, on the property in question and on the time.
Many objects that were called pathological when they were found are now standard textbook examples, and each one belongs to its own area.

## Motivation

Intuition about a class comes from its simplest members.
For functions these are the polynomials and the functions of a calculus course, and their graphs have a slope at all but a few points.
So it is natural to guess that every continuous function is differentiable at most points.
A pathological object shows that the guess is false.

It does more than refute a guess.
It shows which hypothesis a theorem really needs, since any correct theorem must exclude the pathology.
The [[mean value theorem|0BARQY52N5]] assumes differentiability on an open interval, and the Weierstrass function shows that continuity alone would not be enough.
In this way a pathology is a [[counterexample|0ED72CTBNP]] that sharpens the statements around it.

## Notation

No symbol marks a pathology.
Authors write "a pathological example", "a pathology", "pathological behavior", or "for well-behaved functions".
The words "nice" and "sufficiently nice" mark a class that excludes pathologies, often without a precise definition, and a careful author replaces them by a condition such as "continuously differentiable".

The word has two readings.
In the first, "pathological" means *against intuition*: the Cantor set is pathological because it has length $0$ and as many points as $[0, 1]$.
In the second, "pathological" means *rare*, an exception that a theorem may ignore.
The two readings can disagree, because a set can defeat intuition and still be typical.
To tell which one an author means, look for a size statement: "the pathological cases form a set of measure zero" is the second reading, and a bare "pathological example" is usually the first.
The related word "degenerate" means a limit case of a definition, such as a triangle whose three corners lie on one line.

## Remarks

### A first pathology: the Weierstrass function

The [[Weierstrass function|01A0MK1730]] is a sum of cosine waves that get smaller in height and faster in frequency:
$$W(x) = \sum_{n = 0}^{\infty} a^n \cos(b^n \pi x), \qquad 0 < a < 1, \ b \text{ an odd integer}, \ ab > 1 + \tfrac{3\pi}{2}.$$
For example, $a = \tfrac{1}{2}$ and $b = 13$ work, since $ab = 6.5$ and $1 + \tfrac{3\pi}{2} \approx 5.71$.

Continuity is the easy half.
Each term is continuous, and the $n$-th term is at most $a^n$ in size, so the series converges uniformly by comparison with the geometric series $\sum a^n = \frac{1}{1 - a}$.
A uniform limit of continuous functions is continuous.

The hard half is that $W$ has no derivative anywhere.
The reason, in outline, is that the $n$-th wave has slope of size about $(ab)^n \pi$, and $ab > 1$ makes these slopes grow without bound, so no single slope survives at any point.

### Pathologies built to order

Each standard pathology defeats one specific picture.
[[The Cantor set|ZJ4WMR747A]] has length $0$, contains no interval, and is uncountable.
[[Thomae's function|6R8EVWZ6TH]] is continuous at each irrational number and discontinuous at each rational number.
The [[Dirichlet function|0T4EJ8ZJM9]], equal to $1$ on the rationals and $0$ on the irrationals, is discontinuous at every point.
A [[Vitali set|WYHGXY471C]] has no [[Lebesgue measure|2Z2QVWZ262]] at all, and a [[space-filling curve|QPRHC4DZ20]] is a continuous map from $[0, 1]$ onto the square $[0, 1]^2$.

The word is relative to the class.
The Cantor set is pathological as a subset of the line, but in topology it is a basic model space.
It is also relative to time: the functions of Weierstrass and Dirichlet are now routine examples in a first course of analysis.

### When the pathology is typical

In 1931 Banach showed that the functions that are differentiable at even one point form a [[meagre set|0XGCZ4GDZ6]] in the space of continuous functions on an interval, with the uniform distance.
So, in the sense of the [[Baire category theorem|0A7KGAYHGV]], most continuous functions are nowhere differentiable.

This is where the two readings of the word split.
The Weierstrass function is pathological in the first reading, because it defeats the picture of a graph.
It is not pathological in the second reading, because functions like it are the typical case and the smooth functions are the exception.
A theorem about all continuous functions cannot ignore such functions as rare.

### What is not pathological

[[The absolute value function is not pathological|CP6K030FG0]]: it fails to be differentiable at one point, $0$, and the corner of its graph is exactly what a drawing shows.
A polynomial is well-behaved: it is continuous, differentiable any number of times, and has finitely many zeros unless it is the zero polynomial.
The function $f(x) = 1/x$ on $(0, 1)$ is unbounded, but it is not pathological, since its graph matches the picture that intuition gives.
So a counterexample need not be pathological: $|x|$ refutes "continuous implies differentiable" without defeating anyone's picture.

### Watch out

The first error is to treat "pathological" as a formal property.
It is a judgment, and two authors can disagree about one object; a proof can never use "$f$ is not pathological" as a hypothesis.

The second error is to assume that pathologies are rare and may be ignored.
Banach's theorem shows that nowhere differentiable functions are typical among continuous functions, so a claim about all continuous functions must cover them.

The third error is to test a claim about a large class only on smooth members.
The claim "every continuous function on $[0, 1]$ is differentiable at some point" passes every test with polynomials, $\sin$, $\exp$ and $|x - \tfrac{1}{2}|$, and it is still false.

### History

Karl Weierstrass presented his continuous, nowhere differentiable function to the Prussian Academy of Sciences in 1872.
In 1931 Banach proved that the continuous functions differentiable at some point form a meagre set.

### Try it

First, is the function $\sin(1/x)$ on $(0, 1]$ pathological?
Most authors would not say so: it oscillates infinitely often near $0$, but it is differentiable at every point of its domain, and its graph can be pictured.

Second, is the Cantor set pathological when you study it as a compact metric space?
No: in topology it is a basic model, since every nonempty compact metric space is a continuous image of it.

## Explanations

### L1 human

Most graphs in school are smooth curves, perhaps with a few corners.
A pathological function has a graph that is very different from these pictures.
The Weierstrass function has a graph with no breaks, but with tiny corners at every point, so it has no slope anywhere.
Mathematicians call such objects pathological because they defeat the usual picture.
They are useful, because they show where our intuition stops being reliable.

### L2 human

Test the claim "every continuous function on $[0, 1]$ is differentiable at some point".
It holds for polynomials, for $\sin$ and $\exp$, and for $|x - \tfrac{1}{2}|$, which is differentiable everywhere except at $\tfrac{1}{2}$.
The Weierstrass function with $a = \tfrac{1}{2}$ and $b = 13$ is continuous on $[0, 1]$, since its terms are bounded by
$$\sum_{n = 0}^{\infty} \left(\tfrac{1}{2}\right)^n = 2,$$
and it is differentiable at no point, so the claim is false.
Hence a theorem that needs a derivative must assume one, as the mean value theorem does.
This is the typical use of a pathology: it marks the hypotheses that a theorem cannot drop.
No computer plot can show the pathology, because a screen has finitely many pixels and every plotted curve looks like a polygon.

### L3 human

The words "pathological" and "well-behaved" often have exact replacements inside a field.
In measure theory, well-behaved usually means measurable, and the existence of a Vitali set depends on the [[axiom of choice|0HTGB13FE2]].
In analysis, "generic" has an exact meaning through the Baire category theorem: a property is generic when it holds outside a meagre set, and with this meaning nowhere differentiability is generic.

The same object can be small in one sense and large in another.
The Cantor set has measure $0$ and the cardinality of the continuum, and it is also nowhere dense, so it is small for measure and for category but large for cardinality.
The common pattern is that a regularity class, such as smooth or analytic functions, is a small part of a larger natural class, and the page on [[almost all, generic and in general|N1XSAXCQY3]] treats these notions of size side by side.
