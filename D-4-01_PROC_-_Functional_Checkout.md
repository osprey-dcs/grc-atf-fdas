# Functional Checkout

The purpose of this procedure is to verify the voltage response
of one or more FDAS channels by injecting a known time varying
signals, and comparing against expected responses.

Test input signals will be:

1. Square wave at full amplitude scale (+-10 V, 20Vpp)
2. Offset square wave at half scale (0 -> 10V)

See [Sample test record](sample-function-test-record.csv).

Note: The expected responses shown below were captured with a function generator
      connected directly to the Quartz.
      Added cabling of substantial length will effect the measured signal
      (cf. dispersion and cable impedance).

## Prerequisites

- Load CCCR configuring the channels to be verified to a voltage scale.  (no EGU, ESLO=1.0, ESLO=0.0)
- Successful completion of [D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md) PROC: Measurement Device Calibration for the channels to be checked.
- Successful completion of [Inspecting the Current State and Health](D-4-09_PROC_-_Inspecting_the_Current_State_and_Health.md) for the relevant chassis.
- As necessary, review [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md)
Monitoring a Data-Channel in Real Time.
- Location function generator (eg. Agilent 33220 Waveform generator)
- If relevant, locate test cable set as described in [D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md).

## Preparation

1. Set sample rate to 250Ksps and enable acquisition.  (see [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md))
1. Function generator
  1. Reset function generator to defaults
    - May exclude settings known not to effect output, eg. network address
  1. Ensure output is disabled
  1. Select square wave
 1. Set frequency to 100 KHz
 1. Ensure that sampling is enabled

## Per-Channel Verification

1. Connect function generator to desired channel
1. Monitor desired channel (see [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md)).
  1. Enable FFT if necessary
1. Measure full scale
  1. Disable output
  1. Set offset to zero volts
  1. Set amplitude +-10 V (20Vpp)
  1. Enable output
  1. Compare with [Figure 1]()
  1. Note pass/fail in Full Scale column
1. Measure DC offset
  1. Disable output
  1. Set amplitude +-5 V (10Vpp)
  1. Set offset to +5 V
  1. Enable output
  1. Compare with [Figure 2]()
  1. Note pass/fail in DC Offset column
1. Disable output
1. Disconnect function generator

## Expected Response

Figure 1. Full scale square wave

![Full scale]()

Figure 2. Offset square wave

![Offset]()
