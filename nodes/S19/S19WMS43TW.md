---
tag: S19WMS43TW
kind: concept
name: Mathematical language in education
aliases: [language-of-mathematics-in-education, mathematics-register-in-education]
msc: ["97E40", "97C50"]
topics: [VHGA6J4NZK]
audience: research
uses: [661V0DH7V3, 8ZCZ3HW91Z, QKEX4PD029, 8BZPKYF912]
sources:
  - url: https://en.wikipedia.org/wiki/Language_of_mathematics
    locator: In education
  - url: https://doi.org/10.1080/00029890.2004.11920092
    locator: pages 411-424
  - url: https://doi.org/10.1207/S15327833MTL04023_5
    locator: pages 189-212
  - url: https://doi.org/10.1080/0020739830140305
    locator: pages 293-305
---

## Summary

A class of eight-year-olds is asked to fill the box in $8 + 4 = \square + 5$.
Many children write $12$, and some write $17$, while the answer is $7$.
They have read the sign $=$ as "now write the answer", not as "both sides have the same value".
Karen Falkner, Linda Levi and Thomas Carpenter reported this pattern among elementary school children in 1999, and it shows that even the most common symbol of mathematics must be learned as language.

Mathematical language in education studies how learners acquire the [[language of mathematics|661V0DH7V3]]: its symbols, its definitions, the special meanings it gives to everyday words, and its forms of argument.
Linguists call the words, meanings and forms of a field its register, so this is the study of how students learn the mathematics register.
It also studies learners who learn mathematics in a second language.

## Motivation

A student who misreads a word or a symbol cannot follow a proof, even when the mathematics behind it is within reach.
Many words of mathematics also have an everyday meaning, and the two meanings differ.
In everyday speech "similar" means "alike", but similar triangles have equal angles and proportional sides.
In everyday speech "or" often excludes both, but "$P$ or $Q$" in mathematics is true when both are true.

A [[mathematical definition|8ZCZ3HW91Z]] also works differently from a dictionary entry.
It fixes the meaning, and only the stated conditions count, so a student who reasons from a typical picture instead of the definition will make errors.
Symbols add a third layer, because one symbol can have several meanings, as [[mathematical notation|QKEX4PD029]] describes.
A learner must master all three layers, often without explicit teaching.

## Notation

Research writes "the mathematics register" after Michael Halliday, and "everyday register" for ordinary speech.
Words such as "odd", "prime", "mean", "product", "similar", "volume" and "range" are often called words with a double meaning.
Studies of second-language learners use "bilingual" or "multilingual learners" for students who learn mathematics in a language that is not their first.

## Remarks

### Words that change meaning

Small words cause the largest trouble, because they carry quantifiers.
In "if $x$ is any real number, then $x^2 \ge 0$", the word "any" means "each", so the statement is universal.
In "if any root is negative, the method fails", "any" means "some", so the statement is existential.
[[Ambiguity in mathematical language|8BZPKYF912]] collects more cases of this kind.
Larger words cause trouble in a different way: the student already owns a meaning, and the mathematical meaning has to displace it.

### How students use definitions

Barbara Edwards and Michael Ward (2004) reported on undergraduate mathematics majors from their own studies, which used interviews and written tasks.
Students who could state a definition often did not reason from it.
They reasoned from familiar examples or from their own sense of the concept, and they did not see why a mathematician would insist on the exact wording.
Shlomo Vinner (1983) found the same with functions: many students judged whether a correspondence is a function by their mental picture, not by the definition.
[[Concept image and concept definition|C5S2X0WDJ8]] treats that line of research.

### Learning in a second language

A student who learns mathematics in a second language may solve a problem correctly in symbols and still fail to write the argument in words.
Judit Moschkovich (2002) argued for a sociocultural view of bilingual learners.
In that view, both languages, gestures and objects are resources for mathematical talk, and the teacher's attention moves from missing vocabulary to taking part in mathematical practices such as explaining and arguing.
Her paper is a theoretical argument with classroom examples, not a comparison of teaching methods.

### What belongs elsewhere

The design of notation, such as the choice between $\frac{dy}{dx}$ and $f'$, belongs to [[notation, conventions and jargon|Z2WNQ1DNTX]], since it concerns the language and not how it is learned.
A language course that uses mathematics as its content is language education, because its aim is the language.

### History

The linguist Michael Halliday introduced the idea of a mathematics register in the 1970s.
David Pimm's book *Speaking Mathematically* (1987) brought the idea into mathematics education research and studied spoken language in the classroom.
Research on how students use definitions joined the research on concept images, which began with David Tall and Shlomo Vinner in 1981.

### Watch out

A teacher may assume that a correct definition on the board gives the students the concept.
Students often keep their own meaning of the word, and only a task where the two meanings disagree will reveal it.
A teacher may also read a second-language learner's weak writing as weak mathematics, when the learner reasons well and lacks only the words.
A student may hear "a", "any" or "some" in the everyday sense and so misread the quantifier of a statement.

### Try it

First, what does a child who answers $17$ to $8 + 4 = \square + 5$ do?
The child adds every number in sight, $8 + 4 + 5 = 17$, treating $=$ as a signal to compute.

Second, is the constant function $f(x) = 3$ increasing if the definition says that $x < y$ implies $f(x) \le f(y)$?
Yes, since $3 \le 3$ for all inputs, although the everyday word suggests growth.

## Explanations

### L1 human

Mathematics has its own language.
Some words look like everyday words but mean something else.
In everyday speech an "odd" idea is strange, while in mathematics an odd number leaves remainder $1$ when divided by $2$, such as $7$.
Symbols need learning too: $3 \times 4$, $3 \cdot 4$ and $(3)(4)$ all mean $12$.
Students learn this language slowly, and teachers help when they point out each new meaning.
Students who learn mathematics in a second language must learn two new languages at once.

### L2 human

Follow how a student reads one definition: a real function $f$ is increasing on an interval $I$ when, for all $x, y$ in $I$, if $x < y$, then $f(x) \le f(y)$.
The student first pictures a rising graph, because "increasing" means "growing".
The definition says $\le$, not $<$, so a constant function is increasing, which surprises the everyday reading.
Some books call this property "non-decreasing" and keep "increasing" for $<$, a [[conflicting convention|CSFEP56A7D]] between books.

Now the student must prove that $f(x) = x^3$ is increasing on $\mathbb{R}$.
A student who checks $f(1) < f(2)$ and $f(2) < f(3)$ has used the everyday meaning.
The definition demands arbitrary $x < y$, and then the factorization does the work:
$$y^3 - x^3 = (y - x)(x^2 + xy + y^2), \qquad x^2 + xy + y^2 = \left(x + \tfrac{y}{2}\right)^2 + \tfrac{3}{4} y^2 \ge 0.$$
Since $y - x > 0$, the product is at least $0$, so $x^3 \le y^3$.

The typical use of such an analysis is to plan the first lesson with a new definition: name the everyday meaning, then show where the mathematical meaning differs.
Watch out: the student who checked three values got correct numbers and still never used the definition.

### L3 human

Research on mathematical language joins linguistics, the psychology of concepts and the study of classrooms.
Systemic functional linguistics, in the tradition of Halliday, studies how mathematical texts build meaning with dense noun phrases, symbols and diagrams.
The research on definitions links to the [[concept image and concept definition|C5S2X0WDJ8]] of Tall and Vinner and to [[unpacking definitions|41JZ39GE3F]].
Work on bilingual learners links to the [[social, cultural and linguistic dimensions|3H96N14VQK]] of mathematics education.
