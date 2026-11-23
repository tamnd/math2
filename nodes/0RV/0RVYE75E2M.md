---
tag: 0RVYE75E2M
kind: definition
name: Converse and inverse of an implication
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
defines: 09A3N7ZN5G
uses: [0ZNX6DQ3EJ, 0XR7A7RSXB]
sources:
  - url: https://en.wikipedia.org/wiki/Converse_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Inverse_(logic)
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Definition

"If an animal is a dog, then it is a mammal" has the converse "if an animal is a mammal, then it is a dog" and the inverse "if an animal is not a dog, then it is not a mammal".

Let $\varphi$ and $\psi$ be formulas of propositional logic, and consider the [[implication|0ZNX6DQ3EJ]] $\varphi \to \psi$.
The converse of $\varphi \to \psi$ is the implication $\psi \to \varphi$.
The inverse of $\varphi \to \psi$ is the implication $\neg \varphi \to \neg \psi$, where $\neg$ is [[negation|0XR7A7RSXB]].

For a universal statement $\forall x\, (P(x) \to Q(x))$, the converse is $\forall x\, (Q(x) \to P(x))$ and the inverse is $\forall x\, (\neg P(x) \to \neg Q(x))$.

## Notation

There is no special symbol for the converse or the inverse.
The converse $\psi \to \varphi$ is sometimes written $\varphi \leftarrow \psi$.
Negation is also written $\sim \varphi$, $\varphi'$ or $\overline{\varphi}$, and the arrow is also written $\supset$ or $\Rightarrow$.

## Remarks

### A syntactic definition

The definition takes a given implication and produces a new formula, whatever the truth values are.
The converse and the inverse of a true implication can be false.
"If $n = 2$, then $n$ is prime" is true, but its converse "if $n$ is prime, then $n = 2$" is false for $n = 3$.
Its inverse "if $n \neq 2$, then $n$ is not prime" is false for $n = 3$ as well.
The inverse is the [[contrapositive|04T1CT7212]] of the converse, so classically the two are logically equivalent.
The concept [[converse and inverse of an implication|09A3N7ZN5G]] gives the truth tables, the intuitionistic difference and the common errors.

### Watch out

Negate each part correctly: the negation of $x > 3$ is $x \le 3$, not $x < 3$.

### Try it

Form the converse and the inverse of "if $x > 3$, then $x^2 > 9$" for a real number $x$, and test them at $x = -4$.
The converse is "if $x^2 > 9$, then $x > 3$", and the inverse is "if $x \le 3$, then $x^2 \le 9$".
At $x = -4$ we have $x^2 = 16 > 9$ and $x \le 3$, so this one value refutes both.

## Explanations

### L1 human

The converse reads the arrow backwards.
"If an animal is a dog, then it is a mammal" is true.
Its converse, "if an animal is a mammal, then it is a dog", is false, because a cat is a mammal.
The inverse puts "not" in front of both parts: "if an animal is not a dog, then it is not a mammal".
The cat shows that the inverse is false too.

### L2 human

We form the converse and the inverse of "if $x > 3$, then $x^2 > 9$", for a real number $x$.
The antecedent is $x > 3$, and the consequent is $x^2 > 9$.
The converse exchanges them: "if $x^2 > 9$, then $x > 3$".
The inverse negates both and keeps the order: "if $x \le 3$, then $x^2 \le 9$".
The value $x = -4$ gives $x^2 = 16 > 9$ and $x \le 3$, so it refutes the converse and the inverse at the same time.
A common slip is to negate only one part.
