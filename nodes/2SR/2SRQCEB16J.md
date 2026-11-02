---
tag: 2SRQCEB16J
kind: statement
role: theorem
name: Ohsawa–Takegoshi extension theorem
msc: [32D15, 32W05, 32U05]
uses: [AHYZMSBBNH, FF2P7ER3QT, 507C34W0ZT]
about: [507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Ohsawa%E2%80%93Takegoshi_L2_extension_theorem
same_as:
  wikidata: Q25111495
  wikipedia: Ohsawa–Takegoshi L2 extension theorem
---

## Statement

Let $n \ge 2$ and let $\Omega \subseteq \C^n$ be a bounded [[pseudoconvex|AHYZMSBBNH]] open set.
Let $H = \set{z \in \C^n : z_n = 0}$, and let $\psi$ be a [[plurisubharmonic function|FF2P7ER3QT]] on $\Omega$.
Then there is a constant $C > 0$, depending only on the diameter of $\Omega$, with the following property.
For every holomorphic function $f$ on $\Omega \cap H$ with
$$\int_{\Omega \cap H} \abs{f}^2 e^{-\psi}\, d\lambda_{n-1} < \infty,$$
there is a [[holomorphic function|507C34W0ZT]] $F$ on $\Omega$ with $F = f$ on $\Omega \cap H$ and
$$\int_\Omega \abs{F}^2 e^{-\psi}\, d\lambda_n \le C \int_{\Omega \cap H} \abs{f}^2 e^{-\psi}\, d\lambda_{n-1}.$$
Here $\lambda_k$ denotes Lebesgue measure on $\C^k$, and $\Omega \cap H$ is viewed as an open subset of $\C^{n-1}$.

## Remarks

The point is that $C$ does not depend on $\psi$ or on $f$.
The proof solves a $\bar\partial$-equation with $L^2$ estimates for a weight that is singular along $H$, using a twisted form of the Bochner–Kodaira–Morrey–Kohn identity.
One extends $f$ smoothly with a cutoff in $z_n$ and corrects the extension by a solution $u$ of $\bar\partial u = g$ whose weight $e^{-\psi}/\abs{z_n}^2$ forces $u$ to vanish on $H$.
The sharp value of the constant was later found by Błocki and by Guan and Zhou, and it yields the Suita conjecture on the Bergman kernel of plane domains.
Example: take $\psi = 0$ and let $\Omega$ be the unit ball.
Then every holomorphic $f$ on the unit ball of $\C^{n-1}$ with $\int \abs{f}^2 < \infty$ extends to a square integrable holomorphic function on the unit ball of $\C^n$.
For the ball this is easy, because the trivial extension $F(z', z_n) = f(z')$ is defined on the ball and satisfies $\int_\Omega \abs{F}^2 \le \pi \int_{\Omega \cap H} \abs{f}^2$.
For a general $\Omega$ the point $(z', 0)$ need not lie in $\Omega$ when $(z', z_n)$ does, so the trivial extension is not defined on $\Omega$, and the theorem is needed.

## Explanations

### L1 human

Take a holomorphic function on a slice of a domain cut by a hyperplane.
The theorem says it extends to a holomorphic function on the whole domain, and the extension is not much bigger than the original function.
The size is measured by weighted square integrals, and the bound holds uniformly for all plurisubharmonic weights.

### L2 human

The theorem refines Cartan's theorem B, which gives an extension from a closed submanifold of a Stein manifold but without control of its size.
Because the constant is uniform in the weight, the theorem can be applied to singular weights such as $\psi = c \log \abs{g}$.
This makes it a key tool in the theory of multiplier ideals: it is used in Demailly's approximation of plurisubharmonic functions and in Siu's proof of the invariance of plurigenera.
