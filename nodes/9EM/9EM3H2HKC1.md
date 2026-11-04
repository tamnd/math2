---
tag: 9EM3H2HKC1
kind: statement
role: proposition
name: Russell's axiom of reducibility
sources:
  - wikipedia: en:10591072@r1331016515
    locator: Axiom of reducibility, section Russell's axiom of reducibility
    note: adopted
    mention: wikipedia://en/10591072#CP6C
    sections: [Statement]
inventory: [8KYHRCVF7Y]
---

## Statement

The axiom of reducibility states that any truth function (i.e. propositional function) can be expressed by a formally equivalent *predicative* truth function. It made its first appearance in Bertrand Russell's (1908) *Mathematical logic as based on the theory of types*, but only after some five years of trial and error. In his words: Thus a predicative function of an individual is a first-order function; and for higher types of arguments, predicative functions take the place that first-order functions take in respect of individuals. We assume then, that every function is equivalent, for all its values, to some predicative function of the same argument. This assumption seems to be the essence of the usual assumption of classes \[modern sets\] . . . we will call this assumption the *axiom of classes*, or the ***axiom of reducibility***.

For relations (functions of two variables such as "For all x and for all y, those values for which f(x,y) is true" i.e. ∀x∀y: f(x,y)), Russell assumed an *axiom of relations*, or \[the same\] ***axiom of reducibility***.

In 1903, he proposed a possible process of evaluating such a 2-place function by comparing the process to double integration: One after another, plug into *x* definite values *a<sub>m</sub>* (i.e. the particular *a<sub>j</sub>* is "a constant" or a parameter held constant), then evaluate f(*a<sub>m</sub>*,*y<sub>n</sub>*) across all the *n* instances of possible *y<sub>n</sub>*. For all *y<sub>n</sub>* evaluate f(a<sub>1</sub>, *y<sub>n</sub>*), then for all *y<sub>n</sub>* evaluate f(*a<sub>2</sub>*, *y<sub>n</sub>*), etc until all the *x* = *a<sub>m</sub>* are exhausted). This would create an *m* by *n* matrix of values: TRUE or UNKNOWN. (In this exposition, the use of indices is a modern convenience.)

In 1908, Russell made no mention of this [[matrix|0VD9ZSWWJG]] of *x*, *y* values that render a two-place function (e.g. relation) TRUE, but by 1913 he has introduced a matrix-like concept into "function". In \*12 of Principia Mathematica (1913) he defines "a matrix" as "any function, of however many variables, which does not involve any apparent variables. Then any possible function other than a matrix is derived from a matrix by means of generalisation, i.e. by considering the proposition which asserts that the function in question is true with all possible values or with some values of one of the arguments, the other argument or arguments remaining undetermined". For example, if one asserts that "∀y: f(x, y) is true", then *x* is the apparent variable because it is unspecified.

Russell now defines a matrix of "individuals" as a *first-order* matrix, and he follows a similar process to define a *second-order matrix*, etc. Finally, he introduces the definition of a *predicative function*:

A function is said to be *predicative* when it is a matrix. It will be observed that, in a hierarchy in which all the variables are individuals or matrices, a matrix is the same thing as an elementary function \[cf. 1913:127, meaning: the function contains *no* apparent variables\]. ¶ "Matrix" or "predicative function" is a primitive idea.

From this reasoning, he then uses the same wording to propose the same *axioms of reducibility* as he did in his 1908.

As an aside, Russell in his 1903 considered, and then rejected, "a temptation to regard a relation as definable in extension as a class of couples", i.e. the modern set-theoretic notion of [[ordered pair|0JQWWFCS9R]]. An intuitive version of this notion appeared in Frege's (1879) *Begriffsschrift* (translated in van Heijenoort 1967:23); Russell's 1903 followed closely the work of Frege (cf. Russell 1903:505ff). Russell worried that "it is necessary to give sense to the couple, to distinguish the referent from the relatum: thus a couple becomes essentially distinct from a class of two terms, and must itself be introduced as a primitive idea. It would seem, viewing the idea philosophically, that sense can only be derived from some relational proposition . . . it seems therefore more correct to take an intensional view of relations, and to identify them rather with class-concepts than with classes". As shown below, Norbert Wiener (1914) reduced the notion of relation to class by his definition of an ordered pair.
