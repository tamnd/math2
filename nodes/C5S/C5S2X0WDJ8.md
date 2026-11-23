---
tag: C5S2X0WDJ8
kind: concept
name: Concept image and concept definition
aliases: [concept-image, concept-definition, evoked-concept-image, tall-vinner]
msc: ["97C30", "97E40", "97I20"]
topics: [VHGA6J4NZK]
audience: research
uses: [8ZCZ3HW91Z, 0EPAT51DXQ, 05M5SWSZZD, 0X3WGX95FE]
sources:
  - url: https://doi.org/10.1007/BF00305619
    locator: pages 151-169
  - url: https://doi.org/10.1080/0020739830140305
    locator: pages 293-305
  - url: https://en.wikipedia.org/wiki/Concept_image_and_concept_definition
    locator: lead section
  - url: https://doi.org/10.1080/00029890.2004.11920092
    locator: pages 411-424
---

## Summary

A first-year student recites without error that a [[function|0EPAT51DXQ]] from $\mathbb{R}$ to $\mathbb{R}$ assigns to each real number exactly one real number.
Five minutes later she is shown $f(x) = x^2$ for $x \ge 0$ and $f(x) = -x$ for $x < 0$.
She says that this is two functions, not one, because a function has a formula.
Her answer does not come from the definition she just recited.
It comes from a picture built over years of school examples, in each of which a function had one formula.

David Tall and Shlomo Vinner named the two sides of this gap in 1981.
A person's concept image of a mathematical concept is the whole mental structure that the person links with it: pictures, examples, properties and processes.
The concept definition is a form of words that specifies the concept.
A student can know the formal [[definition|8ZCZ3HW91Z]] and still reason from an image that conflicts with it, and many errors in proofs come from such conflicts.

## Motivation

Teachers had long seen students who could state a definition and not use it.
Tall and Vinner gave names to the picture and to the definition, so that research and teaching could talk about the gap between them.
Their 1981 paper, in Educational Studies in Mathematics, studied limits and continuity, where the gap is wide: students' images of "approaching" and of "drawing without lifting the pen" differ from the epsilon-delta definitions.
The pair of terms then spread to almost every concept taught at school and university.

## Notation

Tall and Vinner used five terms, and later research keeps them.

- The concept image is the total mental structure linked with a concept, built over years and changing over time.
- The evoked concept image is the part of the image that is active at a given moment.
- The concept definition is a form of words that specifies the concept: a personal concept definition is the student's own wording, and the formal concept definition is the one mathematicians accept.
- A potential conflict factor is a part of the image that conflicts with another part or with the formal definition.
- A cognitive conflict factor is a potential conflict factor that is evoked together with the part it conflicts with, so that the student notices the conflict.

## Remarks

### Four images and where they fail

[[The function as a formula|E2MPB6KK9V]] is the image of the opening story, built from school examples, and it rejects or doubts functions defined by cases.
[[The tangent line as a line that touches once|2PVD1J6J0G]] is built from circles, and it fails for the curve $y = x^3$, which crosses its tangent at $0$.

For the [[limit of a sequence|05M5SWSZZD]], many students picture a value that the terms approach but never reach.
The image fails for the constant sequence $a_n = 1$, whose limit is $1$ and whose terms all equal $1$.

For a [[continuous function|0X3WGX95FE]], a common image is a graph drawn without lifting the pen.
The image says that $f(x) = 1/x$ is not continuous, because its graph has two branches.
By the definition, $f$ is continuous at each point of its domain, since that domain excludes $0$.

### What it is not

[[A textbook definition is a concept definition, not a concept image|PXQQW9TFM1]], because the words on the page specify the concept but are not the mental structure of any person.
A single wrong rule, such as $(a + b)^2 = a^2 + b^2$, is not a concept image either.
It may come from part of an image, such as "squaring distributes", but the image is the whole structure linked with a concept, and an error is at most a sign of one part of it.

### How images and definitions interact

An image can fit every example a student has met and still conflict with the definition, and the conflict shows only on a new example.
So an image is not wrong in itself: mathematicians also have rich images, and those images guide their intuition.
The formal definition does not replace the image.
Teaching aims at an image that agrees with the definition, and at the habit of checking the image against the definition when they might differ.
Different parts of one image can also conflict, and the conflict stays harmless until both parts are evoked at once.

### History

Tall and Vinner published "Concept image and concept definition in mathematics with particular reference to limits and continuity" in 1981, in Educational Studies in Mathematics.
Vinner (1983) applied the ideas to the concept of function, and found that many students who had learned the set definition judged examples by images of formulas and graphs.
Later research used the pair for derivatives, groups and many other concepts.
Barbara Edwards and Michael Ward (2004) studied how university students use mathematical definitions, and found that many did not use definitions the way mathematicians do.

### Watch out

A student who can recite a definition may still reason from an image that conflicts with it, as in the opening story.
Giving only typical examples makes the problem worse, because the image then contains features of those examples that the definition does not require.
And a counterexample shown once without discussion often changes nothing: the student files it as a strange exception and keeps the image.
The image changes when the student has to decide the case by the definition, and then adds the case to the image.

### Try it

A student says that $g(x) = 5$ is not a function "because there is no $x$ in it".
Which part of the image is at work, and what does the definition say?
The image is "a function is a formula in $x$"; the definition only asks for exactly one output for each input, and $g$ gives the output $5$ to every input.

A student says that the sequence $1, \tfrac{1}{2}, 1, \tfrac{1}{3}, 1, \tfrac{1}{4}, \dots$ has limit $0$ because "it gets closer and closer to $0$".
Does it?
No, because the terms equal to $1$ never get close to $0$; the image of "getting closer" ignores the definition's demand that all terms after some point stay close.

## Explanations

### L1 human

When you think of a triangle, you probably picture one with a flat bottom and a point on top.
That picture is part of your concept image: all the pictures and examples that come to mind.
The concept definition is the words: "a polygon with three sides".
Usually the picture and the words agree.
But if you only picture triangles with a flat bottom, you may not see a triangle turned upside down as a triangle.
Many mistakes in mathematics happen when the picture and the words do not agree.

### L2 human

We find a conflict between image and definition for the [[derivative|0V1EJCT8G6]].
A student's image is "the derivative at a point is the slope of the line that touches the graph there".
The formal definition is
$$f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h},$$
when the limit exists.
Test $f(x) = |x|$ at $a = 0$, where the image suggests the touching line $y = 0$.
For $h > 0$ the quotient is $|h|/h = 1$, and for $h < 0$ it is $|h|/h = -1$.
The one-sided limits are $1$ and $-1$, so the limit does not exist and $f$ has no derivative at $0$.

The image gives a line, and the definition gives no derivative.
The resolution is that $y = 0$ meets the graph only at $0$, but meeting once does not make a line a tangent; tangency needs the limit.
The theory is used to plan tasks like this one, where an example evokes the conflicting part of the image together with the definition.

### L3 human

The pair belongs to the cognitive research on advanced mathematical thinking, in which Tall was a central figure.
It connects with [[mathematical language in education|S19WMS43TW]], since a concept definition is a piece of mathematical language with special meanings.
It explains part of the research on [[student difficulties with proof|5K2969GSWE]]: a proof must use the definition, and a student who reasons from the image writes arguments that the definition does not support.
[[Choosing good definitions|S1R1VD31BS]] shows the other side, where mathematicians choose definitions that agree as far as possible with the shared images of a concept.
