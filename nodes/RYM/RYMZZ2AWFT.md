---
tag: RYMZZ2AWFT
kind: statement
role: theorem
name: Feferman-Vaught theorem
aliases: [feferman-vaught-theorem]
msc: ["03C20", "03C30"]
topics: [HZG1YP26AB]
audience: grad
about: [WJ73XYBNE4, F4WRD396PB]
uses: [WJ73XYBNE4, HYJ10AF6RT, 0XADJKM699, 00E0YZCERH, P3B1V182N4]
history:
  first_stated: "Solomon Feferman and Robert Vaught, 1959"
  notes: "Fundamenta Mathematicae 47; it extends work of Mostowski of 1952 on direct products of theories."
sources:
  - url: https://en.wikipedia.org/wiki/Feferman%E2%80%93Vaught_theorem
    locator: Statement of the theorem for direct products
---

## Statement

Let $L$ be a signature.
For every $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$ one can effectively find $L$-formulas $\theta_1(\bar{x}), \dots, \theta_k(\bar{x})$ and a formula $\Phi(X_1, \dots, X_k)$ in the first-order language of [[Boolean algebras|0XADJKM699]] with the following property.

For every nonempty set $I$, all $L$-structures $\mathcal{M}_i$ ($i \in I$) with nonempty domains, and all $a_1, \dots, a_n \in \prod_{i \in I} M_i$,
$$\prod_{i \in I} \mathcal{M}_i \models \varphi(a_1, \dots, a_n) \iff \mathcal{P}(I) \models \Phi\big([\![ \theta_1(\bar{a}) ]\!], \dots, [\![ \theta_k(\bar{a}) ]\!]\big).$$
Here $\prod_{i \in I} \mathcal{M}_i$ is the [[direct product|WJ73XYBNE4]], $[\![ \theta(\bar{a}) ]\!] = \set{i \in I : \mathcal{M}_i \models \theta(a_1(i), \dots, a_n(i))}$, and $\mathcal{P}(I)$ is the [[power set|00E0YZCERH]] Boolean algebra $(\mathcal{P}(I), \cup, \cap, {}^c, \emptyset, I)$.

## Remarks

### Why each hypothesis is needed

- Nonempty domains: if one domain is empty, the product is empty and has no elements to evaluate formulas at.
- First-order formulas: for $I = \set{1}$ the product is $\mathcal{M}_1$, and "well ordered" separates $(\N, <)$ from its nonprincipal ultrapower, although both satisfy the same first-order formulas.
- The truth sets are needed, not only the theories of the factors: for a formula with parameters, the answer depends on where each parameter coordinate satisfies each $\theta_j$.

### Consequences

- If $\mathcal{M}_i \equiv \mathcal{N}_i$ for every $i \in I$, then $\prod_i \mathcal{M}_i \equiv \prod_i \mathcal{N}_i$: for sentences, the truth sets of the $\theta_j$ agree.
- In particular $\mathcal{M} \equiv \mathcal{N}$ implies $\mathcal{M}^I \equiv \mathcal{N}^I$ for every $I$.
- Decidability: by prime factorization, $(\N_{>0}, \cdot)$ is a weak direct power of $(\N, +)$. The version of the theorem for weak products reduces [[Skolem arithmetic|X86G2FXTPC]] to Presburger arithmetic, so it is decidable.
- For an ultrafilter $\mathcal{U}$, the quotient $\mathcal{P}(I) / \mathcal{U}$ has two elements, and the version for reduced products gives [[Łoś's theorem|AGYBSTD7BG]].

### Converse

The truth of $\varphi$ in the product does not determine the factors: $\Z \times \set{0} \cong \set{0} \times \Z$ as groups, while the factors at index $1$ are not elementarily equivalent.
So the theorem goes in one direction only: from the factors to the product.

### Generalizations

- Reduced products: with the same $\theta_j$ and $\Phi$, $\prod_i \mathcal{M}_i / F \models \varphi([\bar{a}])$ if and only if $\mathcal{P}(I) / F \models \Phi([\![ \theta_1(\bar{a}) ]\!] / F, \dots)$.
- Generalized products: Feferman and Vaught allow any Boolean algebra of subsets of $I$ and products closed under gluing elements along its sets.
- Weak direct products, sums of linear orders and disjoint unions of structures obey similar composition theorems, which reduce the theory of the whole to the theories of the parts.

## History

Solomon Feferman and Robert Vaught published the theorem in 1959, in "The first order properties of products of algebraic systems", Fundamenta Mathematicae 47.
It extends Andrzej Mostowski's 1952 work on direct products of theories.
The [[proof by induction on formulas|6D6HZFQVVV]] follows their method.

## Explanations

### L1 human

In a product, an element is a list with one entry from each factor.
To decide a statement about some lists, we look at each factor separately and record where certain simpler statements hold.
The theorem says that this record, a few sets of positions, is enough to decide the original statement.
For example, the statement "$a$ is the zero element" holds in a product of groups exactly when it holds at every position.

### L2 human

We compute the reduction for $\varphi(x) = \exists y \, (y + y = x)$ in a product of abelian groups.

1. Let $\theta(x, y)$ be $y + y = x$. For atomic $\theta$, the product satisfies $\theta(a, b)$ exactly when $[\![ \theta(a, b) ]\!] = I$.
2. A witness $b$ must satisfy $y + y = a(i)$ in each factor. Such a $b(i)$ exists exactly when $i \in [\![ \exists y \, (y + y = x)(a) ]\!]$.
3. So we may take $\theta_1 = \varphi$ and for $\Phi(X_1)$ the formula $X_1 = 1$, where $1$ is the top element $I$.
4. In $\Z \times \Q$, the element $(4, 1)$ is a double, since $4 = 2 + 2$ and $1 = 1/2 + 1/2$. The element $(3, 1)$ is not, since $3$ is odd.

The typical use is to compute the theory of a product from the theories of the factors.
The trap is to think that $\Phi$ is always "$X_1 = 1$"; for formulas with negation, the truth sets may be proper and nonempty.

### L3 human

The theorem is the model-theoretic form of a composition principle: the theory of a composite structure is computed from the theories of its parts and of the index structure.
Shelah's composition method for monadic second-order theories of linear orders and the composition theorems for sums of structures follow the same pattern.
In the Boolean-valued view, a product is a $\mathcal{P}(I)$-valued structure, and the theorem says that the $\mathcal{P}(I)$-valued truth of $\varphi$ is a first-order definable function, given by $\Phi$, of the truth values of the $\theta_j$.
For [[reduced products|F4WRD396PB]] and ultraproducts, passing to the quotient algebra gives the theorems on [[Horn formulas|8RRECJJM3G]] and Łoś's theorem.
