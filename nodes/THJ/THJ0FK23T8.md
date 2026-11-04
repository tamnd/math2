---
tag: THJ0FK23T8
kind: statement
role: proposition
name: Von Neumann's 1925 axiom system
sources:
  - wikipedia: en:528491@r1330985339
    locator: Von Neumann–Bernays–Gödel set theory, section History > Von Neumann's 1925 axiom system
    note: adopted
    mention: wikipedia://en/528491#QLAT
    sections: [Statement]
inventory: [XFXC99EKPR]
---

## Statement

Von Neumann published an introductory article on his axiom system in 1925. In 1928, he provided a detailed treatment of his system. Von Neumann based his axiom system on two domains of primitive objects: functions and arguments. These domains overlap—objects that are in both domains are called argument-functions. Functions correspond to classes in NBG, and argument-functions correspond to sets. Von Neumann's primitive operation is function application, denoted by \[*a*, *x*\] rather than *a*(*x*) where *a* is a function and *x* is an argument. This operation produces an argument. Von Neumann defined classes and sets using functions and argument-functions that take only two values, *A* and *B*. He defined *x* ∈ *a* if \[*a*, *x*\] ≠ *A*.

Von Neumann's work in set theory was influenced by Georg Cantor's articles, Ernst Zermelo's 1908 axioms for set theory, and the 1922 critiques of Zermelo's set theory that were given independently by Abraham Fraenkel and Thoralf Skolem. Both Fraenkel and Skolem pointed out that Zermelo's axioms cannot prove the existence of the set {*Z*<sub>0</sub>, *Z*<sub>1</sub>, *Z*<sub>2</sub>, ...} where *Z*<sub>0</sub> is the set of [[natural numbers|0MWKJ44V5A]] and *Z*<sub>*n*+1</sub> is the [[power set|00E0YZCERH]] of *Z*<sub>*n*</sub>. They then introduced the axiom of replacement, which would guarantee the existence of such sets. However, they were reluctant to adopt this axiom: Fraenkel stated "that Replacement was too strong an axiom for 'general set theory'", while "Skolem only wrote that 'we could introduce' Replacement".

Von Neumann worked on the problems of Zermelo set theory and provided solutions for some of them:

- **A theory of ordinals**
  - Problem: Cantor's theory of [[ordinal numbers|0RDJK7EQYY]] cannot be developed in Zermelo set theory because it lacks the axiom of replacement.
  - Solution: Von Neumann recovered Cantor's theory by defining the ordinals using sets that are well-ordered by the ∈-relation, and by using the axiom of replacement to prove key theorems about the ordinals, such as every well-ordered set is order-isomorphic with an ordinal. In contrast to Fraenkel and Skolem, von Neumann emphasized how important the replacement axiom is for set theory: "In fact, I believe that no theory of ordinals is possible at all without this axiom."
- **A criterion identifying classes that are too large to be sets**
  - Problem: Zermelo did not provide such a criterion. His set theory avoids the large classes that lead to the paradoxes, but it leaves out many sets, such as the one mentioned by Fraenkel and Skolem.
  - Solution: Von Neumann introduced the criterion: A class is too large to be a set if and only if it can be mapped onto the class *V* of all sets. Von Neumann realized that the set-theoretic paradoxes could be avoided by not allowing such large classes to be members of any class. Combining this restriction with his criterion, he obtained his axiom of limitation of size: A class *C* is not a member of any class if and only if *C* can be mapped onto *V*.
- **Finite axiomatization**
  - Problem: Zermelo had used the imprecise concept of "definite propositional function" in his axiom of separation.
  - Solutions: Skolem introduced the axiom schema of separation that was later used in ZFC, and Fraenkel introduced an equivalent solution. However, Zermelo rejected both approaches "particularly because they implicitly involve the concept of natural number which, in Zermelo's view, should be based upon set theory." Von Neumann avoided axiom schemas by formalizing the concept of "definite propositional function" with his functions, whose construction requires only finitely many axioms. This led to his set theory having finitely many axioms. In 1961, Richard Montague proved that ZFC cannot be finitely axiomatized.
- **The axiom of regularity**
  - Problem: Zermelo set theory starts with the empty set and an infinite set, and iterates the axioms of pairing, union, power set, separation, and choice to generate new sets. However, it does not restrict sets to these. For example, it allows sets that are not well-founded, such as a set *x* satisfying *x* ∈ *x*.
  - Solutions: Fraenkel introduced an axiom to exclude these sets. Von Neumann analyzed Fraenkel's axiom and stated that it was not "precisely formulated", but it would approximately say: "Besides the sets ... whose existence is absolutely required by the axioms, there are no further sets." Von Neumann proposed the axiom of regularity as a way to exclude non-well-founded sets, but did not include it in his axiom system. In 1930, Zermelo became the first to publish an axiom system that included regularity.
