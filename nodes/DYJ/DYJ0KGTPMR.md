---
tag: DYJ0KGTPMR
kind: topic
name: Mathematical logic
msc: ["03Bxx", "03Fxx", "03Gxx"]
---

## Summary

Mathematical logic is the study of formal languages, formal proofs and the meaning of formulas with the methods of mathematics.
A formal system has a language, axioms and rules of inference, and a proof in the system is a finite sequence of formulas that obeys these rules.
Logic gives precise meanings to the words statement, proof and truth, so it supports the foundations of mathematics, and it has many uses in computer science.
Boole and Frege started the modern subject in the 19th century, and the results of Gödel, Tarski, Gentzen and Church in the 1930s gave it its present form.
This topic collects the mathematical logic pages of math2.
Its sub-areas are listed below, in reading order.
Reasoning and proof, model theory, set theory, computability theory, and type theory and constructive mathematics have their own topics.

## Remarks

### What the area is about

Mathematical logic studies the reasoning of mathematics with the methods of mathematics.
Its objects are [[formal languages|5MFZ4VNY6D]], the [[formal systems|~113060c3]] that derive formulas of these languages, and the [[structures|983GZBQYT4]] in which the formulas are true or false.
The area asks what can be expressed in a language, what can be proved in a system, and how proof and truth are related.

Logic has two roles in mathematics.
As a branch of mathematics it has its own definitions, theorems and open problems, like algebra or topology.
As a [[foundation|EFFRJFW67Y]] it gives the exact meaning of "statement", "proof" and "theorem", and so it tells which arguments the other branches may use.

Logic is traditionally divided into four branches.

- [[Proof theory|N4EDJNMTEF]] studies proofs as finite objects: their structure, their transformations and the strength of theories.
- [[Model theory|HFTBG5PMXC]] studies the relation between theories and the structures that satisfy them.
- [[Set theory|RTHHCX84HN]] studies sets, the objects from which most of mathematics is built, and the axioms that describe them.
- [[Computability theory|X14Y880PN5]] studies which functions and sets an algorithm can compute, and how hard the others are.

The four branches are linked.
Gödel's [[completeness theorem|WQ1ZE255SF]] joins proof theory and model theory: a sentence of [[first-order logic|086QKPF0A6]] is provable exactly when it is true in every model.
The [[incompleteness theorems|X9WYNYE29C]] join proof theory and computability: a consistent theory with a computable set of axioms that contains enough arithmetic leaves some sentence undecided.
Set theory builds new models of its axioms with model-theoretic methods, and computability theory shows that some logics are undecidable.
In math2 this area holds proof theory and the logics themselves, and model theory, set theory and computability theory have their own areas.

The main theorems of the area are the following.

- The completeness theorem (Gödel, 1929): first-order provability equals truth in all models.
- The [[compactness theorem|1NR3HAWG9D]]: a set of first-order sentences has a model if each finite subset has a model.
- The incompleteness theorems (Gödel, 1931): a consistent, effectively axiomatized theory that contains enough arithmetic does not decide every sentence, and it does not prove its own consistency.
- [[Tarski's undefinability theorem|YRV6SYK2BY]]: arithmetical truth is not definable in arithmetic.
- [[Church's theorem|VA6BNNY2YC]] (Church and Turing, 1936): validity in first-order logic is undecidable.
- The [[cut-elimination theorem|AYRZ98Y0NW]] (Gentzen): each proof in the sequent calculus can be transformed into a proof without the cut rule.

Logic has many uses in computer science.
Programs are checked by [[model checking|VNY0VXVZ53]] in [[modal|C3RZY20ETK]] and temporal logics.
The [[Boolean satisfiability problem|3QKF32ZAKN]] was the first problem shown to be NP-complete, and SAT solvers decide large instances of it in practice.
The [[Curry-Howard correspondence|A77FER1Q5H]] identifies proofs with programs, and it is the base of type theory and of [[proof assistants|YM6PRDE88V]].
[[Descriptive complexity theory|YRHZEF2JMZ]] describes complexity classes by the logics that define them.

### History

Aristotle gave the first formal logic, the syllogistic, in the 4th century BC, and the Stoics studied the logic of connectives.
George Boole treated logic as algebra in 1847 and 1854.
Gottlob Frege gave the first formal language with quantifiers in his *Begriffsschrift* of 1879.
Whitehead and Russell derived a large part of mathematics in a formal system in *Principia Mathematica* (1910 to 1913).
In the 1920s David Hilbert proposed his [[program|P1RW6JWX73]]: formalize mathematics and prove its consistency by finitary means.

The 1930s gave the subject its present form.
Gödel proved the completeness theorem in 1929 and the incompleteness theorems in 1931.
Alfred Tarski defined truth in a formal language in 1933.
Gerhard Gentzen introduced natural deduction and the sequent calculus in 1934 and 1935, and he proved the consistency of arithmetic in 1936.
Alonzo Church and Alan Turing showed in 1936 that first-order validity is undecidable.

After 1950 the four branches grew into separate fields.
Saul Kripke and others gave a semantics for modal and intuitionistic logic in the late 1950s and the 1960s.
Paul Cohen invented forcing in 1963 and proved that the [[continuum hypothesis|0MN2MER9WN]] does not follow from the axioms of ZFC.
The [[history of mathematical logic|~060dac5f]] gives a longer account.

### How to read the area

A reader who is new to logic starts with [[logic, formal systems and foundations|H8QZY0RZXZ]], which gives the general notions, and with [[propositions, connectives and quantifiers|PM1AYWABA7]].
Then the core course follows, in this order.
[[The propositional calculus|JDK63589SA]] treats the logic of connectives completely.
[[First-order languages and syntax|PSRDJXRW53]], [[structures, satisfaction and truth|NJDME6F845]] and [[proof systems for first-order logic|TTCRX3NFNY]] give the syntax, the semantics and the proofs of first-order logic.
[[Completeness, compactness and interpolation|FBWW4J1XWG]] joins the semantics and the proofs.

After the core course the reader can choose among four lines.

- Limits of formal systems: [[decidability|E4AVTNWE9E]], [[formal arithmetic|QHCRN4JVG0]], [[the incompleteness theorems|HXHHWY3328]] and [[natural independence results|T6FK1E7GJ1]].
- Proof theory: [[structural proof theory|R10RMQCJQX]], [[ordinal analysis|XTTKZTYDSD]], [[proof interpretations|8XY7JYZKFW]], [[provability logic|3E7M66WW6Q]], [[reverse mathematics|BY8AAFN7C5]], [[bounded arithmetic|RA380RWEC0]] and [[proof complexity|CBAF7J051K]]. This line needs the incompleteness theorems.
- Non-classical logics: [[modal logic|SKY7AQFG1V]], then [[correspondence and bisimulation|SPQVNPZDTB]] and [[applied modal logics|CQM9SRN8PM]], and also [[intuitionistic|38EQ20GR7M]], [[many-valued|WZP584JQ06]], [[substructural|98QF5J4W16]] and [[other non-classical logics|NJB94B39QK]].
- Algebra and truth: [[algebraic logic|QYA4H5Y7VR]] and [[truth and the semantic paradoxes|6Q4JJ2MMV8]].

[[Second-order logic and extensions of first-order logic|MDHDYV8QZW]] can be read at any time after the core course.

### Related areas

[[Reasoning and proof|SGSVYFDSYK]] treats logic as a tool of practice: how to read statements and how to write proofs.
[[Model theory|F3AXVABC35]], [[set theory|G9W9J6KPAR]] and [[computability theory|ZNC3817RA6]] are the other three classical branches of logic.
[[Type theory and constructive mathematics|K6P3NSQEZ3]] holds the lambda calculus, the Curry-Howard correspondence and constructive mathematics, and [[category theory|Y97P9CSMEN]] holds categorical logic and toposes.
[[Order, lattices and universal algebra|V1VVQR12AQ]] holds Boolean and Heyting algebras as algebras.
[[Theory of computation|52TNMMSXD3]] holds SAT as a problem and the logics of programs, and [[mathematical software and formalization|F3F5GGYHMM]] holds proof assistants and automated theorem proving.
[[Philosophy of mathematics|NTJ5XW0PVD]] holds logicism, formalism and intuitionism as views of mathematics, and [[history of mathematics|EJZNJJ6M7S]] holds the history of logic beyond the survey essay.

### Sub-areas

1. [[Logic, formal systems and foundations|H8QZY0RZXZ]]
1. [[Propositions, connectives and quantifiers|PM1AYWABA7]]
1. [[The propositional calculus|JDK63589SA]]
1. [[First-order languages and syntax|PSRDJXRW53]]
1. [[Structures, satisfaction and truth|NJDME6F845]]
1. [[Proof systems for first-order logic|TTCRX3NFNY]]
1. [[Completeness, compactness and interpolation|FBWW4J1XWG]]
1. [[Second-order logic and extensions of first-order logic|MDHDYV8QZW]]
1. [[Decidability of logics and theories|E4AVTNWE9E]]
1. [[Formal arithmetic and its fragments|QHCRN4JVG0]]
1. [[Gödel's incompleteness theorems and related limits|HXHHWY3328]]
1. [[Natural independence results and fast-growing functions|T6FK1E7GJ1]]
1. [[Structural proof theory|R10RMQCJQX]]
1. [[Ordinal analysis and ordinal notations|XTTKZTYDSD]]
1. [[Proof interpretations and conservation results|8XY7JYZKFW]]
1. [[Provability and interpretability logics|3E7M66WW6Q]]
1. [[Reverse mathematics and subsystems of second-order arithmetic|BY8AAFN7C5]]
1. [[Bounded arithmetic|RA380RWEC0]]
1. [[Propositional proof complexity|CBAF7J051K]]
1. [[Syntax, Kripke semantics and completeness of modal logic|SKY7AQFG1V]]
1. [[Modal correspondence, bisimulation and extended modal logics|SPQVNPZDTB]]
1. [[Applied modal logics|CQM9SRN8PM]]
1. [[Intuitionistic and intermediate logics|38EQ20GR7M]]
1. [[Many-valued and fuzzy logics|WZP584JQ06]]
1. [[Substructural, linear and relevance logics|98QF5J4W16]]
1. [[Paraconsistent, free, non-monotonic and other non-classical logics|NJB94B39QK]]
1. [[Algebraic logic|QYA4H5Y7VR]]
1. [[Truth and the semantic paradoxes|6Q4JJ2MMV8]]
