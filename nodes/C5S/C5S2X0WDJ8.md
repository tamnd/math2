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

A person's concept image of a mathematical concept is the whole mental structure that the person links with it: pictures, examples, properties and processes.
The concept definition is a form of words that specifies the concept.
David Tall and Shlomo Vinner introduced the pair in 1981, with examples from limits and continuity.
A student can know the formal [[definition|8ZCZ3HW91Z]] and still reason from a concept image that conflicts with it.
The distinction matters because many errors in proofs come from such conflicts, and because the evoked image, not the definition, often drives a student's reasoning.

## Motivation

A student recites the definition of a [[function|0EPAT51DXQ]] as a rule that assigns to each input exactly one output.
In the next task, the same student says that a function defined by two formulas on two intervals "is two functions".
The student's answer does not come from the definition that the student just recited.
It comes from a picture built from years of examples, in which each function had one formula.
Tall and Vinner gave names to the picture and to the definition, so that research and teaching can talk about the gap between them.

## Notation

Tall and Vinner (1981) used the following terms.

- Concept image: the total cognitive structure associated with a concept, built over years and changing over time.
- Evoked concept image: the part of the concept image that is active at a given time.
- Concept definition: a form of words that specifies the concept. A personal concept definition is the student's own wording; the formal concept definition is the one accepted by mathematicians.
- Potential conflict factor: a part of the concept image that conflicts with another part or with the formal definition.
- Cognitive conflict factor: a potential conflict factor that is evoked at the same time as the part it conflicts with, so that the student notices the conflict.

## Remarks

### Examples

1. [[The tangent line as a line that touches once|2PVD1J6J0G]]: the image comes from circles and fails for the curve $y = x^3$.
2. [[The function as a formula|E2MPB6KK9V]]: the image comes from school examples and rejects functions defined by cases.
3. Limit of a sequence: a student pictures a limit as a value that the terms approach but never reach. The image fails for the constant sequence $a_n = 1$, whose [[limit|05M5SWSZZD]] is $1$ and whose terms all equal $1$.
4. Continuity: a student pictures a [[continuous function|0X3WGX95FE]] as one whose graph can be drawn without lifting the pen. The image says that $f(x) = 1/x$ is not continuous, because its graph has two branches. By the definition, $f$ is continuous at each point of its domain $x \neq 0$.

### Non-examples

1. [[A textbook definition is a concept definition, not a concept image|PXQQW9TFM1]]. The words on the page specify the concept, but they are not the mental structure of any person.
2. A wrong calculation, such as $(a + b)^2 = a^2 + b^2$, is not a concept image. It may come from an image of "squaring distributes", but the error itself is a rule, not the whole structure linked with a concept.

### Basic properties

1. A concept image can be correct for all examples a student has met and still conflict with the definition. The conflict shows only on new examples.
2. A concept image is not wrong in itself. Mathematicians also have rich concept images, which guide their intuition.
3. The formal definition does not replace the image. Teaching aims at an image that agrees with the definition, and at the habit of checking the image against the definition.
4. Different parts of a concept image can conflict with each other. The conflict is harmless until both parts are evoked at once.

### History

Tall and Vinner published their paper in 1981, in the journal Educational Studies in Mathematics.
Vinner (1983) applied the ideas to the concept of function, and found that many students judged examples by images of formulas and graphs, not by the set definition.
Later research used the pair for derivatives, limits, groups and many other concepts.
Barbara Edwards and Michael Ward (2004) studied how university students use mathematical definitions, and found that many did not use the definitions as mathematicians do.

### Common errors

1. A teacher thinks that a student who can recite a definition understands it. The student may still reason from an image that conflicts with it.
2. A teacher gives only typical examples. The students' images then contain features of the typical examples that the definition does not require.
3. A researcher calls each error a concept image. The term means the whole structure linked with a concept, and an error is at most a sign of one part of it.

## Explanations

### L1 human

When you think of a "triangle", you probably picture one with a flat bottom and a point on top.
That picture is part of your concept image: all the pictures and examples that come to mind.
The concept definition is the words: "a polygon with three sides".
Usually the picture and the words agree.
But if you only picture triangles with a flat bottom, you may not see a triangle turned upside down as a triangle.
Many mistakes in mathematics happen when the picture and the words do not agree.

### L2 human

We find a conflict between image and definition for the [[derivative|0V1EJCT8G6]].
A student's image: "the derivative at a point is the slope of the line that touches the graph there".
The formal definition: $f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$, if the limit exists.

1. Test $f(x) = |x|$ at $a = 0$. The image suggests that the graph has a "touching line" at $0$, perhaps $y = 0$.
2. Compute: for $h > 0$, $\frac{|h| - 0}{h} = 1$, and for $h < 0$, $\frac{|h| - 0}{h} = -1$.
3. The one-sided limits are $1$ and $-1$, so the limit does not exist, and $f$ has no derivative at $0$.
4. The image and the definition conflict: the image gives a line, the definition gives no derivative.
5. Resolution: a line such as $y = 0$ meets the graph only at $0$, but this does not make it a tangent line. Tangency needs the limit.

The typical use of the theory is to plan such tasks: an example that evokes the conflicting part of the image together with the definition.
A trap is to give the counterexample without discussion.
The student may treat it as a strange exception and keep the image unchanged.

### L3 human

The pair belongs to the cognitive research on advanced mathematical thinking, in which Tall was a central figure.
It connects with [[mathematical language in education|S19WMS43TW]], since a concept definition is a piece of mathematical language with special meanings.
It explains part of the research on [[student difficulties with proof|5K2969GSWE]]: a proof must use the definition, and a student who reasons from the image writes arguments that the definition does not support.
The page on [[choosing good definitions|S1R1VD31BS]] shows the other side: mathematicians choose definitions that agree as far as possible with the shared images of the concept.
