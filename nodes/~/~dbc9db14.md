---
tag: ~dbc9db14
kind: statement
role: theorem
name: The linear maps between two spaces form a vector space
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
about: [0X9MBPP2Z3]
uses: [0VPCJWGMP9, 05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Vector space of linear maps
  - book: isbn:9783031410253
    locator: Chapter 3
  - book: isbn:9780135367971
    locator: Section 3.2
---

## Statement

Let $F$ be a field and let $V$ and $W$ be vector spaces over $F$.
Then $\Hom_F(V, W)$, with the pointwise operations of its [[definition|0VPCJWGMP9]], is a [[vector space|05EGHEQZAW]] over $F$.
Its zero vector is the zero map $v \mapsto 0$, and the negative of $T$ is the map $v \mapsto -T(v)$.

## Remarks

### Why each hypothesis is needed

- The scalars must commute. The proof that $cT$ is linear uses $c\,a = a\,c$ for $a, c \in F$.
- Over a noncommutative ring $R$, the $R$-linear maps between two left $R$-modules form an abelian group. In general, they do not form an $R$-module.
- $V$ and $W$ must be over the same field, since $T(av) = a\,T(v)$ multiplies by $a$ on both sides.

### Consequences

- The [[dual space|07JBSZE0V4]] $V^* = \Hom(V, F)$ is a vector space.
- The endomorphisms $\End(V) = \Hom(V, V)$ form a vector space, and also an [[algebra|~42300f41]] under composition.
- The [[dimension theorem|0Z9N1ER0W0]] $\dim \Hom(V, W) = \dim V \cdot \dim W$ makes sense.
- Expressions such as $T - \lambda \id_V$ and $a_0 \id + a_1 T + a_2 T^2$ are linear maps.

### Converse

The set $W^V$ of all maps $V \to W$ is also a vector space, and $\Hom(V, W)$ is a subspace of it.
If $W \ne \{0\}$, this subspace is proper: for $w \ne 0$, the constant map $v \mapsto w$ is not linear.
So not every map in the larger space is linear.

### Generalizations

- For modules $M$ and $N$ over a commutative ring $R$, $\Hom_R(M, N)$ is an $R$-module, with the same proof.
- For topological vector spaces, the continuous linear maps form a subspace of $\Hom(V, W)$.

## History

Peano gave the modern definition of vector spaces and linear maps in 1888.
Textbooks such as Axler's and Hoffman and Kunze's prove the present result before they introduce the matrix of a linear map.

## Explanations

### L1 human

Add two linear maps by adding their values, and scale a linear map by scaling its values.
The result is again a linear map.
So the linear maps from $V$ to $W$ form a vector space of their own.

### L2 human

For $S(x, y) = (x, 0)$ and $T(x, y) = (0, y)$ on $\R^2$, the sum is $S + T = \id$.
The map $2S - T$ sends $(x, y)$ to $(2x, -y)$, which is again linear.
The trap is to confuse the sum $S + T$ with the composite $S \circ T$; here $S \circ T = 0$.

### L3 human

The statement says that $\Hom_F(V, W)$ is a subspace of the product $W^V = \prod_{v \in V} W$.
It makes the category of vector spaces over $F$ enriched over itself.
Composition $\Hom(U, V) \times \Hom(V, W) \to \Hom(U, W)$ is bilinear.
