---
tag: 9RN0KYXNT1
kind: statement
role: theorem
name: Łoś–Tarski preservation theorem
aliases: [los-tarski-preservation-theorem, los-tarski-theorem]
msc: ["03C40", "03C52"]
topics: [JYJHB4YBAH]
audience: grad
uses: [WDVVEYD6AT, 92SWXST1ZM, MVCH6N9SNW, 676H7EGTKJ, ZSTEZ3PRT9, 1NR3HAWG9D, DKFGQTRYZE, SCRB74SWQN, CS82V969DE]
about: [ZSTEZ3PRT9, MEC3ZMC4F1]
history:
  notes: The theorem dates from the 1950s and carries the names of Jerzy Łoś and Alfred Tarski. William Tait showed in 1959 that it fails over finite structures.
sources:
  - url: https://en.wikipedia.org/wiki/Łoś–Tarski_preservation_theorem
    locator: Statement
  - book: isbn:9780521587136
same_as:
  wikidata: Q8080822
  wikipedia: Łoś–Tarski preservation theorem
---

## Statement

Let $L$ be a first-order [[signature|WDVVEYD6AT]], and let $T$ be an $L$-[[theory|92SWXST1ZM]].
A [[sentence|DKFGQTRYZE]] is *universal* if it has the form $\forall x_1 \cdots \forall x_n \, \theta$ with $\theta$ quantifier-free, and *existential* if it has the form $\exists x_1 \cdots \exists x_n \, \theta$.
Let $T_\forall$ and $T_\exists$ be the sets of universal and of existential sentences that are consequences of $T$.

1. The class of [[models|MVCH6N9SNW]] of $T$ is closed under [[substructures|676H7EGTKJ]] if and only if $T_\forall$ has the same models as $T$. So the models of $T$ form a [[universal class|ZSTEZ3PRT9]].
2. The class of models of $T$ is closed under extensions if and only if $T_\exists$ has the same models as $T$.
3. A sentence $\varphi$ is preserved by substructures if and only if it is logically equivalent to a universal sentence. It is preserved by extensions if and only if it is logically equivalent to an existential sentence.

Here "closed under substructures" means: if $B \models T$ and $A$ is a substructure of $B$, then $A \models T$.
"Closed under extensions" means: if $A \models T$ and $A$ is a substructure of $B$, then $B \models T$.
A proof is in [[the proof of the Łoś-Tarski theorem|TRXB894JMH]].

## Remarks

### Why each hypothesis is needed

- First-order axioms. The class of [[well-orders|01CGSJ0GNQ]] is closed under substructures, since a subset of a well-order is well-ordered. It is not an [[elementary class|MEC3ZMC4F1]], so it has no universal axioms.
- The signature. In the signature $\set{\cdot}$ the positive integers form a substructure of the group $(\mathbb{Z}, +)$ that is not a group. In $\set{\cdot, {}^{-1}, e}$ the group axioms are universal, and the class is closed under substructures.
- All structures, not only finite ones. Over finite structures the theorem fails, as the next subsection shows.

### Failure over finite structures

Let $L = \set{<, S, \min, \max}$ with $S$ binary and $\min, \max$ constants.
Let $\alpha$ be the universal sentence that says: $<$ is a linear order, every $x$ satisfies $\min \le x \le \max$, and $S(x, y)$ implies that $y$ is the immediate successor of $x$.
Let $\varphi$ be $\alpha \wedge \exists x \, (x \ne \max \wedge \forall y \, \neg S(x, y))$, so $\varphi$ says that the $S$-chain is broken somewhere.
We check five facts.

1. Let $A$ be a finite model of $\alpha$, and let $B$ be a substructure. Then $B \models \alpha$, since $\alpha$ is universal, and $B$ contains $\min$ and $\max$.
2. Suppose that every $x \ne \max$ in $B$ has an $S$-successor in $B$. Then the chain from $\min$ runs through consecutive elements of $A$ up to $\max$, so $B = A$.
3. So a proper substructure of a finite model of $\alpha$ is broken, and it satisfies $\varphi$. Hence finite models of $\varphi$ are closed under substructures.
4. Suppose that $\varphi$ is equivalent on finite structures to $\forall x_1 \cdots \forall x_n \, \theta$. The full chain $C$ on $0 < 1 < \dots < n + 2$ fails $\varphi$, so $C \models \neg\theta(\bar a)$ for some $\bar a$. The substructure on $\bar a$, $0$ and $n + 2$ is proper, so it satisfies $\varphi$ by step 3, but it fails $\theta(\bar a)$, a contradiction.
5. Over infinite structures $\varphi$ is not preserved: the order $\omega + 1 + \omega^*$ is broken only at its middle point, and removing that point gives a model of $\neg\varphi$.

### Consequences

- The integral domains are closed under subrings with $1$, so they have universal axioms; the fields are not, so they have none.
- A finitely axiomatizable theory closed under substructures is axiomatized by one universal sentence, by part 3.
- For every theory $T$, each model of $T_\forall$ embeds in a model of $T$. This is the main lemma of the proof, and it needs no closure hypothesis.

### Converse

The easy direction of each part is the converse: universal sentences pass to substructures by [[this statement|C9494XYEMN]], and existential sentences pass to extensions.

### Generalizations

- Relative form: a formula $\varphi(\bar x)$ is preserved by substructures between models of $T$ if and only if it is equivalent modulo $T$ to a universal formula.
- Unions of chains and $\forall\exists$ sentences: the [[Chang-Łoś-Suszko theorem|RK7NK2P75J]].
- The pattern of [[preservation theorems|T69D2NS1HP]] lists the other constructions.

## History

The theorem dates from the 1950s and carries the names of Jerzy Łoś and Alfred Tarski.
William Tait showed in 1959 that it fails over finite structures, and Yuri Gurevich and Saharon Shelah later found this failure again.

## Explanations

### L1 human

A universal rule says that something holds for all elements, and it never asks for an element to exist.
Such a rule still holds when one keeps only a part of a structure.
The theorem gives the converse: if a list of first-order rules always survives when one passes to a part, then the list can be replaced by universal rules.
So a property of the models, closure under parts, decides the shape of the axioms.

### L2 human

We test the theorem on the theory of fields in the signature $\set{+, -, \cdot, 0, 1}$.

1. The ring $\mathbb{Z}$ is a substructure of the field $\mathbb{Q}$: it contains $0$ and $1$ and is closed under $+$, $-$ and $\cdot$.
2. In $\mathbb{Z}$ the element $2$ has no inverse, so $\mathbb{Z}$ is not a field.
3. So the class of fields is not closed under substructures.
4. By part 1, no set of universal sentences axiomatizes the fields.
5. The class of integral domains is closed under substructures, and its axioms are universal: $0 \ne 1$ and $\forall x \forall y \, (x y = 0 \rightarrow x = 0 \vee y = 0)$, with the ring axioms.

The typical use is to prove that a class has no universal axioms, by one substructure.
A trap is to apply the theorem to a class of finite structures; the example above shows that it fails there.

### L3 human

The proof realizes the diagram of a model of $T_\forall$ inside a model of $T$, by compactness.
It is the simplest case of the general plan of [[preservation theorems|T69D2NS1HP]], which continues with unions of chains, homomorphisms and reduced products.
The theorem gives an inclusion of [[universal classes|ZSTEZ3PRT9]] among elementary classes, and their characterization by substructures and ultraproducts is [[this theorem|JPGDSW2TAP]].
In the language of categories of models, closure under monomorphisms (embeddings) matches universal axioms.
In finite model theory the theorem fails, while Rossman's homomorphism preservation theorem survives; see [[Lyndon's theorem|8DJSRWME2X]].
