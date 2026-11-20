# BIT 2118 Scientific Computing: Tasks 2 to 20

For each task:
- **B** = input values and the mathematical operation performed.
- **D** = meaning of the output in words (and the graph, where there is one).

All outputs are from the original (PDF) programs. Timing results (Task 3) differ on every computer. Simulated data are marked as such.

---

## Task 2: NumPy Arrays and Numerical Computation

**B. Inputs and operation**
- Input: 24 hourly temperatures in °C. Constants 1.8 and 32.
- Mean = (sum of 24 readings) ÷ 24.
- Minimum and maximum of the array.
- Conversion F = 1.8C + 32 applied to the whole array at once.

**D. Output meaning**
- Daily mean is 23.12 °C.
- Coldest reading is 17.50 °C and hottest is 29.40 °C. The spread is 11.9 °C.
- First six Fahrenheit values are 65.3, 64.4, 64.04, 63.5, 64.22, 66.2. They are the early-morning hours on the °F scale (18.5 °C becomes 65.3 °F).
- The day is cool at night, warm by midday, then cooler again.

---

## Task 3: Mathematical Functions and Vectorization

**B. Inputs and operation**
- Input: 1,000,000 simulated latencies between 5 and 250 ms (seed 42).
- Operation: divide by 1000 (ms to s), then square.
- Done twice: with a Python loop and with a vectorized NumPy expression. Both are timed.

**D. Output meaning**
- First squared value 0.03787665 comes from about 0.1946 s (0.1946² ≈ 0.0379). It is inside the expected range (the maximum possible is 0.25² = 0.0625).
- Example run: loop 0.1366 s, vectorized 0.0031 s, speed-up about 43.6x. Your numbers will differ.
- Both give the same values. The vectorized version is faster because NumPy repeats the operation in compiled code.

---

## Task 4: Floating-Point Arithmetic and Numerical Errors

**B. Inputs and operation**
- Input: 0.1, 0.2, 0.3. The true √2 and the approximation 1.414. Values x = 10⁻⁴, 10⁻⁸, 10⁻¹².
- Operations: addition and comparison. Absolute error |true − approx|. Relative error = absolute error ÷ |true|. Two algebraically equal formulas for (√(1+x) − 1)/x.

**D. Output meaning**
- 0.1 + 0.2 = 0.30000000000000004, so `==` gives False. It is wrong only by about 4×10⁻¹⁷.
- `np.isclose` gives True. Use a tolerance, never `==`, for decimals.
- Absolute error of 1.414 is 0.00021356. Relative error is 0.0151%.
- The "direct" formula loses accuracy as x shrinks (0.500044 at x = 10⁻¹²). The "stable" formula stays at 0.5.
- The cause is cancellation: √(1+x) is almost 1, so subtracting 1 wipes out digits.

---

## Task 5: Matrix Algebra and Matrix Operations

**B. Inputs and operation**
- Input: four corners of a unit square, a 45° rotation, scale factors 2.0 (x) and 1.5 (y).
- Operations: build rotation and scaling matrices. Multiply them (`rotation @ scale`). Multiply every point by the result. Compute the determinant.

**D. Output meaning**
- The point (0, 0) stays at the origin.
- (1, 0) moves to (1.414, 1.414): stretched to length 2, then turned 45°.
- The square becomes a 2 by 1.5 rectangle tilted 45° counter-clockwise.
- Determinant ≈ 3 (printed 2.9999999999999996 because of round-off). Area becomes 3 times larger (2 × 1.5). Rotation does not change area.

---

## Task 6: Solution of Systems of Linear Equations

**B. Inputs and operation**
- Input: A = [[4, 2], [8, 12]] (CPU and memory used per server) and b = [20, 72] (totals).
- Operation: solve Ax = b with `np.linalg.solve`, then check with A @ x and the residual b − A @ x.

**D. Output meaning**
- 3 Type A servers and 4 Type B servers.
- Check: 4(3) + 2(4) = 20 CPU and 8(3) + 12(4) = 72 GB.
- A @ x reproduces [20, 72]. The residual is 0, so the answer fits both equations.

---

## Task 7: Gaussian Elimination and LU Decomposition

**B. Inputs and operation**
- Input: a 3×3 matrix A and three different vectors b.
- Operation: factor A = LU once (`lu_factor`). Reuse it for each b (`lu_solve`). Check the residual b − A @ x. Compare with `np.linalg.solve`.

**D. Output meaning**
- Set 1 gives [5, 5, 5]. Set 2 gives [5.317, 5.268, 4.756]. Set 3 gives [4.902, 5.610, 5.537].
- Residual norms are 0 or about 10⁻¹⁵, which is round-off, so the answers are accurate.
- The LU answer matches the direct solver.
- Advantage: factor once, then each new b is cheap.

---

## Task 8: Iterative Methods for Linear Systems

**B. Inputs and operation**
- Input: 5×5 matrix A (each point is the average of its neighbours). b = [100, 0, 0, 0, 20] (boundary temperatures). Start guess of zeros. Tolerance 10⁻⁸.
- Operation: Jacobi and Gauss-Seidel updates, repeated until the largest change is below the tolerance. Direct solution for comparison.

**D. Output meaning**
- Temperatures: 86.67, 73.33, 60.00, 46.67, 33.33 °C. They fall in a straight line from 100 °C to 20 °C.
- Both methods are within about 3×10⁻⁸ °C of the direct answer. They stop early because of the tolerance.
- Iterations: Jacobi 150, Gauss-Seidel 75.
- **Graph** (maximum change vs iteration, log vertical axis):
  - Both curves are nearly straight lines going down, so the error shrinks by a steady factor each step.
  - The Gauss-Seidel line is steeper, so it needs about half the iterations.

---

## Task 9: Eigenvalues and Eigenvectors

**B. Inputs and operation**
- Input: 4×4 adjacency matrix of a network with nodes A, B, C, D. B and C connect to every other node. A and D are not connected to each other.
- Operation: compute eigenvalues and eigenvectors (`np.linalg.eig`). Pick the largest eigenvalue. Normalise its eigenvector so it sums to 1. Verify Av = λv.

**D. Output meaning**
- Dominant eigenvalue is 2.5616, which equals (1 + √17)/2.
- Importance scores: A 0.2192, B 0.2808, C 0.2808, D 0.2192.
- B and C are the most influential nodes because they have the most connections. A and D are equal by symmetry.
- Verification error is about 10⁻¹⁵, so Av = λv holds.

---

## Task 10: Root Finding: Bisection and Fixed-Point

**B. Inputs and operation**
- Input: f(T) = T − 25 − 10e^(−T/20). Bracket [20, 40]. Tolerance 10⁻¹⁰. Fixed-point start T₀ = 30.
- Operations: bisection (halve the interval that keeps the sign change). Fixed-point iteration Tₙ₊₁ = 25 + 10e^(−Tₙ/20).

**D. Output meaning**
- Both methods give an equilibrium temperature of 27.525211 °C, where heat gain equals heat loss.
- Fixed-point needed 13 iterations. Bisection needs about 38 halvings.
- **Graph** (f(T) against temperature, 20 to 40 °C):
  - The curve rises from about −8.7 to about +13.6.
  - It crosses zero at about 27.53 °C (the dashed vertical line).
  - Below that temperature f is negative. Above it, f is positive.

---

## Task 11: Root Finding: Newton-Raphson and Secant

**B. Inputs and operation**
- Input: cash flows [−10000, 3000, 3500, 4000, 2500]. Newton start 0.10. Secant starts 0.05 and 0.20.
- Operation: find the rate r where NPV(r) = Σ CFₜ/(1+r)ᵗ = 0. Newton uses the derivative. Secant uses two points.

**D. Output meaning**
- Both give an IRR of 11.542461%.
- At this rate the discounted inflows exactly repay the 10,000 investment.
- NPV at the solution is 0.000000, which confirms the root.
- If the cost of borrowing is below 11.54%, the project is worthwhile.

---

## Task 12: Polynomial and Nonlinear Equation Solving

**B. Inputs and operation**
- Input: circle x² + y² = 4 and parabola y = x² − 1. Starting guesses (1, 1) and (−1, 1).
- Operation: solve the two nonlinear equations together with `scipy.optimize.root`, so that both residuals are near 0.

**D. Output meaning**
- The curves cross at two points: (1.5175, 1.3028) and (−1.5175, 1.3028).
- The points are mirror images because both curves are symmetric about the y-axis.
- Residuals are about 10⁻¹³ (effectively 0). `Converged: True`.
- Each starting guess found the intersection on its own side.

---

## Task 13: Interpolation

**B. Inputs and operation**
- Input: temperatures at hours 8 to 14: [18, 20, 22.5, 24, 25, 25.5, 25]. Target time 10:30. Estimates every 10 minutes.
- Operations: linear interpolation (straight line between neighbours) and cubic spline (smooth cubic curves).

**D. Output meaning**
- At 10:30 the linear estimate is 23.25 °C (the average of 22.5 and 24).
- The cubic estimate is 23.36 °C. It is slightly higher because the spline follows the curve of the data.
- Both estimates are close, so the temperature is rising smoothly.
- **Graph** (temperature against hour):
  - The dots are the hourly measurements.
  - The linear line is made of straight segments with corners at each dot.
  - The cubic line is smooth. Both pass through every dot.
  - Temperature rises quickly in the morning and levels off near 25 °C.

---

## Task 14: Curve Fitting and Approximation

**B. Inputs and operation**
- Input: users [50, 100, ..., 350] and response times [82, 95, 115, 145, 185, 238, 305] ms.
- Operation: least-squares fit of y = ax² + bx + c with `curve_fit` (minimise the sum of squared residuals). Compute RMSE. Predict at 400 users.

**D. Output meaning**
- Fitted model: y = 0.002167x² − 0.1345x + 85.00.
- RMSE is 1.55 ms, so the curve follows the data closely.
- Predicted response at 400 users is about 377.86 ms. This is extrapolation, so treat it with care.
- **Graph** (response time against users):
  - The dots rise slowly at first, then more steeply.
  - The fitted curve passes very close to every dot and continues up to 400 users.
  - The server slows down faster as load increases.

---

## Task 15: Numerical Differentiation

**B. Inputs and operation**
- Input: times 0 to 6 s and GPS positions [0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0] m.
- Operation: speed = change in position ÷ change in time. Forward difference at the start, central differences in the middle, backward difference at the end.

**D. Output meaning**
- Estimated speed rises from 4.80 m/s to 8.00 m/s, so the vehicle is speeding up.
- Middle values use both neighbours, so they are more accurate. The two end values use one side only.
- Example: at t = 3 s, (22.7 − 10.2) ÷ 2 = 6.25 m/s.
- **Graph** (speed against time):
  - A line with dots rising from about 4.8 to 8.0 m/s.
  - The slope is the acceleration, about 0.6 to 0.7 m/s² in the middle, and it levels off at the end.

---

## Task 16: Numerical Integration

**B. Inputs and operation**
- Input: smart-meter power readings [0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9] kW every 2 hours (0 to 12 h).
- Operation: energy = ∫ power dt (area under the curve) by the trapezoidal rule and by Simpson's rule.
- Note: `np.trapezoid` needs NumPy 2.0 or later. `scipy.integrate.trapezoid` works on every version.

**D. Output meaning**
- Energy used in 12 hours: 15.700 kWh (trapezoid) and 15.800 kWh (Simpson).
- The two differ by only 0.100 kWh, so the estimate is reliable.
- Average power is about 1.3 kW (15.7 ÷ 12).
- Simpson's rule is usually more accurate for smooth data because it fits parabolas.

---

## Task 17: ODEs: Euler Method

**B. Inputs and operation**
- Input: Tambient = 25 °C, T₀ = 90 °C, k = 0.12 per minute, step h = 1 minute, end time 30 minutes.
- Operation: Euler update Tₙ₊₁ = Tₙ + h·(−k(Tₙ − Tambient)). Compare with the exact solution T = 25 + 65e^(−0.12t).

**D. Output meaning**
- After 30 minutes Euler gives 26.40 °C and the exact answer is 26.78 °C. The error is 0.3720 °C.
- The object has almost cooled to room temperature.
- Euler is slightly low because it takes straight steps along a curve. A smaller h would reduce the error.
- **Graph** (temperature against time):
  - Both curves fall from 90 °C and flatten near 25 °C.
  - They drop fast at first, then slowly.
  - The Euler dots lie slightly below the exact line.

---

## Task 18: Numerical Solution of ODEs Using SciPy

**B. Inputs and operation**
- Input: Vs = 5 V, R = 1000 Ω, C = 0.001 F, V₀ = 0 V. Time span 0 to 5 s.
- Operation: solve dV/dt = (Vs − V)/(RC) with `solve_ivp` (adaptive step size). Compare with V = Vs(1 − e^(−t/RC)).

**D. Output meaning**
- The solver succeeded.
- The capacitor voltage at 5 s is 4.9663 V, almost the full 5 V supply.
- The maximum error against the exact curve is about 9×10⁻¹⁰ V, effectively zero.
- **Graph** (capacitor voltage against time):
  - The solid and dashed curves lie on top of each other.
  - The voltage rises quickly from 0 V, reaches about 63% (3.16 V) at 1 s (the time constant RC), then flattens near 5 V.

---

## Task 19: Numerical Optimization

**B. Inputs and operation**
- Input: cost per unit A = 12, B = 18. Capacity per unit A = 100, B = 170. Capacity must be at least 1000. Start [5, 3]. Both allocations ≥ 0.
- Operations: minimise cost 12x + 18y subject to 100x + 170y ≥ 1000 (`minimize`, SLSQP). A loop then tests whole-server combinations.

**D. Output meaning**
- Best plan: 0 Type A and 5.882 Type B. Capacity is exactly 1000 and the minimum cost is 105.88.
- Type B is cheaper per unit of capacity (18 ÷ 170 = 0.106 against 12 ÷ 100 = 0.12), so the solver uses only B.
- With whole servers, the best is 6 Type B: capacity 1020 and cost 108.

---

## Task 20: Random Numbers and Monte Carlo Methods

**B. Inputs and operation**
- Input: capacity 1000, mean demand 850, standard deviation 120, N = 100,000 scenarios, seed 42 (simulated data).
- Operation: draw random demands from a normal distribution. Mark those above capacity. Probability = overloaded count ÷ total.

**D. Output meaning**
- Estimated overload probability is 10.6160% (10,616 of 100,000 cases).
- Theory gives P(Z > 1.25) ≈ 10.56%, so the simulation agrees.
- About 1 day in 10 the server would be overloaded.
- **Graph** (estimated probability against number of simulations, log x-axis):
  - The curve jumps around when there are few simulations.
  - It settles near 0.106 as the number grows.
  - More simulations give a steadier answer.
