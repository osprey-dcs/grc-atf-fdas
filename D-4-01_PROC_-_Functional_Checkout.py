#!/usr/bin/python3

print("""\
# FDAS System Functional Checkout

The purpose of this procedure is to bring the FDAS system
into a known functional state.

## Prerequisites

- Availability of a CCCR file configuring the channels to be verified to a voltage scale.  (no EGU, ESLO=1.0, ESLO=0.0)
- Locate function generator (eg. Agilent 33220 Waveform generator)
- Locate test cable set as described in [D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md).

## Preparation

Configuring function generator for AC response test

1. Function generator
  1. Reset function generator to defaults
    - May exclude settings known not to effect output, eg. network address
    - May use setting save/restore feature
  1. Ensure output is disabled
  1. Select sine wave
  1. Set offset to zero volts
  1. Set amplitude +-10 V (20 Vpp)
  1. Set frequency to 9 KHz
  1. Set output to high impedence (HighZ)

Note: Running [D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)
      will reconfigure the function generator.
      It is recommended to reset and setup, then save settings once,
      and thereafter restore settings following each calibration run.

## Expected Response

Figure 1. Chassis Scope screen showing expected response to 9 KHz sine wave.

![Expected response](image/quartz-250ksps-9khz-sine-20Vpp-full.png)

Figure 2. Chassis Scope zoomed in in both time and frequency.

![Expected response](image/quartz-250ksps-9khz-sine-20Vpp-zoom.png)

Essential frequency (FFT) response characteristics.

- Primary peak at 9 KHz
    - Amplitude of 5 V
    - Sharp peak <= 3 frequency points
- No other peaks above -80 dB relative (0.0005 V)

The important relationship is the relative size of the peak at 9 KHz to all other peaks,
which should be at least -80 dB less ($10^\\frac{-80}{20} = \\frac{1}{10000} = 0.0001$).

By default, the
[Chassis Scope](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md)
screen shows FFT on a log/log plot with base 10.

To simplify interpretation, adjust the FFT Plot scale so that
only peaks above the -80 dB threshold will be visible.
Leave the horizontal scale on auto.

- Change vertical scale to 1e-6 -> 10
- Uncheck auto-scale

Right click on the plot area and select `Configure Plot` from the menu which appears.

Figure 3. Phoebus plot configuration dialog

![Plot config](image/Phoebus_plot_config.png)

## Process

1. If applicable, run through the "System Power Up" section of [D.4.3](D-4-03_PROC_-_Start-up_and_Shut-down.md).
1. Run [D.4.9](D-4-09_PROC_-_Inspecting_the_Current_State_and_Health.md.) Inspecting the Current State and Health of the system
1. Set sample rate to 250Ksps and enable acquisition.  (see [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md))
""".rstrip())

for chas in range(1, 33):
    print(f'''\
1. Chassis {chas}.  Connect signal generator.
    - [ ] Successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)).
'''.rstrip())
    for chan in range(1, 33):
        sig = (chas-1)*32 + chan
        print(f'''\
    - [ ] Channel {chan}, signal {sig}.  Verify AC response
'''.rstrip())

print('''\
1. Make a test recording, at least 10 seconds, according to [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md).
    - Observe channels according to [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md).
1. View this recording according to [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md).
1. Export this recording according to [D.4.8](D-4-08_PROC_-_Export_Data_from_the_System.md).

## References

- Quartz [functional test](https://github.com/osprey-dcs/quartz-daq-250-24/blob/master/documentation/functional-testing.md#alias-rejection-testing)
report.

'''.rstrip())
