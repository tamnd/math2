---
tag: ZERBQSTZB5
kind: definition
name: Algebraic proof systems
msc: ["03F20", "68Q17", "13P10"]
topics: [CBAF7J051K]
audience: research
defines: 1Q046J0AW2
uses: [3V24CYWDT6, T3SXVH3ZZC, 0B3D4C8YF2, D85VZWS9QK, FN734RQYM6, AM0BYNK5YJ]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Automatability
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_Nullstellensatz
    locator: lead section
---

## Definition

With $1$ for true, the clause $x$ becomes $1 - x$ and the clause $\neg x$ becomes $x$, each $0$ exactly when its clause is true.
Their sum is the constant $1$, so the two clauses cannot both hold, and an algebraic proof system refutes a CNF by reaching $1$ in this way.

Fix a field $\mathbb{F}$ and work in $\mathbb{F}[x_1, \dots, x_n]$.
A refutation of polynomials $f_1, \dots, f_m$, such as the translation of a CNF in the Notation below, shows that they have no common $0$-$1$ zero.
The *Boolean axioms* are the polynomials $x_j^2 - x_j$ for $j = 1, \dots, n$, whose common zeros in $\mathbb{F}^n$ are the $0$-$1$ points.

### Nullstellensatz

A *Nullstellensatz refutation* of $f_1, \dots, f_m$ is a list of polynomials $g_1, \dots, g_m, h_1, \dots, h_n$ such that
$$\sum_{i=1}^m g_i f_i + \sum_{j=1}^n h_j \, (x_j^2 - x_j) = 1$$
holds as a polynomial identity.
Its *degree* is the largest degree of the products $g_i f_i$ and $h_j (x_j^2 - x_j)$.
Its *size* is the total number of monomials of these products.

### Polynomial calculus

A *polynomial calculus derivation* from $f_1, \dots, f_m$ is a sequence of polynomials, the *lines*, each obtained in one of three ways.

1. **Axiom.** It is one of $f_1, \dots, f_m$ or a Boolean axiom.
2. **Linear combination.** It is $a f + b g$ for earlier lines $f, g$ and $a, b \in \mathbb{F}$.
3. **Multiplication.** It is $x_j f$ for an earlier line $f$ and a variable $x_j$.

A *polynomial calculus refutation* is a derivation whose last line is the constant polynomial $1$.
Its *degree* is the largest degree of a line, its *size* is the total number of monomials, and its *length* is the number of lines.

## Notation

A [[clause|T3SXVH3ZZC]] $C$ with positive literals $C^+$ and negative literals $C^-$ translates to the polynomial
$$P_C = \prod_{x \in C^+} (1 - x) \cdot \prod_{\neg x \in C^-} x.$$
At a $0$-$1$ point, $P_C$ vanishes exactly when some factor does, that is, when the point satisfies $C$.
A [[CNF formula|0B3D4C8YF2]] $F$ translates to the set of the $P_C$ for its clauses.

We write NS for the Nullstellensatz system, PC for polynomial calculus and SOS for sum of squares.
Many authors use the opposite convention, with $0$ for true, and then the translation of $x$ is $x$ instead of $1 - x$.
PCR is the variant of PC with a second variable $\bar x_j$ for each $x_j$ and the axioms $x_j + \bar x_j - 1$, so that every clause translates to a single monomial.
The Positivstellensatz system is the general form of SOS, in which the certificate may use products of the inequalities of the problem, as in the [[Positivstellensatz|FN734RQYM6]].

## Remarks

### Sum of squares, the third system

The third algebraic system works over $\mathbb{F} = \mathbb{R}$.
A *sum-of-squares refutation* of $f_1, \dots, f_m$ is a list $g_1, \dots, g_m, h_1, \dots, h_n$ together with polynomials $s_1, \dots, s_t$ such that
$$\sum_{i=1}^m g_i f_i + \sum_{j=1}^n h_j \, (x_j^2 - x_j) + \sum_{l=1}^t s_l^2 = -1$$
holds as a polynomial identity.
Its degree is the largest degree of the terms $g_i f_i$, $h_j (x_j^2 - x_j)$ and $s_l^2$.

### Soundness

All three systems are sound.
At a common $0$-$1$ zero of $f_1, \dots, f_m$, every line of a PC derivation vanishes, by induction on the lines, and $1$ does not vanish.
For NS, the left side of the identity vanishes at such a point, and the right side is $1$.
For SOS over $\mathbb{R}$, the left side is at least $0$ at such a point, and the right side is $-1$.

### Completeness

NS, and hence PC, is complete for unsatisfiable CNFs.
Let $F$ be unsatisfiable, and for each $a \in \{0,1\}^n$ choose a clause $C_a$ of $F$ that $a$ falsifies.
Let $\delta_a = \prod_{a_j = 1} x_j \prod_{a_j = 0} (1 - x_j)$, so that $\sum_a \delta_a = \prod_j (x_j + (1 - x_j)) = 1$.
Since $P_{C_a}(a) = 1$, the polynomials $\delta_a P_{C_a}$ and $\delta_a$ have the same value at every $0$-$1$ point.
So their difference vanishes on $\{0,1\}^n$ and has degree at most $2n$.
A polynomial $g$ that vanishes on $\{0,1\}^n$ is a sum $\sum_j h_j (x_j^2 - x_j)$ with terms of degree at most $\deg g$.
To see this, replace $x_j^2$ by $x_j$ step by step, where each step subtracts a term $m (x_j^2 - x_j)$.
The multilinear result vanishes on $\{0,1\}^n$, so it is $0$.
Summing over $a$ gives a Nullstellensatz refutation of degree at most $2n$.
[[Hilbert's Nullstellensatz|D85VZWS9QK]] gives the general form: polynomials over an algebraically closed field have no common zero exactly when $1$ is in the ideal they generate.

### Simulations

PC simulates NS in degree.
A term $c \, m f_i$ of an NS refutation of degree $d$, with a monomial $m$, is derived from $f_i$ by multiplying by the variables of $m$ one at a time, and every intermediate line has degree at most $d$.
A final linear combination gives $1$.
PC simulates resolution in degree.
From $P_C (1 - x)$ and $P_D \, x$, multiplication by the missing factors and linear combination give $P_E (1 - x)$ and $P_E \, x$ for $E = C \cup D$, and their sum is $P_E$.
So a resolution refutation of width $w$ gives a PC refutation of degree at most $w + 1$.
The size can grow, since $P_E$ can have $2^{\lvert E \rvert}$ monomials.
SOS simulates NS in degree, since an NS refutation multiplied by $-1$ is an SOS refutation with no squares.
If $f_1, \dots, f_m$ have no common real zero, then part 1 of the [[Positivstellensatz|FN734RQYM6]], applied to $f_i \geq 0$ and $-f_i \geq 0$, gives an SOS certificate.

### Search in bounded degree

Clegg, Edmonds and Impagliazzo showed in 1996 that a PC refutation of degree $d$ in $n$ variables, if one exists, can be found in time $n^{O(d)}$.
The algorithm is a version of the [[Gröbner basis|C83KPT47R0]] algorithm that keeps only polynomials of degree at most $d$.
This is the algebraic analogue of the width-based search for resolution, and it is a form of [[automatizability|WBECDG163W]] in degree.

### Lower bounds by duality

A degree lower bound for NS comes from a linear functional.
Let $V_d$ be the vector space of polynomials of degree at most $d$, and let $\Lambda \colon V_d \to \mathbb{F}$ be linear.
Assume that $\Lambda(1) = 1$, and that $\Lambda(m f) = 0$ for every axiom $f$, Boolean axioms included, and every monomial $m$ with $\deg(m f) \leq d$.
Then $f_1, \dots, f_m$ have no NS refutation of degree at most $d$.

1. Assume that $\sum_i g_i f_i + \sum_j h_j (x_j^2 - x_j) = 1$ is a refutation of degree at most $d$, and write each $g_i$ as a sum $\sum_m c_{i,m} m$ of monomials.
2. Over a field, $\deg(g f) = \deg g + \deg f$ for non-zero $g$ and $f$.
   So each monomial $m$ of $g_i$ has $\deg(m f_i) \leq \deg(g_i f_i) \leq d$, and the same holds for the $h_j$.
3. Apply $\Lambda$ to the identity.
   By linearity, the left side becomes a sum of terms $c_{i,m} \Lambda(m f_i)$ and similar terms for the $h_j$, and each term is $0$.
4. The right side gives $\Lambda(1) = 1$, and $0 \neq 1$ is a contradiction.

Such a $\Lambda$ is called a *design* in the literature on NS lower bounds.

### Lower bounds for pigeonhole formulas

Beame, Impagliazzo, Krajíček, Pitassi and Pudlák introduced the Nullstellensatz system and proved degree lower bounds for it.
Clegg, Edmonds and Impagliazzo introduced polynomial calculus in 1996.
Razborov proved in 1998 that, over every field and for every $m > n$, every PC refutation of $\mathrm{PHP}^m_n$ has degree at least $n/2 + 1$.
Here the pigeon axioms are $1 - \sum_{j} x_{ij}$ and the hole axioms are $x_{ij} x_{kj}$.

### Size from degree

Impagliazzo, Pudlák and Sgall proved a size-degree relation for PC.
If polynomials of degree at most $d_0$ in $n$ variables have a PC refutation of size $S$, then they have one of degree $O(d_0 + \sqrt{n \log S})$.
So there is a constant $c$ such that, if every refutation has degree at least $d$, then every refutation has size $\exp(\Omega((d - c d_0)^2 / n))$.

### Tseitin formulas

Over a field of characteristic other than $2$, the [[Tseitin formulas|JXTCC6KXNG]] of suitable bounded-degree expanders need PC degree linear in the number $n$ of variables.
This is a theorem of Buss, Grigoriev, Impagliazzo and Pitassi from 2001.
By the size-degree relation, with $d_0$ bounded by the degree of the graph, they then need PC size $\exp(\Omega(n))$.
Over $\mathbb{F}_2$ the same formulas are easy.
The constraint of a vertex $v$ with charge $\chi(v)$ is the linear polynomial $\sum_{e \ni v} x_e + \chi(v)$, which PC derives from the clauses of $v$ in a degree that depends only on the degree of the graph.
Every edge lies on two vertices, so the sum of these polynomials over all $v$ is $\sum_v \chi(v)$, which is $1$ because the total charge is odd.

### Examples on separate pages

- [[A Nullstellensatz refutation of three clauses|GKWHNGBQXZ]], of degree $2$.
- [[A polynomial calculus refutation for two pigeons and one hole|S8FKECAJEA]], of degree $2$.
- [[An identity on the Boolean cube that is not a certificate|PSNXBQGWYB]], which shows why the Boolean axioms are part of the system.

### Watch out

Every bound in these systems names a measure, and the measures behave differently.
A degree lower bound gives a size lower bound only through the size-degree relation, which needs the initial degree $d_0$ to be small.
A lower bound for NS is weaker than one for PC, since PC simulates NS in degree.

## Explanations

### L1 human

Write "true" as $1$ and "false" as $0$, and turn each clause into a polynomial that is $0$ exactly when the clause is true.
If all clauses are true, all these polynomials are $0$.
An algebraic proof combines the polynomials, multiplying them by other polynomials and adding, until it reaches the constant $1$.
Since a combination of zeros is zero, and $1$ is not zero, the clauses cannot all be true.

### L2 human

We refute the clauses $x \vee y$, $\neg x$ and $\neg y$ with Nullstellensatz.

1. The polynomials are $(1 - x)(1 - y)$, $x$ and $y$.
2. The certificate is $(1 - x)(1 - y) + (1 - y) \cdot x + 1 \cdot y$.
3. Expand: $1 - x - y + xy + x - xy + y = 1$.
4. The degree is $2$, since $(1 - x)(1 - y)$ and $(1 - y) x$ have degree $2$.

The typical use of these systems is to measure degree: a lower bound on the degree often gives a lower bound on the size, by the size-degree relation.
A trap is to forget the Boolean axioms: an identity that holds only at $0$-$1$ points is not a certificate unless the Boolean axioms appear in it.

### L3 human

Algebraic proof systems connect proof complexity with commutative algebra.
An NS refutation of degree $d$ is a witness that $1$ lies in the ideal of the axioms with a representation of degree $d$, and PC of degree $d$ is close to the Gröbner basis algorithm restricted to degree $d$.
SOS adds real positivity, through sums of squares, and its refutations of bounded degree are dual to the relaxations of the hierarchy of [[sum-of-squares optimization|AM0BYNK5YJ]].
The field matters: parity is easy over $\mathbb{F}_2$ and hard over other fields, while the pigeonhole principle is hard in degree over every field.
A lower bound for these systems says nothing about [[Frege systems|J2BAR09TPF]], and the [[cutting-planes system|KKCX2HQP2K]] refutes the pigeonhole formulas in polynomial size.
