# Assumptions for Tasks 2–20

This document summarizes the assumptions encoded in the code for Tasks 2–20.
“Base” means the original task program, “modified” means the parameter-variation
program, and “real-world” means the applied example program.

## Task 2: NumPy Arrays and Numerical Computation

- **Base:**
  - The data represents 24 hourly temperature readings for one day.
  - The readings are stored in degrees Celsius.
  - Mean, minimum, and maximum are calculated across the complete array.
- **Modified parameter:**
  - Every original reading is increased by 5 degrees Celsius.
  - The temperature pattern and other calculations remain unchanged.
- **Real-world case:**
  - One cabinet-temperature reading is available per hour, from 00:00.
  - Readings are in degrees Celsius.
  - The alarm threshold is 30 degrees Celsius, chosen for the exercise.
  - The readings are sample data, not real ESP32/DHT22 measurements.

## Task 3: Mathematical Functions and Vectorization

- **Base:**
  - Latency values are simulated uniformly between 5 and 250 ms.
  - One million readings are generated.
  - Seed 42 is used to make random generation reproducible.
  - Timing results vary with the computer and runtime environment.
- **Modified parameter:**
  - The sample size changes from one million to 100,000 readings.
  - The uniform range and random seed remain unchanged.
- **Real-world case:**
  - The sensor signal is a 50 Hz sine wave with amplitude 1.5 V.
  - The signal is centred at 1.65 V.
  - The sampling rate is 100,000 samples per second for 10 seconds.
  - Independent Gaussian noise with standard deviation 0.05 V is added.
  - The signal is simulated rather than measured from a real sensor.

## Task 4: Floating-Point Arithmetic and Numerical Errors

- **Base:**
  - Decimal values such as 0.1, 0.2, and 0.3 are represented using binary floating-point arithmetic.
  - Small values in floating-point expressions may be affected by rounding and cancellation.
  - The stable formula is assumed to avoid the accuracy loss in the direct formula.
- **Modified parameter:**
  - The approximation of square root 2 improves from 1.414 to 1.41421.
  - An additional test value of 10^-16 is included.
- **Real-world case:**
  - The timer ticks every 0.1 s for exactly 1,000,000 ticks.
  - The exact elapsed time is 100,000 s.
  - Float64, float32, and integer tick-count methods are compared.
  - No real microcontroller is used; the behavior is simulated.

## Task 5: Matrix Algebra and Matrix Operations

- **Base:**
  - The object is a unit square in the x-y plane.
  - The rotation is 45 degrees counter-clockwise.
  - Scaling is 2.0 along x and 1.5 along y.
  - Points are stored as row vectors.
- **Modified parameter:**
  - The rotation angle changes to 90 degrees.
  - Scaling and the original square remain unchanged.
- **Real-world case:**
  - The accelerometer is rotated only around the vertical axis.
  - Its x-y axes are twisted 30 degrees counter-clockwise relative to the robot axes.
  - Sensor readings are accelerations in the sensor coordinate system.
  - The readings and mounting offset are invented for the exercise.

## Task 6: Solution of Systems of Linear Equations

- **Base:**
  - Type A servers use 4 CPU units and 8 GB memory per server.
  - Type B servers use 2 CPU units and 12 GB memory per server.
  - Observed totals are exactly 20 CPU units and 72 GB.
  - Server counts are real-valued solutions unless otherwise indicated.
- **Modified parameter:**
  - Server resource usage remains unchanged.
  - Observed totals change to 26 CPU units and 92 GB memory.
- **Real-world case:**
  - Resistors and voltage sources are ideal.
  - The circuit operates in steady DC.
  - R1, R2, and R3 are 10 ohms.
  - Source voltages are 12 V and 6 V.
  - Both mesh currents are defined as clockwise.

## Task 7: Gaussian Elimination and LU Decomposition

- **Base:**
  - Matrix A is fixed and invertible.
  - One LU factorization is reused for several right-hand-side vectors.
  - Direct solving is used as a reference check.
- **Modified parameter:**
  - The bottom-right coefficient of A changes from 3 to 6.
  - Other matrix coefficients and right-hand-side vectors remain unchanged.
- **Real-world case:**
  - Resistors are ideal and the network operates in steady DC.
  - Three nodes form a linear network with fixed ground and inter-node resistors.
  - The conductance matrix remains constant.
  - Only injected currents change between time steps.
  - Current vectors are invented exercise values.

## Task 8: Iterative Methods for Linear Systems

- **Base:**
  - The system represents steady-state temperature distribution.
  - Each interior temperature is the average of its immediate neighbors.
  - Zero is the initial temperature guess.
  - Convergence stops when the largest update is below 10^-8.
- **Modified parameter:**
  - The stopping tolerance changes from 10^-8 to 10^-3.
  - The grid and boundary conditions remain unchanged.
- **Real-world case:**
  - Heat flow is one-dimensional and in steady state.
  - The strip has no sideways heat loss and no internal heat generation.
  - The strip is divided into 20 equally spaced interior points.
  - The chip end is fixed at 85 degrees Celsius.
  - The connector end is fixed at 25 degrees Celsius.
  - The boundary values and grid are chosen for the exercise.

## Task 9: Eigenvalues and Eigenvectors

- **Base:**
  - The network is undirected.
  - The adjacency matrix is symmetric and unweighted.
  - Eigenvector centrality is calculated from the dominant eigenvector.
- **Modified parameter:**
  - An additional undirected link is added between nodes A and D.
  - The new link has weight 1, consistent with the original adjacency matrix.
- **Real-world case:**
  - Radio links are two-way and equally weighted.
  - C1, C2, and C3 form a tightly linked core.
  - C1 also links to H.
  - H links to leaves L1 and L2.
  - The leaf nodes have no links other than to H.
  - The network is synthetic rather than a real deployment.

## Task 10: Root Finding - Bisection and Fixed-Point

- **Base:**
  - The heat-balance equation contains the relevant root between 20 and 40 degrees Celsius.
  - The fixed-point iteration starts at 30 degrees Celsius.
- **Modified parameter:**
  - The heat-gain coefficient doubles from 10 to 20.
  - The temperature bracket and tolerance remain unchanged.
- **Real-world case:**
  - The silicon diode follows the ideal Shockley model.
  - Supply voltage is 5 V.
  - Series resistance is 1000 ohms.
  - Saturation current is 10^-12 A.
  - Ideality factor is 1.
  - Thermal voltage is 0.02585 V, corresponding to approximately 300 K.
  - Parasitic resistance, diode degradation, and temperature variation are ignored.

## Task 11: Root Finding - Newton-Raphson and Secant

- **Base:**
  - Cash flows occur once per year at exact annual intervals.
  - Discounting uses (1 + r)^t.
  - Newton-Raphson starts at 10%.
  - The secant method starts at 5% and 20%.
- **Modified parameter:**
  - One or more cash-flow parameters are changed.
  - The same root-finding assumptions remain in effect.
- **Real-world case:**
  - The ADC is 10-bit, so counts range from 0 to 1023.
  - The fixed resistor is 10 kOhms.
  - The assumed ADC reading is 384.
  - The thermistor uses a beta equation with R0 = 10 kOhms.
  - T0 is 298.15 K, and beta is 3950 K.
  - ADC and resistance measurements are assumed to contain no noise.

## Task 12: Polynomial and Nonlinear Equation Solving

- **Base:**
  - The system is defined by a circle of radius 2 and the parabola y = x^2 - 1.
  - Initial guesses of (1, 1) and (-1, 1) select the two symmetric solutions.
- **Modified parameter:**
  - The circle radius changes from 2 to 3.
  - The parabola and initial guesses remain unchanged.
- **Real-world case:**
  - Two receivers are at exact positions (0, 0) and (10, 0).
  - Assumed distances are 5 m and square root 45 m.
  - The node position is the intersection of two exact circles.
  - Distance-measurement noise and multipath effects are ignored.

## Task 13: Interpolation

- **Base:**
  - Temperature varies continuously between measured hourly values.
  - Linear interpolation assumes a straight line between neighboring points.
  - Cubic interpolation is valid over the full time interval.
  - The target time lies inside the interpolation range.
- **Modified parameter:**
  - The modified dataset replaces the original measurements or target.
- **Real-world case:**
  - ADC counts 100–900 are paired with exact simulated calibration temperatures.
  - Interpolation stays within the lookup-table range.
  - ADC values and calibration temperatures are noise-free.

## Task 14: Curve Fitting and Approximation

- **Base:**
  - The response-time relationship is assumed to be quadratic.
  - Least squares is used to estimate coefficients.
  - RMSE measures closeness of fit.
  - Predicted 400-user performance is extrapolated outside the exact measured range.
- **Modified parameter:**
  - The modified dataset or model parameters replace the original values.
- **Real-world case:**
  - Sensor voltage follows V = 500 + 10T, with random noise of approximately 5 mV.
  - A straight-line calibration model is assumed.
  - Eight temperatures are evenly spaced from 0 to 70 degrees Celsius.
  - The calibration data are simulated.

## Task 15: Numerical Differentiation

- **Base:**
  - Position measurements are accurate.
  - Time samples are equally spaced.
  - Forward differences are used at the beginning.
  - Central differences are used in the middle.
  - Backward differences are used at the end.
- **Modified parameter:**
  - The modified position or time data replace the original data.
- **Real-world case:**
  - An encoder provides 20 counts per wheel revolution.
  - The wheel circumference is 0.20 m per revolution.
  - Encoder counts map directly and exactly to position.
  - Time samples are 0.1 s apart.
  - Noise and encoder quantization timing effects are ignored.

## Task 16: Numerical Integration

- **Base:**
  - Power readings are equally spaced every two hours.
  - The trapezoidal rule assumes linear changes between readings.
  - Simpson's rule assumes local quadratic changes.
- **Modified parameter:**
  - The modified readings or integration interval replace the original values.
- **Real-world case:**
  - The current readings describe one repeating sensor duty cycle.
  - Nine readings are spaced exactly one second apart.
  - The battery capacity is assumed to be 1000 mAh.
  - The same duty cycle repeats indefinitely.
  - Current is assumed constant between sampled readings.

## Task 17: Ordinary Differential Equations - Euler Method

- **Base:**
  - Newton cooling is assumed.
  - Ambient temperature is 25 degrees Celsius.
  - Initial object temperature is 90 degrees Celsius.
  - The cooling coefficient is 0.12 per minute.
  - Euler integration uses a one-minute step.
- **Modified parameter:**
  - One or more of the cooling coefficient, initial value, step size, or final time changes.
- **Real-world case:**
  - The chip is modeled as a lumped thermal object.
  - Thermal resistance is 40 K/W.
  - Heat capacity is 2 J/K.
  - The chip dissipates 0.5 W continuously.
  - The chip starts at ambient temperature.
  - No heat source other than chip dissipation is modeled.

## Task 18: Numerical Solution of ODEs Using SciPy

- **Base:**
  - The circuit is a fixed-source RC charging circuit.
  - The source voltage is 5 V.
  - The capacitor starts at 0 V.
  - The time constant RC is 1 s.
- **Modified parameter:**
  - Component values or the simulation interval change.
- **Real-world case:**
  - The supercapacitor starts at 5 V.
  - The load resistance is 1000 ohms.
  - Capacitance is 0.1 F.
  - The node brown-out voltage is 3.3 V.
  - Discharge follows an ideal exponential.
  - Leakage resistance and supercapacitor ESR are ignored.

## Task 19: Numerical Optimization

- **Base:**
  - Cost and capacity are linear functions of server allocations.
  - Allocations are nonnegative.
  - Required capacity is at least 1000 units.
- **Modified parameter:**
  - The modified costs, capacities, or constraints replace the base values.
- **Real-world case:**
  - Type A nodes cover 40 m^2 and cost 15 per node.
  - Type B nodes cover 90 m^2 and cost 28 per node.
  - At least 1000 m^2 of coverage is required.
  - Continuous allocation is solved first.
  - Whole-node combinations are checked afterward.
  - Coverage, cost, and integer-node requirements are assumed exactly as stated.

## Task 20: Random Numbers and Monte Carlo Methods

- **Base:**
  - Daily demand follows a normal distribution.
  - Mean demand is 850 units.
  - Demand standard deviation is 120 units.
  - Capacity is 1000 units.
  - 100,000 independent scenarios are generated.
  - Seed 42 makes the simulation reproducible.
- **Modified parameter:**
  - The capacity, demand distribution, trial count, or seed changes.
- **Real-world case:**
  - Ten sensors operate independently.
  - Each sensor works with probability 0.95.
  - A day is degraded when fewer than nine sensors work.
  - 100,000 independent days are simulated.
  - Working status is independent across sensors and across days.
  - The 95% success probability is assumed and is not based on field measurements.
