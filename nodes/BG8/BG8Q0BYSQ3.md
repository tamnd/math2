---
tag: BG8Q0BYSQ3
kind: statement
role: theorem
name: Fagin's theorem
msc: [03C13, 68Q19, 68Q15]
uses: [983GZBQYT4, G6X7SZSNC5, DKFGQTRYZE, 758EYCN27B]
about: [4XRVJE0KAN]
sources:
  - url: https://en.wikipedia.org/wiki/Fagin's_theorem
same_as:
  wikidata: Q2226670
  wikipedia: Fagin's theorem
---

## Statement

Let $\sigma$ be a finite relational signature.
Let $\mathcal K$ be a class of finite $\sigma$-[[structures|983GZBQYT4]] that is closed under isomorphism.
Then the following are equivalent.

1. The class $\mathcal K$ is in NP: some nondeterministic [[Turing machine|758EYCN27B]] decides, in time polynomial in the size of a finite $\sigma$-structure $A$, whether $A \in \mathcal K$.
2. There is an existential [[second-order|G6X7SZSNC5]] [[sentence|DKFGQTRYZE]] $\exists R_1 \cdots \exists R_k \, \varphi$ such that a finite $\sigma$-structure belongs to $\mathcal K$ if and only if it satisfies this sentence.

Here $R_1, \ldots, R_k$ are relation variables, and $\varphi$ is a first-order sentence in the signature $\sigma \cup \set{R_1, \ldots, R_k}$.

## Remarks

From 2 to 1: a machine guesses the relations $R_1, \ldots, R_k$ on the finite universe, which takes polynomially many bits.
It then checks the first-order sentence $\varphi$, which takes polynomial time for a fixed $\varphi$.
From 1 to 2: the sentence guesses a linear order of the universe and relations that encode an accepting computation of the machine.
The computation of length $n^c$ is coded with tuples of length $c$, and $\varphi$ checks that each step follows the transition rules.

Example: the class of finite graphs that admit a proper colouring with three colours is in NP.
It is defined by the sentence $\exists R \, \exists G \, \exists B \, \varphi$.
Here $\varphi$ says that each vertex lies in $R$, $G$ or $B$, and that no edge joins two vertices in the same set.

## Explanations

### L1 human

The theorem matches a kind of computing problem with a kind of logical description.
A problem is in NP when a proposed solution can be checked quickly.
Fagin's theorem says these are exactly the properties of finite structures of the form "there exist some relations such that a first-order condition holds".
The relations play the role of the solution that is guessed.

### L2 human

Fagin's theorem started descriptive complexity, which characterises complexity classes by logics without any reference to machines.
It shows that NP is closed under complement if and only if existential second-order logic has the same power as universal second-order logic on finite structures.
Other results of this kind characterise P on ordered finite structures by first-order logic with a least fixed point operator.
The theorem belongs to [[finite model theory|4XRVJE0KAN]], where classical tools such as compactness are not available.
