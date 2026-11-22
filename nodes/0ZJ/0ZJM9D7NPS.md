---
tag: 0ZJM9D7NPS
kind: statement
role: theorem
name: Canonical isomorphism with the double dual
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug2
about: [07JBSZE0V4]
uses: [0M856Q1AMZ, 00889YD15K, 018W3V3TCT, 0RJF668P1T]
formal:
  - system: lean4
    library: mathlib
    decl: Module.evalEquiv
    match: weaker
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Injection into the double-dual
  - book: isbn:9783031410253
    locator: Section 3F
  - book: isbn:9780134860244
    locator: Section 2.6
---

## Statement

Every vector sits inside the double dual as the form "evaluate at me", and in finite dimension this fills the whole double dual without any choice of basis.
Let $F$ be a field and let $V$ be a vector space over $F$, of any dimension.
Let $V^{**} = (V^*)^*$ be the dual of the [[dual space|0M856Q1AMZ]] $V^*$.
The *evaluation map* $\operatorname{ev}_V \colon V \to V^{**}$ is defined by
$$\operatorname{ev}_V(v)(f) = f(v) \qquad (v \in V,\ f \in V^*).$$

1. Each $\operatorname{ev}_V(v)$ is a linear form on $V^*$, and $\operatorname{ev}_V$ is a [[linear map|0RJF668P1T]].
2. The map $\operatorname{ev}_V$ is injective.
3. The map $\operatorname{ev}_V$ is an isomorphism if and only if $V$ is [[finite-dimensional|018W3V3TCT]].

## Remarks

### A first computation

Take $V = \mathbb{R}^2$, with the coordinate forms $x$ and $y$ as a basis of $V^*$.
A form on $V^*$ is fixed by its values on $x$ and $y$.
For $v = (3, -1)$, the element $\operatorname{ev}(v)$ sends $x$ to $3$ and $y$ to $-1$.
On the form $f = 2x + 5y$, linearity of $\operatorname{ev}(v)$ gives
$$\operatorname{ev}(v)(f) = 2 \cdot 3 + 5 \cdot (-1) = 1,$$
and directly $f(3, -1) = 6 - 5 = 1$.
Conversely, let $\Phi \in V^{**}$ send $x$ to $4$ and $y$ to $7$.
Then $\Phi = \operatorname{ev}(4, 7)$, since both agree on a basis of $V^*$.
So every element of $V^{**}$ comes from a vector, as part 3 promises.

### Why each hypothesis is needed

Part 3 needs finite dimension.
For $V = F^{(\mathbb{N})}$, the coordinate forms and the form $s$ that adds up all terms are independent in $V^*$.
So there is a form $\Phi$ on $V^*$ that is $0$ on every coordinate form and $1$ on $s$.
A vector $v$ with $\operatorname{ev}(v) = \Phi$ would have all coordinates $0$, so $v = 0$, but $\operatorname{ev}(0)(s) = 0 \ne 1$.
The [[proof|A03D8FXB92]] gives the details, and the [[Erdős-Kaplansky theorem|S5ET1HG2ZX]] gives a second proof: in infinite dimension, $\dim V^{**} > \dim V^* > \dim V$.

Part 2 needs enough forms to detect every nonzero vector, and over a field a basis supplies them.
Over the ring $\mathbb{Z}$ this fails: every $\mathbb{Z}$-linear map $\mathbb{Z}/2\mathbb{Z} \to \mathbb{Z}$ is $0$, so the double dual of $\mathbb{Z}/2\mathbb{Z}$ is $0$ and the evaluation map is not injective.

### What it gives you

In finite dimension, each element of $V^{**}$ is $\operatorname{ev}_V(v)$ for exactly one $v$.
So $V$ is, in effect, the dual of $V^*$, and the roles of $V$ and $V^*$ become symmetric.
For example, every basis $\varphi_1, \dots, \varphi_n$ of $V^*$ is the dual basis of exactly one basis of $V$.
To find it, take the dual basis $\varphi_1^*, \dots, \varphi_n^*$ of $V^{**}$ and put $v_i = \operatorname{ev}_V^{-1}(\varphi_i^*)$.
Then $\varphi_j(v_i) = \varphi_i^*(\varphi_j) = \delta_{ij}$.
In the same way, the dual basis of a dual basis $b_1^*, \dots, b_n^*$ is $\operatorname{ev}_V(b_1), \dots, \operatorname{ev}_V(b_n)$, since $\operatorname{ev}_V(b_j)(b_i^*) = b_i^*(b_j) = \delta_{ij}$.

### Why it is called canonical

The definition of $\operatorname{ev}_V$ uses no basis, no inner product and no other choice.
The [[naturality lemma|R19758JQWE]] makes this precise: for each linear map $f \colon V \to W$, we have $f^{**} \circ \operatorname{ev}_V = \operatorname{ev}_W \circ f$.
The [[example of the evaluation map|J3X26BSQEY]] compares it with the isomorphisms $V \cong V^*$ that a basis gives, which change when the basis changes.
In the language of category theory, $\operatorname{ev}$ is a [[natural transformation|KYCPCC57FT]] from the identity functor to the double dual functor.

### Watch out

The canonical isomorphism $V \cong V^{**}$ does not give a canonical isomorphism $V \cong V^*$.
In $\mathbb{R}^2$, the basis $(1, 0), (0, 1)$ sends $(1, 0)$ to the form $x$, but the basis $(1, 0), (1, 1)$ sends $(1, 0)$ to the form $x - y$.
Only the double dual can be identified with $V$ without choices.
Also, "isomorphism" in part 3 really needs finite dimension: in infinite dimension $\operatorname{ev}_V$ is injective but never onto.

### Generalizations

For a finitely generated free module over a commutative ring, the evaluation map is again an isomorphism, by the same dual basis argument.
Mathlib states the finite case as `Module.evalEquiv`, which does not include the injectivity in infinite dimension.
For normed spaces, the evaluation map into the continuous bidual is an isometric embedding, by the Hahn-Banach theorem.
The spaces for which it is onto are called reflexive, and the [[continuous dual space|4A82S5FVRT]] treats them.

## History

Samuel Eilenberg and Saunders Mac Lane introduced categories, functors and natural transformations in a paper of 1945.
The map from a vector space to its double dual is one of the standard examples that motivated their notion of a natural transformation.

## Explanations

### L1 human

A vector $v$ can act on linear forms: it sends each form $f$ to the number $f(v)$.
So each vector gives a way of turning forms into numbers, which is an element of the double dual.
For example, the vector $(3, -1)$ sends the form $2x + 5y$ to $6 - 5 = 1$.
Different vectors give different results on some form, so no information is lost.
In finite dimension, every element of the double dual comes from exactly one vector in this way.

### L2 human

Here is a typical use: recovering a vector from what the forms say about it.
In $V = \mathbb{R}^2$, take the basis $\varphi_1 = x + y$ and $\varphi_2 = x - y$ of $V^*$, and let $\Phi \in V^{**}$ satisfy $\Phi(\varphi_1) = 5$ and $\Phi(\varphi_2) = 1$.
Part 3 says that $\Phi = \operatorname{ev}(v)$ for exactly one $v = (a, b)$.
That vector must satisfy
$$a + b = 5, \qquad a - b = 1,$$
so $a = 3$ and $b = 2$.
Check: $\varphi_1(3, 2) = 5$ and $\varphi_2(3, 2) = 1$.
This is how the theorem is used in practice: a vector is the same thing as a consistent list of values of forms on it.
Watch out: in infinite dimension some elements of $V^{**}$ come from no vector at all.

### L3 human

The evaluation maps make the double dual functor naturally isomorphic to the identity functor on finite-dimensional spaces.
No such statement can even be formulated for $V \to V^*$ in the same way, because the dual functor reverses the direction of maps while the identity functor keeps it.
For infinite-dimensional $V$, the image $\operatorname{ev}_V(V)$ is a proper subspace of a much larger space.
In functional analysis, the same question for the continuous bidual leads to reflexive spaces.
Within linear algebra, the identification $V = V^{**}$ makes later results symmetric, such as $f^{**} = f$ for the [[dual map|0AZ5ARP287]] and $U^{00} = U$ for the [[annihilator|0ASHNYF7AG]].
