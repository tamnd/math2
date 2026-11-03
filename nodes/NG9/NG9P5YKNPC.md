---
tag: NG9P5YKNPC
kind: definition
name: Weighted automaton
msc: [68Q45, 16Y60]
defines: KBKTZ7XY1C
uses: [D31S3GR51T, RABRP2KG81, 1P6EP01HZF, SFMYM96C1B]
sources:
  - url: https://en.wikipedia.org/wiki/Weighted_automaton
---

## Definition

Let $(K, \oplus, \otimes, 0, 1)$ be a [[semiring|D31S3GR51T]] and let $\Sigma$ be an [[alphabet|RABRP2KG81]].
A *weighted automaton* over $K$ and $\Sigma$ is a tuple $A = (Q, \lambda, \mu, \gamma)$ where:

1. $Q$ is a finite set of states;
2. $\lambda \colon Q \to K$ gives the initial weights;
3. $\mu \colon \Sigma \to K^{Q \times Q}$ gives, for each letter $a$, a $Q \times Q$ matrix $\mu(a)$ of transition weights;
4. $\gamma \colon Q \to K$ gives the final weights.

Extend $\mu$ to [[strings|1P6EP01HZF]] by $\mu(a_1 \cdots a_n) = \mu(a_1) \cdots \mu(a_n)$, a product of matrices over $K$, with $\mu(\varepsilon)$ the identity matrix.
The *weight* of $w \in \Sigma^*$ is
$$f_A(w) = \bigoplus_{p, q \in Q} \lambda(p) \otimes \mu(w)_{p, q} \otimes \gamma(q).$$
The map $f_A \colon \Sigma^* \to K$ is a formal power series with coefficients in $K$ and noncommuting variables in $\Sigma$.

## Remarks

Equivalently, $f_A(w)$ is the sum over all paths labelled $w$ of the product of the initial weight, the transition weights and the final weight along the path.
Example: over the semiring $(\N, +, \cdot)$ with $\Sigma = \set{a, b}$, take $Q = \set{1, 2}$, $\lambda = (1, 0)$, $\gamma = (0, 1)$, $\mu(a) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $\mu(b)$ the identity matrix.
Since $\mu(a)^k = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$, the weight of $w$ is $\mu(w)_{1,2}$, the number of $a$'s in $w$.
Non-example: a device with infinitely many states, such as one that tracks the exact count of $a$'s minus $b$'s, fails clause 1.
Over the Boolean semiring $(\set{0, 1}, \lor, \land)$, a weighted automaton is an [[NFA|SFMYM96C1B]], possibly with several initial states, and its weight function is the indicator function of its language.
Commutativity of $\otimes$ is not required.
