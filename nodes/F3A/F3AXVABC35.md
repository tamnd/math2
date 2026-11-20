---
tag: F3AXVABC35
kind: topic
name: Model theory
msc: ["03Cxx"]
---

## Summary

Model theory is the study of mathematical structures through the formal sentences that are true in them.
A model of a theory is a structure, that is a set with functions, relations and constants, in which every sentence of the theory is true.
Model theory classifies theories by the behavior of their models and of their definable sets, and its results have applications in algebra, algebraic geometry and number theory.
The subject grew from the work of Löwenheim, Skolem, Gödel and Tarski, and Tarski and Abraham Robinson made it a separate branch of logic in the 1950s.
This topic collects the model theory pages of math2.
Its sub-areas are listed below, in reading order.
Mathematical logic, set theory and computability theory have their own topics.

## Remarks

### What the area is about

Model theory studies the relation between formal [[theories|92SWXST1ZM]] and the [[structures|983GZBQYT4]] in which they are true.
A structure is a set with functions, relations and constants, such as a group, a field, an ordered set or a graph.
A first-order sentence is true or false in a structure, and a [[model|MVCH6N9SNW]] of a theory is a structure in which all its sentences are true.
The area asks three kinds of questions.
Which classes of structures can a theory describe, and how many models of each size does it have?
Which structures can a theory not tell apart?
Which sets can a formula define inside one structure, and how complicated are they?

Two slogans describe the subject.
Chang and Keisler wrote that model theory is universal algebra plus logic.
Hodges wrote that it is algebraic geometry minus fields: it studies the [[definable sets|CY1TXHF6KQ]] of a structure as algebraic geometry studies the zero sets of polynomials.

The main theorems of the area are the following.

- The [[compactness theorem|1NR3HAWG9D]]: a set of first-order sentences has a model if each finite subset has a model.
- The [[Löwenheim-Skolem theorem|484M0TZ1S7]]: a theory in a countable language with an infinite model has models of every infinite cardinality.
- [[Łoś's theorem|AGYBSTD7BG]]: a sentence is true in an ultraproduct exactly when it is true in almost all factors.
- [[Morley's theorem|V7N84P60SJ]]: a countable theory that is categorical in one uncountable cardinal is categorical in all of them.
- [[Quantifier elimination|7FDDXV3JK7]] for algebraically closed fields and real closed fields, which describes their definable sets.
- The o-minimality of the real exponential field, proved by Wilkie.

The applications reach algebra, geometry and number theory.
The [[Ax-Kochen theorem|PHT3TJCS90]] transfers results between $p$-adic fields and fields of power series.
Hrushovski's proof of the Mordell-Lang conjecture for function fields and Pila's proof of cases of the André-Oort conjecture use model-theoretic methods.
[[Nonstandard analysis|WM62GKCBWN]] gives rigorous infinitesimals, and [[finite model theory|4XRVJE0KAN]] links logic with computational complexity.

### History

Leopold Löwenheim proved in 1915 that a first-order sentence with an infinite model has a countable model, and Thoralf Skolem extended the result in 1920 and 1922.
Kurt Gödel proved the completeness theorem in 1929, Anatoly Mal'cev proved the compactness theorem for languages of any size in 1936, and Alfred Tarski defined truth in a formal language in 1933.
In the 1950s Tarski and Abraham Robinson made model theory a branch of mathematics with applications to algebra, and Jerzy Łoś proved his theorem on ultraproducts in 1955.
Michael Morley proved his categoricity theorem in 1965, and Saharon Shelah then built the classification theory of complete theories.
From the 1980s, the work of Zilber, Hrushovski, Pillay, van den Dries, Wilkie and others joined model theory with algebraic geometry and number theory.
The [[history of model theory|JNBJW8RTJD]] gives a longer account.

### How to read the area

A reader starts with [[basic notions of model theory|AY09KYSW81]], which needs the semantics of first-order logic and the compactness theorem from mathematical logic.
Then the core course follows, in this order.
[[Elementary extensions and the Löwenheim-Skolem theorems|2RE7GWWXM5]] and [[ultraproducts|HZG1YP26AB]] give the basic constructions of models.
[[Back-and-forth methods|N64R1MGDBN]], [[types and saturated models|Z772KEC9BY]] and [[countable models|6XEXRME4C1]] compare and count models.
[[Quantifier elimination|1A9JSC5YG8]] describes the definable sets of concrete theories.

After the core course the reader can choose among three lines.

- Pure model theory: [[Fraïssé theory|ZS8X8KS54R]], [[preservation theorems|JYJHB4YBAH]], [[interpretations|SZRM3N6BXW]], then [[strongly minimal sets|S4EZ9JZJS6]], [[stable theories|2T8HMVV8SB]] and [[NIP theories|RS09CRTDRA]].
- Tame geometry and algebra: [[o-minimality|QS8ZBPAFJN]], the [[model theory of fields|Q3S2YF9BCR]] and [[applications to Diophantine geometry|VYT6EX1HH1]].
- Logic and arithmetic: [[models of arithmetic|XFKQW3988J]], [[infinitary logics|VBYC17XY83]] and [[finite model theory|CBPS8B13S4]].

The full list of sub-areas, in reading order, is given below.

### Related areas

[[Mathematical logic|DYJ0KGTPMR]] holds the syntax and semantics of first-order logic, the completeness and compactness theorems, and the incompleteness theorems.
[[Set theory|G9W9J6KPAR]] supplies ordinals, cardinals and ultrafilters, and it uses model-theoretic methods to build models of its axioms.
[[Computability theory|ZNC3817RA6]] holds decidability of theories as a question about algorithms, and [[theory of computation|52TNMMSXD3]] holds descriptive complexity from the side of complexity classes.
[[Order, lattices and universal algebra|V1VVQR12AQ]] holds varieties and Boolean algebras, which model theory treats as special elementary classes.
[[Philosophy of mathematics|NTJ5XW0PVD]] and [[history of mathematics|EJZNJJ6M7S]] hold the questions of meaning and the wider history of logic.

### Sub-areas

1. [[Basic notions of model theory|AY09KYSW81]]
1. [[Elementary extensions and the Löwenheim-Skolem theorems|2RE7GWWXM5]]
1. [[Ultraproducts and product constructions|HZG1YP26AB]]
1. [[Back-and-forth methods and Ehrenfeucht-Fraïssé games|N64R1MGDBN]]
1. [[Types and saturated models|Z772KEC9BY]]
1. [[Countable models and categoricity|6XEXRME4C1]]
1. [[Fraïssé theory and homogeneous structures|ZS8X8KS54R]]
1. [[Quantifier elimination and model completeness|1A9JSC5YG8]]
1. [[Preservation and definability theorems|JYJHB4YBAH]]
1. [[Interpretations and imaginaries|SZRM3N6BXW]]
1. [[Indiscernibles and two-cardinal theorems|W9CHA4PD9H]]
1. [[Strongly minimal sets, Morley rank and categoricity|S4EZ9JZJS6]]
1. [[Stable theories and forking|2T8HMVV8SB]]
1. [[Classification theory and neostability|VDNEZE5N3H]]
1. [[NIP theories|RS09CRTDRA]]
1. [[O-minimality and tame geometry|QS8ZBPAFJN]]
1. [[Geometric stability and definable groups|B0B87T6RRF]]
1. [[Model theory of fields|Q3S2YF9BCR]]
1. [[Model theory of valued fields|5BRV55Q3W5]]
1. [[Applications to Diophantine geometry|VYT6EX1HH1]]
1. [[Decidability and definability in number theory|ZQFA17MJSB]]
1. [[Models of arithmetic|XFKQW3988J]]
1. [[Model-theoretic foundations of nonstandard analysis|T28ZZJRDJ6]]
1. [[Infinitary logics and abstract model theory|VBYC17XY83]]
1. [[Continuous logic and metric structures|YK237G414T]]
1. [[Model theory of modules and other special theories|SE149N6AA8]]
1. [[Finite model theory and descriptive complexity|CBPS8B13S4]]
