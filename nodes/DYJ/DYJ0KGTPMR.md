---
tag: DYJ0KGTPMR
kind: topic
name: Mathematical logic
msc: ["03Bxx", "03Fxx", "03Gxx"]
---

## Summary

Write a proof as a list of lines, where each line is an axiom or follows from earlier lines by a fixed rule.
Then a computer can check the proof line by line, without knowing what any line means.
In 1931 Kurt Gödel showed that this precision has a price.
In any consistent system of this kind that contains enough arithmetic, some statement about whole numbers can be neither proved nor refuted.
Mathematical logic is the part of mathematics that makes results like this possible.
It gives exact definitions of statement, proof and truth, treats them as mathematical objects, and proves theorems about them.
Three questions run through the whole subject: what a language can express, what a system can prove, and how proof and truth are related.
The answers shape the foundations of mathematics, and they reach into computer science through algorithms, programs and proof assistants.
The reading order below starts with statements and first-order logic.
From there it branches into the limits of formal systems, proof theory, modal and other non-classical logics, and the algebra of logic and the theory of truth.

## Remarks

### Reading order

The first seven items form the core course, and every later item uses it.
After the core the groups below can be read in any order, with two exceptions.
Proof theory, items 13 to 19, needs the incompleteness theorems of item 11, and items 21 and 22 build on item 20.

1. [[Logic, formal systems and foundations|H8QZY0RZXZ]]: learn what a formal system is, and why consistency and soundness are theorems about a system rather than theorems inside it.
2. [[Propositions, connectives and quantifiers|PM1AYWABA7]]: read, combine and negate statements built from "and", "or", "if", "for all" and "there exists", the everyday tools of every proof.
3. [[The propositional calculus|JDK63589SA]]: see one whole logic at once, with truth tables, normal forms, and proof systems that prove exactly the tautologies.
4. [[First-order languages and syntax|PSRDJXRW53]]: build terms and formulas with variables and quantifiers, and handle free variables and substitution with care.
5. [[Structures, satisfaction and truth|NJDME6F845]]: give formulas a meaning in a structure, and define what it means for a sentence to be true there.
6. [[Proof systems for first-order logic|TTCRX3NFNY]]: compare Hilbert systems, natural deduction, the sequent calculus and tableaux as ways to write formal proofs.
7. [[Completeness, compactness and interpolation|FBWW4J1XWG]]: prove that formal proofs reach exactly the valid sentences, and draw compactness and other consequences from that fact.

### Reading order, continued: beyond first-order logic and its limits

Item 8 stands apart from the others in this group, and it can be read at any time after the core.

8. [[Second-order logic and extensions of first-order logic|MDHDYV8QZW]]: see what stronger logics gain in expressive power, and which theorems of the core they lose in exchange.
9. [[Decidability of logics and theories|E4AVTNWE9E]]: find out which theories an algorithm can decide, such as Presburger arithmetic, and why first-order validity is not one of them.
10. [[Formal arithmetic and its fragments|QHCRN4JVG0]]: meet Peano arithmetic and its weaker relatives, the theories in which the limits of proof are usually measured.
11. [[Gödel's incompleteness theorems and related limits|HXHHWY3328]]: understand why a consistent theory with computable axioms and enough arithmetic leaves sentences undecided and cannot prove its own consistency.
12. [[Natural independence results and fast-growing functions|T6FK1E7GJ1]]: see ordinary combinatorial statements, such as Goodstein's theorem, that are true but cannot be proved in Peano arithmetic.

### Reading order, continued: proof theory

13. [[Structural proof theory|R10RMQCJQX]]: transform proofs, remove the cut rule, and read off facts about a theory from the shape of its proofs.
14. [[Ordinal analysis and ordinal notations|XTTKZTYDSD]]: measure the strength of a theory by an ordinal, as Gentzen did for Peano arithmetic with the ordinal $\varepsilon_0$.
15. [[Proof interpretations and conservation results|8XY7JYZKFW]]: translate one theory into another, as Gödel's Dialectica interpretation does, and show that a strong theory proves no new statements of a simple form.
16. [[Provability and interpretability logics|3E7M66WW6Q]]: treat "the theory proves" as a modal operator, and find the exact laws that it obeys.
17. [[Reverse mathematics and subsystems of second-order arithmetic|BY8AAFN7C5]]: ask which axioms an ordinary theorem really needs, and find that many theorems are equivalent to one of five systems.
18. [[Bounded arithmetic|RA380RWEC0]]: study weak theories whose provably total functions match complexity classes such as polynomial time.
19. [[Propositional proof complexity|CBAF7J051K]]: ask how long the shortest proof of a tautology must be, a question tied to whether NP equals coNP.

### Reading order, continued: non-classical logics

20. [[Syntax, Kripke semantics and completeness of modal logic|SKY7AQFG1V]]: read "necessarily" and "possibly" in frames of possible worlds, and prove completeness for the standard modal systems.
21. [[Modal correspondence, bisimulation and extended modal logics|SPQVNPZDTB]]: match modal axioms with properties of frames, and learn when modal formulas cannot tell two models apart.
22. [[Applied modal logics|CQM9SRN8PM]]: use modal logics of time, knowledge and programs, among them the logics behind model checking.
23. [[Intuitionistic and intermediate logics|38EQ20GR7M]]: drop the law of excluded middle, and see the logic that constructive proofs obey.
24. [[Many-valued and fuzzy logics|WZP584JQ06]]: allow truth values between true and false, as in the logics of Łukasiewicz and Gödel.
25. [[Substructural, linear and relevance logics|98QF5J4W16]]: control how often a premise may be used, and require the premises to be relevant to the conclusion.
26. [[Paraconsistent, free, non-monotonic and other non-classical logics|NJB94B39QK]]: reason from inconsistent data, about names that may denote nothing, and with defaults that new information can withdraw.

### Reading order, continued: algebra and truth

27. [[Algebraic logic|QYA4H5Y7VR]]: turn logics into algebras, such as Boolean and Heyting algebras, and prove theorems about logics with the tools of algebra.
28. [[Truth and the semantic paradoxes|6Q4JJ2MMV8]]: face the liar sentence, and see how Tarski's hierarchy, Kripke's fixed points and axiomatic theories describe truth without contradiction.

### Prerequisites

The core course needs no logic in advance.
It does need comfort with sets, functions and proof by induction, because most theorems about formulas are proved by induction on how the formulas are built.
[[Reasoning and proof|SGSVYFDSYK]] gives that practice.
The later groups use more: some countable sets and cardinals for compactness, some computability for decidability and incompleteness, and ordinals for ordinal analysis.

### The four branches

Logic studies [[formal languages|5MFZ4VNY6D]], the [[formal systems|439M8B4DY2]] that derive formulas of these languages, and the [[structures|983GZBQYT4]] in which the formulas are true or false.
It is traditionally divided into four branches.

- [[Proof theory|N4EDJNMTEF]] studies proofs as finite objects: their structure, how they can be transformed, and how strong a theory is.
- [[Model theory|HFTBG5PMXC]] studies how theories relate to the structures that satisfy them.
- [[Set theory|RTHHCX84HN]] studies sets, from which most of mathematics is built, and the axioms that describe them.
- [[Computability theory|X14Y880PN5]] studies which functions and sets an algorithm can compute, and how hard the others are.

The reading order above covers proof theory and the logics themselves.
Model theory, set theory and computability theory are large enough to have areas of their own.

### How the branches meet

The branches are joined by a few great theorems.
Gödel's [[completeness theorem|WQ1ZE255SF]] joins proofs and models: a sentence of [[first-order logic|086QKPF0A6]] is provable exactly when it is true in every model.
The [[incompleteness theorems|X9WYNYE29C]] join proofs and computation, because "computable set of axioms" is a notion from computability theory.
Set theory builds new models of its own axioms with the methods of model theory, and computability theory shows that some logics have no decision procedure.

Logic also plays two roles at once.
As a branch of mathematics it has its own definitions, theorems and open problems, just as algebra or topology does.
As a [[foundation|EFFRJFW67Y]] it says exactly what a statement, a proof and a theorem are, and so it tells the other branches which arguments they may use.

### The main theorems

A handful of results anchor the whole subject.

- The completeness theorem (Gödel, 1929): a first-order sentence is provable exactly when it is true in all models.
- The [[compactness theorem|1NR3HAWG9D]]: a set of first-order sentences has a model if each of its finite subsets has a model.
- The incompleteness theorems (Gödel, 1931): a consistent theory with computable axioms and enough arithmetic does not decide every sentence, and it does not prove its own consistency.
- [[Tarski's undefinability theorem|YRV6SYK2BY]]: truth in arithmetic cannot be defined by a formula of arithmetic.
- [[Church's theorem|VA6BNNY2YC]] (Church and Turing, 1936): no algorithm decides validity in first-order logic.
- The [[cut-elimination theorem|AYRZ98Y0NW]] (Gentzen): every proof in the sequent calculus can be turned into a proof without the cut rule.

### Logic in computer science

Many ideas of logic now do daily work in computing.
Hardware and software are checked by [[model checking|VNY0VXVZ53]] against specifications written in [[modal|C3RZY20ETK]] and temporal logics.
The [[Boolean satisfiability problem|3QKF32ZAKN]] was the first problem shown to be NP-complete, and yet SAT solvers decide large instances of it in practice.
The [[Curry-Howard correspondence|A77FER1Q5H]] identifies proofs with programs, and it underlies type theory and [[proof assistants|YM6PRDE88V]].
[[Descriptive complexity theory|YRHZEF2JMZ]] describes complexity classes by the logics that can define them.

### History

Aristotle gave the first formal logic, the syllogistic, in the 4th century BC, and the Stoics studied the logic of connectives.
George Boole treated logic as algebra in 1847 and 1854.
Gottlob Frege gave the first formal language with quantifiers in his *Begriffsschrift* of 1879.
Whitehead and Russell derived a large part of mathematics in a formal system in *Principia Mathematica* (1910 to 1913).
In the 1920s David Hilbert proposed his [[program|P1RW6JWX73]]: formalize mathematics, and prove its consistency by finitary means.

The 1930s gave the subject its present form.
Gödel proved the completeness theorem in 1929 and the incompleteness theorems in 1931.
Alfred Tarski defined truth for formal languages in 1933.
Gerhard Gentzen introduced natural deduction and the sequent calculus in 1934 and 1935, and he proved the consistency of arithmetic in 1936.
Alonzo Church and Alan Turing showed in 1936 that first-order validity is undecidable.

After 1950 the four branches grew into separate fields.
Saul Kripke and others gave a semantics for modal and intuitionistic logic in the late 1950s and the 1960s.
Paul Cohen invented forcing in 1963 and proved that the [[continuum hypothesis|0MN2MER9WN]] does not follow from the axioms of ZFC.
The [[history of mathematical logic|WP3602P9EH]] tells the story at greater length.

### Related areas

[[Reasoning and proof|SGSVYFDSYK]] treats logic as a working tool: how to read statements and how to write proofs.
[[Model theory|F3AXVABC35]], [[set theory|G9W9J6KPAR]] and [[computability theory|ZNC3817RA6]] are the other three classical branches of logic.
[[Type theory and constructive mathematics|K6P3NSQEZ3]] holds the lambda calculus, the Curry-Howard correspondence and constructive mathematics.
[[Category theory|Y97P9CSMEN]] holds categorical logic and toposes.
[[Order, lattices and universal algebra|V1VVQR12AQ]] treats Boolean and Heyting algebras as algebras.
[[Theory of computation|52TNMMSXD3]] holds SAT as a computational problem and the logics of programs.
[[Mathematical software and formalization|F3F5GGYHMM]] holds proof assistants and automated theorem proving.
[[Philosophy of mathematics|NTJ5XW0PVD]] holds logicism, formalism and intuitionism as views of what mathematics is.
[[History of mathematics|EJZNJJ6M7S]] holds the history of logic beyond the survey above.
