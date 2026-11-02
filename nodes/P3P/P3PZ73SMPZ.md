---
tag: P3PZ73SMPZ
kind: counterexample
name: Moments of the log-normal distribution
msc: [44A60, "60E05"]
uses: [4W40NHWPQT, 01XAHPADBA, 04YG690N5V, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Log-normal_distribution
---

## Counterexample

Let $f$ be the density of the standard [[log-normal distribution|4W40NHWPQT]]:
$$f(x) = \frac{1}{x \sqrt{2\pi}} \exp\left(-\frac{(\ln x)^2}{2}\right) \quad (x > 0), \qquad f(x) = 0 \quad (x \le 0).$$
Its [[moments|01XAHPADBA]] are $\int_0^\infty x^n f(x)\, dx = e^{n^2/2}$ for every integer $n \ge 0$.
For a real number $a$ with $-1 \le a \le 1$, put
$$f_a(x) = f(x)\bigl(1 + a \sin(2\pi \ln x)\bigr) \quad (x > 0), \qquad f_a(x) = 0 \quad (x \le 0).$$
Each $f_a$ is a [[probability density|04YG690N5V]], because $f_a \ge 0$ and it has the same total mass as $f$ by the computation below.
Check that $f_a$ has the same moments as $f$.
It suffices to show $\int_0^\infty x^n f(x) \sin(2\pi \ln x)\, dx = 0$ for every integer $n \ge 0$.
The substitution $x = e^y$ turns this integral into $\int_\R e^{ny} \varphi(y) \sin(2\pi y)\, dy$, where $\varphi(y) = e^{-y^2/2}/\sqrt{2\pi}$ is the [[standard normal|05AQE0QR0D]] density.
Since $e^{ny} \varphi(y) = e^{n^2/2} \varphi(y - n)$, the substitution $y = u + n$ gives
$$e^{n^2/2} \int_\R \varphi(u) \sin(2\pi u + 2\pi n)\, du = e^{n^2/2} \int_\R \varphi(u) \sin(2\pi u)\, du = 0,$$
because $n$ is an integer and the last integrand is odd.
So the densities $f_a$, $-1 \le a \le 1$, are pairwise different and all have the moments $e^{n^2/2}$.
Hence the moment problem for this moment sequence is not [[determinate|H0GY2J14CA]]: it is [[indeterminate|GCTN4BZ1ET]].

## Remarks

The log-normal law has all moments finite, yet its moments do not determine it.
The moments grow like $e^{n^2/2}$, so fast that [[Carleman's condition|RVZ831CNYW]] fails.
The normal distribution, whose moments grow much more slowly, is determined by its moments.

## Explanations

### L1 human

One might hope that knowing all the averages $E[X], E[X^2], E[X^3], \dots$ pins down a random quantity.
The log-normal law shows that this can fail.
Adding a small wiggle $a \sin(2\pi \ln x)$ to its density changes the shape, but every moment stays exactly the same.
The wiggles cancel out in each moment because, after taking logarithms, they become an odd function against a bell curve.
