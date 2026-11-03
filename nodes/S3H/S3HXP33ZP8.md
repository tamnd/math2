---
tag: S3HXP33ZP8
kind: statement
role: fact
name: Ginzburg criterion
msc: [82B27, 82B26]
uses: [XJ4NRM74W6, 1DGJYHG10E, ENWMTRJRND]
about: [1DGJYHG10E, XJ4NRM74W6]
sources:
  - url: https://en.wikipedia.org/wiki/Ginzburg_criterion
same_as:
  wikidata: Q5563311
  wikipedia: Ginzburg criterion
---

## Statement

Let $d \ge 1$, and consider a real order parameter field $m \colon \R^d \to \R$.
Its Landau–Ginzburg free energy is
$$\mathcal{F}[m] = \int_{\R^d} \Big( a t \, m(x)^2 + b \, m(x)^4 + c \, \abs{\nabla m(x)}^2 \Big) \, dx.$$
Here $a, b, c > 0$ are constants, $T_c > 0$ is the mean-field critical temperature and $t = (T - T_c)/T_c$.
Let $k_B$ be the Boltzmann constant and define the Ginzburg number $\mathrm{Gi}$ by
$$\mathrm{Gi}^{(4-d)/2} = \frac{k_B T_c \, b}{a^{2 - d/2} \, c^{d/2}} \quad (d \ne 4).$$
Let $m_0^2 = a \abs{t} / (2b)$ be the squared mean-field order parameter for $t < 0$.
In the Gaussian approximation, consider the mean square fluctuation of $m$ averaged over a correlation volume.
Its ratio to $m_0^2$ is of order $(\mathrm{Gi} / \abs{t})^{(4-d)/2}$, up to a factor that depends only on $d$.
Hence mean-field theory is self-consistent near $T_c$ exactly when this ratio is small:

1. if $d < 4$, it holds only for $\abs{t} \gg \mathrm{Gi}$ and fails as $t \to 0$;
2. if $d > 4$, the ratio tends to $0$ as $t \to 0$, and mean-field theory holds up to the critical point.

## Remarks

The idea: the mean-field correlation length is $\xi \sim (c / (a \abs{t}))^{1/2}$ and the susceptibility is $\chi \sim 1/(a \abs{t})$.
The integral of the [[correlation function|ENWMTRJRND]] over a ball of radius $\xi$ is of order $k_B T_c \chi$, so the fluctuation per unit volume there is about $k_B T_c \chi / \xi^d$.
Comparing it with $m_0^2 = a \abs{t} / (2b)$ gives the condition $k_B T_c b \ll a^{2 - d/2} c^{d/2} \abs{t}^{2 - d/2}$.
The borderline dimension $d = 4$ is the upper critical dimension of the Ising universality class, where mean-field exponents hold with logarithmic corrections.

Example: in conventional superconductors the coherence length is long, so $c$ is large and $\mathrm{Gi}$ is tiny.
So the mean-field Ginzburg–Landau theory works there except extremely close to $T_c$.

## Explanations

### L1 human

[[Mean-field theory|1DGJYHG10E]] ignores fluctuations: it treats the order parameter as if it were the same everywhere.
The Ginzburg criterion checks when this is safe, by comparing the size of the fluctuations with the size of the order itself.
In three dimensions the fluctuations always win close enough to the critical point.
How close depends on the material, and the Ginzburg number measures it.

### L2 human

The criterion is a self-consistency test of [[Landau theory|XJ4NRM74W6]] with a gradient term, done inside that theory.
It explains why mean-field exponents are wrong for the three-dimensional Ising model, but right above four dimensions.
The renormalization group later confirmed the picture: below four dimensions the Gaussian fixed point is unstable to the $m^4$ term, and above four dimensions this term is irrelevant.
In a temperature window $\abs{t} \gg \mathrm{Gi}$ one sees mean-field behaviour, and in the window $\abs{t} \ll \mathrm{Gi}$ one sees the true critical exponents.
