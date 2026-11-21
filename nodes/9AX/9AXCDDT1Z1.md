---
tag: 9AXCDDT1Z1
kind: concept
name: Teaching linear algebra
msc: ["97H60", "15-01"]
topics: [VKVAJ94SKZ]
audience: ug1
uses: [Y7PBW8VD4Q]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_algebra
    locator: lead section
  - book: isbn:9780321982384
    locator: Preface
  - book: isbn:9783031410253
    locator: Preface
  - book: isbn:9781733146678
    locator: Chapter 1
  - url: https://hefferon.net/linearalgebra/
  - url: https://understandinglinearalgebra.org/
---

## Summary

Teaching linear algebra is hard because the course asks students to compute and to think abstractly at the same time.
The part of mathematics education that studies how students learn the subject of the [[overview|Y7PBW8VD4Q]], and how courses present it, has the MSC class 97H60.
Its main questions are the order of the ideas, the place of proofs and the place of software.
A matrix-first course starts with linear systems and matrices in $\mathbb{R}^n$, and an abstract-first course starts with vector spaces and linear maps.
The choice matters, because for many students linear algebra is the first course with abstract structure, and it serves engineering, science, economics and computing as well as mathematics.

## Motivation

A first course in linear algebra has students from mathematics, physics, engineering, economics and computer science in the same room.
They need different things: some need algorithms and matrix skills, some need geometric intuition, and some need a first contact with axioms and proofs.
Research in mathematics education found that many students can row reduce a matrix but cannot say what a span or a basis is.
So the central problem of course design is to connect the computations with the concepts behind them.

## Notation

The abbreviation LACSG stands for the Linear Algebra Curriculum Study Group.
A CAS, a computer algebra system, computes with exact numbers and symbols, while numerical software works with floating-point numbers.
The difference matters in class: a CAS gives the exact rank of a matrix, and numerical software gives a rank that depends on a tolerance.

## Remarks

### Five ways to start a course

Textbooks show the range of choices.
Lay starts with linear systems, row reduction and the equation $A x = b$, and reaches abstract vector spaces only in chapter 4.
Strang also starts in $\mathbb{R}^n$, but with vectors, dot products and the column picture of $A x = b$, and he organizes the course around the four fundamental subspaces of a matrix.
Axler starts with vector spaces over $\mathbb{R}$ and $\mathbb{C}$ and puts determinants near the end, the approach of [[linear algebra without determinants|4C6EBHFF3R]].
Hefferon, a free text, starts with linear systems and proves the results from the first page, and Austin, also free, builds each section around activities with cells of live computation.

### What a first course is not

A course in numerical linear algebra is not a first course.
It assumes the theory and studies the rounding errors and the cost of algorithms.
A course of matrix computations only, with no subspaces and no linear maps, is also not what the curriculum studies have in mind, because it leaves out the concepts that later courses need.

### The recommendations of the study group

The LACSG met in 1990 and published its recommendations in the *College Mathematics Journal* in 1993.
Its authors were Carlson, Johnson, Lay and Porter.
They asked that the first course be matrix-oriented and that it serve the client disciplines, such as engineering and economics.
They also asked faculty to consider the needs and interests of the students, to use technology, and to offer a second course in matrix theory.
Many American courses moved toward a matrix-oriented first course after these recommendations.

### Proofs and software

In many curricula the first course in linear algebra is also the first contact with definitions and proofs.
Some departments add a separate transition course on proofs, so that linear algebra does not carry the whole load.
Software takes over the long computations.
MATLAB and Octave, Python with NumPy, and Sage are the common choices; Moler wrote the first MATLAB in the 1970s so that his students could use the linear algebra libraries of the time without writing Fortran.

### History

Linear algebra became a standard first-year or second-year course in the second half of the 20th century, often after calculus.
In the 1990s research groups, among them those of Dorier in France and Sierpinska in Canada, studied the difficulties that students have with the formal concepts.
Their work and the LACSG recommendations shaped many textbooks of the following decades.

### Watch out

A course can teach the algorithms without the meaning.
Then a student computes a row echelon form but cannot say what it tells about the [[column space|03AJKXH1AV]], for example that the pivot columns of the original matrix give a basis of it.
A course can also start with axioms and no examples, and then students learn the words without the objects.
The essay on [[common errors|79YPKR857M]] lists the student errors that follow from both habits.

### Try it

Name one advantage of a matrix-first course for an engineering student.
The student meets $A x = b$ in the first week and can use it at once in a circuit or a structure problem.

Name one risk of a purely numerical computation of the rank.
A computed pivot such as $10^{-15}$ may stand for an exact $0$, so the computed rank can be too large.

## Explanations

### L1 human

Linear algebra can be taught in two main orders.
One order starts with sets of equations and tables of numbers, and later reaches the general ideas.
The other order starts with the general ideas, and uses the tables as examples.
Most first courses for engineers and scientists use the first order, because those students need the tables early.

### L2 human

A typical matrix-first syllabus runs as follows.
It starts with linear systems, row reduction and the description of solution sets.
Then come matrix operations, inverses and the invertible matrix theorem, and after them determinants.
The middle of the course treats vector spaces, subspaces, bases, dimension and rank.
It ends with eigenvalues and diagonalization, and with orthogonality, projections and least squares.

Software enters where hand computation stops: the row reduction of large matrices, and the eigenvalues of matrices whose characteristic polynomial has no roots that you can find by hand.
Watch out: a computer gives decimal answers, so a computed rank or a computed zero can be wrong by rounding.

### L3 human

Sierpinska described three modes of thinking in linear algebra: synthetic-geometric, analytic-arithmetic and analytic-structural.
A student who moves between the picture of a plane, its equation and the idea of a two-dimensional subspace uses all three.
Dorier described the "obstacle of formalism", in which students use the formal language without its meaning.
Course designs that respond to this start from a problem, such as a linear system or a geometric transformation, and introduce the general notion as the tool that solves it.
The school side of the subject, vectors in the plane and in space, belongs to the area on [[school curricula|9AHB6RQVDE]].
